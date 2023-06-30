from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By
import pytest
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains

def self(args):
    pass

@pytest.mark.usefixtures('setup')
class TestMain:
    driver = None

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("A/B Test Control")
    @allure.description("")
    def test_1(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопкуA/B Testing"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a').click()
            element = self.browser.find_element(By.XPATH, '//*[@id="content"]/div/h3').text
            if element =='A/B Test Variation 1':
                assert element == 'A/B Test Variation 1', 'Ошибка!'
            elif element == 'A/B Test Variation 2':
                assert element == 'A/B Test Variation 2', 'Ошибка!'

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('Add/Remove Elements')
    @allure.description('')
    def test_2(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Add/Remove Elements'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Add Element'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимаем кнопку Delete'):
            self.browser.find_element(By.XPATH, '//*[@id="elements"]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("Entry Ad")
    @allure.description("")
    def test_3(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Entry Ad"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[15]/a').click()
        with allure.step("Нажать на кнопку Close"):
            self.browser.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p').click()
            element = self.browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/h3').text
        assert element == 'Entry Ad', 'Ошибка!'

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('File Download')
    @allure.description('')
    def test_4(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку File Download'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[17]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Waterfall.JPG'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку TestImage.jpg'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[2]').click()
        with allure.step('Нажимает кнопку 1684034092109.jpg'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[3]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку pistas.txt'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[4]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('Dropdown')
    @allure.description('')
    def test_5(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Dropdown'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку '):
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/select').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("Dynamic Loading")
    @allure.description("")
    def test_6(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Dynamic Loading"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[14]/a').click()
        with allure.step("Нажать на кнопку Example 1: Element on page that is hidden"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[1]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Start"):
            self.browser.find_element(By.XPATH, '//*[@id="start"]/button').click()
            time.sleep(7)
            element = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/h4').text
        assert element == 'Hello World!', 'Ошибка!'

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("Floating Menu")
    @allure.description("")
    def test_7(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Floating Menu"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[19]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Home"):
            self.browser.find_element(By.XPATH, '//*[@id="menu"]/ul/li[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку News"):
            self.browser.find_element(By.XPATH, '//*[@id="menu"]/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Contact"):
            self.browser.find_element(By.XPATH, '//*[@id="menu"]/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку About"):
            self.browser.find_element(By.XPATH, '//*[@id="menu"]/ul/li[4]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('Checkboxes')
    @allure.description('')
    def test_8(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Checkboxes'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку checkbox 1'):
            self.browser.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку checkbox 2'):
            self.browser.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('Challenging DOM')
    @allure.description('')
    def test_9(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Challenging DOM'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[5]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку foo'):
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[1]/a[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку baz'):
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[1]/a[2]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку bar'):
             self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[1]/a[3]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('JQuery UI Menus')
    @allure.description('')
    def test_10(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку JQuery UI Menus'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[28]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Enable'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Back to JQuery UI'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-8"]/a').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('Dynamic Controls')
    @allure.description('')
    def test_11(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Dynamic Controls'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[13]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку A checkbox'):
            self.browser.find_element(By.XPATH, '//*[@id="checkbox"]/input').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Remove'):
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("Shifting Content")
    @allure.description("")
    def test_12(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Shifting Content"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[39]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Example 1: Menu Element"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/a[1]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Contact Us"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            element = self.browser.find_element(By.XPATH, '/html/body/h1').text
        assert element == 'Not Found', 'Ошибка!'

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("WYSIWYG Editor")
    @allure.description("")
    def test_13(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку WYSIWYG Editor"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[44]/a').click()
        with allure.step("Нажать на кнопку Align center"):
            self.browser.find_element(By.XPATH,'//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[4]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("Forgot Password")
    @allure.description("")
    def test_14(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Forgot Password"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[20]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Forgot Password"):
            self.browser.find_element(By.XPATH, '//*[@id="email"]').send_keys('alana1728@yandex.ru')
        with allure.step("Нажать на кнопку Retrieve password"):
            self.browser.find_element(By.XPATH, '//*[@id="form_submit"]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            element = self.browser.find_element(By.XPATH, '/html/body/h1').text
        assert element == 'Internal Server Error', 'Ошибка!'

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("Status Codes")
    @allure.description("")
    def test_15(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Status Codes"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[42]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку 200"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            element = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/p').text

    @allure.feature('Тест Welcome to the-internet')
    @allure.story('Multiple Windows')
    @allure.description('')
    def test_16(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('http://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Multiple Windows'):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[33]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку Click Here'):
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("")
    @allure.description("")
    def test_17(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Drag and Drop"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[10]/a').click()
        with allure.step("drag"):
            drag = self.browser.find_element(By.XPATH, '//*[@id="column-a"]')
            drop = self.browser.find_element(By.XPATH, '//*[@id="column-b"]')
            ActionChains(self.browser).drag_and_drop(drag, drop).perform()

    @allure.feature("Тест Welcome to the-internet")
    @allure.story("")
    @allure.description("")
    def test_17(self):
        with allure.step("Открыть ссылку"):
            self.browser.get('https://the-internet.herokuapp.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Нажать на кнопку Drag and Drop"):
            self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[10]/a').click()
        with allure.step("drag"):
            drag = self.browser.find_element(By.XPATH, '//*[@id="column-a"]')
            drop = self.browser.find_element(By.XPATH, '//*[@id="column-b"]')
            ActionChains(self.browser).click_and_hold(drag).move_to_element(drop).release().perform()













