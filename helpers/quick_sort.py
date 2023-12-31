def quick_sort_by_price(arr, type):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x["fields"][type] <= pivot["fields"][type]]
        greater = [x for x in arr[1:] if x["fields"][type] > pivot["fields"][type]]
        return quick_sort_by_price(less, type) + [pivot] + quick_sort_by_price(greater, type)
    
def quick_sort_by_price_desc(arr, type):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x["fields"][type] > pivot["fields"][type]]
        greater = [x for x in arr[1:] if x["fields"][type] <= pivot["fields"][type]]
        return quick_sort_by_price_desc(less, type) + [pivot] + quick_sort_by_price_desc(greater, type)