import random, string
import webbrowser
import time
import requests

print("""
██╗░░██╗███████╗░█████╗░███╗░░██╗
╚██╗██╔╝██╔════╝██╔══██╗████╗░██║
░╚███╔╝░█████╗░░██║░░██║██╔██╗██║
░██╔██╗░██╔══╝░░██║░░██║██║╚████║
██╔╝╚██╗███████╗╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝
Made by Alliege
""")

num=input('[Xeon] Input how many codes you want to generate and Check: ')

f=open("Nitro Codes.txt", "w", encoding='utf-8')

print("[Xeon] Wait, Generating... ")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

#Check

with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("[Xeon] Valid | {} ".format(line.strip("\n")))
            break
        else:
            print("[Xeon] Invalid | {}".format(line.strip("\n")))
input("[Xeon] The end! PRess Enter 5 times to close the program.")
input("4")
input("Thanks for using Xeon! (3)")
input("2")
input("1")
