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
