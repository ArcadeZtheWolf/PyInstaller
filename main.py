import os


def Uninstall(program):
    os.system("cd ~")
    os.system("sudo rm -r " + program)

def Install(program):
    os.system("cd ~")
    os.system("git clone https://github.com/ArcadeZtheWolf/" + program + ".git")
    os.system("cd " + program)
    os.system("chmod +x setup.command")
    os.system("chmod +x makefiles.command")
    os.system("chmod +x configfiles.command")
    print (program + " has been installed! To finish setup cd " + program + " and run ./setup.command")

def rm():
    print ("""What program would you like to uninstall?
1. MessageCreator
2. Quit
""")
    uninstall=input("#")
    if uninstall == "1":
        Uninstall('MessageCreator')
    elif uninstall == "2":
        print ("Cya!")
        os.kill
    elif uninstall != " ":
        print ("Invalid")
        rm()
        
def inst():
    print ("""What would you like to install?
1. MessageCreator
2. Quit
""")
    install=input("#")
    if install == "1":
        Install("MessageCreator")
        main()
    elif install == "2":
        print ("Cya soon!")
        os.kill
    elif install != " ":
        print ("Invalid option")
        inst()

def main():
    print ("Welcome to ArcadeZtheWolf's PyInstaller")
    print (" ")
    print ("""Please select an option:
1. Install
2. Uninstall
3. Quit
""")
    select=input("#")
    if select == "1":
        inst()
    elif select == "2":
        rm()
    elif select == "3":
        print ("Bye!")
        os.kill
    elif select != " ":
        print ("Invalid")
        main()

main()
