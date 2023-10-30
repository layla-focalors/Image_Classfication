import os
PATH = 'C:\\Users\\starl\\Downloads\\class\\data\\origin\\'
result = os.listdir(PATH)

for i in result:
    if i[0:3] == 'cat':
        # print(PATH + i)
        os.system(f'move {PATH + i} "C:\\Users\\starl\\Downloads\\class\\data\\cat\\"')
    else:
        # print('dogs')
        os.system(f'move {PATH + i} "C:\\Users\\starl\\Downloads\\class\\data\\dog\\"')
    print(f"processing now : {PATH + i}")
# 파일 자동 분류 프로그램 ( 이름의 3글자를 읽어서 처리 ) 
