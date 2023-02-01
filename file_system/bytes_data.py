class Bytes_data:

    def __init__(self, filename, name, offset, data_range):
        self.offset = offset
        self.data_range = data_range
        self.byte_array = bytearray()
        print(hex(self.offset), hex(self.data_range), self.byte_array)

        count = 0
        byte_array = bytearray()
        with open(filename, 'rb') as f:
            f.seek(self.offset)
            while True:
                if data_range == 0:
                    break
                count += 1
                data = f.read(1)
                # print(data)
                # if data == b'':
                #     break
                byte_array += data
                if count == self.data_range:
                    break