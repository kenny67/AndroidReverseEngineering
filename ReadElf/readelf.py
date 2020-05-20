# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
-------------------------------------------------
   File Name：    readelf.py
   Description :  分析so文件
   Author :       Andy Zhong
   date：          2020/5/20
-------------------------------------------------
   Change Activity:
                   2020/5/20:
-------------------------------------------------
"""

__author__ = 'Andy Zhong'

import sys
import mmap
import binascii


def hexlify(data):
    return '0x' + binascii.hexlify(data).decode()


class ELFFile(object):
    def __init__(self, elf):
        self.header = ELFHeader(elf)
        self.program_headers = []
        current = self.header.phoff
        for i in range(self.header.phnum):
            p_header = ProgramHeader(elf, self.header, current)
            self.program_headers.append(p_header)
            current += self.header.phentsize

        self.section_headers = []
        self.strtable = None
        current = self.header.shoff
        for i in range(self.header.shnum):
            s_header = SectionHeader(elf, self.header, current)
            if i == self.header.shstrndx:
                self.strtable = StrTableSection(elf, s_header)
            self.section_headers.append(s_header)
            current += self.header.shentsize

    def print_program_header(self):
        if len(self.program_headers) == 0:
            print('There is no program header....')
            return
        ProgramHeader.print_title()
        for header in self.program_headers:
            header.print()

    def print_section_header(self):
        if len(self.section_headers) == 0:
            print('There is no section header....')
            return
        SectionHeader.print_section_header_title()
        for header in self.section_headers:
            header.print()


class ELFHeader(object):
    def __init__(self, elf):
        self.magic = elf[0:3]
        if self.magic != b'\x7fEL':
            raise ValueError('Illegal file format: ', self.magic)
        self.clazz = elf[4]
        self.data = elf[5]

        original = lambda x: x
        # (attr_name, size, transform_func)
        items = [('version', 1, self.int_from_bytes),
                 ('osabi', 1, None),
                 ('abiversion', 1, None),
                 ('pad', 7, original),
                 ('type', 2, None),
                 ('machine', 2, None),
                 ('e_version', 4, self.int_from_bytes),
                 ('entry', 8 if self.is_64 else 4, original),
                 ('phoff', 8 if self.is_64 else 4, self.int_from_bytes),
                 ('shoff', 8 if self.is_64 else 4, self.int_from_bytes),
                 ('flags', 4, None),
                 ('ehsize', 2, self.int_from_bytes),
                 ('phentsize', 2, self.int_from_bytes),
                 ('phnum', 2, self.int_from_bytes),
                 ('shentsize', 2, self.int_from_bytes),
                 ('shnum', 2, self.int_from_bytes),
                 ('shstrndx', 2, self.int_from_bytes)]
        current = 0x06
        for item in items:
            attr_name, size, transform_func = item
            next_current = current + size
            value = elf[current: next_current]
            current = next_current
            if transform_func is not None:
                value = transform_func(value)
            elif size != 1 and self.is_little:
                value = value[::-1]
            setattr(self, attr_name, value)

    def int_from_bytes(self, bytes):
        return int.from_bytes(bytes, 'little' if self.is_little else 'big', signed=True)

    @property
    def is_little(self):
        return self.data == 1

    @property
    def is_64(self):
        return self.clazz == 2

    def _class_desc(self):
        return 'ELF64' if self.is_64 else 'ELF32'

    def _data_desc(self):
        return "2's complement, little endian" if self.is_little else "2's complement, big endian"

    def _osabi_desc(self):
        abi = {b'\x00': "System V",
               b'\x01': "HP-UX",
               b'\x02': "NetBSD",
               b'\x03': "Linux",
               b'\x04': "GNU Hurd",
               b'\x06': "Solaris",
               b'\x07': "AIX",
               b'\x08': "IRIX",
               b'\x09': "FreeBSD"}
        return abi[self.osabi]

    def _type_desc(self):
        type = {
            b'\x00\x00': "NONE",
            b'\x00\x01': "REL",
            b'\x00\x02': "EXEC",
            b'\x00\x03': "DYN",
            b'\x00\x04': "CORE",
            b'\xfe\x00': "LOOS",
            b'\xfe\xff': "HIOS",
        }
        return type[self.type]

    def _machine_desc(self):
        machine = {
            b'\x00\x00': 'NONE',
            b'\x00\x02': 'SPARC',
            b'\x00\x03': 'x86',
            b'\x00\x08': 'MIPS',
            b'\x00\x14': "PowerPC",
            b'\x00\x16': "S390",
            b'\x00\x28': 'ARM',
            b'\x00\x2A': "SuperH",
            b'\x00\x32': 'IA-64',
            b'\x00\x3E': 'x86-64',
            b'\x00\xB7': 'AArch64',
            b'\x00\xF3': 'RISC-V'
        }
        return machine[self.machine]

    def print(self):
        width = 45
        print('ELF Header: ')
        print('  Class:'.ljust(width), self._class_desc())
        print('  Data:'.ljust(width), self._data_desc())
        print('  OS/ABI:'.ljust(width), self._osabi_desc())
        print('  Type:'.ljust(width), self._type_desc())
        print('  Machine:'.ljust(width), self._machine_desc())
        print('  Entry point address:'.ljust(width), hex(self.int_from_bytes(self.entry)))
        print('  Start of program headers:'.ljust(width), self.phoff, ' (bytes into file)')
        print('  Start for section headers:'.ljust(width), self.shoff, ' (bytes into file)')
        print('  Flags:'.ljust(width), self.flags)
        print('  Size of this header:'.ljust(width), self.ehsize, ' (bytes)')
        print('  Size of program header:'.ljust(width), self.phentsize, ' (bytes)')
        print('  Number of program headers:'.ljust(width), self.phnum)
        print('  Size of section headers:'.ljust(width), self.shentsize, ' (bytes)')
        print('  Number of section headers:'.ljust(width), self.shnum)
        print('  Section header string table index:'.ljust(width), self.shstrndx)
        print('')


class ProgramHeader(object):
    def __init__(self, elf, elf_header, base):
        address_offset = 8 if elf_header.is_64 else 4
        items = [
            ('type', 4, None),
            ('flags', 4 if elf_header.is_64 else 0, None),
            ('offset', address_offset, elf_header.int_from_bytes),
            ('vaddr', address_offset, None),
            ('paddr', address_offset, None),
            ('filesz', address_offset, elf_header.int_from_bytes),
            ('memsz', address_offset, elf_header.int_from_bytes),
            ('flags', 0 if elf_header.is_64 else 4, None),
            ('align', address_offset, elf_header.int_from_bytes)]
        current = base
        for item in items:
            attr_name, size, transform_func = item
            current_next = current + size
            if size == 0:
                continue
            value = elf[current: current_next]
            if transform_func is not None:
                value = transform_func(value)
            elif elf_header.is_little:
                value = value[::-1]
            setattr(self, attr_name, value)
            current = current_next

    @staticmethod
    def print_item(items, item_width=10):
        content = ' '.join(
            [str(item).center(item_width) if type(item) is not tuple else str(item[0]).center(item[1]) for item in
             items])
        print(content)

    def _type_desc(self):
        types = {
            b'\x00\x00\x00\x00': 'NULL',
            b'\x00\x00\x00\x01': 'LOAD',
            b'\x00\x00\x00\x02': 'DYNAMIC',
            b'\x00\x00\x00\x03': 'INTERP',
            b'\x00\x00\x00\x04': 'NOTE',
            b'\x00\x00\x00\x05': 'SHLIB',
            b'\x00\x00\x00\x06': 'PHDR',
            b'\x60\x00\x00\x00': 'LOOS',
            b'\x6F\xFF\xFF\xFF': 'HIOS',
            b'\x70\x00\x00\x00': 'LOPROC',
            b'\x7F\xFF\xFF\xFF': 'HIPROC'
        }
        if self.type in types:
            return types[self.type]
        return hexlify(self.type)

    @staticmethod
    def print_title():
        ProgramHeader.print_item(['type', 'flags', 'offset', \
                                  ('vaddr', 20), ('paddr', 20), \
                                  'filesz', 'memsz', 'align'])

    def print(self):
        ProgramHeader.print_item([self._type_desc(), hexlify(self.flags), self.offset, \
                                  (hexlify(self.vaddr), 20), (hexlify(self.paddr), 20), \
                                  self.filesz, self.memsz, self.align])


class SectionHeader(object):
    def __init__(self, elf, elf_header, base):
        self.elf = elf
        address_len = 8 if elf_header.is_64 else 4
        items = [
            ('name', 4, None),
            ('type', 4, None),
            ('flags', address_len, None),
            ('addr', address_len, None),
            ('offset', address_len, elf_header.int_from_bytes),
            ('size', address_len, elf_header.int_from_bytes),
            ('link', 4, elf_header.int_from_bytes),
            ('info', 4, None),
            ('addralign', address_len, elf_header.int_from_bytes),
            ('entsize', address_len, elf_header.int_from_bytes)
        ]
        current = base
        for item in items:
            attr_name, size, transform_func = item
            next_current = current + size
            value = elf[current: next_current]
            if transform_func is not None:
                value = transform_func(value)
            elif elf_header.is_little:
                value = value[::-1]
            current = next_current
            setattr(self, attr_name, value)

    def _type_desc(self):
        types = {
            b'\x00\x00\x00\x00': 'NULL',
            b'\x00\x00\x00\x01': 'PROGBITS',
            b'\x00\x00\x00\x02': 'SYMTAB',
            b'\x00\x00\x00\x03': 'STRTAB',
            b'\x00\x00\x00\x04': 'RELA',
            b'\x00\x00\x00\x05': 'HASH',
            b'\x00\x00\x00\x06': 'DYNAMIC',
            b'\x00\x00\x00\x07': 'NOTE',
            b'\x00\x00\x00\x08': 'NOBITS',
            b'\x00\x00\x00\x09': 'REL',
            b'\x00\x00\x00\x0A': 'SHLIB',
            b'\x00\x00\x00\x0B': 'DYNSYM',
            b'\x00\x00\x00\x0E': 'INIT_ARRAY',
            b'\x00\x00\x00\x0F': 'FINI_ARRAY',
            b'\x00\x00\x00\x10': 'PREINIT_ARRAY',
            b'\x00\x00\x00\x11': 'GROUP',
            b'\x00\x00\x00\x12': 'SYMTAB_SHNDX',
            b'\x00\x00\x00\x13': 'NUM',
        }
        if self.type in types:
            return types[self.type]
        return hexlify(self.type)

    def _flag_desc(self):
        flags = {
            0x01: 'WRITE',
            0x02: 'ALLOC',
            0x04: 'EXECINSTR',
            0x10: 'MERGE',
            0x20: 'STRINGS',
            0x40: 'INFO_LINK',
            0x80: 'LINK_ORDER',
            0x100: 'OS_NONCONFORMING',
            0x0200: 'GROUP',
            0x0400: 'TLS',
            0x0ff00000: 'MASKOS',
            0xf0000000: 'MASKPROC',
            0x40000000: 'ORDERED',
            0x80000000: 'EXCLUDE'
        }
        flag = int.from_bytes(self.flags, byteorder='big')
        if flag in flags:
            return flags[flag]
        else:
            return hexlify(self.flags)

    def _name_desc(self):
        if self.elf.strtable is None:
            return hexlify(self.name)
        else:
            return hexlify(self.name)

    @staticmethod
    def print_section_header_title():
        ProgramHeader.print_item(['name', ('type', 15), ('flags', 20), \
                                  ('addr', 20), ('offset', 5), ('size', 8), \
                                  ('link', 8), 'info', 'addralign'])

    def print(self):
        ProgramHeader.print_item([hexlify(self.name), (self._type_desc(), 15), (self._flag_desc(), 20), \
                                  (hexlify(self.addr), 20), (self.offset, 5), (self.size, 8), \
                                  (self.link, 8), hexlify(self.info), self.addralign])


class StrTableSection(object):
    def __init__(self, elf, strtable_header):
        content = elf[strtable_header.offset: strtable_header.offset + strtable_header.size]
        self.strs = content.split(b'\x00')


if __name__ == '__main__':
    # file_path = sys.argv[1]
    file_path = input("[请输入您的so文件路径，如：C:\\Users\\Administrator\\Desktop\\libcms.so]==>>>")
    print("\n")
    # file_path = r"C:\Users\Administrator\Desktop\libcms.so"
    print("read elf info from: ", file_path)
    elffile = open(file_path, 'r')
    map = mmap.mmap(elffile.fileno(), 0, access=mmap.ACCESS_READ)
    elf = ELFFile(map)
    elf.header.print()
    print('\nELF Program Headers:')
    elf.print_program_header()
    print('\nELF Section Headers: ')
    elf.print_section_header()
    map.close()
    elffile.close()
