#shitbot

import datetime as dt
import sys
import time
import math

def shitbot():
    
    def loadscreen():
        print("checking for updates...")
        animation = ["[#.........]","[##........]", "[###.......]", "[####......]", "[#####.....]", "[######....]", "[#######...]", "[########..]", "[#########.]", "[##########]"]
        for i in range(len(animation)):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

        
    def installanimation():
        #not sure how to make it actually install shit lmfao
        print("installing updates...")
        animation = ["[#.........]","[##........]", "[###.......]", "[####......]", "[#####.....]", "[######....]", "[#######...]", "[########..]", "[#########.]", "[##########]"]
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\ndone")
        print("\n")

        
    def shitbot_MainMenu():
        print("welcome to shitbot version 16.2")
        userCommandInputWelcome=input("Enter a command: ")
        if(userCommandInputWelcome.startswith("/shitbot")):
            if(userCommandInputWelcome.endswith("help")):
                shitbot_MenuOption_Help()
            elif(userCommandInputWelcome.endswith("version")):
                shitbot_MenuOption_Version()
            elif(userCommandInputWelcome.endswith("check")):
                shitbot_MenuOption_Check()
            elif(userCommandInputWelcome.endswith("autoupdate")):
                shitbot_MenuOption_AutoUpdate()
            elif(userCommandInputWelcome.endswith("bugreport")):
                shitbot_MenuOption_BugReport()
            elif(userCommandInputWelcome.endswith("meme")):
                shitbot_MenuOption_meme()
            elif(userCommandInputWelcome.endswith("suggest")):
                shitbot_MenuOption_Suggest()
            elif(userCommandInputWelcome.endswith("health")):
                shitbot_MenuOption_Health()
                if(userCommandInputWelcome.endswith("health aggression")):
                    print("aggression")
            elif(userCommandInputWelcome.endswith("lockdown")):
                shitbot_MenuOption_Lockdown()
            elif(userCommandInputWelcome.endswith("exit")):
                shitbot_MenuOption_Exit()
            else:
                print("Not a command\n\n")
                shitbot_MainMenu()
        else:
            print("not a command\n\n")
            shitbot_MainMenu()

            
    def shitbot_MenuOption_Help():
        print('''
command list:
    /shitbot exit
        exit shitbot
    /shitbot help
        display this help menu
    /shitbot version
        check the current version of shitbot
    /shitbot check
        check for updates for shitbot
    /shitbot autoupdate
        enable or disable automatic updating
    /shitbot meme
        shitbot will search the infinte realms and return to you the finest quality meme
    /shitbot health
        gives you friendly reminders to do healthy things throughout the day
        - this command works in unity with
            /shitbot health aggression (1-10)
                control how aggressively shitbot tells you to do healthy things
    /shitbot suggest (suggestion)
        suggest something new for shitbot to do
    /shitbot bugreport (bugreport)
        report something shitbot doesnt do correctly
    /shitbot lockdown
        for an administrator to put shitbot into lockdown mode in case of security issues
''')
        input("press enter\n")
        shitbot_MainMenu()

        
    def shitbot_MenuOption_Version():
        #make the version into a static number
        #that only changes when "/shitbot check : y" is done
        now = dt.datetime.now()
        y=sum=int(now.year) - int(2000)
        m=(now.month)
        print("current shitbot version is {}.{}\n".format(y,m))
        input("press enter\n")
        shitbot_MainMenu()


    def shitbot_MenuOption_Check():
        loadscreen()
        now = dt.datetime.now()
        year=sum=int(now.year) - int(2000)
        mon=(now.month)
        if (year,mon == now.year,now.month): # this doesnt work because the version isnt really a thing
            print("no updates found")
        else:
            check_UpdatesFoundInstallPrompt=input("updates found\ninstall? (y/n): ")
            if(check_UpdatesFoundInstallPrompt == "y"):
                installanimation()
                input("press enter")
                shitbot_MainMenu()
            elif(check_UpdatesFoundInstallPrompt == "n"):
                print("not installing updates")
                shitbot_MainMenu()
            else:
                print("not an option")
                shitbot_MainMenu()
            
        input("press enter")
        shitbot_MainMenu()


    def shitbot_MenuOption_AutoUpdate():
        print("placeholder")
    def shitbot_MenuOption_BugReport():
        print("placeholder")
    def shitbot_MenuOption_meme():
        print("placeholder")
    def shitbot_MenuOption_Suggest():
        print("placeholder")
    def shitbot_MenuOption_Health():
        print("placeholder")
    def shitbot_MenuOption_Lockdown():
        print("placeholder")
    def shitbot_MenuOption_Exit():
        exit
    shitbot_MainMenu()
shitbot()    

