import requests
from concurrent.futures import ThreadPoolExecutor

def check_url(sub, domain):
    url = f"http://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            print(f"[FOUND] {url}")
    except:
        pass

domain = input("Enter domain: ")
with open("wordlist.txt") as f:
    subs = f.read().splitlines()

# This part makes it "the best"
with ThreadPoolExecutor(max_workers=20) as executor:
    for sub in subs:
        executor.submit(check_url, sub, domain)
