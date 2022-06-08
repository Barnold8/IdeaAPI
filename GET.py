# File for testing the return values of the web server

import requests


REQUEST = input("Write get request:\t")

x = requests.get("http://127.0.0.1:8000/"+REQUEST)


def printHTML(HTML):

    text = ""

    for chars in HTML:
        if chars == "<":
            text += "\n<"
        elif chars == ">":
            text += ">\n"
        else:
            text += chars
    print(text)


print("="*60)
print("Status code: {}".format(x.status_code))
print("Headers: {}".format(x.headers))

f = REQUEST.split("/")
if f[0].lower() == "json":
    print(x.json())
else:
    printHTML(x.text)

print("="*60)

