# the input for other searches can be put into this script

def get_info():
    ans = 'y' #input("Do you want to use the predefined search? (y/n): ")
    info = {}
    if ans == 'y':
        info['keywords'] = 'Análise de Dados'
        info['location'] = 'Brasil'
        info['times'] = '2592000'
        info['tipo'] = '1'
        info['experience'] = '1'
        info['modalidade'] = '1'
    else:
        info['keywords'] = input("keyword:")
        info['location'] = input("location:")
        info['times'] = input("times:")
        info['tipo'] = input("tipo:")
        info['experience'] = input("experience:")
        info['modalidade'] = input("modalide:")
    return info

info = get_info()
print(info)