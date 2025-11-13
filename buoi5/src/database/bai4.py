while True:
    try:
        s = input("Nhập vào chuỗi số nguyên: ")
        if not s.strip():
            print("Bạn chưa nhập gì cả, vui lòng nhập lại.")
            continue
        if " " in s:
            ls = s.strip().split()
        else:
            ls = list(s.strip())
        if not all(ch.isdigit() for ch in ls):
            print("Dữ liệu không hợp lệ! Vui lòng chỉ nhập số.")
            continue
        break
    except ValueError as e:
        print("Dữ liệu bạn nhập không hợp lệ:", e)

max_len = 0
max_sub = []
current_sub = []

for num in ls:
    if num not in current_sub:
        current_sub.append(num)
    else:
        idx = current_sub.index(num)
        current_sub = current_sub[idx+1:]
        current_sub.append(num)

    if len(current_sub) > max_len:
        max_len = len(current_sub)
        max_sub = current_sub.copy()

print("Độ dài đoạn con dài nhất là:", max_len)
print("Đoạn con đó là:", tuple(max_sub))
