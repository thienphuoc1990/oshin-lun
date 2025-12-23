"""
DEMO CÁC THUẬT TOÁN SINH HOÁN VỊ
File này minh họa cách sử dụng và so sánh các thuật toán khác nhau
"""

import time
from typing import List, Callable, Any
from permutation_algorithms import (
    permutations_backtrack,
    permutations_heap,
    permutations_next,
    permutations_itertools,
    count_permutations,
    permutation_rank,
    kth_permutation,
    is_permutation,
    permutations_backtrack_with_trace
)


def print_separator(char="-", length=80):
    """In ra dòng phân cách"""
    print(char * length)


def demo_basic_usage():
    """Demo cách sử dụng cơ bản"""
    print_separator("=")
    print("DEMO 1: SỬ DỤNG CƠ BẢN")
    print_separator("=")

    arr = [1, 2, 3]
    print(f"\nSinh hoán vị của {arr}:\n")

    # Backtracking
    print("1. Thuật toán Quay lui (Backtracking):")
    result = list(permutations_backtrack(arr))
    for i, perm in enumerate(result, 1):
        print(f"   {i}. {perm}")

    # Heap's Algorithm
    print("\n2. Thuật toán Heap:")
    result = list(permutations_heap(arr))
    for i, perm in enumerate(result, 1):
        print(f"   {i}. {perm}")

    # Next Permutation
    print("\n3. Thuật toán Next Permutation (thứ tự từ điển):")
    result = list(permutations_next(arr))
    for i, perm in enumerate(result, 1):
        print(f"   {i}. {perm}")

    # Itertools
    print("\n4. Sử dụng itertools:")
    result = list(permutations_itertools(arr))
    for i, perm in enumerate(result, 1):
        print(f"   {i}. {perm}")


def demo_with_strings():
    """Demo với chuỗi ký tự"""
    print_separator("=")
    print("DEMO 2: HOÁN VỊ CỦA CHUỖI KÝ TỰ")
    print_separator("=")

    word = "ABC"
    arr = list(word)
    print(f"\nCác hoán vị của từ '{word}':\n")

    result = list(permutations_next(arr))
    for i, perm in enumerate(result, 1):
        print(f"   {i}. {''.join(perm)}")


def demo_performance_comparison():
    """So sánh hiệu suất các thuật toán"""
    print_separator("=")
    print("DEMO 3: SO SÁNH HIỆU SUẤT")
    print_separator("=")

    test_sizes = [3, 5, 7, 8]

    algorithms = [
        ("Backtracking", permutations_backtrack),
        ("Heap's Algorithm", permutations_heap),
        ("Next Permutation", permutations_next),
        ("Itertools", permutations_itertools)
    ]

    for n in test_sizes:
        arr = list(range(1, n + 1))
        expected_count = count_permutations(arr)

        print(f"\nKích thước: n={n} (Số hoán vị: {expected_count})")
        print(f"{'Thuật toán':<20} {'Thời gian (s)':<15} {'Số hoán vị':<15} {'Kết quả'}")
        print_separator("-")

        for name, func in algorithms:
            start_time = time.time()
            count = sum(1 for _ in func(arr))
            elapsed_time = time.time() - start_time

            status = "✓ OK" if count == expected_count else "✗ ERROR"
            print(f"{name:<20} {elapsed_time:<15.6f} {count:<15} {status}")


def demo_utilities():
    """Demo các hàm tiện ích"""
    print_separator("=")
    print("DEMO 4: CÁC HÀM TIỆN ÍCH")
    print_separator("=")

    arr = [1, 2, 3, 4]
    print(f"\nMảng: {arr}")
    print(f"Số hoán vị có thể: {count_permutations(arr)}")

    print("\n--- Tìm thứ hạng của hoán vị ---")
    test_perms = [
        [1, 2, 3, 4],
        [2, 1, 3, 4],
        [4, 3, 2, 1]
    ]
    for perm in test_perms:
        rank = permutation_rank(perm)
        print(f"Hoán vị {perm} có thứ hạng: {rank}")

    print("\n--- Tìm hoán vị thứ k ---")
    test_ranks = [0, 1, 5, 23]
    for k in test_ranks:
        perm = kth_permutation(arr, k)
        print(f"Hoán vị thứ {k}: {perm}")

    print("\n--- Kiểm tra 2 mảng có phải hoán vị của nhau không ---")
    arr1 = [1, 2, 3]
    arr2 = [3, 1, 2]
    arr3 = [1, 2, 4]
    print(f"{arr1} và {arr2}: {is_permutation(arr1, arr2)}")
    print(f"{arr1} và {arr3}: {is_permutation(arr1, arr3)}")


