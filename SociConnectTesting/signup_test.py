import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# đọc dữ liệu
with open(file='./Data_Testing/data_signup.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)


# Xác định chỉ số của các cột
username_index = headers.index('Username')
email_index = headers.index('Email')
password_index = headers.index('Password')
confirm_password_index = headers.index('Confirm Password')

# Trích xuất các giá trị username, email, password và confirm password
# for row in data:
#     username = row[username_index]
#     email = row[email_index]
#     password = row[password_index]
#     confirm_password = row[confirm_password_index]
#     print(f"Username: {username}")
#     print(f"Email: {email}")
#     print(f"Password: {password}")
#     print(f"Confirm Password: {confirm_password}")
#     print()

# print(data)




# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Tối đa hóa cửa sổ trình duyệt
driver.maximize_window()

# Mở trang web của ứng dụng
driver.get('http://127.0.0.1:8000/signup')
sleep(5)

# Định danh các phần tử trên trang web
username_input = driver.find_element(By.ID, 'signup-username')
email_input = driver.find_element(By.ID, 'signup-email')
password_input = driver.find_element(By.ID, 'signup-password')
confirm_password_input = driver.find_element(By.ID, 'signup-confirm-password')
register_button = driver.find_element(By.ID, 'signup-submit')

for i in range(len(data)):
    username_input.send_keys(data[i][1])
    email_input.send_keys(data[i][2])
    password_input.send_keys(data[i][3])
    confirm_password_input.send_keys(data[i][4])


    # Nhấp vào nút Đăng ký
    register_button.click()
    sleep(2)

    # nếu đăng ký thành công thì tự đăng nhập vào trang chủ
    home = driver.find_element(By.ID, 'settings-home')
    home.click()
    if home is not None:

        avatar = driver.find_element(By.ID, 'index-avatar')
        avatar.click()
        sleep(1)

        logout = driver.find_element(By.ID, 'index-logout')
        logout.click()
        print("Đăng ký thành công!!!")
    else:
        print("Đăng ký không thành công!")


# Đóng trình duyệt
driver.quit()
