# Merge-sort-multiprocessing

Hàm merge_sort(array) được sử dụng để sắp xếp mảng bằng phương pháp merge sort thông thường. Nếu độ dài mảng nhỏ hơn hoặc bằng 1, mảng được coi là đã được sắp xếp. Nếu không, mảng ban đầu được chia thành hai phần bằng cách lấy chỉ số trung bình của mảng và gọi đệ quy merge_sort() trên mỗi phần. Sau đó, hai phần này được hợp nhất bằng hàm merge().

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

Hàm merge(left_array, right_array) được sử dụng để hợp nhất hai mảng con đã được sắp xếp. Hai chỉ số i và j được sử dụng để theo dõi vị trí hiện tại trong mảng con bên trái và bên phải. Với mỗi phần tử của mảng con, phần tử nhỏ hơn sẽ được thêm vào kết quả và chỉ số tương ứng được tăng lên 1. Cuối cùng, mảng kết quả được hợp nhất từ các phần tử còn lại trong mảng con bên trái hoặc bên phải.

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

## Demo
![image](https://user-images.githubusercontent.com/94096493/224488350-5f275e74-aa70-4a62-9d11-9ad9d0010975.png)
