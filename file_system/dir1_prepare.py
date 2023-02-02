from endian import to_be, to_le
from file_manage import FileManage


class dir_prepare:
    """
    dir1_prepare class
    """
    def __init__(self, filename, br, dir_offset):
        self.result_list = list()

        offset = dir_offset
        while True:
            byte_array = bytearray()
            count = 0
            with open(filename, 'rb') as f:
                f.seek(offset)
                while True:
                    count += 1
                    data = f.read(1)
                    if data == b'':
                        break
                    byte_array += data
                    if count == 32:
                        break
            f.close()
            offset += 32

            if byte_array == bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'):
                break

            name = byte_array[:8].decode('latin-1').encode("utf-8").strip()
            attribute = byte_array[11]
            first_cluster = int(to_le(byte_array[26:28] + byte_array[20:22]), 16)
            dir_offset = br.data_region + ((first_cluster - br.cluster_num_of_root_dir) * br.cluster_size)
            file_size = int(to_le(byte_array[28:]), 16)
            extension = byte_array[8:11].decode('latin-1').encode("utf-8").strip()
            file_manage = FileManage(name, attribute, first_cluster, dir_offset, file_size, extension)

            if attribute == 16 or attribute == 32:
                print("")
                print("name:", file_manage.name)
                print("attribute:", file_manage.attribute)
                print("first cluster:", hex(file_manage.first_cluster))
                print("dir_offset:", hex(file_manage.dir_offset), file_manage.first_cluster,
                      br.cluster_num_of_root_dir, hex(br.data_region))
                print("file_size:", hex(file_manage.file_size))
                print("extension:", file_manage.extension)
            self.result_list.append(file_manage)
