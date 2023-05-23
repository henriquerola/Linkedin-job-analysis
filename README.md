# Linkedin job analysis
Scripts that takes data from the job tab on linkedin and returns skills mentioned

# Prerequisites
To run all the components in this repository you will need to install python and some libraries:

```bash
pip install pandas
pip install seaborn
pip install selenium
pip install webdriver_manager
```
# Explanation
What each script does and how to use it:

## searchdata.py
In this script you can choose your search terms, including 'job name', 'location', 'time', 'type', 'experience' and 'modality'. This will be used on scraping.py.

You can run scraping.py directly, in which case you will be prompted to choose new search terms.

## scraping.py
This script collects job descriptions from Linkedin and stores on the job descriptions.csv file.

you will need to provide a valid username/email and password. It is recommended to not use your main account.

### 🛑 Disclaimer
The use of automated means to access LinkedIn without the express permission of LinkedIn is PROHIBITED.

LinkedIn will BLOCK you if you are scraping too much data and/or you don't have permission.

## skills.py
List of +150 skills, libraries and relevant tools for tech jobs. this will be used on cleaning.py.

## cleaning.py 
This script will use skills.py to search for the selected terms on job_descriptions.csv and put it on a dataframe format on database.csv.

## output.py
This is the script that I used to generate the graphics on the Analysis section.

# 📊 Analysis

## Objective
Extrack terms from job descriptions (Brazil only) and compare the results with Stack Overflow Developer Survey 2022. I want to see if there is a big difference between the survey data and data extracted on a 
specific context, in this case, job descriptions on brazil (from 04/2023 to 05/2023). The secondary objective is to analyze the difference (or lack of) between remote and in person jobs, as well as entry level and
junior-senior level positions.

## Relevant questions and hypothesis
- Is there any relevant difference between my results and the survey? if yes what are they and what is the most probable cause.

Hypothesis: No. If there is it would most likely be by either the limitation of descriptions used (1001 descriptions per row of data) or by a general change in demand from the market. 

- Is there any relevant change in the most requested skills by changing it from remote to in person?

Hypothesis: No. The skills needed are still the same, the only variation that I can think is if there is a bigger focus on mentioning skills for remote jobs.

- Is there any relevant change in the most requested skills by changing it from entry level to senior level?

Hypothesis: Yes. I expect that entry level jobs would mention general skills more (like excel and python) and senior level jobs will mention more specific skills (like machine learning tools for data science).

## Technical challenges
- Some search combinations results in less than 1001 jobs, making them less reliable for a comparison/analysis. Only the ones with 1001 jobs where used.
- Linkedin search engine sometimes will give remote jobs even when is searching only for in person jobs, affecting the depth of the conclusions that can be done. that happens with job level too. It
probably did not affect much on the final results for the questions that I have were pretty general.   

## Top 10 skills (sum of all)
![Somatório](https://github.com/henriquerola/Linkedin-job-analysis/assets/107077420/49de064b-0770-43e6-b0eb-4e80139951f6)

## remote vs in person 
![Engenheiro de software](https://github.com/henriquerola/Linkedin-job-analysis/assets/107077420/d7c43fcb-595c-437f-bf21-a8ebd1e02d70)

## entry level vs junior-senior level
![Analista de dados](https://github.com/henriquerola/Linkedin-job-analysis/assets/107077420/7ac4b7f7-c8dc-465e-921b-9b581df1c518)

## Final Results
- Is there any relevant difference between my results and the survey? if yes what are they and what is the most probable cause.

Conclusion: In general, no. The only big difference is that terms like python and excel appeared more than javascript and html/CSS. That can be explained by the focus given to each data, Stack Overflow did a
survey using data from all developers, while my research focused on data science types.

- Is there any relevant change in the most requested skills by changing it from remote to in person?

Conclusion: Yes. It was observed a slight increase in the mention of terms for remote jobs in general on all valid comparisons.

- Is there any relevant change in the most requested skills by changing it from entry level to senior level?

Conclusion: in a sense yes, junior-senior levels seemed to mention skills slightly more frequently then entry levels, but no difference could be observed on the variance between general and specific skills/tools. 

## Possible improvements for a more in-depth analysis
- Use of NLP (Natural Language Processing) for the gathering of relevant terms.
- Extrack more data to eliminate underfitting and false trends, making more in-depth analysis possible.
- diversify the places from which data is extracted. (Other job posting sites, google, social media..)

# Inspirations and fonts
- [Stack Overflow Developer Survey 2022](https://survey.stackoverflow.co/2022/)
- lukebarousse [video](https://www.youtube.com/watch?v=1kU_ASADlPY&t=307s)
