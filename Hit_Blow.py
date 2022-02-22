import random

l1 = [i for i in range(10)]
random.shuffle(l1)
l2 = [l1[0], l1[1], l1[2], l1[3]]
print(l2)#3つ取り出してる



print("Hit and Browゲーム開始")


bool1 = True
while bool1:
    hit_count = 0
    brow_count = 0

    choose_num = input("enter 4 numbers:")#数字入力
    guess = list(choose_num)#配列に格納
    num_list = list(map(int, guess))#数字に変換
    for i in range(4):
        if l2[i] == num_list[i]:
            hit_count += 1



    if l2[0] == num_list[1] or l2[0] == num_list[2] or l2[0] == num_list[3]:
        brow_count += 1


    if l2[1] == num_list[2] or l2[1] == num_list[3] or l2[1] == num_list[0]:
        brow_count += 1


    if l2[2] == num_list[0] or l2[2] == num_list[1] or l2[2] == num_list[3]:
        brow_count += 1


    if l2[3] == num_list[0] or l2[3] == num_list[1] or l2[3] == num_list[2]:
        brow_count += 1

    print("{}  Hit".format(hit_count))
    print("{}  Blow".format(brow_count))

    if l2 == num_list:
        print("ALL HIT!\nゲーム終了")
        bool1 = False




"""
        
        
    
    
入力文字数超過に対するエラーコードがまだかけていない
入力文字が等しい場合の警告もまだ

        
        
        
        
"""