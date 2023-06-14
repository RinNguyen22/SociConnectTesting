import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os


def convert_apsolute_path(relative_path):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    absolute_path = os.path.join(BASEDIR, relative_path)
    return absolute_path

images = ["./Data_Testing/images/img1.jpg", "./Data_Testing/images/img2.jpg", "./Data_Testing/images/img3.jpg",
            "./Data_Testing/images/img4.jpg", "./Data_Testing/images/img5.jpg", "./Data_Testing/images/img6.jpg",
            "./Data_Testing/images/img7.png", "./Data_Testing/images/img8.jpg", "./Data_Testing/images/img9.jpg",
            "./Data_Testing/images/img10.jpg"]

images_path = [convert_apsolute_path(image_path) for image_path in images]
print(images_path)

# đọc dữ liệu
with open(file='./Data_Testing/data_login.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)


# Xác định chỉ số của các cột
username_index = headers.index('Username')
email_index = headers.index('Password')
password_index = headers.index('Email')
confirm_password_index = headers.index('Caption')

#Trích xuất các giá trị username, email, password và confirm password
for row in data:
    username = row[username_index]
    email = row[email_index]
    password = row[password_index]
    confirm_password = row[confirm_password_index]
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Confirm Password: {confirm_password}")
    print()

print(data)




# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Tối đa hóa cửa sổ trình duyệt
driver.maximize_window()

# Mở trang web của ứng dụng
driver.get('http://127.0.0.1:8000/signin')
sleep(5)

# username_input = driver.find_element(By.ID, 'signin-username')
# password_input = driver.find_element(By.ID, 'signin-password')
# login_button = driver.find_element(By.ID, 'signin-submit')

# BASEDIR = os.path.abspath(os.path.dirname(__file__))

# # Đường dẫn tương đối đến file ảnh
# relative_path = "./Data_Testing/images/img1.jpg"

# # Kết hợp BASEDIR và đường dẫn tương đối
# absolute_path = os.path.join(BASEDIR, relative_path)

# username_input.send_keys("test")
# password_input.send_keys("test1234")
# sleep(1)

# # Nhấp vào nút Đăng nhập
# login_button.click()
# sleep(2)

# upload = driver.find_element(By.ID, "index-uploat-btn")
# upload.click()
# sleep(2)

# # Định vị phần tử <input> cho việc tải lên tập tin hình ảnh
# choose_file = driver.find_element(By.XPATH, "//input[@type='file']")

# # Gửi đường dẫn đến tập tin hình ảnh cho phần tử <input>
# choose_file.send_keys(absolute_path)
# sleep(2)

# caption_elem = driver.find_element(By.ID, 'index-caption')
# caption_elem.send_keys("Hi")
# sleep(2)

# submit_elem = driver.find_element(By.ID, 'index-upload-submit')
# submit_elem.click()

# sleep(5)




for i in range(len(data)):
    # Định danh các phần tử trên trang web
    username_input = driver.find_element(By.ID, 'signin-username')
    password_input = driver.find_element(By.ID, 'signin-password')
    login_button = driver.find_element(By.ID, 'signin-submit')
    sleep(1)
    
    username_input.send_keys(data[i][1])
    password_input.send_keys(data[i][2])
    sleep(1)

    # Nhấp vào nút Đăng nhập
    login_button.click()
    sleep(2)

    upload = driver.find_element(By.ID, "index-uploat-btn")
    if upload is not None:
        upload.click()
        sleep(2)

        # Định vị phần tử <input> cho việc tải lên tập tin hình ảnh
        choose_file = driver.find_element(By.XPATH, "//input[@type='file']")

        # Gửi đường dẫn đến tập tin hình ảnh cho phần tử <input>
        choose_file.send_keys(images_path[i])
        sleep(2)

        caption_elem = driver.find_element(By.ID, 'index-caption')
        caption_elem.send_keys(data[i][4])
        sleep(2)

        submit_elem = driver.find_element(By.ID, 'index-upload-submit')
        submit_elem.click()

        sleep(5)
        avatar = driver.find_element(By.ID, 'index-avatar')
        avatar.click()
        sleep(1)

        logout = driver.find_element(By.ID, 'index-logout')
        logout.click()
        print("Đăng nhập và post thành công!!!")
    else:
        print("Đăng nhập không thành công!!!")


# Đóng trình duyệt
driver.quit()
