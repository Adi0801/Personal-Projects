#a-z
#0-9
#. _ time 1
# @ time-1
# . pos--(-3 or -4)
#in regex to give first condion use ^[range] ,and  + to join condion ,[\c1c2..] search dor the charcter c1 and c2 in the regex string,? give either 0 or 1 (for only one charcter)
#and \w for searching specfic string in whole string \w{2,3} search on specfic postion $ search from backside---note no space btween condions
 
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('Enter your email:')

#search function of regex help to compare the given email by email_condtion

if re.search(email_condition,user_email):
    print("Valid Email")
else:
    print("Wrong email")