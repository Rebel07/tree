#1번
a=str(input('문자열 : '))
print('문자열 길이 :',len(a))
print('첫 번째 문자 :',a[0])
print('두 번째 문자 :',a[1])
print('마지막 문자 :',a[-1])

#2번
a=str(input('문자열 : '))
print('개별 문자 출력 :',end='')
for i in range (len(a)):
    print(a[i],end='')
print('')
print('역순 개별 문자 출력 :',end='')
for i in range (len(a)-1,-1,-1):
    print(a[i],end='')

#3번
score=int(input('점수 : '))
if score >= 0 and score <= 100:
    if score >= 90:
        print(score,':','A')
    elif score >= 80:
        print(score,':','B')
    elif score >= 70:
        print(score,':','C')
    elif score >= 60:
        print(score,':','D')
    else:
        print(score,':','F')
else:
    print('입력가능한 점수 범위는 0~100입니다.')

#4번
deg = {10:'A',9:'A',8:'B',7:'C',6:'D',5:'F',4:'F',3:'F',2:'F',1:'F',0:'F'}
score=int(input('점수 : '))
score_d=score//10
if score >= 0 and score <= 100:
    print(score,':',deg[score_d])
else:
    print('입력가능한 점수 범위는 0~100입니다.')

#5번
items = {'라면':650,'우유':1100,'콜라':1200,'캔커피':500,'과자':700}
s=0
while True:
    it=str(input('제품명 : '))

    if it in items:
        s=s+items[it]
        print('[%s:%d] > %d'%(it,items[it],s))
    elif it=='':
        print('총 급액 :',s)
        break
    else:
        print(it,'는 미등록 제품입니다.')

#6번
engkor_dict = dict()
while True:
    eng = input('영어 단어 : ')
    kor = input('한글 단어 : ')
    if eng != '' and kor != '':
        engkor_dict[eng] = kor
    else:
        print(engkor_dict)
        break

#7번
engkor_dict = dict()
while True:
    eng = input('영어 단어 : ')
    if not len(engkor_dict) > 0:
        print('사전이 비어 있습니다.')
        print('단어를 추가합니다.')
        kor = input('한글 단어 : ')
        engkor_dict[eng] = kor
    if eng not in engkor_dict and eng != '':
        print('%s 단어가 등록되어 있지 않습니다.'%(eng))
        print('단어를 추가합니다.')
        kor = input('한글 단어 : ')
        engkor_dict[eng] = kor
    elif eng in engkor_dict:
            print('%s : %s'%(eng,engkor_dict[eng]))
    if eng == '':
        print(engkor_dict)
        break

#8번
import time
for i in range(1,6):
    print(i,end=' ');time.sleep(1)

#9번
import math
a = float(input('실수 : '))
print(a,':',math.ceil(a))
print(a,':',math.floor(a))
print(a,':',math.trunc(a))
