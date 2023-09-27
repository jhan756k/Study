import random

# 당대표 - 죽이기, 보호하기, 탄핵소추안
# 보좌관 - 추적하기 (연속X)

# 민주 대표0, 민주 보좌관1, 국힘대표2, 국힘 보좌관3
# 연속 안되게 수정

times = 1
win = ""
wstat = 0
lstat = 0
mstat = 0

for _ in range(times): # 게임 횟수
    # 게임 초기화
    alive = [True, True, True, True]
    save = [[0, 0, 0, 0]]
    game = [[True, True, True, True]]
    n = 0

    while True: # 게임 턴 진행
        n+=1 
        print("턴", n)
        for x in range(len(save[n-1])):
            print(save[n-1][x])
        print(game[n-1])
        print()
        
        if not alive[0] and not alive[2]: # 둘다 죽으면
            mstat += 1
            win = "무승부"
            break
        elif not alive[0]:
            lstat += 1
            win = "국힘"
            break
        elif not alive[2]:
            wstat += 1
            win = "민주"
            break

        # 민주 턴 시작 -----------------------------

        # 민주 대표 일
        mpres = random.randint(0, 3) # 0: 국힘 대표 암살 1: 국힘 보좌관 암살 2: 본인 보호 3: 보좌관 보호

        if mpres == 0 or mpres == 1: # 만약 암살하는데
            if alive[3]: # 보좌관 살아있으면
                mpres = 1 # 보좌관 암살
            else: # 보좌관 없으면 
                mpres = 0 # 대표 암살

        elif mpres == 2 or mpres == 3: # 만약 보호하는데
            if not alive[1]: # 보좌관 죽었으면
                mpres = 2 # 본인 보호

        # 민주 보좌관 일
        mhelp = random.randint(0, 1) # 0: 국힘 대표 추적 1: 국힘 보좌관 추적 
        if not alive[mhelp+2]:
            mhelp = 1 - mhelp # 살아있는 사람으로 바꿈
        if not alive[1]: # 본인 뒤지면
            mhelp = 4 # 죽음

        # 국힘 턴 시작 -----------------------------
        
        # 국힘 대표 일
        gpres = random.randint(0, 3) # 0: 민주 대표 암살 1: 민주 보좌관 암살 2: 본인 보호 3: 보좌관 보호
        if gpres == 0 or gpres == 1: # 만약 암살하는데
            if alive[1]: # 보좌관 살아있으면
                gpres = 1 # 보좌관 암살
            else: # 보좌관 없으면 
                gpres = 0 # 대표 암살

        elif gpres == 2 or gpres == 3: # 만약 보호하는데
            if not alive[3]: # 보좌관 죽었으면
                gpres = 2 # 본인 보호

        # 국힘 보좌관 일
        ghelp = random.randint(0, 1) # 0: 민주 대표 추적 1: 민주 보좌관 추적
        if not alive[ghelp]:
            ghelp = 1 - ghelp # 살아있는 사람으로 바꿈
        if not alive[3]: # 본인 뒤지면
            ghelp = 4 # 죽음

        # 할일 끝 ---------------------------------

        temp = []
        if mpres == 0:
            temp.append("민주 대표가 국힘 대표 암살시도")
        elif mpres == 1:
            temp.append("민주 대표가 국힘 보좌관 암살시도")
        elif mpres == 2:
            temp.append("민주 대표가 본인 보호")
        elif mpres == 3:
            temp.append("민주 대표가 보좌관 보호")

        if mhelp == 0:
            temp.append("민주 보좌관이 국힘 대표 추적")
        elif mhelp == 1:
            temp.append("민주 보좌관이 국힘 보좌관 추적")
        elif mhelp == 4:
            pass
        
        if gpres == 0:
            temp.append("국힘 대표가 민주 대표 암살시도")
        elif gpres == 1:
            temp.append("국힘 대표가 민주 보좌관 암살시도")
        elif gpres == 2:
            temp.append("국힘 대표가 본인 보호")
        elif gpres == 3:
            temp.append("국힘 대표가 보좌관 보호")

        if ghelp == 0:
            temp.append("국힘 보좌관이 민주 대표 추적")
        elif ghelp == 1:
            temp.append("국힘 보좌관이 민주 보좌관 추적")
        elif ghelp == 4:
            pass

        save.append(temp)
        # 정산 ------------------------------------

        # 민주당 대표 정산
        if mpres == 0: # 국힘 대표 암살
            if gpres == 2: # 국힘 대표가 본인 보호
                pass
            elif ghelp == 0: # 국힘 보좌관에게 추적당하면
                pass
            else: # 아니면 죽음
                alive[2] = False

        elif mpres == 1: # 국힘 보좌관 암살
            if gpres == 3: # 국힘 대표가 보좌관 보호
                pass
            elif ghelp == 0: # 국힘 보좌관에게 추적당하면
                pass
            else: # 아니면 죽음
                alive[3] = False

        # 국힘 대표 정산
        if gpres == 0: # 민주 대표 암살
            if mpres == 2: # 민주 대표가 본인 보호
                pass
            elif mhelp == 0: # 민주 보좌관에게 추적당하면
                pass
            else:
                alive[0] = False
        
        elif gpres == 1: # 민주 보좌관 암살
            if mpres == 3: # 민주 대표가 보좌관 보호
                pass
            elif mhelp == 0: # 민주 보좌관에게 추적당하면
                pass
            else:
                alive[1] = False 

        game.append([alive[0], alive[1], alive[2], alive[3]])
    print(win)

# print(wstat/times, lstat/times, mstat/times)
# print(save)