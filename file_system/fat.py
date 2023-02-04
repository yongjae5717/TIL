from endian import to_be


class fat_table:
    def __init__(self, filename, br):

        self.fat_table_list = list()

        offset = br.fat_region
        finish_count = br.num_of_sector_FAT_area // 4 + 1

        flag = 0
        while flag != finish_count:
            with open(filename, 'rb') as f:
                f.seek(offset)
                byte_array = f.read(4)
            flag += 1
            offset += 4

            be_byte_array = to_be(byte_array)
            self.fat_table_list.append(be_byte_array)
