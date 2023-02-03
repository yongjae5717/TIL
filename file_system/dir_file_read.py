from dir_prepare import dir_prepare
from cluster_rule import cluster_rule


class DirFileRead:
    def __init__(self, filename, br, dir_pre, fatTable, node_path, root_mgmt):
        for data in dir_pre.result_list:
            self.path = node_path
            if data.first_cluster >= len(fatTable.fat_table_list):
                continue

            if data.attribute == 16:
                self.path += str(data.name)[2:][:-1]
                if self.path[-1] == ".":
                    continue
                dir_pre = dir_prepare(filename, br, data.dir_offset)
                root_mgmt.add([self.path, []])
                DirFileRead(filename, br, dir_pre, fatTable, self.path + "/", root_mgmt)

            elif data.attribute == 32:
                self.path += str(data.name)[2:][:-1] + "." + str(data.extension)[2:][:-1]
                cluster_n = cluster_rule(fatTable.fat_table_list, data.first_cluster, br.data_region,
                                         br.cluster_num_of_root_dir, br.cluster_size)
                root_mgmt.add([self.path, cluster_n.cluster_list])
