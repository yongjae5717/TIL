from cluster_chain import ClusterChain


class cluster_num:
    def __init__(self, fatTable, first_cluster, dir_offset, cluster_num_of_root_dir, cluster_size):
        self.cluster_num = first_cluster
        self.cluster_list = list()
        cluster_chain = ClusterChain()
        while True:
            if self.cluster_num == len(fatTable):
                break
            if fatTable[self.cluster_num] in cluster_chain.eof:
                break
            cluster_offset = dir_offset + (self.cluster_num - cluster_num_of_root_dir) * cluster_size
            if int('0x0000002', 0) <= self.cluster_num + 1 <= int('0xfffffef', 0):
                self.cluster_list.append((hex(cluster_offset), hex(cluster_size)))
            self.cluster_num += 1
