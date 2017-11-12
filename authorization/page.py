from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

login_locator = "//a[@href='#login']"
user_locator = "id('login')//input[@name='username']"
password_locator = "id('login')//input[@name='password']"
submit_locator = "id('login')//input[@class='button']"


def login(wait):
    login = wait.until(expected.element_to_be_clickable((By.XPATH, login_locator)))
    return login


def user(wait):
    user = wait.until(expected.element_to_be_clickable((By.XPATH, user_locator)))
    return user


def password(wait):
    password = wait.until(expected.element_to_be_clickable((By.XPATH, password_locator)))
    return password


def submit(wait):
    submit = wait.until(expected.element_to_be_clickable((By.XPATH, submit_locator)))
    return submit