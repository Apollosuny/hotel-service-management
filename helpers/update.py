class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def sequential_search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def update_node(self, target, new_data):
        node = self.sequential_search(target)
        if node:
            node.data = new_data
            return "Sửa thành công"
        else:
            return "Không tìm thấy nút với dữ liệu cần sửa"

    def display(self):
        current = self.head
        while current:
            print(f"Data: {current.data}")
            current = current.next


# Ví dụ sử dụng
linked_list = LinkedList()

# Thêm các nút vào danh sách liên kết
linked_list.add_node("Dữ liệu 1")
linked_list.add_node("Dữ liệu 2")
linked_list.add_node("Dữ liệu 3")

# Hiển thị danh sách liên kết ban đầu
print("Danh sách liên kết ban đầu:")
linked_list.display()

# Cập nhật nút có dữ liệu là "Dữ liệu 2"
result = linked_list.update_node("Dữ liệu 2", "Dữ liệu mới")
print(result)

# Hiển thị danh sách liên kết sau khi cập nhật
print("Danh sách liên kết sau khi cập nhật:")
linked_list.display()