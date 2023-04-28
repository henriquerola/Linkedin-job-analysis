import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from searchdata import info as data
# install chrome extension
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
time.sleep(20)
# copy information to pass to the url
info = data.copy()

# description --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# &f_TPR=r tempo (86400 igual 24 horas)
# &keywords= cargo a pesquisar
# &location= localização
# &f_WT= (1,2,3) presencial hibrido remoto
# &f_JT= tipo de vaga (f,p,c,t,i) Tempo integral Meio período Contrato Temporário Estágio
# &f_E= nivel de experiencia (1,2,3,4,5,6) Estágio Assistente Júnior Pleno-sênior DiretorExecutivo
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# navigate to the Jobs tab and search 
driver.get("https://www.linkedin.com/jobs/search/?&f_TPR=r"+info['times']+"&keywords="+info['keywords']+"&location="+info['location']+"&f_WT="+info['modalidade']+"&f_E="+info['experience']+"&refresh=true")

time.sleep(5)

# select location of all jobs boxes
job_loc = driver.find_element(By.CLASS_NAME, "jobs-search-results-list") #"scaffold-layout__list-container"

# Open a CSV file to write the job descriptions
with open('job_descriptions.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['job_description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

# Iterate over each job listing and extract the job description (1 to 40)
    for i in range(1,40):
        try: 
            # Click on the job listing to expand the description
            job = job_loc.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li["+str(i)+"]") 
            job.click()
            # Wait for the job description to load
            time.sleep(1)
    
            # Find the job description element and extract the text
            job_description = driver.find_element(By.ID, 'job-details').text
            
            #write the job description into csv file
            writer.writerow({'job_description': job_description})
        except:
            continue

time.sleep(8)

# close the web driver
driver.quit()