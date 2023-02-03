import sys
from boot_record import Boot_Record
from dir_prepare import dir_prepare
from fat import fat_table
from node import NodeMgmt
from dir_file_read import DirFileRead


def main():

    """ exportPath, search_file format example
    search_file = "/DIR1/PORT.JPG"
    exportPath = "AllFiles"
    """
    filename, exportPath = sys.argv[1], sys.argv[2]
    # filename, search_file, exportPath = sys.argv[1], sys.argv[2], sys.argv[3]

    br = Boot_Record(filename)

    dir_offset = br.data_region

    dir_pre = dir_prepare(filename, br, dir_offset)

    fatTable = fat_table(filename, br)

    root_mgmt = NodeMgmt(["/", []])
    DirFileRead(filename, br, dir_pre, fatTable, "/", root_mgmt)

    root_mgmt.all_files_export(filename, exportPath)
    # root_mgmt.selected_file_export(filename, search_file, exportPath)


if __name__ == "__main__":
    main()
