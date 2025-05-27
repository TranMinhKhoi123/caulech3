# Hướng dẫn cài đặt thư viện cần thiết:
# 1. Mở Command Prompt hoặc Terminal
# 2. Chạy lệnh sau để cài đặt thư viện:
#    pip install eth-account mnemonic

# Import các thư viện cần thiết
from eth_account import Account
from mnemonic import Mnemonic
import os
from datetime import datetime

def generate_wallet():
    # Tạo đối tượng Mnemonic
    mnemo = Mnemonic("english")
    
    # Sinh cụm từ Mnemonic ngẫu nhiên (12 từ)
    mnemonic_words = mnemo.generate(strength=128)
    
    # Tạo seed từ cụm từ Mnemonic
    seed = mnemo.to_seed(mnemonic_words)
    
    # Tạo tài khoản từ seed
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic_words)
    
    # Lấy private key và địa chỉ ví
    private_key = account.key.hex()
    wallet_address = account.address
    
    return mnemonic_words, private_key, wallet_address

def save_wallet_info(mnemonic, private_key):
    # Tạo tên file với timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"wallet_info_{timestamp}.txt"
    
    # Lưu thông tin vào file
    with open(filename, "w") as f:
        f.write("CẢNH BÁO: Giữ bí mật các thông tin này!\n\n")
        f.write(f"Cụm từ Mnemonic:\n{mnemonic}\n\n")
        f.write(f"Private Key:\n{private_key}\n")
    
    return filename

def main():
    print("Đang tạo ví mới...\n")
    
    # Tạo ví mới
    mnemonic, private_key, address = generate_wallet()
    
    # Lưu thông tin vào file
    filename = save_wallet_info(mnemonic, private_key)
    
    # Hiển thị thông tin
    print(f"Đã tạo ví thành công!\n")
    print(f"Địa chỉ ví của bạn:\n{address}\n")
    print(f"Thông tin ví đã được lưu vào file: {filename}")
    print("\nLƯU Ý QUAN TRỌNG:")
    print("1. Giữ an toàn file thông tin ví của bạn")
    print("2. Không chia sẻ Private Key với bất kỳ ai")
    print("3. Sao lưu cụm từ Mnemonic ở nơi an toàn")

if __name__ == "__main__":
    main()