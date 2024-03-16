from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import time


# Instantiate Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://klaaradmin-trials711.orangehrmlive.com/client/#/dashboard")
driver.maximize_window()
# Enter username
driver.find_element(By.ID, "txtUsername").send_keys("Admin")

# Enter password
driver.find_element(By.ID, "txtPassword").send_keys("SyN6Ktl@O0")

# Click on login button
driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/form/div[4]/button").click()

# Navigate to the employee section
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/header/nav/top-menu/div/div[1]/div[2]/top-level-menu-item[1]/div/a").click()

time.sleep(7)
#Click on add employee
element_to_hover = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/section/div[3]/ui-view/div[1]/div/div/div/div/a")
actions = ActionChains(driver)
actions.move_to_element(element_to_hover).click().perform()
time.sleep(10)
# Add first name, middle name, and last name
driver.find_element(By.ID,"first-name-box").send_keys("Sample")
driver.find_element(By.ID, "middle-name-box").send_keys("10")
driver.find_element(By.ID, "last-name-box").send_keys("Name")
time.sleep(3)
# Auto Generate Employee ID on/off
driver.find_element(By.XPATH, "//div[@class='custom-control custom-switch']").click()

# New Employee ID
driver.find_element(By.ID, "employeeId").send_keys("5432")

# Change date
date_input = driver.find_element(By.ID, "joinedDate")
date_input.clear()
new_date = datetime.now() + timedelta(days=5)
date_input.send_keys(new_date.strftime("%Y-%m-%d"))
time.sleep(6)
# Choose the location as the "India Office"
location_dropdown = driver.find_element(By.XPATH, "//div[@class='filter-option']")
location_dropdown.click()
location_Value = driver.find_element(By.ID, "bs-select-1-10")
location_Value.click()

# Enable "Create Login Details" and add a username and password. Set the Admin Role to "Regional HR Admin."
create_login_details_switch = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[5]/div/div/span/div[2]")
create_login_details_switch.click()
login_username_field = driver.find_element(By.ID, "username")
login_password_field = driver.find_element(By.ID, "password")
login_cpassword_field = driver.find_element(By.ID, "confirmPassword")
login_username_field.send_keys("Sample10")
login_password_field.send_keys("SampleName10")
login_cpassword_field.send_keys("SampleName10")
admin_role_dropdown = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[11]/div/div[3]/div/div[1]/button")
admin_role_dropdown.click()
admin_role_Value =  driver.find_element(By.ID, "bs-select-5-3")
admin_role_Value.click()

time.sleep(10)

driver.find_element(By.XPATH, "(//div[@class='custom-control custom-switch'])[3]").click()
Region_dropdown = driver.find_element(By.XPATH, "//div[@class='multi-select-container']").click()
Region_Value= driver.find_element(By.ID, "IN")
Region_Value.click()

driver.find_element(By.XPATH, "(//div[@class='custom-control custom-switch'])[4]").click()
time.sleep(3)
Last_Region_dropdown = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[12]/div/div[3]/div/div/div/div[3]/div/div[2]/oxd-multiselect/div/div/div/div/input")
Last_Region_dropdown.click()
Last_Region_Value= driver.find_element(By.ID, "4")
Last_Region_Value.click()

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

time.sleep(10)

# Skip adding personal details and click on the "Next" button
driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

time.sleep(20)

# Select "Full-Time Permanent" as the employment status and add comments
employment_status_dropdown = driver.find_element(By.XPATH, "(//div[@class='filter-option'])[2]")
employment_status_dropdown.click()
status_field = driver.find_element(By.ID, "bs-select-23-4")
status_field.click()
driver.find_element(By.ID, "comment").send_keys("Tech Employee")

# Click on the "Next" Button and verify that you have landed on the Contact Details page
driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

time.sleep(15)
# Skip adding contact details, click on the "Next" button, and verify that you have landed on the Onboarding page
driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

time.sleep(15)
# In the dropdown, select "Onboarding - India" and Save. Verify the pop-up message upon saving
# onboarding_dropdown = driver.find_element(By.XPATH, "//div[@class='select-wrapper initialized']")
Onboarding_dropdown = driver.find_element(By.XPATH, "//input[@value='-- Select --']")
Onboarding_dropdown.click()
time.sleep(5)
Last_Region_Value= driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/section/div[3]/ui-view/div[1]/div/employee-onboarding/form/materializecss-decorator/div/sf-decorator[1]/div/div/ul/li[2]")
Last_Region_Value.click()


save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
save_button.click()

time.sleep(15)

# Once the new user is added, verify that you have landed on the employee details page
Verify = driver.find_element(By.XPATH, "(//div[@class='widget-header'])[1]")
actual = Verify.text
expected = "Leave Balance"

if actual == expected:
    print("Successfully Created New Employee")
else:
    print(" FAILED to Create Employee ")

time.sleep(30)

##### TEST 1 COMPLETED ######