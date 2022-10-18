print('4 Задание','\n')

import csv
with open('books_original.csv','r',encoding='cp1251') as file:
    reader=csv.reader(file,delimiter=';')
    count_more_price=0 # Количество поставок большей цены
    count_low_price=0  # Количество поставок меньшей цены
    count=0 # Общее количество поставок
    count_book = 0 # Количество книг стоющее больше цены
    price=0 # Цена каждой книги

    for row in reader:
        row_txt=[]
        for i in row:
            f=i.replace('.','.')
            row_txt.append(f)
            if len(row_txt)>8 and len(row_txt)<10:
                if 'Цена поступления' not in row_txt[7]:
                    price = float(row_txt[7])
                if 'Кол-во выдач' not in row_txt[8]:
                    count_book = float(row_txt[8])
                count += count_book
                if price > 150:
                    count_more_price += count_book
                count_low_price = count - count_more_price

y=(round((count_low_price/count)*100)) #Процентное соотношение количество поставок меньшей цены к общее количество поставок
x=(round((count_more_price/count)*100)) #Процентное соотношение количество поставок большей цены к общее количество поставок
c=0 # Флаг

for i in range(100,0,-1):
    if y>x:
        if i>y and c==0:
            print(i,'%')
        if y>=i and x<i:
            print(i,'%','\t'*4,'\u001b[48;5;21m','\t'*8,'\u001b[0m')
            c+=1
        if x>=i:
            print(i,'%','\t'*4,'\u001b[48;5;21m','\t'*8,'\u001b[0m','\t', '\u001b[48;5;46m', '\t' * 8, '\u001b[0m')
    else:
        if i>x and c==0:
            print(i,'%')
        if x>=i and y<i:
            print(i,'%','\t'*4,'\u001b[48;5;21m','\t'*8,'\u001b[0m')
            c+=1
        if y>=i:
            print(i,'%','\t'*4,'\u001b[48;5;21m','\t'*8,'\u001b[0m','\t', '\u001b[48;5;46m', '\t' * 8, '\u001b[0m')
print('0 %'+'\t'*9+'\u001b[38;5;27my','\t'*9,'\u001b[38;5;46mx',)

