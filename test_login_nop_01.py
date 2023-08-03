class Test_cred_nop():
    def test_cred_nop(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver import ActionChains
        from selenium.webdriver.support.select import Select

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        time.sleep(10)
        driver.get('https://demo.nopcommerce.com/')

        # -----------------------------------------register----------------
        driver.find_element(By.XPATH, "//a[@class='ico-register']").click()  # click on registration button

        driver.find_element(By.XPATH, "//label[@for='gender-female']").click()  # check on female

        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys('priya')  # check of first name

        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys('S')

        Date = Select(driver.find_element(By.XPATH, "//select[@name='DateOfBirthDay']"))  # date
        Date.select_by_index(3)
        Month = Select(driver.find_element(By.XPATH, "//select[@name='DateOfBirthMonth']"))  # month
        Month.select_by_index(3)
        Year = Select(driver.find_element(By.XPATH, "//select[@name='DateOfBirthYear']"))  # year
        Year.select_by_visible_text('1992')

        driver.find_element(By.XPATH, "//input[@type='email']").send_keys('ho@gmail.com')  # email

        driver.find_element(By.XPATH, "//input[@id='Company']").send_keys('IT_solutions')  # company name

        driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()  # checkbox tick

        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('vampire@321')  # password

        driver.find_element(By.XPATH, "(//input[@id='ConfirmPassword'])[1]").send_keys('vampire@321')  # password

        driver.find_element(By.XPATH, "//button[@id='register-button']").click()  # redister click
        # ------------------------------------------login_-----------------------------
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()  # login

        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys('ho@gmail.com')  # email

        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('vampire@321')  # password
        driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()  # click on login
        if driver.find_element(By.XPATH, "//h2[normalize-space()='Welcome to our store']"):
            print('login succesful')
        else:
            print('login fail')
        # -----------------------------------mousehover---------------------------------------------------
        time.sleep(10)
        computer = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
        desktop = driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Desktops']")
        action = ActionChains(driver)
        action.move_to_element(computer).move_to_element(desktop).click().perform()
class Test_cred_login():
    def test_cred_login(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.common import NoSuchElementException

        # 1 open Browser
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)

        driver.get('https://automation.credence.in')
        driver.find_element(By.LINK_TEXT, 'Login').click()  # for login

        # verify the login is failed or succeed
        try:
            driver.find_element(By.LINK_TEXT, 'Login').click()
            print('login pass')
        except:
            print('Failed')

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys('horrorstreetcafe@gmail.com')  # for email
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Credence@1234')  # password enter
        # driver.find_element(By.XPATH,"//input[@type='checkbox']").click()     #check box
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # login

        # check wether the page login succefully looking at Page TITLE ' credkart'
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print('login successful')
        except NoSuchElementException:
            print('Failed')

        # -- verify it takes to shop page is open after login

        try:
            driver.find_element(By.LINK_TEXT, 'Shop')
            print('You are on shop page')
        except NoSuchElementException:
            print('Try again')

