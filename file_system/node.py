import os


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.path = ""

    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def all_files_export(self, filename, exportPath):
        node = self.head
        while node.next:
            path, data = node.data
            destination_dir = os.path.join(exportPath,  path[1:])
            if not os.path.exists(destination_dir) and not data:
                os.makedirs(destination_dir)
            elif data:
                byte_array = bytearray()
                for dir_offset, cluster_size in data:
                    count = 0
                    with open(filename, 'rb') as f:
                        f.seek(int(dir_offset, 16))
                        while True:
                            count += 1
                            data = f.read(1)
                            byte_array += data
                            if count == int(cluster_size, 16):
                                break
                    f.close()
                    with open(destination_dir, "wb") as f:
                        f.write(byte_array)
                    f.close()

            print(path, data)
            node = node.next

    def selected_file_export(self, filename, dataPath, exportPath):
        node = self.head
        while node.next:
            path, data = node.data
            destination_dir = os.path.join(exportPath,  path[1:])

            if not os.path.exists(destination_dir) and not data:
                os.makedirs(destination_dir)
            elif data and path == dataPath:
                byte_array = bytearray()
                for dir_offset, cluster_size in data:
                    count = 0
                    with open(filename, 'rb') as f:
                        f.seek(int(dir_offset, 16))
                        while True:
                            count += 1
                            data = f.read(1)
                            byte_array += data
                            if count == int(cluster_size, 16):
                                break
                    f.close()
                with open(destination_dir, "wb") as f:
                    f.write(byte_array)
                f.close()
                break

            print(path, data)
            node = node.next