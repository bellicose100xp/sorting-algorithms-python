# sorts in place
def merge_sort(arr: list[int]):
    if len(arr) > 1:
        mid: int = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # this returns the sorted left_arr and right_arr 
        # this is because arrays are passed by referece and we are modifying original array later in the function
        merge_sort(left_arr)
        merge_sort(right_arr)

        l: int = 0  # left_arr index
        r: int = 0  # right_arr index
        i: int = 0  # sorted 'arr' index

        # we are combining the sorted left and right arr into the arr directly
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                arr[i] = left_arr[l]
                l += 1
            else:
                arr[i] = right_arr[r]
                r += 1
            i += 1
        
        while l < len(left_arr):
            arr[i] = left_arr[l]
            i += 1
            l += 1
        
        while r < len(right_arr):
            arr[i] = right_arr[r]
            i += 1
            r += 1

arr = [5, -4, 3, 2, 1]
merge_sort(arr)
print(arr)

                
