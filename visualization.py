"""
TRỰC QUAN HÓA THUẬT TOÁN SINH HOÁN VỊ
Module này cung cấp các công cụ để trực quan hóa quá trình sinh hoán vị
"""

import time
import sys
from typing import List, Any
from permutation_algorithms import (
    permutations_backtrack_with_trace,
    permutations_next,
    next_permutation
)


class Colors:
    """Màu sắc cho terminal (ANSI escape codes)"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'


def clear_screen():
    """Xóa màn hình (cross-platform)"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def visualize_backtracking(arr: List[Any], delay: float = 0.5):
    """
    Trực quan hóa quá trình backtracking

    Args:
        arr: Mảng cần sinh hoán vị
        delay: Thời gian delay giữa các bước (giây)
    """
    clear_screen()
    print(f"{Colors.BOLD}{Colors.CYAN}=== TRỰC QUAN HÓA THUẬT TOÁN BACKTRACKING ==={Colors.RESET}\n")
    print(f"Mảng đầu vào: {arr}")
    print(f"Số hoán vị: {len(arr)}! = {factorial_simple(len(arr))}\n")
    print(f"{Colors.YELLOW}Chú thích:{Colors.RESET}")
    print(f"  {Colors.GREEN}+ Thêm phần tử{Colors.RESET}")
    print(f"  {Colors.BLUE}✓ Hoàn thành hoán vị{Colors.RESET}")
    print(f"  {Colors.RED}← Quay lui{Colors.RESET}\n")

    input("Nhấn Enter để bắt đầu...")

    completed_count = 0

    for perm, depth, action in permutations_backtrack_with_trace(arr):
        indent = "  " * depth

        # Tạo visualization cho trạng thái hiện tại
        visual = create_array_visual(perm, arr)

        if action == 'complete':
            completed_count += 1
            print(f"\n{indent}{Colors.BLUE}✓ HOÀN THÀNH #{completed_count}: {visual}{Colors.RESET}")
        elif action.startswith('add'):
            element = action.split()[1]
            print(f"{indent}{Colors.GREEN}+ Thêm {element}: {visual}{Colors.RESET}")
        elif action.startswith('backtrack'):
            print(f"{indent}{Colors.RED}← Quay lui: {visual}{Colors.RESET}")

        time.sleep(delay)

    print(f"\n{Colors.BOLD}Tổng cộng: {completed_count} hoán vị{Colors.RESET}")


def visualize_next_permutation(arr: List[Any], delay: float = 1.0):
    """
    Trực quan hóa thuật toán Next Permutation

    Args:
        arr: Mảng cần sinh hoán vị
        delay: Thời gian delay giữa các hoán vị (giây)
    """
    clear_screen()
    print(f"{Colors.BOLD}{Colors.CYAN}=== TRỰC QUAN HÓA THUẬT TOÁN NEXT PERMUTATION ==={Colors.RESET}\n")

    arr = sorted(arr)
    print(f"Bắt đầu từ hoán vị nhỏ nhất: {arr}\n")

    input("Nhấn Enter để bắt đầu...")
    print()

    count = 1
    print(f"{count:3d}. {create_array_visual(arr, arr, highlight_all=True)}")
    time.sleep(delay)

    while next_permutation(arr):
        count += 1
        print(f"{count:3d}. {create_array_visual(arr, arr, highlight_all=True)}")
        time.sleep(delay)

    print(f"\n{Colors.BOLD}Tổng cộng: {count} hoán vị{Colors.RESET}")


