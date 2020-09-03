def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
        print(arr)


l = [6, 1, 4, 10, 7, 8, 9, 3, 2, 5]
insertion_sort(l)


"""
-Keep track of key
-If condition for a swap is reached, keep track of the current item (working index) as it will be compared again to it's prior element after the swap
-Nested loop O(n^2)
-use print statements to debug

# compare key to to item - 1 ex. list[key] < list[key - 1]
"""
