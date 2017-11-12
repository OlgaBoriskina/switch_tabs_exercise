from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

frame_locator = "//iframe[@src='frames-windows/defult4.html']"
link_locator = "//a[@href='#']"
open_windows_locator = "//a[@href='#example-1-tab-4']"


def switch_to_frame(driver,wait):
    frame = wait.until(expected.element_to_be_clickable((By.XPATH, frame_locator)))
    driver.switch_to.frame(frame)


def link_open_windows(wait):
    link = wait.until(expected.element_to_be_clickable((By.XPATH, link_locator)))
    return link


def get_new_hanler_ind(current, handles):
    for hendle in handles:
        if hendle <> current:
            hanler_index = handles.index(hendle)
            break
    return hanler_index


def get_difference_handler(handles, new_handles):
    list_handles= set(handles)
    list_new_handles = set(new_handles)
    result = list(list(list_handles ^ list_new_handles))
    return result


def switch_tabs(driver,wait):
    driver.find_element_by_xpath(open_windows_locator).click()
    switch_to_frame(driver,wait)
    link_open_windows(wait).click()
    current = driver.current_window_handle
    handles = driver.window_handles
    hanler_ind = get_new_hanler_ind(current, handles)
    driver.switch_to_window(driver.window_handles[hanler_ind])
    link_open_windows(wait).click()
    new_handles = driver.window_handles
    result = get_difference_handler(handles, new_handles)
    return result