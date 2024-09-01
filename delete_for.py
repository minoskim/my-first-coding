import pandas as pd
from pandas import read_excel
import pyperclip
import time


capturelist = read_excel(r"C:\python11\selenium\naver\deleteProduct.xlsx")

for i in range(len(capturelist.index)):
    codeNumber = str(capturelist['자사상품코드'][i])



    # driver.execute_script("document.body.style.zoom='100%'")
    
    # copyPageAddress = input("상세페이지를 복사할 스마트스토어 주소를 입력 하세요.. ")
    print("삭제할 자사상품코드 번호를 입력 하세요.. ", f"{codeNumber}")
    pyperclip.copy(codeNumber)
    exec(open(r"C:\python11\selenium\naver\no_pro_del(20230806)_for.py",'rt',encoding='UTF-8').read())
    time.sleep(0.5)
    # input()
    # exec(open(r"C:\python11\selenium\naver\fastinput0(20231012)_for.py",'rt',encoding='UTF-8').read())o

        
