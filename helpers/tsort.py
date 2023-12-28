class HotelRoom:
    def __init__(self, room_number, occupancy, price):
        self.room_number = room_number
        self.occupancy = occupancy
        self.price = price

def insertion_sort(arr, key=lambda x: x.price):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and key(key_value) < key(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value

def merge(left, right, key=lambda x: x.price):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr, key=lambda x: x.price):
    min_run = 32

    for i in range(0, len(arr), min_run):
        insertion_sort(arr[i:min((i + min_run), len(arr))], key=key)

    size = min_run
    while size < len(arr):
        for start in range(0, len(arr), size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (len(arr) - 1))
            merged_array = merge(
                left=arr[start:midpoint + 1],
                right=arr[midpoint + 1:end + 1],
                key=key
            )
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr

# Example usage:
if __name__ == "__main__":
    # Test the hotel management system
    rooms = [
        HotelRoom(room_number=101, occupancy=2, price=150),
        HotelRoom(room_number=103, occupancy=1, price=100),
        HotelRoom(room_number=102, occupancy=2, price=180),
        HotelRoom(room_number=105, occupancy=1, price=120),
        HotelRoom(room_number=104, occupancy=2, price=200),
    ]

    print("Rooms (unsorted):")
    for room in rooms:
        print(f"Room {room.room_number} - Occupancy: {room.occupancy}, Price: ${room.price}")

    sorted_rooms = timsort(rooms, key=lambda x: x.price)

    print("\nRooms (sorted by price):")
    for room in sorted_rooms:
        print(f"Room {room.room_number} - Occupancy: {room.occupancy}, Price: ${room.price}")
