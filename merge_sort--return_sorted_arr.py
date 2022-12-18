# returns new sorted array
def merge_sort(arr: list[int]) -> list[int]:
    """
    T: O(n log n)
    """
    if len(arr) > 1:
        # split array in the middle
        mid: int = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # sort left side and right side
        sorted_left = merge_sort(left_arr)
        sorted_right = merge_sort(right_arr)
        l: int = 0  # left_arr index
        r: int = 0  # right_arr index

        # initialize empty sorted array
        sorted_arr: list[int] = []

        # we are combining the sorted left and right arr into the arr directly
        while l < len(sorted_left) and r < len(sorted_right):
            if sorted_left[l] < sorted_right[r]:
                sorted_arr.append(sorted_left[l])
                l += 1
            else:
                sorted_arr.append(sorted_right[r])
                r += 1
        
        while l < len(sorted_left):
            sorted_arr.append(sorted_left[l])
            l += 1
        
        while r < len(sorted_right):
            sorted_arr.append(sorted_right[r])
            r += 1

        return sorted_arr
    else:
        return arr

arr = [5, -4, 3, 2, 1, -3]
sorted_arr = merge_sort(arr)
print(sorted_arr)

                
