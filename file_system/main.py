import sys
import os
sys.setrecursionlimit(10 ** 6)
from boot_record import Boot_Record
from dir1_prepare import dir_prepare
from fat import fat_table
from node import NodeMgmt
from dir_file_read import DirFileRead


def main():

    filename = sys.argv[1]
    br = Boot_Record(filename)

    dir_offset = br.data_region

    dir_pre = dir_prepare(filename, br, dir_offset)

    fatTable = fat_table(filename, br)

    root_mgmt = NodeMgmt(["/", []])
    dir_file_read = DirFileRead(filename, br, dir_pre, fatTable, "/", root_mgmt)

    print("-------------node--------------")
    root_mgmt.make_dir()


if __name__ == "__main__":
    main()