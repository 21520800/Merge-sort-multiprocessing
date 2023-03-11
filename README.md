# Merge-sort-multiprocessing

Hàm merge_sort(array) được sử dụng để sắp xếp mảng bằng phương pháp merge sort thông thường. Nếu độ dài mảng nhỏ hơn hoặc bằng 1, mảng được coi là đã được sắp xếp. Nếu không, mảng ban đầu được chia thành hai phần bằng cách lấy chỉ số trung bình của mảng và gọi đệ quy merge_sort() trên mỗi phần. Sau đó, hai phần này được hợp nhất bằng hàm merge():

```
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    return merge(left_array, right_array)
    
```

Hàm merge(left_array, right_array) được sử dụng để hợp nhất hai mảng con đã được sắp xếp. Hai chỉ số i và j được sử dụng để theo dõi vị trí hiện tại trong mảng con bên trái và bên phải. Với mỗi phần tử của mảng con, phần tử nhỏ hơn sẽ được thêm vào kết quả và chỉ số tương ứng được tăng lên 1. Cuối cùng, mảng kết quả được hợp nhất từ các phần tử còn lại trong mảng con bên trái hoặc bên phải:

```
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
```
Hàm merge_subarrays(subarrays) được sử dụng để hợp nhất các mảng con đã được sắp xếp trên các tiến trình khác nhau thành một mảng đã sắp xếp. Hàm này sử dụng một danh sách con trỏ để theo dõi chỉ số đầu tiên của mỗi mảng con, và lặp lại việc lấy phần tử nhỏ nhất từ danh sách con trỏ cho đến khi tất cả các phần tử của tất cả các mảng con đã được thêm vào danh sách kết quả.

```
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
    
```

Cuối cùng, hàm parallel_merge_sort(array, num_processes) được sử dụng để sắp xếp mảng ban đầu bằng cách chia mảng thành các mảng con và thực hiện sắp xếp trên các mảng con này trên các tiến trình khác nhau. Nếu số lượng tiến trình chỉ là 1, hàm merge_sort() được gọi trên toàn bộ mảng ban đầu. Ngược lại, số lượng tiến trình được chia nhỏ hơn số phần tử của mảng ban đầu và mỗi mảng con được gửi đến một tiến trình khác nhau để sắp xếp. Sau đó, kết quả của việc sắp xếp các mảng con được hợp nhất với nhau bằng cách sử dụng hàm merge_subarrays(). Việc này được thực hiện trên một tiến trình khác nhau với mỗi mảng con. Cuối cùng, kết quả của việc hợp nhất các mảng con trên các tiến trình khác nhau được trả về là một mảng đã sắp xếp.

```
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
        
```
## Demo
![image](https://user-images.githubusercontent.com/94096493/224488350-5f275e74-aa70-4a62-9d11-9ad9d0010975.png)
