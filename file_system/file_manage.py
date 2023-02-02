class FileManage:
    def __init__(self, name, attribute, first_cluster, dir_offset, file_size, extension):
        self.name = name
        self.attribute = attribute
        self.first_cluster = first_cluster
        self.dir_offset = dir_offset
        self.file_size = file_size
        self.extension = extension
