print('3 Задание','\n')

y=0
while y<10:
    y+=1
    if y==1:
        print('y''\n''|')
    if y==2:
        print('|'+'\t'*(y+4)+' '+'*')
    if y==3:
        print('|'+'\t'*(y+2)+' '+'*')
    if y==4:
        print('|'+'\t'*(y)+' '+'*')
    if y==5:
        print('|'+'\t'*(y-2)+' '+'*')
    if y==6:
        print('|'+'\t'*(y-4)+' '+'*')
    if y==7:
        print('|'+'\t'*(y-6)+' '+'*')
    if y==8:
        print('|'+'\t'*(y-8)+' '+'*')
if y==10:
    print('|'+'–––'*10+'x''\n''0')
