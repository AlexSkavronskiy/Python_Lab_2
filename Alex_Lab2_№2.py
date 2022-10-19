a='***'
b=' '+a
c='  '+a
d='   '+a
flag=0
while flag!=20:
    flag += 1
    if flag==1 or flag==19:
        print('\t'*6,a,'\t'*11, a)
    if flag==2 or flag==18:
        print('\t'*5, b+d,'\t'*9, b+d)
    if flag == 3 or flag == 17:
        print('\t'*4, c+d*2,'\t'*8, c+d*2)
    if flag == 4 or flag == 16:
        print('\t'*3, d*4,'\t'*6, d*4)
    if flag == 5 or flag==15:
        print('\t'*3, a+d*4,'\t'*5, a+d*4 )
    if flag == 6 or flag == 14:
        print('\t'*2, b+d*5,'\t'*3, b+d*5)
    if flag == 7 or flag == 13:
        print('\t',c+d*6,'\t'*2,c+d*6)
    if flag == 8 or flag == 12:
        print("\t"+a+d*7,c+d*7)
    if flag==9:
        print(' '+'***   '*17)