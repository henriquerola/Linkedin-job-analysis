import time
import csv
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
time.sleep(20)
keywords = 'cientista de dados'
location = 'Brasil'
times = '8600'
tipo = '1'
experience = '1'
modalidade = '1'
# navigate to the Jobs tab
# horario / experiencia / tipo de vaga / nome da vaga / local colocar no link abaixo
# &f_TPR=r tempo (86400 igual 24 horas)
# &keywords= pesquisa
# &location= localização
# &f_WT= (1,2,3) presencial hibrido remoto
# &f_JT= tipo de vaga (f,p,c,t,i)Tempo integral Meio período Contrato Temporário Estágio
# &f_E= nivel de experiencia (1,2,3,4,5,6) Estágio Assistente Júnior Pleno-sênior DiretorExecutivo
# &refresh=true

driver.get("https://www.linkedin.com/jobs/search/?&f_TPR=r"+times+"&keywords="+keywords+"&location="+location+"&f_WT="+modalidade+"&f_E="+experience+"&refresh=true")

# Pegar informações das vagas
time.sleep(5)
job_loc = driver.find_element(By.CLASS_NAME, "jobs-search-results-list") #"scaffold-layout__list-container"

# Open a CSV file to write the job descriptions
with open('job_descriptions.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['job_description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

# Iterate over each job listing and extract the job description (1 to 24)
    for i in range(1,5):
        try: 
            # Click on the job listing to expand the description
            job = job_loc.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li["+str(i)+"]") 
            job.click()
            # Wait for the job description to load
            time.sleep(1)
    
            # Find the job description element and extract the text
            job_description = driver.find_element(By.ID, 'job-details').text
            # Print the job description
            #print(job_description)
            #print("-" * 50)
            writer.writerow({'job_description': job_description})
        except:
            continue

time.sleep(400)


# close the web driver
time.sleep(8)
driver.quit()