import time
t=input("Enter AM or PM:")
time=int(input("Enter time:"))
a=input("Are you leaving Home[y/n]:")
if(a=='n' or a=='N'):
    while(t=='AM' or t=='am'):
        if(time==12 or time==1 or time==2 or time==3 or time==4 or time==5 or time==6):
            print("Lights and fans on the living room ,kitchen,verandah to be switched off")
            print("fans on the bedroom to be switched on")
            break
        elif(time==7):
            print("Lights on the bedroom to be switched on")
            print("Lights on the living room to be switched on")
            print("Lights on the kitchen to be switched on")
            print("Lights on the verandah to be switched off")
            break
        elif(time==8 or time==9 or time==10):
            print("Lights and fans on the bedroom to be switched off")
            print("Lights and fans on the living room to be switched on")
            print("Lights on the kitchen to be switched on")
            print("Lights on the dining room to be switched on")
            print("Lights on the verandah to be switched off")
            break
        else:
            print("All the lights on the home to be turned off")
    while(t=='PM' or t=='pm'):
        if(time==10 or time==11):
            print("Lights and fans on the bedroom to be switched on")
            print("Lights on the kitchen,living room and verandah to switched off")
            break
        elif(time==12 or time==1):
            print("Lights on the kitchen to be turned on")
            print("Lights on the bedroom and verandah to be turned off")
            break
        elif(time==2):
            print("Lights on the Dining room to be turned on")
            print("Lights on the living room to be turned off")
            print("Lights on the bedroom to be turned off")
            print("Lights on the verandah to be turned off")
            break
        elif(time==3 or time==4):
            print("Lights on the kitchen to be turned off")
            print("Lights on the verandah to be turned off")
            break
        elif(time==5):
            print("Lights on the kitchen to be turned on")
            print("Lights and fans on the living room to be turned on")
            break
        elif(time==6 or time==7):
            print("Lights and fans on the living room to be turned on")
            print("Lights on the verandah to be turned on")
            print("Lights on the kitchen to be turned off")
            break
        elif(time==8 or time==9):
            print("Lights on the kitchen to be turned on")
            print("Lights on the dining room to be turned on")
            break
        else:
            print("All the lights and fans on the home to be turned off")

else:
    print("All the lights on the home to be turned off")
if(a=='n' or a=='N'):
    b=input("Want to use bathroom:[y/n]")
    if(b=='y' or b=='Y'):
        print("Lights on the bathroom to be switched on")
    else:
        print("Lights on the bathroom to be switched off")
