from endian import to_le


class Boot_Record:
    def __init__(self, filename):
        with open(filename, 'rb') as f:
            byte_array = f.read(512)

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
