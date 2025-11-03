import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

print(
    Fore.BLUE 
    + Back.YELLOW 
    + "Hi, It's theBappy"
    + Fore.YELLOW 
    + Back.BLUE
    + "I love coding"
)

print(Back.CYAN + "Hi, I am from USA")
print(Fore.RED + Back.GREEN + "from Derbin Street.")