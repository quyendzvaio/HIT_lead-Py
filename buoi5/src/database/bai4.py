while True:
    try:
        s = input("Nhập vào chuỗi số nguyên (cách nhau bởi dấu cách): ")
        if not s.strip():
            print("Bạn chưa nhập gì cả, vui lòng nhập lại.")
            continue
        ls = s.strip().split()
        break
    except ValueError as e:
        print("Dữ liệu bạn nhập không hợp lệ:", e)

def timkiemdoandai(ls):
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

    return max_len, max_sub

count_list2, new_list1 = timkiemdoandai(ls)
print("Độ dài đoạn con dài nhất là:", count_list2)
print("Đoạn con đó là:", tuple(new_list1))
