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
driver.maximize_window()

# navigate to the LinkedIn login page
url = "https://www.linkedin.com/login"
driver.get(url)

# enter the user's login credentials
username = "Usermail"
password = "******"
username_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"username")))
password_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"password")))
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# wait for the page to load
time.sleep(8)

# copy information to pass to the url
info = data.copy()

# navigate to the Jobs tab and search (Requires searchdata.py)
driver.get("https://www.linkedin.com/jobs/search/?&f_TPR=r"+info['times']+"&keywords="+info['keywords']+"&location="+info['location']+"&f_WT="+info['modalidade']+"&f_E="+info['experience']+"&refresh=true")

# wait for the page to load
time.sleep(5)

# select location of all jobs boxes
job_loc = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")

# Open a CSV file to write the job descriptions
with open('job_descriptions.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['job_description', str(data['keywords']), str(data['location']), str(data['times']), str(data['tipo']), str(data['experience']), str(data['modalidade'])]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # write search information as header
    writer.writeheader()

# Iterate over each job listing and extract the job description (1 to 40)
    next_page = True
    counter = 1
    pagen = 1
    max = 1
    try: 
        max = int(driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[6]/ul/li["+str(10)+"]").text)
    except:
        quit()

    # extrack job description
    while next_page:
        for i in range(1,40):
            try: 
                # Click on the job listing to expand the description
                job = job_loc.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li["+str(i)+"]") 
                job.click()
                
                # Wait for the job description to load
                time.sleep(0.5)
        
                # Find the job description element and extract the text
                job_description = driver.find_element(By.ID, 'job-details').text
                
                # write job description into the csv file
                writer.writerow({'job_description': job_description})
            except:
                continue
            
        # find the next page button if exists
        try:
            pagen += 1
            if pagen > max: # failsafe
                button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[5]/ul/li["+str(100)+"]")
            elif pagen == 2: # first page has diferent xpath 
                counter += 1
                button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[6]/ul/li["+str(counter)+"]")
            elif pagen < 10: # logic until the first ...
                counter += 1
                button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[5]/ul/li["+str(counter)+"]")
            elif 10 <= pagen < max - 6: # logic page 10 until max - 7
                counter = 7
                button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[5]/ul/li["+str(counter)+"]")
            elif pagen >= max - 6: # logic for the last 7 pages
                counter = pagen - max + 10
                button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[5]/ul/li["+str(counter)+"]")
            
            # click next page button if exists
            button.click() 
            
            # wait for the next page to load
            time.sleep(3)        
        except:
            next_page = False 

# close the web driver
driver.quit()