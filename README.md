# THUẬT TOÁN SINH HOÁN VỊ (Permutation Generation Algorithm)

## 1. Giới thiệu về Hoán vị

**Hoán vị** là một cách sắp xếp các phần tử của một tập hợp theo một thứ tự nhất định. Với n phần tử phân biệt, có n! (n giai thừa) hoán vị khác nhau.

**Ví dụ:** Với tập {1, 2, 3}, có 3! = 6 hoán vị:
- (1, 2, 3)
- (1, 3, 2)
- (2, 1, 3)
- (2, 3, 1)
- (3, 1, 2)
- (3, 2, 1)

## 2. Các thuật toán sinh hoán vị

### 2.1. Thuật toán Quay lui (Backtracking)

**Ý tưởng:**
- Xây dựng hoán vị từng bước
- Tại mỗi bước, thử tất cả các phần tử chưa được sử dụng
- Khi đã chọn đủ n phần tử, ta có một hoán vị hoàn chỉnh
- Quay lui để thử các khả năng khác

**Độ phức tạp:** O(n × n!)

**Ưu điểm:**
- Dễ hiểu, dễ cài đặt
- Có thể dễ dàng áp dụng các ràng buộc

**Nhược điểm:**
- Không sinh hoán vị theo thứ tự từ điển

### 2.2. Thuật toán Hoán đổi (Swap-based / Heap's Algorithm)

**Ý tưởng:**
- Sinh hoán vị bằng cách hoán đổi các phần tử
- Heap's Algorithm là một biến thể hiệu quả

**Độ phức tạp:** O(n!)

**Ưu điểm:**
- Rất hiệu quả về mặt tính toán
- Mỗi hoán vị được sinh bằng đúng 1 phép hoán đổi

**Nhược điểm:**
- Khó hiểu hơn
- Không sinh theo thứ tự từ điển

### 2.3. Thuật toán sinh hoán vị kế tiếp (Next Permutation)

**Ý tưởng:**
- Bắt đầu từ hoán vị nhỏ nhất (sắp xếp tăng dần)
- Liên tục sinh hoán vị kế tiếp cho đến hoán vị lớn nhất

**Các bước:**
1. Tìm i lớn nhất sao cho a[i] < a[i+1]
2. Nếu không tìm thấy → đây là hoán vị cuối cùng
3. Tìm j lớn nhất sao cho a[i] < a[j]
4. Hoán đổi a[i] và a[j]
5. Đảo ngược đoạn từ a[i+1] đến cuối

**Độ phức tạp:** O(n) cho mỗi hoán vị

**Ưu điểm:**
- Sinh hoán vị theo thứ tự từ điển
- Hiệu quả, dễ kiểm soát
- Có thể bắt đầu từ bất kỳ hoán vị nào

**Nhược điểm:**
- Cần hiểu rõ thuật toán để cài đặt đúng

### 2.4. Sử dụng thư viện itertools (Python built-in)

Python cung cấp sẵn `itertools.permutations()` để sinh hoán vị một cách hiệu quả.

## 3. So sánh các phương pháp

| Thuật toán | Thứ tự | Độ phức tạp | Khó | Ứng dụng |
|-----------|---------|-------------|-----|----------|
| Backtracking | Không | O(n×n!) | Dễ | Học tập, bài toán ràng buộc |
| Heap's Algorithm | Không | O(n!) | Trung bình | Hiệu suất cao |
| Next Permutation | Từ điển | O(n×n!) | Trung bình | Cần thứ tự, tìm kiếm |
| itertools | Từ điển | O(n!) | Rất dễ | Sản phẩm thực tế |

## 4. Cấu trúc Project

```
oshin_lun/
├── README.md                    # Tài liệu này
├── permutation_algorithms.py   # Cài đặt các thuật toán
├── demo.py                      # Ví dụ sử dụng và so sánh
└── visualization.py             # Trực quan hóa quá trình
```

## 5. Cách sử dụng

### Chạy demo:
```bash
python demo.py
```

### Chạy visualization:
```bash
python visualization.py
```

### Sử dụng trong code:
```python
from permutation_algorithms import (
    permutations_backtrack,
    permutations_heap,
    permutations_next,
    permutations_itertools
)

# Sinh hoán vị của [1, 2, 3]
arr = [1, 2, 3]
result = list(permutations_backtrack(arr))
print(result)
```

## 6. Ứng dụng thực tế

- **Tổ hợp tối ưu:** Bài toán người du lịch (TSP)
- **Mật mã học:** Sinh khóa, kiểm tra tất cả khả năng
- **Game:** Sinh các trạng thái khác nhau
- **Lập lịch:** Sắp xếp công việc, thời khóa biểu
- **Toán học:** Chứng minh, tìm kiếm mẫu

## 7. Tham khảo

- Donald Knuth - The Art of Computer Programming, Volume 4
- Robert Sedgewick - Permutation Generation Methods
- Python itertools documentation
