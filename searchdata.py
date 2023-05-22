# description --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# time (86400 equals to 24 hours, 2592000 equals to 1 month)
# keywords (job name (datascientist, software engineer etc)
# location (country city and/or state)
# modality (1 = in person,2 = hybrid,3 = work from home)  
# type (f = Full time,p = Part time,t = Temporary Contract,i = Internship)
# experience (1 = Internship ,2 = Assistant,3 = Junior,4 = Full-senior,5 = Executive,6 = Director) Estágio Assistente Júnior Pleno-sênior DiretorExecutivo
# OBS: '%2C' signifies space, thefore if you want to search for full time(f) and part time(p) jobs, you should write 'f%2Cp'
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# get info 
def get_info():
    ans = input("Do you want to use the predefined search? (y/n): ")
    info = {}
    if ans == 'y': # predefined search
        info['keywords'] = 'job name' 
        info['location'] = 'location'
        info['times'] = 'time'
        info['tipo'] = 'type'
        info['experience'] = 'experience'
        info['modalidade'] = 'modality'
    else: # write new info
        info['keywords'] = input("keyword: ")
        info['location'] = input("location: ")
        info['times'] = input("time interval: ")
        info['tipo'] = input("type: ")
        info['experience'] = input("experience: ")
        info['modalidade'] = input("modality: ")
    return info

info = get_info()
