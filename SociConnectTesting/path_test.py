import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# đọc dữ liệu
with open(file='./Data_Testing/data_path.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)

# print(data)

driver = webdriver.Chrome()

# mở rộng full kích thước màn hình
driver.maximize_window()

# điều hướng trang signup
driver.get("http://127.0.0.1:8000/signup")
sleep(3)

# điều hướng đến trang login
signup_login_btn = driver.find_element(By.ID, 'signup-login')
signup_login_btn.click()
sleep(1)
 

for i in range(len(data)):
    # select đến username, password và button login
    username_input = driver.find_element(By.ID, 'signin-username')
    password_input = driver.find_element(By.ID, 'signin-password')
    login_button = driver.find_element(By.ID, 'signin-submit')
    sleep(1)

    # nhập dữ liệu tự động cho username và password
    username_input.send_keys(data[i][1])
    password_input.send_keys(data[i][2])
    sleep(1)

    # Nhấp vào nút Đăng nhập, điều hướng đến trang chủ /
    login_button.click()
    sleep(3)

    # điều hướng đến trang search mà không nhập dữ liệu tìm kiếm nào
    search_button = driver.find_element(By.ID, 'index-search-submit')
    search_button.click()
    sleep(2)

    # điều hướng đến trang thông tin cá nhân của người cần tìm kiếm (dữ liệu đọc từ file data)
    input_search = driver.find_element(By.XPATH, "//input[@type='text']")
    input_search.send_keys(data[i][4])
    sleep(2)

    button_search = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_search.click()
    sleep(1)

    # điều hướng đến /profile/<username>
    user_result = driver.find_element(By.ID, data[i][4])
    user_result.click()
    sleep(1)

    # điều hướng ngược lại /search
    driver.back()
    sleep(2)

    # điều hướng đến trang profile cá nhân 
    my_profile_btn = driver.find_element(By.ID, data[i][1])
    my_profile_btn.click()
    sleep(2)

    # điều hướng đến trang chỉnh sửa profile cá nhân /settings
    settings_btn = driver.find_element(By.ID, 'profile-settings')
    settings_btn.click()
    sleep(2)

    # chỉnh sửa bio và location
    bio_textarea = driver.find_element(By.ID, 'about')
    # clear data
    bio_textarea.clear()
    bio_textarea.send_keys(data[i][5])
    sleep(1)

    location_textarea = driver.find_element(By.ID, 'settings-location')
    location_textarea.clear()
    location_textarea.send_keys(data[i][6])
    sleep(2)

    button_save = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_save.click()
    sleep(1)

    # quay trở về trang chủ
    cancel_button = driver.find_element(By.ID, "cancel-settings")
    cancel_button.click()
    sleep(2)

    # forward lại trang profile cá nhân
    driver.back()
    sleep(2)

    # trở về home với link home
    home_link = driver.find_element(By.ID, 'settings-home')
    home_link.click()
    sleep(3)

    # đăng xuất
    avatar = driver.find_element(By.ID, 'index-avatar')
    avatar.click()
    sleep(1)

    logout = driver.find_element(By.ID, 'index-logout')
    logout.click()
    sleep(1)

# điều hướng đến url 404
driver.get("http://127.0.0.1:8000/abcxyz")
sleep(2)

# điều hướng đến admin
driver.get("http://127.0.0.1:8000/admin/")
sleep(2)

admin_user = driver.find_element(By.ID, 'id_username')
admin_user.send_keys('admin')

admin_password = driver.find_element(By.ID, 'id_password')
admin_password.send_keys('@admin123')
sleep(2)

login_admin_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
login_admin_btn.click()
sleep(2)

# logout khỏi admin
logout_admin_btn = driver.find_element(By.ID, 'logout-form')
logout_admin_btn.click()
sleep(2)

driver.quit()