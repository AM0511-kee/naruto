import random
def guess_users(x):
    low=1
    high=x
    feedback=''
    while feedback !='c':
        guess=random.randint(low,high)
        feedback=(input(f"if {guess} is high (H),if low (L),or corect (C)")).lower()
        if feedback=='h':
            high = guess-1
        elif feedback=='l':
            low = guess+1

    
    print("yay!!! guess is correct")

guess_users(10)
