import accessabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import conftest


def test_signup_invalid_email_and_name():
    # OPEN PAGE
    driver = conftest.driver()
    time.sleep(2)

    # SIGN UP BUTTON
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass
    time.sleep(10)

    # case 1
    # EMPTY NAME AND MAIL
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("")
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("")
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    test = False
    # CHECK THE ERROR MESSGAE
    try:
        test = 'Please select an item in the list.' == driver.find_element(By.ID,
                                                                           accessabilities.signup_month_list_id).get_attribute(
            "validationMessage")
    except NoSuchElementException:
        pass

    print('INVALID MAIL AND NAME SIGN UP')

    if test:
        print('Test Successful')
    else:
        print('Test Failed')

    # CLOSE THE PAGE
    conftest.teardown(driver)
    time.sleep(2)


def test_signup_invalid_email_only():
    # OPEN PAGE
    driver = conftest.driver()
    time.sleep(2)
    # SIGN UP BUTTON
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass

    # VALID NAME
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("Yasmeen")
    except NoSuchElementException:
        pass
    # EMPTY MAIL
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("")
    except NoSuchElementException:
        pass
    # NEXT BUTTON
    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    test = False
    # CHECK THE ERROR MESSAGE
    try:
        test = 'Please select an item in the list.' == driver.find_element(By.ID,
                                                                           accessabilities.signup_month_list_id).get_attribute(
            "validationMessage")
    except NoSuchElementException:
        pass

    print('INVALID MAIL AND VALID NAME SIGN UP')

    if test:
        print('Test Successful')
    else:
        print('Test Failed')

    conftest.teardown(driver)
    time.sleep(2)


def test_signup_invalid_name_only():
    # OPEN PAGE
    driver = conftest.driver()
    time.sleep(2)
    # SIGN UP BUTTON
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass

    # INVALID NAME
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("")
    except NoSuchElementException:
        pass

    # VALID MAIL
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("yasmeen_zaki01@gmail.com")
    except NoSuchElementException:
        pass
    # NEXT BUTTON
    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass
    # CHECK THE ERROR MESSAGE
    test = False
    try:
        test = 'Please select an item in the list.' == driver.find_element(By.ID,
                                                                           accessabilities.signup_month_list_id).get_attribute(
            "validationMessage")
    except NoSuchElementException:
        pass

    print('INVALID NAME AND VALID MAIL SIGN UP')

    if test:
        print('Test Successful')
    else:
        print('Test Failed')

    # CLOSE PAGE
    conftest.teardown(driver)
    time.sleep(2)


def test_signup_invalid_date_only():
    # OPEN PAGE
    driver = conftest.driver()
    time.sleep(2)
    # SIGN UP BUTTON
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass

    # VALID NAME
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("Yasmeen")
    except NoSuchElementException:
        pass
    # VALID MAIL
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("yasmeen_zaki01@gmail.com")
    except NoSuchElementException:
        pass
    # NEXT BUTTON
    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    test = False
    try:
        test = 'Please select an item in the list.' == driver.find_element(By.ID,
                                                                           accessabilities.signup_month_list_id).get_attribute(
            "validationMessage")
    except NoSuchElementException:
        pass

    print('INVALID DATE SIGN UP')

    if test:
        print('Test Successful')
    else:
        print('Test Failed')

    # CLOSE PAGE
    conftest.teardown(driver)
    time.sleep(2)


def test_signup_valid_date_only():
    # OPEN PAGE
    driver = conftest.driver()
    time.sleep(2)
    # SIGN UP BUTTON
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass

    # INVALID NAME
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("")
    except NoSuchElementException:
        pass
    # INVALID MAIL
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("")
    except NoSuchElementException:
        pass

    # VALID DATE
    try:
        Select(driver.find_element(By.ID, accessabilities.signup_month_list_id)).select_by_visible_text('August')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_day_list_id)).select_by_visible_text('21')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_year_list_id)).select_by_visible_text('2001')
    except NoSuchElementException:
        pass

    # NEXT BUTTON
    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    # CHECK THE ERROR MESSAGE
    test = False
    try:
        test = driver.find_element(By.ID,
                                   accessabilities.signup_name_error) and driver.find_element(By.XPATH,
                                                                                              accessabilities.signup_email_error)
    except NoSuchElementException:
        pass

    print('VALID DATE SIGN UP WITH INVALID DATA')
    if test:
        print('Test Successful')
    else:
        print('Test Failed')

    # CLOSE PAGE
    conftest.teardown(driver)
    time.sleep(2)


def test_signup_valid_date_and_name():
    # OPEN PAGE
    driver = conftest.driver()
    time.sleep(2)
    # SIGN UP BUTTON
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass

    # VALID NAME
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("Yasmeen")
    except NoSuchElementException:
        pass
    # INVALID MAIL
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("")
    except NoSuchElementException:
        pass
    # VALID MONTH
    try:
        Select(driver.find_element(By.ID, accessabilities.signup_month_list_id)).select_by_visible_text('August')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_day_list_id)).select_by_visible_text('21')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_year_list_id)).select_by_visible_text('2001')
    except NoSuchElementException:
        pass

    # NEXT BUTTON
    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass
    # CHECK THE ERROR MESSAGE
    test = False
    try:
        test = driver.find_element(By.XPATH, accessabilities.signup_email_error).is_displayed()
    except NoSuchElementException:
        pass

    print('VALID DATE AND NAME SIGN UP')
    if test:
        print('Test Successful')
    else:
        print('Test Failed')

    # CLOSE PAGE
    conftest.teardown(driver)
    time.sleep(2)


