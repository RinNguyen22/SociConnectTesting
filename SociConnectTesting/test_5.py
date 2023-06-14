import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import randrange

# đọc dữ liệu kiểm thử 
with open(file='./Data_Testing/data_5.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)

# print(data)


driver = webdriver.Chrome()

# mở rộng full kích thước màn hình
driver.maximize_window()

# điều hướng trang signup
driver.get("http://127.0.0.1:8000/signin")
sleep(2.5)

view_user_list = ["view1", "view2", "view3", "view4"]
window_size = driver.get_window_size()
width = window_size['width']
height = window_size['height']

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

    search_input = driver.find_element(By.ID, 'index-search')
    search_input.send_keys(data[i][3])
    sleep(1.5)

    search_btn = driver.find_element(By.ID, 'index-search-submit')
    search_btn.click()
    sleep(3)

    # điều hướng ngược lại home
    driver.back()

    # nhấn vào view user đề xuất
    random_number = randrange(4)
    view_user_btn = driver.find_element(By.ID, view_user_list[random_number])
    view_user_btn.click()
    sleep(1)

    # follow
    follow_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    follow_btn.click()
    sleep(2)

    # Get the screen height
    screen_height = driver.execute_script("return window.innerHeight")

    # Scroll down 50% of the screen height
    driver.execute_script("window.scrollBy(0, arguments[0]);", screen_height/2)

    # Tạo đối tượng ActionChains
    actions = ActionChains(driver)

    # Di chuyển chuột đến tọa độ dựa trên kích thước màn hình
    actions.move_by_offset(width/2, height/2).perform()

    # Thực hiện click
    actions.click().perform()
    sleep(2)

    # Get the screen height
    screen_height = driver.execute_script("return window.innerHeight")

    # Scroll up 50% of the screen height
    driver.execute_script("window.scrollBy(0, -arguments[0]);", screen_height/2)
    sleep(1)

    ava = driver.find_element(By.CLASS_NAME ,"user-avatar")
    ava.click()
    sleep(1)

    # unfollow
    unfollow_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    unfollow_btn.click()
    sleep(2)

    home_btn = driver.find_element(By.ID, 'profile-home')
    home_btn.click()
    sleep(2)

    # đăng xuất
    avatar = driver.find_element(By.ID, 'index-avatar')
    avatar.click()
    sleep(1)

    logout = driver.find_element(By.ID, 'index-logout')
    logout.click()
    sleep(1)

driver.quit()
