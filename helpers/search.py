
def searchForRoomType(linklist,name=None,price=None,num_adults=None,num_children=None):
        # Initialize current to head
        current = linklist.head.next
        # Loop till current not equal to None
        ArrRoom = []
        while current != None:
            if (current.data.price == price or price == None) and (current.data.name == name or name == None) and (current.data.num_adults == num_adults or num_adults == None) and (current.data.num_children == num_children or num_children == None):
                ArrRoom.append(current.data)
            current = current.next
        if len(ArrRoom) == 0:
                return "Not found"
        else : 
                return ArrRoom




