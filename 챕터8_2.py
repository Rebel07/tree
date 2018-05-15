a=str(input('문자열 : '))
print('개별 문자 출력 :',end='')
for i in range (len(a)):
    print(a[i],end='')
print('')
print('역순 개별 문자 출력 :',end='')
for i in range (len(a)-1,-1,-1):
    print(a[i],end='')