def visualize_next_permutation_detailed(arr: List[Any]):
    """
    Trực quan hóa chi tiết từng bước của thuật toán Next Permutation

    Args:
        arr: Mảng cần sinh hoán vị
    """
    def find_pivot(a):
        """Tìm vị trí pivot (i lớn nhất sao cho a[i] < a[i+1])"""
        i = len(a) - 2
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1
        return i

    def find_successor(a, i):
        """Tìm vị trí successor (j lớn nhất sao cho a[i] < a[j])"""
        j = len(a) - 1
        while a[j] <= a[i]:
            j -= 1
        return j

    clear_screen()
    print(f"{Colors.BOLD}{Colors.CYAN}=== NEXT PERMUTATION - CHI TIẾT TỪNG BƯỚC ==={Colors.RESET}\n")

    arr = sorted(arr)
    print(f"Hoán vị ban đầu: {arr}\n")

    input("Nhấn Enter để xem bước tiếp theo...")

    count = 0
    max_iterations = 10  # Giới hạn số bước để demo

    while count < max_iterations:
        count += 1
        print(f"\n{Colors.BOLD}{'=' * 60}{Colors.RESET}")
        print(f"{Colors.BOLD}Bước {count}: Tìm hoán vị kế tiếp{Colors.RESET}")
        print(f"{Colors.BOLD}{'=' * 60}{Colors.RESET}\n")

        print(f"Hoán vị hiện tại: {create_array_visual(arr, arr, highlight_all=True)}\n")

        # Bước 1: Tìm pivot
        print(f"{Colors.YELLOW}Bước 1: Tìm i lớn nhất sao cho arr[i] < arr[i+1]{Colors.RESET}")
        pivot = find_pivot(arr)

        if pivot < 0:
            print(f"{Colors.RED}→ Không tìm thấy! Đây là hoán vị cuối cùng.{Colors.RESET}")
            break

        print(f"{Colors.GREEN}→ Tìm thấy i = {pivot}, arr[{pivot}] = {arr[pivot]}{Colors.RESET}")
        print(f"   {create_array_with_highlight(arr, [pivot], Colors.GREEN)}\n")

        # Bước 2: Tìm successor
        print(f"{Colors.YELLOW}Bước 2: Tìm j lớn nhất sao cho arr[i] < arr[j]{Colors.RESET}")
        successor = find_successor(arr, pivot)
        print(f"{Colors.GREEN}→ Tìm thấy j = {successor}, arr[{successor}] = {arr[successor]}{Colors.RESET}")
        print(f"   {create_array_with_highlight(arr, [pivot, successor], Colors.CYAN)}\n")

        # Bước 3: Hoán đổi
        print(f"{Colors.YELLOW}Bước 3: Hoán đổi arr[{pivot}] và arr[{successor}]{Colors.RESET}")
        arr[pivot], arr[successor] = arr[successor], arr[pivot]
        print(f"{Colors.GREEN}→ Sau hoán đổi: {create_array_visual(arr, arr, highlight_all=True)}{Colors.RESET}\n")

        # Bước 4: Đảo ngược
        print(f"{Colors.YELLOW}Bước 4: Đảo ngược đoạn từ vị trí {pivot+1} đến cuối{Colors.RESET}")
        arr[pivot + 1:] = reversed(arr[pivot + 1:])
        print(f"{Colors.GREEN}→ Kết quả: {create_array_visual(arr, arr, highlight_all=True)}{Colors.RESET}\n")

        input("Nhấn Enter để tiếp tục...")

    if count >= max_iterations:
        print(f"\n{Colors.YELLOW}(Đã hiển thị {max_iterations} bước đầu tiên...){Colors.RESET}")


def create_array_visual(current: List[Any], full: List[Any], highlight_all: bool = False) -> str:
    """
    Tạo visualization cho mảng

    Args:
        current: Mảng hiện tại (có thể chưa đầy đủ)
        full: Mảng đầy đủ (để biết kích thước)
        highlight_all: Nếu True, highlight tất cả phần tử

    Returns:
        Chuỗi visualization
    """
    result = "["
    for i in range(len(full)):
        if i < len(current):
            if highlight_all:
                result += f"{Colors.GREEN}{current[i]}{Colors.RESET}"
            else:
                result += f"{Colors.CYAN}{current[i]}{Colors.RESET}"
        else:
            result += f"{Colors.WHITE}__{Colors.RESET}"

        if i < len(full) - 1:
            result += ", "

    result += "]"
    return result


def create_array_with_highlight(arr: List[Any], indices: List[int], color: str) -> str:
    """
    Tạo visualization cho mảng với highlight các vị trí cụ thể

    Args:
        arr: Mảng
        indices: Các vị trí cần highlight
        color: Màu sắc để highlight

    Returns:
        Chuỗi visualization
    """
    result = "["
    for i in range(len(arr)):
        if i in indices:
            result += f"{color}{arr[i]}{Colors.RESET}"
        else:
            result += str(arr[i])

        if i < len(arr) - 1:
            result += ", "

    result += "]"
    return result


