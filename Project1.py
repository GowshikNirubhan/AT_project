from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Project:
    
    def new_emplyee(self,url):
        #admin credentials
        usernameA = "Admin"
        passwordA = "admin123"
        firstname= input('Enter First Name:')
        lastname= input('Enter Last Name:')
        employee_name= input('Enter Employee Name:')
        username = input('Enter User Name:')
        user_password= input('Enter User Password:')
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        #open the webpage
        self.driver.get(url)
        time.sleep(4)
    
        #credentials xpath
        usernameA_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        passwordA_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login_button_xpath= "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

        #fill the crednetials   
        usernameA_xpath=self.driver.find_element(by=By.XPATH, value=usernameA_xpath)
        passwordA_xpath=self.driver.find_element(by=By.XPATH, value=passwordA_xpath)
        login_button_xpath=self.driver.find_element(by=By.XPATH, value=login_button_xpath)
        
        usernameA_xpath.send_keys(usernameA)
        passwordA_xpath.send_keys(passwordA)
        time.sleep(4)

        #login
        login_button_xpath.click()
        time.sleep(4)

    #create employee in PIM 
        #pim and add xpath
        pim_xpath="//a[@href='/web/index.php/pim/viewPimModule']"
        add_employee_xpath="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a"
        firstname_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
        lastname_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input"
        save_button_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"

        #navigate to PIM and add employee
        self.driver.find_element(by=By.XPATH, value=pim_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=add_employee_xpath).click()
        time.sleep(2)
        firstname_xpath=self.driver.find_element(by=By.XPATH, value=firstname_xpath)
        lastname_xpath=self.driver.find_element(by=By.XPATH, value=lastname_xpath)
        save_button_xpath=self.driver.find_element(by=By.XPATH, value=save_button_xpath)

        #fill the employee name and  save
        firstname_xpath.send_keys(firstname)
        lastname_xpath.send_keys(lastname)
        time.sleep(3)
        save_button_xpath.click()
        time.sleep(5)

    #admin navigate and create user
        #admin and add xpath
        admin_xpath="//a[@href='/web/index.php/admin/viewAdminModule']"
        add_button_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
       
        #navigate to admin and add
        self.driver.find_element(by=By.XPATH, value=admin_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=add_button_xpath).click()
        time.sleep(3)
        
    
        #user role
        user_role_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
        self.driver.find_element(by=By.XPATH, value=user_role_xpath).click()
        time.sleep(2)

        role_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]'
        role_xpath=self.driver.find_element(by=By.XPATH, value= role_xpath)
        action=ActionChains(self.driver)
        action.move_to_element(role_xpath).perform()

        ESS_role_xpath=self.driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]')
        action.move_to_element(ESS_role_xpath).click().perform()
        time.sleep(2)
    
        #user status 
        user_status_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div'
        self.driver.find_element(by=By.XPATH, value=user_status_xpath).click()
        time.sleep(2)

        status_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]'
        status_xpath=self.driver.find_element(by=By.XPATH, value= status_xpath)
        action=ActionChains(self.driver)
        action.move_to_element(status_xpath).perform()

        enable_xpath=self.driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]')
        action.move_to_element(enable_xpath).click().perform()
        time.sleep(2)
        
        #employee name
        employee_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input'
        employee_name_xpath=self.driver.find_element(by=By.XPATH, value=employee_name_xpath)
        time.sleep(2)
        
        employee_name_xpath.click()
        time.sleep(2)
        employee_name_xpath.send_keys(employee_name)
        time.sleep(2)
        
        #select employee name
        select_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]'
        select_name_xpath=self.driver.find_element(by=By.XPATH, value= select_name_xpath)
        action=ActionChains(self.driver)
        action.move_to_element(select_name_xpath).perform()

        select_xpath=self.driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]')
        action.move_to_element(select_xpath).click().perform()
        time.sleep(2)

        #user name
        username_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'
        username_xpath=self.driver.find_element(by=By.XPATH, value=username_xpath)
        username_xpath.click()
        
        username_xpath.send_keys(username)
        #time.sleep(2)

        #password
        user_password_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
        confirm_password_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'

        user_password_xpath=self.driver.find_element(by=By.XPATH, value=user_password_xpath)
        confirm_password_xpath=self.driver.find_element(by=By.XPATH, value=confirm_password_xpath)

        user_password_xpath.send_keys(user_password)
        confirm_password_xpath.send_keys(user_password)
        time.sleep(2)
         
        #save
        save_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]'
        self.driver.find_element(by=By.XPATH, value= save_xpath).click()
        time.sleep(8)

    #verify user
        #search new user
        verify_username_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        verify_username_xpath=self.driver.find_element(by=By.XPATH, value=verify_username_xpath)

        verify_username_xpath.click()

        verify_username_xpath.send_keys(username)
        time.sleep(2)

        search_button_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
        search_button_xpath=self.driver.find_element(by=By.XPATH, value=search_button_xpath)
        search_button_xpath.click()
        time.sleep(3)


    #logout
        profile_dropdown_xpath='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
        profile_dropdown_xpath=self.driver.find_element(by=By.XPATH, value=profile_dropdown_xpath)

        profile_dropdown_xpath.click()
        time.sleep(2)

        logout_button_xpath='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
        logout_button_xpath=self.driver.find_element(by=By.XPATH, value=logout_button_xpath)

        logout_button_xpath.click()
        time.sleep(3)

    #new login    
        #credentials xpath values
        usernameA_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        passwordA_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login_button_xpath= "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        
        #fill the new crednetials   
        usernameA_xpath=self.driver.find_element(by=By.XPATH, value=usernameA_xpath)
        passwordA_xpath=self.driver.find_element(by=By.XPATH, value=passwordA_xpath)
        login_button_xpath=self.driver.find_element(by=By.XPATH, value=login_button_xpath)
        
                
        usernameA_xpath.send_keys(username)
        passwordA_xpath.send_keys(user_password)
        time.sleep(4)

        #login
        login_button_xpath.click()
        time.sleep(10)
        
        self.driver.close()
       


p = Project()
url = "https://opensource-demo.orangehrmlive.com/"
p.new_emplyee(url)