
import re
# input_string = input("Enter Email address : ")
# regex_pattern = r'\d{3}'
# result = bool(re.match(regex_pattern, input_string))
# print("Valid Email address" if result else "Invalid Email address")
with open('C:\\Users\\Lenovo\\Python projects\\Projects\\Borzisty\\PZ_14\\hotline.txt', 'r+', encoding='utf-8') as f:
    while True:
        print(re.search(r'\d{11}$', f.readline()))
        next(f)