def visualize_tree(arr: List[Any], max_depth: int = 3):
    """
    Vẽ cây quyết định của thuật toán backtracking (text-based)

    Args:
        arr: Mảng cần sinh hoán vị
        max_depth: Độ sâu tối đa để vẽ (tránh quá dài)
    """
    clear_screen()
    print(f"{Colors.BOLD}{Colors.CYAN}=== CÂY QUYẾT ĐỊNH BACKTRACKING ==={Colors.RESET}\n")
    print(f"Mảng: {arr}")
    print(f"(Chỉ hiển thị {max_depth} cấp đầu tiên)\n")

    def draw_tree(depth, current, used, prefix=""):
        if depth > max_depth:
            return

        if len(current) == len(arr):
            print(f"{prefix}└─ {Colors.GREEN}{current}{Colors.RESET}")
            return

        available = [arr[i] for i in range(len(arr)) if not used[i]]

        for idx, elem in enumerate(available):
            is_last = (idx == len(available) - 1)

            # Tìm vị trí thực của elem trong arr
            real_idx = next(i for i in range(len(arr)) if arr[i] == elem and not used[i])

            new_current = current + [elem]
            new_used = used.copy()
            new_used[real_idx] = True

            connector = "└─" if is_last else "├─"
            extension = "   " if is_last else "│  "

            print(f"{prefix}{connector} {Colors.CYAN}{elem}{Colors.RESET} {Colors.WHITE}{new_current}{Colors.RESET}")

            draw_tree(depth + 1, new_current, new_used, prefix + extension)

    draw_tree(1, [], [False] * len(arr))


def factorial_simple(n: int) -> int:
    """Tính giai thừa đơn giản"""
    if n <= 1:
        return 1
    return n * factorial_simple(n - 1)


def demo_menu():
    """Menu chính cho visualization"""
    while True:
        clear_screen()
        print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}   TRỰC QUAN HÓA THUẬT TOÁN SINH HOÁN VỊ{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}\n")

        print("Chọn chế độ visualization:\n")
        print("  1. Backtracking - Xem quá trình từng bước")
        print("  2. Next Permutation - Xem các hoán vị theo thứ tự")
        print("  3. Next Permutation - Chi tiết từng bước")
        print("  4. Cây quyết định Backtracking")
        print("  0. Thoát\n")

        choice = input("Lựa chọn của bạn: ").strip()

        if choice == "0":
            print("\nTạm biệt!")
            break

        # Nhập mảng
        print("\nNhập các phần tử cách nhau bởi dấu cách")
        print("(Ví dụ: 1 2 3 hoặc A B C)")
        print("Nhấn Enter để sử dụng mặc định [1, 2, 3]")

        user_input = input("Nhập: ").strip()

        if user_input:
            try:
                # Thử parse số
                arr = [int(x) for x in user_input.split()]
            except ValueError:
                # Nếu không phải số, dùng chuỗi
                arr = user_input.split()
        else:
            arr = [1, 2, 3]

        if choice == "1":
            print("\nNhập thời gian delay (giây) giữa các bước:")
            print("(Khuyến nghị: 0.3 - 1.0)")
            try:
                delay = float(input("Delay: ").strip() or "0.5")
            except ValueError:
                delay = 0.5
            visualize_backtracking(arr, delay)
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "2":
            print("\nNhập thời gian delay (giây) giữa các hoán vị:")
            print("(Khuyến nghị: 0.5 - 1.5)")
            try:
                delay = float(input("Delay: ").strip() or "1.0")
            except ValueError:
                delay = 1.0
            visualize_next_permutation(arr, delay)
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "3":
            visualize_next_permutation_detailed(arr)
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "4":
            print("\nNhập độ sâu tối đa để hiển thị:")
            print("(Khuyến nghị: 2-4, tùy thuộc kích thước màn hình)")
            try:
                max_depth = int(input("Độ sâu: ").strip() or "3")
            except ValueError:
                max_depth = 3
            visualize_tree(arr, max_depth)
            input("\nNhấn Enter để quay lại menu...")

        else:
            print(f"\n{Colors.RED}Lựa chọn không hợp lệ!{Colors.RESET}")
            time.sleep(1)


if __name__ == "__main__":
    try:
        demo_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Đã dừng bởi người dùng. Tạm biệt!{Colors.RESET}")
        sys.exit(0)
