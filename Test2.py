from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime
from datetime import datetime, timedelta


# Set up Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://klaaradmin-trials711.orangehrmlive.com/client/#/dashboard")
driver.maximize_window()

# Fill in username
driver.find_element(By.ID, "txtUsername").send_keys("Admin")

# Fill in password
driver.find_element(By.ID, "txtPassword").send_keys("SyN6Ktl@O0")

# Click on login button
driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/form/div[4]/button").click()


time.sleep(10)

# Click on the desired link
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/header/nav/top-menu/div/div[1]/div[2]/top-level-menu-item[1]/div/a").click()

time.sleep(10)

driver.find_element(By.ID, "employee_name_quick_filter_employee_list_value").send_keys("Sample 10 Name")

time.sleep(5)

Emp_ID = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/section/div[3]/ui-view/div[1]/div/div/div/table/tbody/tr/td[2]/a")
actual = Emp_ID.text
expected = "5432"

if actual == expected:
    Emp_ID.click()
else:
    print("Employee NOT Found")

time.sleep(15)

driver.find_element(By.XPATH, "(//div[@class='oxd-button-label-wrapper'])[2]").click()

time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/section/div[3]/ui-view/ui-view/div[1]/div/div/list/div/div[1]/button").click()

time.sleep(15)

# Fill in all required fields to create a goal
Goal_Name_field = driver.find_element(By.ID, "name_value")
Goal_Name = "Test Goal " + datetime.now().strftime("%Y%m%d%H%M%S")
Goal_Name_field.send_keys(Goal_Name)

time.sleep(5)

# # In the editor, insert an image
# editor = driver.find_element(By.CLASS_NAME, "mce-ico mce-i-mce-ico mce-i-settings")
# editor.send_keys(os.path.abspath("C:\TASK\image.jpg"))

# # Set the priority of the goal to "High", and the weight should be set to "20"

goal_date = driver.find_element(By.ID, "dueDate")
goal_date.clear()
new_goal = datetime.now() + timedelta(days=20)
goal_date.send_keys(new_goal.strftime("%Y-%m-%d"))
time.sleep(6)

driver.find_element(By.XPATH, "(//div[@class='input-group-append'])[2]").click()
driver.find_element(By.XPATH, "//*[@id=\"bs-select-5-2\"]/span").click()

weight_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/section/div[3]/ui-view/ui-view/div/div/div/div[2]/form/div/div/oxd-decorator[1]/div/div[2]/div/div[4]/div/div/div/div/oxd-spinner/div/input")
weight_field.clear()
weight_field.send_keys("10")

# # Once the goal is saved, verify the Goal Details
save_button = driver.find_element(By.XPATH, "//*[@id=\"addGoalContainer\"]/div/div[2]/form/div/div/oxd-decorator[4]/div/div[2]/button/span")
save_button.click()

time.sleep(20)

Verify_goal = driver.find_element(By.XPATH, "//div[@class='goal-name-wrapper']")
actual = Verify_goal.text
expected = Goal_Name

if actual == expected:
    print("Goal details match the data entered while creating the goal.")
else:
    print("Goal details NOT matching the expected data.")

# Close the browser
driver.quit()
