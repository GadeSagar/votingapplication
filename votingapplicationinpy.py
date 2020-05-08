
import random


num1 = int(input("Enter the nummber of candidates:"))
cand1 = input(f'Enter {num1} candidates now:\n').split()
print("Candidates are :", cand1)
print('Voting is live .............. Please wait for the results..........')
print("Voting has been finished..... and wait is over")
print("Here are the results")
votes = []
for i in range ( 0, num1):
    c = random.randrange(1,100,3)
    votes.append(c)

for j in range(num1):
    print(cand1[j], ':', votes[j])
print("Here the winner is ...")

maximum = max(votes)
count = 0

for k in range(num1):
    if votes[k] == maximum:
        count = k
print(cand1[count], ":", maximum)
