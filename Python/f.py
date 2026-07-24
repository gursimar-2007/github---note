# list=[7,2,8,3,5]
# n=(len(list))
# for i in range(n):
#     for j in range(0,n-i-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list[j])
# # list_data = [1, 2, 3, 4, 5]
def bubble_sort(arr):
    n = len(arr)
    # Outer loop to traverse through all array elements
    for i in range(n):
        # swapped = False
        
        # Inner loop for adjacent comparisons (last i elements are already sorted)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # swapped = True
                
        # If no two elements were swapped by inner loop, then break
        # if not swapped:
            # break

# Example usage:
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
print("Sorted array:", data)
