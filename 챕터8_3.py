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
