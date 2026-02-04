# assignment-3
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1
while True:
    inch = float(input("Nhập số inch: "))
    if inch < 0:
        print("Kết thúc chương trình.")
        break
    cm = inch * 2.54
    print(f"{inch} inch = {cm} cm")
numbers = []

while True:
    s = input("Nhập một số (nhấn Enter để thoát): ")
    if s == "":
        break
    numbers.append(float(s))

if numbers:
    print("Số nhỏ nhất:", min(numbers))
    print("Số lớn nhất:", max(numbers))
else:
    print("Không có số nào được nhập.")
import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Đoán số (1-10): "))
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct")
        break
correct_user = "python"
correct_pass = "rules"
attempts = 0

while attempts < 5:
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")

    if username == correct_user and password == correct_pass:
        print("Welcome")
        break
    else:
        print("Sai thông tin đăng nhập.")
        attempts += 1

if attempts == 5:
    print("Access denied")
    def middle_char(s):
    n = len(s)
    if n % 2 == 0:
        return s[n//2 - 1 : n//2 + 1]
    else:
        return s[n//2]

print(middle_char("Python"))   # th
print(middle_char("Code"))     # de
def viet_tat(cum_tu):
    print(viet_tat("vat the la khong xac dinh"))

    ket_qua = ""
    for tu in cum_tu.split():
        ket_qua += UFO.upper()
    return ket_qua

