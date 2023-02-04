from endian import to_le
from file_manage import FileManage


class dir_prepare:
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

            self.result_list.append(file_manage)
