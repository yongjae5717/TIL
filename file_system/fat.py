from endian import to_be, to_le


class fat_table:
    """
    fat table class
    """
    def __init__(self, filename, br):

        self.fat_table_list = list()

        offset = br.fat_region
        finish_count = br.num_of_sector_FAT_area // 4 + 1

        flag = 0
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
                    if count == 4:
                        break
            f.close()
            flag += 1
            offset += 4

            if flag == finish_count:
                break

            be_byte_array = to_be(byte_array)
            self.fat_table_list.append(be_byte_array)