email=input("Enter your Email:")#g@g.in,
k,j,d=0,0,0
if len(email)>=6:#required condition--1
    if email[0].isalpha():#rc-2
        if ("@" in email ) and (email.count("@")==1):#rc-3
            if(email[-4]==".") ^ (email[-3]=="."):#rc-4
                for i in email:
                    if i==i.isspace(): #general condion-1
                        k=1
                    elif i==i.isalpha():#gc-2
                        if i==i.upper():#gc-3
                            j=1
                    elif i.isdigit:#gc-4
                        continue
                    elif i=="_" or i=="." or i=="@":#gc-5
                        continue
                    else:#general commdtion any other things expect above is onvalid
                        d=1



                if k==1 or j==1 or d==1:
                    print("Invalid Email")
            
            else:
                print("Error-Dot availble in some other postion")
        else:
            print("There should be only one @")
    else:
        print("First charcter should be alphabet")
else:
    print("email length is invalid")