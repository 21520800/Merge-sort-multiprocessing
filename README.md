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

## Demo
![image](https://user-images.githubusercontent.com/94096493/224488350-5f275e74-aa70-4a62-9d11-9ad9d0010975.png)
