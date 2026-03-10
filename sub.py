def sub(a, b):
    """Hàm trả về hiệu của a và b"""
    return a - b

if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH TÍNH HIỆU ---")
    # Nhập dữ liệu (float)
    a = float(input("Mời bạn nhập số a: "))
    b = float(input("Mời bạn nhập số b: "))
    
    # In kết quả
    print(f"Kết quả phép trừ {a} - {b} là: {sub(a, b)}")