import random 

#Generate random 4 Colors
colors = ['R','B','Y','G','W','O']
Trial = 10
color_length = 4

#genrate random code From the colors (4 color code)
def generate_code():
    guess  = []
    for _ in range(4):
        ch = random.choice(colors)
        guess.append(ch)
    print(guess)
    return guess
    
#user Input By handling invalid Inputs
def user_input():
    while True:
        user = input('Guess the Code(space separated):').upper().split(' ')
        if len(user)!=color_length:
         print(f'You must Choose {color_length} Colors !!')
         continue
        for color in user:
            if color not in colors:
                print(f"Invalid Color :{color}. Try Again!!")
                break
        else:
            break
    return user  
            
#Logic of the Code
def matchPattern(guess,user):
    c = {} #color count 
    cp = 0
    ip= 0 
    for color in guess:
        if color not in c:
            c[color]=0
        c[color]+=1
    #find the corect position
    for guess_color,user_color in zip(guess,user):
        if guess_color==user_color:
            cp+=1
            c[guess_color]-=1
    #find the incorrect position        
    for guess_color,user_color in zip(guess,user):
        if guess_color in c and c[guess_color]>0:
            ip +=1
            c[guess_color]-=1

    return cp,ip

#lOgic o the code
def game():
    code = generate_code()
    print(f'Welcome to the MasterMind Game !\n You have 10 tries To guess the Code. \n You Must Choose Four colors From These : {colors}')
    for attempts in range(1,Trial+1):
        guess = user_input()
        cp,ip = matchPattern(guess,code)
        if cp == color_length:
            print(f'\nHurray!! You have guessed The code In {attempts} Attempt.\n')
            break
        print(f'Correct Postion :{cp} | Incorrect Postion :{ip} \n Attempts Left : {attempts}')
        
    else:
        print('You have Ran out Of trials!!\n The code was :',*code)

if  __name__ == '__main__':
    game()