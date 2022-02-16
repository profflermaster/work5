from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_name(driver):
    driver.get("http://192.168.1.69:8081/admin/")
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img")), message='')


def test_check_username(driver):
    driver.get("http://192.168.1.69:8081/admin/")
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-username")), message='')


def test_check_password(driver):
    driver.get("http://192.168.1.69:8081/admin/")
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")), message='')


def test_check_login(driver):
    driver.get("http://192.168.1.69:8081/admin/")
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn")), message='')
    assert el.text == "Login"


def test_check_panel(driver):
    driver.get("http://192.168.1.69:8081/admin/")
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-title")), message='')
    assert el.text == "Please enter your login details."
