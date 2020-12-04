import requests
import os
geter = requests.get(input("daj strone: "))
er = input("chcesz wszystko czy najważniejsze?(w,n): ")
if er == 'w':
    print("")
    print(geter.text)
if er == 'n':
    print("")
    print(geter.status_code)
    print("")
    print(geter.cookies)
    print("")
    print(geter.headers)
    print("")
    print(geter.json)
print("")

a = input("chcesz zapisać?(y/n) ")

if a == 'y':
    try:
        num = input("nazwa pliku: ")    
        f = open(f"{num}", "x")
        f.write(geter.text)
    except FileExistsError:
        print("no coś zjebałeś bo plik istnieje :)")
else:
    pass
#test gita
