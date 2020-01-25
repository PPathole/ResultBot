from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class ResultBot():
    def __init__(self, prn, mname):
        self.driver = webdriver.Chrome('C://Users/Admin/chromedriver_win32/chromedriver.exe')
        self.driver.get('http://results.unipune.ac.in')
        
        while self.driver.find_element_by_xpath('.//span[@id = "ctl00_ContentPlaceHolder1_dgvResult_ctl02_lblCourse"]').text != "BE 2015 PERCENTAGE PATTERN EXAM PERIOD OCT-NOV 2019":
            self.driver.refresh()
            time.sleep(3)
            
        
        #if self.driver.find_element_by_xpath('.//span[@id = "ctl00_ContentPlaceHolder1_dgvResult_ctl02_lblCourse"]') == "BE 2015 PERCENTAGE PATTERN EXAM PERIOD OCT-NOV 2019":
        self.driver.find_element_by_xpath('/html/body/form/div[5]/div/center/div/table/tbody/tr[2]/td[4]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/form/div[5]/div[1]/center[1]/div[2]/input').send_keys(prn)
        self.driver.find_element_by_xpath('/html/body/form/div[5]/div[1]/center[1]/div[3]/input').send_keys(mname)
        self.driver.find_element_by_xpath('/html/body/form/div[5]/div[1]/center[1]/div[4]/input').click()
        sleep(2)


ResultBot('YOUR_PRN_NUMBER', 'YOUR_MOTHERS_NAME')
