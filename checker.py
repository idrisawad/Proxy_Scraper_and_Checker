import requests

# List to store working proxies
working_proxies = []

# Open the file containing the proxies
with open("proxies.txt", "r") as f:
    # Iterate over each line in the file
    for proxy in f:
        proxy = proxy.strip() # remove the newline character
        try:
            # Send a request to a website using the proxy
            response = requests.get('http://example.com', proxies={'http': proxy, 'https': proxy}, timeout=3)
            # If the request is successful, add the proxy to the working list
            working_proxies.append(proxy)
        except:
            # If the request failed, the proxy is not working
            pass

# Open a file to save the working proxies
with open("working.txt", "w") as f:
    for proxy in working_proxies:
        f.write(proxy + "\n")

print("Working Proxies saved to working.txt")
