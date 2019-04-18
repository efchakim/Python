#This program simulates the code-breaking game Mastermind. 
#This program checks the players guess against the initial for random numbers between 1-6. 
#Enter four guesses from 1-6, example: 1234.
#By: Diana Hakim

def GenCode():
    'generate four random numbers in a list'
    import random
    List =[]
    for i in range(4):
        ran =random.randrange(1,7)
        List += [int(ran)]
    #List = [4,2,4,6];#List = [2,1,4,5];#List = [2,4,3,1]
    return list(List)


def blackbox(gen, sguess): #works
    'compares two lists and finds if the index and value if the same for each value'
    ans = gen[0:] #ans cannot change
    guess = []
    for i in (list(sguess)):
        i = int(i)
        guess += [i]
    list(guess)
    for i in range(len(guess)):
        if gen[i] == guess[i]: #if correct or gen[i] == int(str(numinp[i]))
            gen[i]=u"\u25A0"
            guess[i]="x"
    return gen, list(guess), ans


def whitebox(gen, guess, ans):
    'compares two lists and finds if values are the same'
    #print(gen)
    
    for i in gen:
        if i in guess:
            new= gen.index(i)
            newguess= guess.index(i)
            guess[newguess]="x"
            gen[new]=u"\u25A1"
    #print(guess)
    #print(gen)
    return gen, guess, ans


def mastermind():
    'this game checks the players guess against the initial for random numbers between 1-6, ex to be entered is 1436.'
    print('\n{:^30}\n{}\n1. {}\n2. {}'.format('Mastermind','Type four guesses from 1-6 ex. 1236',u"\u25A0 means 1 of your ans is in the right position",u"\u25A1 means 1 of your ans is in the wrong position"))
    guessnumber = 0; gen = GenCode()
    List = gen[0:] #'Variables & Assignments' lists are mutable
    while True:
        boxlist = []
        guessnumber += 1
        guess=(input('Enter your guess: '))
        gen = List [0:]
        gen, guess, ans = blackbox(gen, guess)
        if guess == [7,7,7,7]:
            print(ans)
        final = whitebox(gen, guess, ans)
        gen, guess, ans = final
        #print(gen) #testing [6, '□', '□', '■']
        #print(List) #testing [6, 1, 4, 4]
        for i in gen:
            if type(i).__name__ == 'str':
                boxlist += [i]
        for i in sorted(boxlist): #print out all boxes
            print(i, end=' ')
        print()
        if gen.count(u"\u25A0")==4:
            if guessnumber == 1: #1st try
                print('Hey! Good job! You won in {} try!'.format(guessnumber))
                break
            else: #many tries 
                print('Hey! Good job! You won in {} tries!'.format(guessnumber))
                break
            
            
mastermind()
