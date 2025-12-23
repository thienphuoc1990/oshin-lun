"""
CÁC THUẬT TOÁN SINH HOÁN VỊ
Module này cài đặt các thuật toán khác nhau để sinh hoán vị
"""

from typing import List, Generator, Any
from itertools import permutations as itertools_permutations
import copy


# ============================================================================
# 1. THUẬT TOÁN QUAY LUI (BACKTRACKING)
# ============================================================================

def permutations_backtrack(arr: List[Any]) -> Generator[List[Any], None, None]:
    """
    Sinh hoán vị sử dụng thuật toán quay lui

    Ý tưởng:
    - Xây dựng hoán vị từng bước
    - Tại mỗi vị trí, thử tất cả các phần tử chưa được sử dụng
    - Khi đủ n phần tử -> có một hoán vị hoàn chỉnh
    - Quay lui để thử các khả năng khác

    Args:
        arr: Danh sách các phần tử

    Yields:
        Các hoán vị dưới dạng list

    Example:
        >>> list(permutations_backtrack([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    n = len(arr)
    used = [False] * n  # Đánh dấu phần tử đã sử dụng
    current = []  # Hoán vị hiện tại đang xây dựng

    def backtrack():
        # Điều kiện dừng: đã chọn đủ n phần tử
        if len(current) == n:
            yield current.copy()  # Sinh ra một hoán vị
            return

        # Thử từng phần tử chưa được sử dụng
        for i in range(n):
            if not used[i]:
                # Chọn phần tử i
                current.append(arr[i])
                used[i] = True

                # Đệ quy để chọn phần tử tiếp theo
                yield from backtrack()

                # Quay lui: bỏ chọn phần tử i
                current.pop()
                used[i] = False

    yield from backtrack()


def permutations_backtrack_with_trace(arr: List[Any]) -> Generator[tuple, None, None]:
    """
    Giống permutations_backtrack nhưng trả về cả trace để debug/học tập

    Yields:
        tuple (permutation, depth, action) với:
        - permutation: hoán vị hiện tại
        - depth: độ sâu đệ quy
        - action: hành động ('add', 'complete', 'backtrack')
    """
    n = len(arr)
    used = [False] * n
    current = []

    def backtrack(depth=0):
        if len(current) == n:
            yield (current.copy(), depth, 'complete')
            return

        for i in range(n):
            if not used[i]:
                current.append(arr[i])
                used[i] = True
                yield (current.copy(), depth, f'add {arr[i]}')

                yield from backtrack(depth + 1)

                current.pop()
                used[i] = False
                yield (current.copy(), depth, f'backtrack from {arr[i]}')

    yield from backtrack()


# ============================================================================
# 2. THUẬT TOÁN HEAP (HEAP'S ALGORITHM)
# ============================================================================

def permutations_heap(arr: List[Any]) -> Generator[List[Any], None, None]:
    """
    Sinh hoán vị sử dụng thuật toán Heap

    Ý tưởng:
    - Thuật toán của B.R. Heap (1963)
    - Sinh hoán vị bằng cách hoán đổi các phần tử
    - Mỗi hoán vị được sinh bằng đúng 1 phép hoán đổi
    - Rất hiệu quả về mặt tính toán

    Args:
        arr: Danh sách các phần tử

    Yields:
        Các hoán vị dưới dạng list
    """
    arr = arr.copy()  # Không làm thay đổi mảng gốc
    n = len(arr)

    def generate(k):
        if k == 1:
            yield arr.copy()
        else:
            # Sinh các hoán vị với k phần tử đầu tiên
            yield from generate(k - 1)

            # Sinh các hoán vị mới bằng cách hoán đổi
            for i in range(k - 1):
                if k % 2 == 0:
                    # k chẵn: hoán đổi phần tử thứ i với phần tử cuối
                    arr[i], arr[k - 1] = arr[k - 1], arr[i]
                else:
                    # k lẻ: hoán đổi phần tử đầu với phần tử cuối
                    arr[0], arr[k - 1] = arr[k - 1], arr[0]

                yield from generate(k - 1)

    yield from generate(n)


# ============================================================================
# 3. THUẬT TOÁN SINH HOÁN VỊ KẾ TIẾP (NEXT PERMUTATION)
# ============================================================================

def next_permutation(arr: List[Any]) -> bool:
    """
    Biến đổi mảng thành hoán vị kế tiếp theo thứ tự từ điển

    Thuật toán:
    1. Tìm i lớn nhất sao cho arr[i] < arr[i+1]
    2. Nếu không tìm thấy -> đây là hoán vị cuối cùng (return False)
    3. Tìm j lớn nhất sao cho arr[i] < arr[j]
    4. Hoán đổi arr[i] và arr[j]
    5. Đảo ngược đoạn từ arr[i+1] đến cuối

    Args:
        arr: Danh sách các phần tử (sẽ bị thay đổi in-place)

    Returns:
        True nếu tìm được hoán vị kế tiếp, False nếu đây là hoán vị cuối

    Example:
        >>> arr = [1, 2, 3]
        >>> next_permutation(arr)
        True
        >>> arr
        [1, 3, 2]
    """
    n = len(arr)

    # Bước 1: Tìm i lớn nhất sao cho arr[i] < arr[i+1]
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # Bước 2: Nếu không tìm thấy -> hoán vị cuối cùng
    if i < 0:
        return False

    # Bước 3: Tìm j lớn nhất sao cho arr[i] < arr[j]
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1

    # Bước 4: Hoán đổi arr[i] và arr[j]
    arr[i], arr[j] = arr[j], arr[i]

    # Bước 5: Đảo ngược đoạn từ i+1 đến cuối
    arr[i + 1:] = reversed(arr[i + 1:])

    return True


def permutations_next(arr: List[Any]) -> Generator[List[Any], None, None]:
    """
    Sinh tất cả hoán vị theo thứ tự từ điển sử dụng next_permutation

    Args:
        arr: Danh sách các phần tử

    Yields:
        Các hoán vị theo thứ tự từ điển
    """
    arr = sorted(arr)  # Bắt đầu từ hoán vị nhỏ nhất
    yield arr.copy()

    while next_permutation(arr):
        yield arr.copy()


# ============================================================================
# 4. SỬ DỤNG ITERTOOLS (PYTHON BUILT-IN)
# ============================================================================

def permutations_itertools(arr: List[Any]) -> Generator[List[Any], None, None]:
    """
    Sinh hoán vị sử dụng thư viện itertools của Python

    Đây là cách khuyến nghị khi sử dụng trong production vì:
    - Đã được tối ưu hóa cao
    - Đã được kiểm thử kỹ lưỡng
    - Code ngắn gọn, dễ đọc

    Args:
        arr: Danh sách các phần tử

    Yields:
        Các hoán vị dưới dạng list
    """
    for perm in itertools_permutations(arr):
        yield list(perm)


# ============================================================================
# HÀM TIỆN ÍCH
# ============================================================================

def factorial(n: int) -> int:
    """Tính n giai thừa"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def count_permutations(arr: List[Any]) -> int:
    """
    Đếm số lượng hoán vị có thể có

    Nếu các phần tử đều khác nhau: n!
    Nếu có phần tử trùng lặp: n! / (n1! * n2! * ... * nk!)
    với n1, n2, ..., nk là số lần xuất hiện của các phần tử
    """
    from collections import Counter

    n = len(arr)
    counts = Counter(arr)

    result = factorial(n)
    for count in counts.values():
        result //= factorial(count)

    return result


