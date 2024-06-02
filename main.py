import requests
import json

print("Welcome to QuoteAPI, What Kind of quote you want to generate?")
print("[1] Random \n[2] Today")

user = int(input())

dict = {
    1: "random",
    2: "today",
}

if user >= 3 or user < 1:
    print("Please, Enter a valid option!")
    exit()

res = requests.get("https://zenquotes.io/api/{}".format(dict[user]))
response = json.loads(res.text)

quote = response[0]['q']
author = response[0]['a']

print(f'"{quote}" \n\t~{author}')