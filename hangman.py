def hangman(word):
    wrong = 0                                   #プレイヤーが間違えた数。
    stages = ['',
              '______     ',
              '|     |    ',
              '|     0    ',
              '|    /|\   ',
              '|    / \   ',
              ]
    ans_letters = list(word)                    #解答（malphite）を一文字ずつ分解してリスト化したもの。
    board = ['_'] * len(word)                   #　_ * 解答の文字数。入力された正答を記録して表示させる為。
    win = False                                 #ゲームに勝利したかどうかを記録。初期状態はFalse。
    print('Welcome to Hangman!')

    while wrong < len(stages) - 1:              #間違えた数＜ステージの長さ−１（6-1=5）まで繰り返す。
        print('\n')
        msg = 'Enter a letter '
        ans = input(msg)                        #プレイヤーの入力。
        if ans in ans_letters:                  #入力した一文字が答えの中にあれば、
            let_number = ans_letters.index(ans) #indexで入力した一文字がans_letterの何文字目かを取得し、let_numberに代入。
            board[let_number] = ans             #boardのlet_number目に入力した一文字を入れる。
            ans_letters[let_number] = '$'       #重複防止を考慮して正答の一文字に$を代入。
            print(board)                        #正答の現状
            print(stages[wrong])                #誤答の現状
        else:
            print(board)                        #正答の現状
            wrong += 1                          #wrongをインクリメント
            a = 0
            for a in range(0, wrong):           #0~wrongまで、
                print(stages[a+1])              #hangmanを表示
        if '_' not in board:                    #board内に_がなくなった＝正答で埋まった場合
            print('You Win!')
            win = True
            break
    if not win:
        print('You lose... The answer is {}.'.format(word))

hangman('malphite')
