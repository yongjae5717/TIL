import sys
sys.setrecursionlimit(10 ** 6)
from boot_record import Boot_Record
from dir_prepare import dir_prepare
from fat import fat_table
from node import NodeMgmt
from dir_file_read import DirFileRead


def main():

    # filename = sys.argv[1]
    # exportPath = "AllFiles/"
    filename, exportPath = sys.stdin.readline().split()
    br = Boot_Record(filename)

    dir_offset = br.data_region

    dir_pre = dir_prepare(filename, br, dir_offset)

    fatTable = fat_table(filename, br)

    root_mgmt = NodeMgmt(["/", []])
    DirFileRead(filename, br, dir_pre, fatTable, "/", root_mgmt)

    root_mgmt.all_files_export(filename, exportPath)
    root_mgmt.selected_file_export(filename, "/DIR1/PORT.JPG", "SelectedFile/")


if __name__ == "__main__":
    main()