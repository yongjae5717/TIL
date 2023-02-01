class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 노드 관리하는 클래스 만들기
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

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def cur_path(self):
        node = self.head
        self.path = node.data
