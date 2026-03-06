import requests
from concurrent.futures import ThreadPoolExecutor
import sys

# Google standard: Functions use karein taaki code readable ho
def check_subdomain(subdomain, domain):
    """Ek single subdomain ko check karta hai aur status code print karta hai."""
    url = f"http://{subdomain}.{domain}"
    try:
        # Timeout 3 seconds rakha hai taaki script hang na ho
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"[FOUND] {url} (Status: 200 OK)")
        elif response.status_code == 403:
            print(f"[PROTECTED] {url} (Status: 403 Forbidden)")
    except requests.ConnectionError:
        pass
    except requests.KeyboardInterrupt:
        sys.exit()
    except Exception:
        pass

def main():
    print("--- Professional Subdomain Finder ---")
    target_domain = input("Enter domain (e.g., google.com): ").strip()
    
    try:
        with open("wordlist.txt", "r") as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        print("[ERROR] wordlist.txt nahi mili!")
        return

    print(f"[*] Scanning {target_domain} with {len(subdomains)} subdomains...")
    print("-" * 40)

    # Google-level performance: 20 threads ek saath kaam karenge
    with ThreadPoolExecutor(max_workers=20) as executor:
        for sub in subdomains:
            executor.submit(check_subdomain, sub, target_domain)

    print("-" * 40)
    print("[+] Scan Complete.")

if __name__ == "__main__":
    main()
