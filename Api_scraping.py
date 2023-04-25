from linkedin_api import Linkedin
# Authenticate using any Linkedin account credentials
api = Linkedin('RolaRoleiro@gmail.com', 'Beth0813')
# GET a profile
jobs = api.search_jobs(keywords='Cientista de dados', companies=None, experience=None, 
                       job_type=None, job_title=None, industries=None, 
                       location_name='Brasil', remote=False, listed_at=86400, 
                       distance=None, limit=1, offset=0)
print(jobs)