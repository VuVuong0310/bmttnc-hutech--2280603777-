from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()  # Khởi tạo SHA3-256 hash
    sha3_hash.update(message)  # Cập nhật dữ liệu vào hash
    return sha3_hash.digest()  # Trả về giá trị băm

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')  # Nhận đầu vào và mã hóa thành bytes
    hashed_text = sha3(text)  # Gọi hàm băm

    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))  # In chuỗi gốc
    print("SHA-3 Hash:", hashed_text.hex())  # In kết quả hash ở dạng hex

if __name__ == "__main__":  # Sửa lỗi cú pháp kiểm tra main
    main()
