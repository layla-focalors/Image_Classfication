import os
ORIGIN = os.listdir('C:\\Users\\starl\\Downloads\\data\\data\\')
PATH = 'C:\\Users\\starl\\Downloads\\data\\data\\'
EXPORT = 'C:\\Users\\starl\\Downloads\\class\\data2\\'
os.chdir('./data2')
for i in ORIGIN:
    print(i.split('_')[0])
    maken = i.split('_')[0]
    try:
        os.mkdir(maken)
    except:
        pass        
    os.system(f'move {PATH + i} "{str(EXPORT + maken)}"')
    print(f"processing now : {PATH + i}")