def test_signup_valid_date_and_email():
    # OPEN PAGE
    driver = conftest.driver()
    time.sleep(2)
    # SIGN UP BUTTON
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass

    # EMPTY NAME
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("")
    except NoSuchElementException:
        pass
    # VALID MAIL
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("yasmeen_zaki01@gmail")
    except NoSuchElementException:
        pass
    # VALID DATE
    try:
        Select(driver.find_element(By.ID, accessabilities.signup_month_list_id)).select_by_visible_text('August')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_day_list_id)).select_by_visible_text('21')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_year_list_id)).select_by_visible_text('2001')
    except NoSuchElementException:
        pass
    # NEXT BUTTON
    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    # CHECK THE ERROR MESSGAE
    test = False
    try:
        test = driver.find_element(
            By.ID, accessabilities.signup_name_error).is_displayed()
    except NoSuchElementException:
        pass

    print('VALID DATE AND MAIL SIGN UP')
    if test:
        print('Test Successful')
    else:
        print('Test Failed')

    # CLOSE PAGE
    conftest.teardown(driver)
    time.sleep(2)


def test_invalid_email_address():
    # email address without @
    driver = conftest.driver()
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("Yasmeen Zaki")
    except NoSuchElementException:
        pass
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("n")
    except NoSuchElementException:
        pass
    try:
        Select(driver.find_element(By.ID, accessabilities.signup_month_list_id)).select_by_visible_text('August')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_day_list_id)).select_by_visible_text('21')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_year_list_id)).select_by_visible_text('2001')
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    test = False

    try:
        test = ('Please include an' in driver.find_element(By.ID,
                                                           accessabilities.signup_email_textbox_id).get_attribute(
            "validationMessage"))
    except NoSuchElementException:
        pass

    if test:
        print("part 1 is successful")
    else:
        print('Test Failed')

    # email with an '@' but without continuation
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).clear()
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("nossair101@")
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    test = False

    try:
        test = ('Please enter a part following' in driver.find_element(By.ID,
                                                                       accessabilities.signup_email_textbox_id).get_attribute(
            "validationMessage"))
    except NoSuchElementException:
        pass

    if test:
        print("part 2 is successful")
    else:
        print('Test Failed')

    # email without .com
    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).clear()
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("nossair101@fff")
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    test = False

    try:
        test = (driver.find_element(By.CSS_SELECTOR, accessabilities.invalid_email_error)).is_displayed()
    except NoSuchElementException:
        pass

    if test:
        print("part 3 is successful")
    else:
        print('Test Failed')


def test_valid_signup_with_email():
    driver = conftest.driver()
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass
    # case 8
    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("Yasmeen Zaki")
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("nossair101@gmail.com")
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_month_list_id)).select_by_visible_text('August')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_day_list_id)).select_by_visible_text('21')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_year_list_id)).select_by_visible_text('2001')
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    test = False

    try:
        test = ('We sent you a code' == driver.find_element(By.CSS_SELECTOR,
                                                            accessabilities.verification_page_title).text)
    except NoSuchElementException:
        pass

    if test:
        print("Test Successful")
    else:
        print('Test Failed')

    conftest.teardown(driver)


def to_verification_page():
    driver = conftest.driver()
    try:
        driver.find_element(By.ID, accessabilities.sign_up_with_email_button_id).click()
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_name_textbox_id).send_keys("Yasmeen Zaki")
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_email_textbox_id).send_keys("nossair101@gmail.com")
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_month_list_id)).select_by_visible_text('August')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_day_list_id)).select_by_visible_text('21')
    except NoSuchElementException:
        pass

    try:
        Select(driver.find_element(By.ID, accessabilities.signup_year_list_id)).select_by_visible_text('2001')
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.signup_next_button_id).click()
    except NoSuchElementException:
        pass

    return driver


def test_invalid_verification_code_1():
    driver = to_verification_page()
    try:
        driver.find_element(By.ID, accessabilities.verification_code_textbox_id).send_keys(
            accessabilities.incorrect_verification_code_1)
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.verification_page_next_button).click()
    except NoSuchElementException:
        pass

    test = False

    try:
        test = (driver.find_element(By.ID, accessabilities.incorrect_verification_error)).is_displayed()
    except NoSuchElementException:
        pass

    if test:
        print("Test Successful")
    else:
        print('Test Failed')

    conftest.teardown(driver)


def test_invalid_verification_code_2():
    driver = to_verification_page()
    try:
        driver.find_element(By.ID, accessabilities.verification_code_textbox_id).send_keys('')
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.verification_page_next_button).click()
    except NoSuchElementException:
        pass

    test = False

    try:
        test = (driver.find_element(By.ID, accessabilities.incorrect_verification_error_1)).is_displayed()
    except NoSuchElementException:
        pass

    if test:
        print("Test Successful")
    else:
        print('Test Failed')

    conftest.teardown(driver)


def test_invalid_verification_code_3():
    driver = to_verification_page()
    try:
        driver.find_element(By.ID, accessabilities.verification_code_textbox_id).send_keys(
            accessabilities.incorrect_verification_code_3)
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, accessabilities.verification_page_next_button).click()
    except NoSuchElementException:
        pass

    test = False

    try:
        test = (driver.find_element(By.ID, accessabilities.incorrect_verification_error_2)).is_displayed()
    except NoSuchElementException:
        pass

    if test:
        print("Test Successful")
    else:
        print('Test Failed')

    conftest.teardown(driver)
