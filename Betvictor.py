from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.betvictor.com")


#Sign_Up
elem = driver.find_element_by_id("create_account_button").click()

## Title ##
driver.find_element_by_xpath("//*[@id='signup_form']/div[2]/section[1]/div[1]").click()

#Title
elem1 = driver.find_element_by_xpath("//*[@id='signup_form']/div[2]/section[1]/div[1]").click()
elem2 = driver.find_element_by_xpath("//*[@id='signup_form']/div[2]/section[1]/div[1]/div/div/div").click()

##WebElement_Fname ##
driver.find_element_by_css_selector("#account_first_name").send_keys("Marcus")

#WebElement_Sname ##
driver.find_element_by_css_selector("#account_last_name").send_keys("Cruz")

##Data of birthday
driver.find_element_by_css_selector("#signup_form > div.form_container.bv-select > section.personal_details.account-form__section > div.input_row.dob_container > div:nth-child(1) > div > div").click()

#Day 1
driver.find_element_by_css_selector("#signup_form > div.form_container.bv-select > section.personal_details.account-form__section > div.input_row.dob_container > div:nth-child(1) > div > ul > li:nth-child(2)").click()

#Mounth
driver.find_element_by_css_selector("#signup_form > div.form_container.bv-select > section.personal_details.account-form__section > div.input_row.dob_container > div:nth-child(2) > div > div").click()

#January
driver.find_element_by_css_selector(".bv-select-list-account_dobmonth > li:nth-child(2)").click()

#Year
driver.find_element_by_css_selector("#signup_form > div.form_container.bv-select > section.personal_details.account-form__section > div.input_row.dob_container > div:nth-child(3) > div > div").click()

#Year_2000
driver.find_element_by_css_selector("#signup_form > div.form_container.bv-select > section.personal_details.account-form__section > div.input_row.dob_container > div:nth-child(3) > div > ul > li:nth-child(2)").click()

#Email_Address
driver.find_element_by_id("account_email").send_keys("Spaing@hgjhsgd.com")

#Phone_Number
driver.find_element_by_css_selector("#account_home_phone").send_keys("2345678")

#Country
driver.find_element_by_css_selector("#country_id > div > div > div").click()
#driver.find_element_by_css_selector("#account_country_id > option:nth-child(5)").click()
driver.find_element_by_css_selector("#country_id > div > select#account_country_id > option:nth-child(5)").click()

# driver.find_element_by_css_selector("//*[@id='country_id']/div/div/ul/li[5]").click()
#Select(driver.find_element_by_css_selector("#account_country_id")).select_by_index(4)

#Adress_1
#driver.find_element_by_css_selector("#country_id > div > div > div").send_keys("Main Street")

#Adress_2
#select = Select(driver.find_element_by_id("account_address2").send_keys("London")

#Town / City
#driver.find_element_by_name("account_address3").send_keys("U.K")
#driver.find_element_by_css_selector("#account_address3").send_keys("dfghj")
#Post_Code
#elem = driver.find_element_by_name("account[postcode]").send_keys("1234")

















































