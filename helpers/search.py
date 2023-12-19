from linked_list import linked_list 

class room :
    def __init__(self, roomID, price, type):
        self.roomID = roomID
        self.price = price
        self.type = type



linklist = linked_list()

r1 = room(1,"200$","Vip")
r2 = room(2,"300$","Vip")
r3 = room(3,"300$","Normal")
linklist.append(r1)
linklist.append(r2)
linklist.append(r3)
# linklist.display()

def search(linklist, roomID = None,type = None):
        # Initialize current to head
        current = linklist.head.next
        # Loop till current not equal to None
        ArrRoom = []
        while current != None:
            if current.data.roomID == roomID or current.data.type == type :
                # Data found
                ArrRoom.append(current.data)
            current = current.next
        if len(ArrRoom) == 0:
             return "Not found"
        else : 
             return ArrRoom

result = search(linklist,None,"Vip")

print(result)


