'''
Title: Voting
Authour: Michelle Liu
Date:7/03/24
Version:1
'''
#psuedocode:

#ask user age, store in age(integer)
age = int(input("What is your age?"))
#ask user if they are resident store in is_resident(true/false)
is_resident = bool(input("Are you a NZ resident?"))

#decision - if age> 17 and is_resident == True: they can vote else: they can't vote
if age > 17 and is_resident == True:
  print ("You can vote!")
else:
  print("Sorry you cannot vote")
  
