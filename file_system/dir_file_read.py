from dir1_prepare import dir_prepare
from cluster_num import cluster_num


class DirFileRead:
    def __init__(self, filename, br, dir_pre, fatTable, node_mgmt, root_mgmt):
        for data in dir_pre.result_list:
            name, attribute, first_cluster, dir_offset, file_size, extension = data
            node_mgmt.cur_path ()
            path = node_mgmt.path
            if first_cluster >= len (fatTable.fat_table_list):
                continue

            if attribute == 16:
                path += str(name)[2:][:-1]
                if path[-1] == ".":
                    continue
                dir_pre = dir_prepare(filename, br, dir_offset)
                cluster_n = cluster_num(fatTable.fat_table_list, first_cluster, br.data_region, br.cluster_num_of_root_dir,
                                         br.cluster_size)

                node_mgmt.add([path, hex (dir_offset), hex(file_size), cluster_n.cluster_list])
                DirFileRead(filename, br, dir_pre, fatTable, node_mgmt, root_mgmt)

            elif attribute == 32:
                path = str(name)[2:][:-1] + "." + str(extension)[2:][:-1]
                cluster_n = cluster_num(fatTable.fat_table_list, first_cluster, br.data_region, br.cluster_num_of_root_dir,
                                         br.cluster_size)
                node_mgmt.add([path, hex(dir_offset), hex(file_size), cluster_n.cluster_list])

        node = node_mgmt.head
        while node:
            root_mgmt.add (node.data)
            node = node.next
