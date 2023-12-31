from .linked_list import linked_list

def searchForRoomType(linklist,price=None):
        # Initialize current to head
        current = linklist.head.next
        # Loop till current not equal to None
        rooms = []
        while current != None:
            print(current.data)
            if (current.data['fields']['price'] == price or price == None):
                rooms.append(current.data)
            current = current.next
        if len(rooms) == 0:
                return "Not found"
        else : 
                return rooms

def searchPrice(room_types, search):
    # push vào linklist 
    newlinkedlist = linked_list()

    # add data to the linked list 
    for item in room_types:
        newlinkedlist.append(item)

    # search data return the array 
    rooms = searchForRoomType(linklist=newlinkedlist,price=int(search))
    if  rooms == "Not found":
        print("The Room Type has not found!")
    else : 
        print("The Room Type has found!")
    return rooms

def totalPrice(linklist,price=None):
        # Initialize current to head
        current = linklist.head.next
        # Loop till current not equal to None
        data = []
        while current != None:
            if (current.data['fields']['total_price'] == price or price == None):
                data.append(current.data)
            current = current.next
        if len(data) == 0:
                return "Not found"
        else : 
                return data

def searchTotalPrice(room_types, search):
    # push vào linklist 
    newlinkedlist = linked_list()

    # add data to the linked list 
    for item in room_types:
        newlinkedlist.append(item)

    # search data return the array 
    rooms = totalPrice(linklist=newlinkedlist,price=float(search))
    if  rooms == "Not found":
        print("The Room Type has not found!")
    else : 
        print("The Room Type has found!")
    return rooms


