Candidate_1 , Candidate_2 , Candidate_3 , Candidate_4 = "Narendra Modi" , "Arvind Kejriwal" , "Mayavati" , "Rahul Gandhi"
votecount_1 = votecount_2 = votecount_3 = votecount_4 = 0

def castvote() :
    global votecount_1 , votecount_2 , votecount_3 , votecount_4
    print("Please choose one candidate. ")
    print("1.",Candidate_1)
    print("2.",Candidate_2)
    print("3.",Candidate_3)
    print("4." + Candidate_4 + "\n")
    value = int(input())
    if value > 4 or value <=0:
        print("You choose invalid candidate.")
    
    if value <= 4 and value > 0:
        print("\nYou choose :",value)
        print("Thanks for vote.")
    if value == 1:
        votecount_1 += 1
    elif value == 2:
        votecount_2 += 1
    elif value == 3:
        votecount_3 += 1
    elif value == 4:
        votecount_4 += 1

def votecount() :
    global votecount_1 , votecount_2 , votecount_3 , votecount_4
    print("\nVoting statics :")
    print(Candidate_1 + " = " + str(votecount_1))
    print(Candidate_2 + " = " + str(votecount_2))
    print(Candidate_3 + " = " + str(votecount_3))
    print(Candidate_4 + " = " + str(votecount_4))

castvote()
votecount()
    



