import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tour Dashboard")
root.geometry("1000x600")
root.configure(bg="#f5f6fa")

# ===== SIDEBAR =====
sidebar = tk.Frame(root, bg="#2c3e50", width=200)
sidebar.pack(side="left", fill="y")

menu_items = ["Dashboard", "Tour", "Đơn hàng", "Khách", "Tài chính", "Báo cáo", "Cấu hình"]

for item in menu_items:
    btn = tk.Button(sidebar, text=item, fg="white", bg="#2c3e50",
                    bd=0, anchor="w", padx=20, pady=10)
    btn.pack(fill="x")

# ===== HEADER =====
header = tk.Frame(root, bg="#2980b9", height=60)
header.pack(side="top", fill="x")

search = tk.Entry(header, width=40)
search.insert(0, "Tìm kiếm tour, đơn hàng...")
search.pack(side="left", padx=20, pady=15)

user_label = tk.Label(header, text="User: Admin", bg="#2980b9", fg="white")
user_label.pack(side="right", padx=20)

# ===== MAIN CONTENT =====
main = tk.Frame(root, bg="#ecf0f1")
main.pack(fill="both", expand=True)

# Banner
banner = tk.Label(main, text="KHÁM PHÁ VỊNH HẠ LONG - 3 ngày 2 đêm",
                  bg="#3498db", fg="white", font=("Arial", 16, "bold"), pady=20)
banner.pack(fill="x", padx=10, pady=10)

# Nội dung chia 2 cột
content = tk.Frame(main, bg="#ecf0f1")
content.pack(fill="both", expand=True, padx=10)

left = tk.Frame(content, bg="white", bd=1, relief="solid")
left.pack(side="left", fill="both", expand=True, padx=5)

right = tk.Frame(content, bg="white", width=250, bd=1, relief="solid")
right.pack(side="right", fill="y", padx=5)

# ===== LEFT: LỊCH TRÌNH =====
tk.Label(left, text="Lịch trình", font=("Arial", 14, "bold"), bg="white").pack(anchor="w", padx=10, pady=10)

schedule = [
    "Ngày 1: Nhận phòng",
    "13:00 - Thăm vịnh",
    "13:00 - Ăn trưa",
    "13:00 - Tự do",
    "Ngày 2: Tham quan",
    "Ngày 3: Kết thúc"
]

for item in schedule:
    tk.Label(left, text=item, bg="white").pack(anchor="w", padx=20)

# ===== RIGHT: ĐẶT CHỖ =====
tk.Label(right, text="WIDGET ĐẶT CHỖ", font=("Arial", 12, "bold"), bg="white").pack(pady=10)

tk.Label(right, text="Date:", bg="white").pack(anchor="w", padx=10)
date_entry = tk.Entry(right)
date_entry.insert(0, "10/05/2023")
date_entry.pack(padx=10, pady=5)

tk.Label(right, text="Người lớn:", bg="white").pack(anchor="w", padx=10)
adult_spin = tk.Spinbox(right, from_=1, to=10)
adult_spin.pack(padx=10, pady=5)

tk.Label(right, text="Trẻ em:", bg="white").pack(anchor="w", padx=10)
child_spin = tk.Spinbox(right, from_=0, to=10)
child_spin.pack(padx=10, pady=5)

book_btn = tk.Button(right, text="ĐẶT NGAY", bg="#e74c3c", fg="white")
book_btn.pack(pady=15, padx=10, fill="x")

# ===== RUN =====
root.mainloop()