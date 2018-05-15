deg = {10:'A',9:'A',8:'B',7:'C',6:'D',5:'F',4:'F',3:'F',2:'F',1:'F',0:'F'}
score=int(input('점수 : '))
score_d=score//10
if score >= 0 and score <= 100:
    print(score,':',deg[score_d])
else:
    print('입력가능한 점수 범위는 0~100입니다.')
