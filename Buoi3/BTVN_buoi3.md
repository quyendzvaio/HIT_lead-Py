# BỘ BÀI TẬP PYTHON – LIST, STRING, SET, TUPLE


---

##  BÀI 1 – XỬ LÝ DANH SÁCH NÂNG CAO

###  Đề bài
Cho một danh sách số nguyên `numbers`.  
Thực hiện các yêu cầu sau:

1. Loại bỏ các số trùng lặp **nhưng vẫn giữ nguyên thứ tự xuất hiện đầu tiên**.  
2. Tạo danh sách mới:  
   - Số **chẵn** → bình phương  
   - Số **lẻ** → lập phương.  
3. Tính **trung bình cộng** của các phần tử ở **vị trí chỉ số chẵn** trong danh sách ban đầu.  
4. Sắp xếp danh sách theo **giá trị tuyệt đối tăng dần**, **không dùng** `sort()` hoặc `sorted()`.

###  Ví dụ minh họa
```python
numbers = [2, 3, 2, -4, 3, 5]

1. Sau khi loại trùng: [2, 3, -4, 5]
2. List mới: [4, 27, 16, 125]
3. Trung bình vị trí chẵn: (2 + -4) / 2 = -1.0
4. Sắp xếp theo abs: [-4, 2, 3, 5] 
```

##  Bai2: Xử lý chuỗi phức tạp
### Đề bài:

Viết chương trình nhận vào một chuỗi văn bản bất kỳ (có thể chứa dấu, chữ hoa/thường, ký tự đặc biệt).
Thực hiện:

Chuẩn hóa chuỗi:

1. Loại bỏ các ký tự không phải chữ cái hoặc khoảng trắng

2. Chuyển về chữ thường

3. Đếm số nguyên âm và phụ âm trong chuỗi (chỉ tính ký tự chữ).

4. Tách chuỗi thành danh sách từ, sau đó đảo ngược từng từ (không đảo thứ tự các từ).

5. Kiểm tra xem chuỗi có phải là palindrome không (bỏ qua khoảng trắng, hoa/thường).

6. In kết quả.
### Ví dụ:
```python
Input: "Able , was I saw Elba!"
→ Chuẩn hóa: "able was i saw elba"
→ Nguyên âm: 8, Phụ âm: 8
→ Đảo từng từ: ['elbA', 'saw', 'I', 'was', 'ablE']
→ Palindrome: True
```
## Bài 3 – Tổng hợp 
### Đề bài:

Nhập vào một đoạn văn bản.
1. Hãy thực hiện các thao tác thống kê sau mà không dùng dict:

2. Tách tất cả các từ, chuyển hết về chữ thường.

3. Tạo một list các từ duy nhất (không trùng), vẫn theo thứ tự xuất hiện.

4. Đếm số lần xuất hiện của từng từ (bằng cách dùng count() của list hoặc vòng lặp for).

5. In ra từ có tần suất xuất hiện cao nhất, từ dài nhất, và tổng số ký tự trong tất cả các từ.

6. In ra danh sách các từ được sắp xếp theo độ dài giảm dần, nhưng không dùng sort().

## Bài 4 – Kết hợp Set, Tuple, List và String
### Đề bài:

Cho một đoạn văn bản chứa danh sách sinh viên và điểm, ví dụ:
```python
"An:8.5, Binh:7.0, An:9.0, Cuong:6.5, Binh:8.0, Dung:7.5"
```
Thực hiện:

1. Tách dữ liệu thành list các tuple (tên, điểm).
→ [('An', 8.5), ('Binh', 7.0), ('An', 9.0), ...]

2. Tạo set chứa các tên duy nhất.

3. Với mỗi tên, tính điểm trung bình của sinh viên đó (chỉ dùng list, set, for, if).

4. Tìm sinh viên có điểm trung bình cao nhất, thấp nhất.

5. Tạo tuple chứa danh sách sắp xếp giảm dần theo điểm trung bình.
(Không dùng sorted() — tự cài đặt sắp xếp thủ công bằng hoán đổi phần tử.)

### VD:
```python
An: (8.5 + 9.0)/2 = 8.75
Binh: (7.0 + 8.0)/2 = 7.5
Cuong: 6.5
Dung: 7.5
→ Sinh viên cao nhất: An - 8.75
→ Thấp nhất: Cuong - 6.5
→ Sắp xếp: [('An', 8.75), ('Binh', 7.5), ('Dung', 7.5), ('Cuong', 6.5)]
```