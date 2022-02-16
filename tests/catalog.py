from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_desktops(driver):
    driver.get("http://192.168.1.69:8081")
    click_desktops = driver.find_element_by_xpath("//a[contains(text(),'Desktops')]")
    click_desktops.click()
    click_mak = driver.find_element_by_xpath("//a[contains(text(),'Mac (1)')]")
    click_mak.click()
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Mac"


def test_check_components(driver):
    driver.get("http://192.168.1.69:8081")
    click_components = driver.find_element_by_xpath("//a[contains(text(),'Components')]")
    click_components.click()
    click_monitors = driver.find_element_by_xpath("//a[contains(text(),'Monitors (2)')]")
    click_monitors.click()
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Monitors"


def test_check_tablets(driver):
    driver.get("http://192.168.1.69:8081")
    click_tablets = driver.find_element_by_xpath("//a[contains(text(),'Tablets')]")
    click_tablets.click()
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Tablets"


def test_check_software(driver):
    driver.get("http://192.168.1.69:8081")
    click_software = driver.find_element_by_xpath("//a[contains(text(),'Software')]")
    click_software.click()
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Software"


def test_check_phones(driver):
    driver.get("http://192.168.1.69:8081")
    click_phones = driver.find_element_by_xpath("//a[contains(text(),'Phones & PDAs')]")
    click_phones.click()
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")), message='')
    assert el.text == "Phones & PDAs"
