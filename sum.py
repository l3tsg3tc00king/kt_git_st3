def sum(a, b):
    """Hàm trả về tổng của a và b"""
    return a + b

if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH TÍNH TỔNG ---")
    # Nhập dữ liệu (float)
    a = float(input("Mời bạn nhập số a: "))
    b = float(input("Mời bạn nhập số b: "))
    
    # In kết quả
    print(f"Kết quả phép cộng {a} + {b} là: {sum(a, b)}")