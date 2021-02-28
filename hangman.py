import random
def checkt():
    for i in t:
        if i=="_":
            return False
    return True

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''')
win=0
words=["pink","helping","cooker","difficult","fork","don","cake","shake","batman","babyyoda"]
s=random.choice(words)
print(f"no of letters in the word is {len(s)}")
list1=[] 
list1[:0]=s
t=["_"]*len(s)
lose=6

      
while win!=len(t)-1 or lose!=0:
    user=input("Guess a letter: ")
    if user in list1:
        for i in range(len(s)):
            if s[i]==user:
                t[i]=user
                list1.remove(user)
                print("Thats right!")
                string=(",").join(map(str,t))
                print(string)
                win+=1
            
        
        if checkt():
            print("you win!")
            break
    else:
        lose-=1
        string=(",").join(map(str,t))
        print(string)
        
        print("You guessed it wrong!")
        if lose==5:
            print(''' _______
     |/      |
     |      (_)
     |      
     |
    _|___
            ''')
        elif lose==4:
            print('''
       _______
     |/      |
     |      (_)
     |      \|
     |       
     |
    _|___
            ''')
        elif lose==3:
            print('''
       _______
     |/      |
     |      (_)
     |      \|/
     |      
     |
    _|___
            ''')
        elif lose==2:
            print('''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
            ''')
        elif lose==1:
            print('''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
            ''')
        elif lose==0:
            print("You lost!")
            print('''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
            ''')
            break
