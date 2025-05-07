def binary_search(list_, num):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2

        if list_[mid] == num:
            return mid
        
        if list_[mid] < num:
            low = mid + 1
        
        if list_[mid] > num:
            high = mid - 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
ans = binary_search(my_list, 3)

for i in my_list[:ans:]:
    print(i)
