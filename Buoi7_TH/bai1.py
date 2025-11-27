# 🎯 Bài 1 — Quản lý thư viện sách (Library Manager)

# Yêu cầu:

# Tạo class Book (id, title, author, year, status)

# Class Library quản lý danh sách sách

# Chức năng:

# Thêm sách

# Xóa sách

# Tìm kiếm theo tiêu đề / tác giả

# Mượn sách (đổi status → borrowed)

# Trả sách

# Xử lý trường hợp user mượn sách đã mượn rồi.

# OOP bắt buộc dùng:
# Class, collection, method, encapsulation.

class Book:
    def __init__(self, book_id, title, author, year):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = "available"   

    # Getter
    @property
    def id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def status(self):
        return self.__status

    def borrow(self):
        if self.__status == "borrowed":
            raise Exception("Sách đã được mượn!")
        self.__status = "borrowed"

    def return_book(self):
        if self.__status == "available":
            raise Exception("Sách đang ở thư viện, không cần trả.")
        self.__status = "available"

    def __str__(self):
        return f"[{self.__book_id}] {self.__title} - {self.__author} ({self.__status})"

class Library:
    def __init__(self):
        self.books = {} 

    # Thêm sách
    def add_book(self, book: Book):
        if book.id in self.books:
            raise Exception("ID sách đã tồn tại!")
        self.books[book.id] = book

    # Xóa sách
    def remove_book(self, book_id):
        if book_id not in self.books:
            raise Exception("Không tìm thấy sách để xoá.")
        del self.books[book_id]

    # Tìm kiếm theo tiêu đề
    def search_by_title(self, keyword):
        result = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower():
                result.append(book)
        return result

    # Tìm theo tác giả
    def search_by_author(self, keyword):
        result = []
        for book in self.books.values():
            if keyword.lower() in book.author.lower():
                result.append(book)
        return result

    # Mượn sách
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise Exception("Không tìm thấy sách.")
        book = self.books[book_id]
        book.borrow()

    # Trả sách
    def return_book(self, book_id):
        if book_id not in self.books:
            raise Exception("Không tìm thấy sách.")
        book = self.books[book_id]
        book.return_book()

    # In danh sách sách
    def show_all_books(self):
        for b in self.books.values():
            print(b)

if __name__ == "__main__":
    lib = Library()

    # Thêm sách
    lib.add_book(Book(1, "Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 1941))
    lib.add_book(Book(2, "Lão Hạc", "Nam Cao", 1943))
    lib.add_book(Book(3, "Sherlock Holmes", "Arthur Conan Doyle", 1892))

    print("=== Danh sách ban đầu ===")
    lib.show_all_books()

    print("\n=== Tìm kiếm theo tiêu đề 'lão' ===")
    for b in lib.search_by_title("lão"):
        print(b)

    print("\n=== Mượn sách ID 1 ===")
    lib.borrow_book(1)
    lib.show_all_books()

    print("\n=== Thử mượn lại ID 1 (lỗi) ===")
    try:
        lib.borrow_book(1)
    except Exception as e:
        print("Lỗi:", e)

    print("\n=== Trả sách ID 1 ===")
    lib.return_book(1)
    lib.show_all_books()
