# Proxy_Scraper_and_Checker #

### Proxy_Scraper: ###

This script uses the requests library to make a request to the website https://www.socks-proxy.net/, which contains a list of SOCKS5 proxy addresses#

It then uses the BeautifulSoup library to parse the HTML content of the website and find the table containing the proxy addresses. The script iterates over each row in the table, extracts the IP address and port, and appends them to the proxies list in the format 'socks5://IP:port'.

Please note that using web scraping to gather the IPs might not be allowed by the website, and also the IPs might be outdated or blocked by the website, so it's important to check the website's terms of use before scraping.

The script opens a file named "proxies.txt" in write mode and writes each proxy to a new line in the file. It uses the with open statement to handle the file operations, so it will automatically close the file when done, even if an exception is raised.

Additionally, it's important to check the website's terms of use before scraping, and to use the scraped data responsibly.

### Proxy_Checker: ###

This script opens the file "/proxies.txt" in read mode, and for each line in the file, it sends a request to the website "http://example.com" using the proxy specified in the line. If the request is successful, the proxy is considered working and added to the list working_proxies. If the request fails, the proxy is not working and is not added to the list. Finally the script prints the working proxies.

It's important to mention that this script uses HTTP GET request to check the proxy, this might not be the optimal way to check if a proxy is working or not. Also, the website "http://example.com" is only used as an example, you can use any website that you want to check the proxies against.

Also please keep in mind that sending a lot of requests to a website might be consider a scraping and it is important to check the website's terms of use before using it.
