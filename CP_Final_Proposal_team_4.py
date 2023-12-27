

def guessnum(guess, real):

    global out_count
    out_counter = 0
    ball_count = 0
    strike_count = 0

    guess_lst = list(str(guess)) #자릿수 별로 비교해야하기 때문에 str로 치환
    real_lst = list(str(real))

    for i in guess_lst:
        if real_lst.count(i) == 0:
            out_counter+=1
            if out_counter == 2:
                out_count +=1
        for j in real_lst:
            if i == j and real_lst.index(j) != guess_lst.index(i):
                ball_count += 1
            if i == j and real_lst.index(j) == guess_lst.index(i):
                strike_count += 1

    return [ball_count, strike_count, out_count]

def result_lst(guessnum_lst):

    global base_result
    global init_val

    ball_count = guessnum_lst[0]
    strike_count = guessnum_lst[1]
    if ball_count == 1:#안타
        base_result.insert(0,1)
    elif ball_count == 2:#2루타
        base_result.insert(0,1)
        base_result.insert(0,0)
    elif strike_count == 1:#3루타
        base_result.insert(0,1)
        base_result.insert(0,0)
        base_result.insert(0,0)
    elif strike_count == 2:#홈런
        init_val = setnum()
        base_result.insert(0,1)
        base_result.insert(0,0)
        base_result.insert(0,0)
        base_result.insert(0,0)

    if len(base_result) >= 4: #접수합산 
        base_result.insert(3,sum(base_result[3:])) #Index3부터 끝까지 sum
        del base_result[4:] #Index[3]에 sum 값을 저장하고 Index[4]부터 끝까지 삭제

    return base_result

inning = 2
team_1_score_per_inning = [0]*inning
team_2_score_per_inning = [0]*inning

print('''-----------------------------------------
|                                       |
|              Game start!              |
|                                       |
-----------------------------------------''')
for i in range(1, inning):#9회
    for j in range(1, 3):#초 , 말 번갈아가기
        if j == 1:#초 공격
            print(f'The top of {i} inning.')
            print('The opponent\'s number is newly set.')
            # 이닝 초기 세팅
            init_val = setnum()  # 맞춰야할 숫자 세팅
            base_result = [0, 0, 0, 0]  # [1루,2루,3루,홈]
            out_count = 0  # 아웃카운트 초기화
            Q_count = 1  # 질문 횟수 카운트 초기화
            attack = True #While문을 돌리기 위함
            file1 = 'score.txt'#결과값을 저장해둘 텍스트 파일 지정
            while attack:
                if Q_count >= 7:
                    attack = False
                guess_team1 = int(input(f'[{Q_count}] Guess the Opponent\'s Number : '))
                result_lst(guessnum(guess_team1, init_val))
                team_1_score_per_inning[i-1] += base_result[3]
                base_result[3] = 0
                if out_count > 0:  # 아웃이 발생했을때
                    if out_count >= 3:
                        attack = False
                        print()
                        print('-'*41)
                        print('Three OUT!.')
                        print(f'End the top of {i} inning')
                        print(f'You scored {team_1_score_per_inning[i-1]} points in this inning.')
                        print('-'*41)
                        print()
                    else:
                        print()
                        print(f'---------------[{Q_count}]Result----------------')
                        print(f'1st Base: {base_result[0]}')
                        print(f'2nd Base: {base_result[1]}')
                        print(f'3rd Base: {base_result[2]}')
                        print(f'Point:   {team_1_score_per_inning[i-1]}')
                        print(f"It\'s  {out_count} Out right now.")
                        print('-'*41)
                        print()
                else:
                    print()
                    print(f'---------------[{Q_count}]Result----------------')
                    print(f'1st Base: {base_result[0]}')
                    print(f'2nd Base: {base_result[1]}')
                    print(f'3rd Base: {base_result[2]}')
                    print(f'Point:   {team_1_score_per_inning[i-1]}')
                    print(f"It\'s  {out_count} Out right now.")
                    print('-'*41)
                    print()
                if Q_count >= 7:
                    print()
                    print('-'*41)
                    print("You\'ve used up all your attack opportunities")
                    print('-'*41)
                    print()
                Q_count += 1
                

        elif j == 2:
            print(f'The Bottom of {i} inning')
            print('The opponent\'s number is newly set.')
            # 이닝 초기 세팅
            init_val = setnum()  # 맞춰야할 숫자 세팅
            base_result = [0, 0, 0, 0]  # [1루,2루,3루,홈]
            out_count = 0  # 아웃카운트 초기화
            Q_count = 1  # 질문 횟수 카운트 초기화
            attack = True #While문을 돌리기 위함
            while attack:
                if Q_count >= 7:
                    attack = False
                guess_team2 = int(input(f'[{Q_count}] Guess the Opponent\'s Number : '))
                result_lst(guessnum(guess_team2, init_val))
                team_2_score_per_inning[i-1] += base_result[3]
                base_result[3] = 0
                
                if out_count > 0:  # 아웃이 발생했을때
                    if out_count >= 3:
                        attack = False
                        print()
                        print('-'*41)
                        print('Three OUT!.')
                        print(f'End the Bottom of {i} inning')
                        print(f'You scored {team_2_score_per_inning[i-1]} points in this inning.')
                        print()
                    else:
                        print()
                        print(f'---------------[{Q_count}]Result----------------')
                        print(f'1st Base: {base_result[0]}')
                        print(f'2nd Base: {base_result[1]}')
                        print(f'3rd Base: {base_result[2]}')
                        print(f'Point:   {team_2_score_per_inning[i-1]}')
                        print(f"It\'s  {out_count} Out right now.")
                        print('-'*41)
                        print()
                else:
                    print()
                    print(f'---------------[{Q_count}]Result----------------')
                    print(f'1st Base: {base_result[0]}')
                    print(f'2nd Base: {base_result[1]}')
                    print(f'3rd Base: {base_result[2]}')
                    print(f'Point:   {team_2_score_per_inning[i-1]}')
                    print(f"It\'s  {out_count} Out right now.")
                    print('-'*41)
                    print()

                if Q_count >= 7:
                    print()
                    print('-'*41)
                    print("You\'ve used up all your attack opportunities")
                    print('-'*41)
                    print()
                Q_count += 1

with open(file1, 'w') as file11:#위에서 지정한 score.txt에 작성기능으로 가져옴
    line1 = ', '.join(map(str, team_1_score_per_inning))
    #숫자를 원소로 가지는 score_per_inning 리스트의 요소를 모두 str로 바꿔 다시 만들어주는 함수
    #join은 str요소를 가진 list를 앞의 구별자 (우리의 경우 , )로 연결해준다 
    file11.write(line1+'\n')#팀1 점수 입력후 팀2 점수를 다음줄에 작성하기 위한 이스케이프 줄바꿈 문구
    line2 = ', '.join(map(str, team_2_score_per_inning))
    file11.write(line2)
print('----------------------------Game Result----------------------------')
print(f'During this match, Team 1')
for i in range(inning-1):
    print(f'Scored {team_1_score_per_inning[i]} points in the Top of {i+1} inning')
print()
print(f'이번 경기동안 team2은')
for i in range(inning-1):
    print(f'Scored {team_2_score_per_inning[i]} points in the Bottom of {i+1} inning')
print('-'*41)