def demo_backtrack_trace():
    """Demo trace của thuật toán backtracking"""
    print_separator("=")
    print("DEMO 5: TRACE THUẬT TOÁN BACKTRACKING")
    print_separator("=")

    arr = [1, 2, 3]
    print(f"\nTrace quá trình sinh hoán vị của {arr}:\n")

    count = 0
    for perm, depth, action in permutations_backtrack_with_trace(arr):
        indent = "  " * depth
        if action == 'complete':
            count += 1
            print(f"{indent}→ HOÀN THÀNH hoán vị #{count}: {perm}")
        elif action.startswith('add'):
            print(f"{indent}+ {action}")
        elif action.startswith('backtrack'):
            print(f"{indent}← {action}")


def demo_interactive():
    """Demo tương tác với người dùng"""
    print_separator("=")
    print("DEMO 6: CHẾ ĐỘ TƯƠNG TÁC")
    print_separator("=")

    print("\nNhập các số cách nhau bởi dấu cách (ví dụ: 1 2 3)")
    print("Hoặc nhấn Enter để sử dụng mặc định [1, 2, 3, 4]")

    user_input = input("Nhập: ").strip()

    if user_input:
        try:
            arr = [int(x) for x in user_input.split()]
        except ValueError:
            print("Lỗi: Vui lòng nhập các số hợp lệ!")
            return
    else:
        arr = [1, 2, 3, 4]

    print(f"\nĐã chọn mảng: {arr}")
    print(f"Số hoán vị: {count_permutations(arr)}")

    print("\nChọn thuật toán:")
    print("1. Backtracking")
    print("2. Heap's Algorithm")
    print("3. Next Permutation (thứ tự từ điển)")
    print("4. Itertools")

    choice = input("Lựa chọn (1-4): ").strip()

    algorithms = {
        "1": ("Backtracking", permutations_backtrack),
        "2": ("Heap's Algorithm", permutations_heap),
        "3": ("Next Permutation", permutations_next),
        "4": ("Itertools", permutations_itertools)
    }

    if choice not in algorithms:
        print("Lựa chọn không hợp lệ!")
        return

    name, func = algorithms[choice]
    print(f"\n--- Kết quả sử dụng {name} ---\n")

    start_time = time.time()
    result = list(func(arr))
    elapsed_time = time.time() - start_time

    # Hiển thị kết quả
    if len(result) <= 24:
        # Hiển thị tất cả nếu ít hơn 24 hoán vị
        for i, perm in enumerate(result, 1):
            print(f"{i:3d}. {perm}")
    else:
        # Hiển thị 10 hoán vị đầu và 10 hoán vị cuối
        print("10 hoán vị đầu:")
        for i, perm in enumerate(result[:10], 1):
            print(f"{i:3d}. {perm}")

        print(f"\n... (ẩn {len(result) - 20} hoán vị) ...\n")

        print("10 hoán vị cuối:")
        for i, perm in enumerate(result[-10:], len(result) - 9):
            print(f"{i:3d}. {perm}")

    print(f"\nTổng số: {len(result)} hoán vị")
    print(f"Thời gian: {elapsed_time:.6f} giây")


def demo_next_permutation_step():
    """Demo từng bước của thuật toán next permutation"""
    print_separator("=")
    print("DEMO 7: THUẬT TOÁN NEXT PERMUTATION - TỪNG BƯỚC")
    print_separator("=")

    from permutation_algorithms import next_permutation

    arr = [1, 2, 3, 4]
    print(f"Bắt đầu từ: {arr}")
    print("\nCác bước sinh hoán vị kế tiếp:\n")

    count = 1
    print(f"{count:2d}. {arr}")

    # Sinh tối đa 10 hoán vị để minh họa
    for _ in range(9):
        if next_permutation(arr):
            count += 1
            print(f"{count:2d}. {arr}")
        else:
            break

    print("\n... (còn nhiều hoán vị nữa)")


def main():
    """Hàm chính"""
    print("\n" + "=" * 80)
    print(" " * 20 + "DEMO THUẬT TOÁN SINH HOÁN VỊ")
    print("=" * 80)

    demos = [
        ("Sử dụng cơ bản", demo_basic_usage),
        ("Hoán vị chuỗi ký tự", demo_with_strings),
        ("So sánh hiệu suất", demo_performance_comparison),
        ("Các hàm tiện ích", demo_utilities),
        ("Trace Backtracking", demo_backtrack_trace),
        ("Next Permutation từng bước", demo_next_permutation_step),
        ("Chế độ tương tác", demo_interactive)
    ]

    while True:
        print("\n" + "=" * 80)
        print("MENU CHÍNH:")
        for i, (name, _) in enumerate(demos, 1):
            print(f"  {i}. {name}")
        print(f"  0. Thoát")
        print("=" * 80)

        choice = input("\nChọn demo (0-{}): ".format(len(demos))).strip()

        if choice == "0":
            print("\nCảm ơn bạn đã sử dụng! Tạm biệt!")
            break

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(demos):
                print()
                demos[idx][1]()
                input("\nNhấn Enter để tiếp tục...")
            else:
                print("Lựa chọn không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập một số!")


if __name__ == "__main__":
    main()
