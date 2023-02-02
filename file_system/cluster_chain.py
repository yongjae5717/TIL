class ClusterChain:
    def __init__(self):
        self.free_cluster = '0x0000000'
        self.reserved_cluster = list(hex(i) for i in range(int('0xffffff0', 0), int('0xffffff6', 0) + 1))
        self.bad_cluster = '0xffffff7'
        self.eof = list(hex(i) for i in range(int('0xffffff8', 0), int('0xfffffff', 0) + 1))