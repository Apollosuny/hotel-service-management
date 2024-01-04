class node:
    def __init__(self, data=""):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    # Returns the length (integer) of the linked list.
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
    
    def getAll(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        return elems

    # Returns the value of the node at 'index'.
    def get_node_at_index(self, index):
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        return None 

    # Deletes the node at index 'index'.
    def delete_node_by_index(self, index):
        current = self.head
        previous = None
        current_index = 0

        while current:
            if current_index == index:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return 
            previous = current
            current = current.next
            current_index += 1

        print(f"Index {index} out of range")

    # Inserts the node 'node' at index 'index'. Indices begin at 0.
    # If the 'index' is greater than or equal to the length of the linked
    # list the 'node' will be appended.
    def insert_node(self, index, node):
        if index < 0:
            print("ERROR: 'Erase' Index cannot be negative!")
            return
        if index >= self.length():  # append the node
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = node
            return
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                prior_node.next = node
                return
            prior_node = cur_node
            cur_idx += 1
    
    def update_node(self, index, new_data):
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                current.data = new_data
                return "Updated successfully!"
            current = current.next
            current_index += 1
        return "Data not found!"
