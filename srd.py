#тут возможно лишние импорты
#да и дальше будет много говнокода
import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract
import xlwt
from xlwt import Workbook 
import datetime
import xlwt, xlrd
from xlutils.copy import copy as xlcopy

#Распознавание текста на фотке
#img = cv2.imread('che.jpeg')
#text = pytesseract.image_to_string(img, lang="rus")
#f = open('ch.txt','w')
#f.write(text)
#f.close()
#print(text)

#тут получение даты для записи в таблицу, плюс сохранение инфы с чека в тхт(были идеи, что с его будет проще в ексель вводить данные)
a = datetime.datetime.today().strftime("%d-%m-%Y")
#with open('ch.txt', 'r') as f:
#    ch = f.read().splitlines()
#print(ch)

#А тут начинается работа с екселем
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'Date')
sheet1.write(0, 1, 'Product')
sheet1.write(0, 2, 'Price')

tim = sheet1.write(1, 0, a)
sheet1.write(1, 1, 'Coffee')
sheet1.write(1, 2, '2 $')

wb.save('info.xls') 
#пока что при каждом запуске кода таблица создается заново, потом сделаю чтоб просто открывало существующую

read_book = xlrd.open_workbook('info.xls', on_demand=True)
rbook = read_book.get_sheet(0)

cells = rbook.row_slice(rowx=1, end_colx=2)
for cell in cells:
    en = (cell.value)
    print(en)

#if en == 'Date':
#	print('[+]')
#else:
#	print('[-]')