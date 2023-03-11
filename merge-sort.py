import multiprocessing

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    return merge(left_array, right_array)

def merge(left_array, right_array):
    i = j = 0
    result = []

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1

    result += left_array[i:]
    result += right_array[j:]

    return result

def merge_subarrays(subarrays):
    result = []

    while subarrays:
        min_index = 0
        for i in range(1, len(subarrays)):
            if subarrays[i][0] < subarrays[min_index][0]:
                min_index = i

        min_value = subarrays[min_index].pop(0)
        if not subarrays[min_index]:
            subarrays.pop(min_index)

        result.append(min_value)

    return result

def parallel_merge_sort(array, num_processes):
    if num_processes == 1:
        # base case
        return merge_sort(array)
    else:
        # divide array into subarrays and distribute to processes
        subarrays = [array[i::num_processes] for i in range(num_processes)]
        pool = multiprocessing.Pool(processes=num_processes)
        subarrays = pool.map(merge_sort, subarrays)
        pool.close()
        pool.join()
        # merge subarrays back into original array
        merged_array = merge_subarrays(subarrays)
        return merged_array

# example usage
if __name__ == '__main__':
    array = input("Nhập mảng: ")
    array = [int(x) for x in array.split()]

    num_processes = 2
    sorted_array = parallel_merge_sort(array, num_processes)
    print(sorted_array)
