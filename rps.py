N=int(input("number of rounds u want to play "))
a=0 #score of the player
b=0 #score of the computer
for i in range(N):
    your_choice=input("enter your choice:")
    import random
    choices=["rock","paper","scissor"]
    comp_choice=random.choice(choices)
    print("ur choice:",your_choice)
    print("computer choice:",comp_choice)
    if comp_choice==your_choice:
        print("its a tie no point is given to anyone")
    elif (comp_choice=="scissor" and your_choice=="rock") or (comp_choice=="rock" and your_choice=="paper") or  (comp_choice=="paper" and your_choice=="scissor"):
         print("player won")
         a=a+1
    else:
        print("computer won")
        b=b+1
if a>b:
    print("player won the match by the score of:",a)
elif b>a:
    print("computer won the match by the score of:",b)
else:
    print("match tie")
