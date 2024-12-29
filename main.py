from os import system
from time import sleep

file = str(input("File(txt): "))
delay = float(input("Delay(float): "))

system("cls") #win
#system("clear") #unix

with open(file, 'r', encoding='utf-8') as file:
    parse = []
    parse = file.readlines()
    
    for line in parse:
        for ch in line:
            print(ch, end='', flush=True)
            sleep(delay)

input()  