from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Project:
    
    def admin_login(self,url):
        #credentials
        usernameA = "Admin"
        passwordA = "admin123"
       
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        
        #open the webpage
        self.driver.get(url)
        time.sleep(4)
    
        #admin credentials xpath
        usernameA_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        passwordA_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login_button_xpath= "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

        #admin fill the crednetials   
        usernameA_xpath=self.driver.find_element(by=By.XPATH, value=usernameA_xpath)
        passwordA_xpath=self.driver.find_element(by=By.XPATH, value=passwordA_xpath)
        login_button_xpath=self.driver.find_element(by=By.XPATH, value=login_button_xpath)
        
        usernameA_xpath.send_keys(usernameA)
        passwordA_xpath.send_keys(passwordA)
        time.sleep(4)

        #login
        login_button_xpath.click()
        time.sleep(4)

    def TC_PIM_01(self,url):
        #menu and search validation
        try:
            menu=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]')
            print(menu.is_displayed)
        except NoSuchElementException:
            print("Menu not displayed")
        try:
            search_box=self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            print(search_box.is_displayed())
        except NoSuchElementException:
            print("Search box not displayed")
            pass
        time.sleep(3)
        
        #individual menu name validation
        search_menu= input('Enter menu name:')
        search_box.send_keys(search_menu)

        try:
            print(self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').is_displayed())
            time.sleep(2)
        except NoSuchElementException:
            print("Menu not dislplayed")
            
        action=ActionChains(self.driver)
        action.move_to_element(search_box).double_click().click().send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)
        
        
        
        

        #search_box.send_keys(search_menu_02)
        #print(admin_xpath.is_displayed())

url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

p = Project()

p.admin_login(url)

p.TC_PIM_01(url)