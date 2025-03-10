import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow  # Đảm bảo tên class trong UI đúng
import requests

class MyApp(QMainWindow):
    def __init__(self):  # Sửa _init__ thành __init__
        super().__init__()
        self.ui = Ui_MainWindow()  # Sửa lỗi khai báo UI
        self.ui.setupUi(self)
        
        # Kết nối các nút với phương thức API
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)  # Sửa lỗi requests.get(url)
            if response.status_code == 200:
                data = response.json()  # Sửa lỗi data response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # Sửa lỗi khoảng trắng
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API:", response.text)
        except requests.exceptions.RequestException as e:  # Sửa lỗi thiếu dấu `:`
            print("Error:", str(e))

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(),
            "public_key": self.ui.txt_pubkey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_ciphertext.setText(data["cipher_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption Successful")
                msg.exec_()
            else:
                print("Error while calling API:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "cipher_text": self.ui.txt_ciphertext.toPlainText(),
            "private_key": self.ui.txt_privkey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setText(data["plain_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption Successful")
                msg.exec_()
            else:
                print("Error while calling API:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_plaintext.toPlainText(),
            "private_key": self.ui.txt_privkey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_signature.setText(data["signature"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signing Successful")
                msg.exec_()
            else:
                print("Error while calling API:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_plaintext.toPlainText(),
            "signature": self.ui.txt_signature.toPlainText(),
            "public_key": self.ui.txt_pubkey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Verification: " + ("Valid" if data["valid"] else "Invalid"))
                msg.exec_()
            else:
                print("Error while calling API:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
