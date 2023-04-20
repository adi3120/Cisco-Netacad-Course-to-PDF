import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options


driver = webdriver.Firefox()
driver.get('https://www.netacad.com/portal/saml_login')

driver.implicitly_wait(10)

email=""
password=""

email_input = driver.find_element(By.ID, 'idp-discovery-username')

email_input.send_keys(email)

next_button = driver.find_element(By.ID, 'idp-discovery-submit')

next_button.submit()

password_input = driver.find_element(By.ID, 'okta-signin-password')

password_input.send_keys(password)

login_button = driver.find_element(By.ID, 'okta-signin-submit')

login_button.click()

launch_course_link=driver.find_element(By.XPATH, '//a[contains(@href, "https://lms.netacad.com/course/view.php?id=1410004")]')

launch_course_link.click()

module_links=driver.find_elements(By.CLASS_NAME,"activityinstance")
a_tag = module_links[3].find_element(By.TAG_NAME, "a")

a_tag.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

time.sleep(20)


# driver.get_full_page_screenshot_as_file("1.png") 

link="https://contenthub.netacad.com/netess/"
subs=[6,4,5,6,5,5,4,7,3,5,4,7,6,4,7,4,5,4,5,7]

for k,i in enumerate(subs):
	n=0
	for j in range(0,i+1):
		driver.get(link+str(k+1)+"."+str(j)+".1?lng=en")
		time.sleep(15)
		driver.get_full_page_screenshot_as_file(str(k)+"_"+str(n)+".png") 
		n+=1

