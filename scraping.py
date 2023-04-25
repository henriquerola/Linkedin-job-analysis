import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to the LinkedIn login page
url = "https://www.linkedin.com/login"
driver.get(url)

# enter the user's login credentials
username = "RolaRoleiro@gmail.com"
password = "Beth0813"
username_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"username")))
password_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"password")))
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# wait for the page to load
time.sleep(15)

# navigate to the Jobs tab
# horario / experiencia / tipo de vaga / nome da vaga / local colocar no link abaixo
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3573101658&distance=25&f_TPR=r86400&geoId=106057199&keywords=Software%20Engineer&location=Brasil&refresh=true")

# Pegar informações das vagas
time.sleep(5)
job_loc = driver.find_element(By.CLASS_NAME, "jobs-search-results-list") #"scaffold-layout__list-container"
job_listings = job_loc.find_elements(By.ID, "ember") # HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
print(len(job_listings))
# Iterate over each job listing and extract the job description
for job in job_listings:
    # Click on the job listing to expand the description
    job.click()
    
    # Wait for the job description to load
    time.sleep(1)
    
    # Find the job description element and extract the text
    job_description = driver.find_element(By.ID, 'job-details').text

    # Print the job description
    print(job_description)
    print("-" * 50)

time.sleep(400)


# close the web driver
time.sleep(8)
driver.quit()

#<div data-job-id="3557184690" class="job-card-container relative job-card-list
#    job-card-container--clickable
#    
#    job-card-list--underline-title-on-hover  jobs-search-two-pane__job-card-container--viewport-tracking-0">
