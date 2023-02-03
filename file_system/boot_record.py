from endian import to_be, to_le


class Boot_Record:
    """
    Boot Record Class
    """

    def __init__(self, filename):
        count = 0
        byte_array = bytearray()
        with open(filename, 'rb') as f:
            while True:
                count += 1
                data = f.read(1)
                if data == b'':
                    break
                byte_array += data
                if count == 512:
                    break

        self.num_of_FAT_area = int(byte_array[16])
        self.num_of_byte_per_sector = int(to_le(byte_array[11:13]), 16)
        self.num_of_sector_per_cluster = int(byte_array[13])
        self.num_of_sector_reserved = int(to_le(byte_array[14:16]), 16)
        self.num_of_sector_FAT_area = int(to_le(byte_array[36:40]), 16)
        self.cluster_num_of_root_dir = int(to_le(byte_array[44:48]), 16)
        self.fat_region = self.num_of_sector_reserved * self.num_of_byte_per_sector
        self.data_region = self.fat_region + (self.num_of_FAT_area * self.num_of_sector_FAT_area * self.num_of_byte_per_sector)
        self.cluster_size = self.num_of_byte_per_sector * self.num_of_sector_per_cluster
        self.fat_size = self.num_of_sector_FAT_area * self.num_of_byte_per_sector
        self.fat_area_size = self.fat_size * self.num_of_FAT_area
