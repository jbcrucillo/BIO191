str = input("Enter a word: ")

previous_char_isvowel = False
curr_char = ""
current_char_isvowel = False
cnt = 0
syllable_cnt = 0

for c in str:
    curr_char = c
    if (c=="a") or (c=="e") or (c=="i") or (c=="o") or (c=="u") or (c=="y"):
        current_char_isvowel = True
    else:
        current_char_isvowel = False
    
    if cnt == 0:
        previous_char_isvowel = current_char_isvowel
        cnt = cnt + 1
        continue

    elif previous_char_isvowel and current_char_isvowel:
        previous_char_isvowel = False
        continue
    elif previous_char_isvowel == False and current_char_isvowel == False:
        syllable_cnt = syllable_cnt + 1

    previous_char_isvowel = current_char_isvowel

if curr_char == "e":
    syllable_cnt = syllable_cnt - 1
if syllable_cnt <=0:
    syllable_cnt = 1
else:
     syllable_cnt = syllable_cnt + 1

print ("Syllables:", syllable_cnt)
