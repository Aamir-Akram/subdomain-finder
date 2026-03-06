import requests

domain = input("Enter domain: ")

with open("wordlist.txt") as f:
    subs = f.read().splitlines()

for sub in subs:
    url = f"http://{sub}.{domain}"

    try:
        r = requests.get(url, timeout=3)
        print("[FOUND]", url)
    except:
        pass