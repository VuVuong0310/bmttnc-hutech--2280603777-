import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)  # Khởi tạo BLAKE2b với độ dài 64 bytes
    blake2_hash.update(message)  # Cập nhật dữ liệu vào hash
    return blake2_hash.digest()  # Trả về giá trị băm

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')  # Nhận đầu vào và mã hóa thành bytes
    hashed_text = blake2(text)  # Gọi hàm băm

    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))  # In chuỗi gốc
    print("BLAKE2 Hash:", hashed_text.hex())  # In kết quả hash ở dạng hex

if __name__ == "__main__":  # Sửa lỗi cú pháp
    main()