def is_permutation(arr1: List[Any], arr2: List[Any]) -> bool:
    """
    Kiểm tra arr2 có phải là hoán vị của arr1 không
    """
    from collections import Counter
    return Counter(arr1) == Counter(arr2)


def permutation_rank(perm: List[Any]) -> int:
    """
    Tính thứ hạng của hoán vị (theo thứ tự từ điển, bắt đầu từ 0)

    Example:
        >>> permutation_rank([1, 2, 3])
        0
        >>> permutation_rank([3, 2, 1])
        5
    """
    sorted_perm = sorted(perm)
    n = len(perm)
    rank = 0

    for i in range(n):
        # Đếm số phần tử nhỏ hơn perm[i] ở bên phải
        smaller_count = 0
        for j in range(len(sorted_perm)):
            if sorted_perm[j] == perm[i]:
                smaller_count = j
                sorted_perm.pop(j)
                break

        # Cộng vào rank
        rank += smaller_count * factorial(n - i - 1)

    return rank


def kth_permutation(arr: List[Any], k: int) -> List[Any]:
    """
    Tìm hoán vị thứ k (theo thứ tự từ điển, bắt đầu từ 0)

    Args:
        arr: Danh sách các phần tử (đã sắp xếp)
        k: Thứ hạng cần tìm (0-indexed)

    Returns:
        Hoán vị thứ k

    Example:
        >>> kth_permutation([1, 2, 3], 0)
        [1, 2, 3]
        >>> kth_permutation([1, 2, 3], 5)
        [3, 2, 1]
    """
    arr = sorted(arr)
    n = len(arr)
    result = []
    remaining = arr.copy()

    for i in range(n):
        # Tính số hoán vị cho mỗi phần tử ở vị trí i
        perms_per_element = factorial(n - i - 1)

        # Tìm phần tử cần chọn
        index = k // perms_per_element
        result.append(remaining[index])
        remaining.pop(index)

        # Cập nhật k
        k %= perms_per_element

    return result


if __name__ == "__main__":
    # Test nhanh
    arr = [1, 2, 3]

    print("=== Test Backtracking ===")
    print(list(permutations_backtrack(arr)))

    print("\n=== Test Heap's Algorithm ===")
    print(list(permutations_heap(arr)))

    print("\n=== Test Next Permutation ===")
    print(list(permutations_next(arr)))

    print("\n=== Test Itertools ===")
    print(list(permutations_itertools(arr)))

    print("\n=== Utilities ===")
    print(f"Số hoán vị: {count_permutations(arr)}")
    print(f"Rank của [1,2,3]: {permutation_rank([1, 2, 3])}")
    print(f"Rank của [3,2,1]: {permutation_rank([3, 2, 1])}")
    print(f"Hoán vị thứ 0: {kth_permutation(arr, 0)}")
    print(f"Hoán vị thứ 5: {kth_permutation(arr, 5)}")
