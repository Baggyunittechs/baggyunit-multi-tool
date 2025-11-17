import sys
import requests
import os
def ip_scanner():
    print("________________ BAGGYUNIT MULTI-TOOL ______________________")
    print(" ")
    print("scanning your ip address...........")
    print("_____________________ ")
    print("operating system: ", sys.platform)
    os.system("ip route")
    print("_______________________")

def web_scanner():
    print("_________________BAGGYUNIT MULTI-TOOL________________________")
    if len(sys.argv) < 3:
        print("usage: python sys.py -sC <https://yourwebsite.com>")
        sys.exit()

    website = sys.argv[2]
    print("scanning the webiste...............")
    try:
        response = requests.get(website) 
        print("Status Code:", response.status_code) 
        if response.status_code == 200: 
            print("Website is UP") 
        else: 
            print("Website responded but not OK") 
    except Exception as e: 
        print("Error:", e)

def web_scanner2():
    website2 = input("enter your website: ")
    print("scanning the website......................")
    try:
        response2 = requests.get(website2)
        if response2.status_code == 200:
            print("_____________________ ")
            print(f"{response2.status_code} OK")
            print("Website is UP")
            print("_____________________ ")
        else:
            print("website is up but not in 200 ok")
    except Exception as e:
        print("error:", e)
        
def main():
    print("_________________BAGGYUNIT MULTI-TOOL________________________")
    print("for shortcut:\nscan web =>> python sys.py -sC https://website.com\ncheck or scan your address =>> python sys.py -ip")
    print("usage: choose option 1 or 2")
    print("1. webscanning\n2. ip address scanning")
    print("_____________________ ")
    options = int(input("choose your number eg 1 or 2: "))
    
    if options == 1:
        ip_scanner()
    elif options == 2:
        web_scanner2()
    else:
        print("invalid option!!")
    

if len(sys.argv) < 2:
    main()
    sys.exit()
else:
   argument = sys.argv[1]
   
if argument == "website" or argument == "-sC":
    web_scanner()
elif argument == "address" or argument == "-ip":
    ip_scanner()
elif argument == "help" or argument == "-p":
    main()
else:
    print("invalid argument!")