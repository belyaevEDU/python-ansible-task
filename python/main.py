import requests

def handleCode(response: requests.Response) -> None:
    code = response.status_code

    if 100 <= code and code < 400:
        print(f"Status code: {code}")
        print(f"Body: {response.content.decode()}\n")
    elif 400 <= code and code < 600:
        raise Exception(f"Exception raised. Status code: {code}\n")

# В соответствии документации httpstat
POSSIBLE_STATUS_CODES = "100-103,200-208,226,300-308,400-426,427-428,431,440,449-451,460,463,494-499,500-508,510-511"
# Оригинальный сервис отключили из-за наплыва трафика (ссылка в README), поэтому использую зеркало
BASE_URL = "https://tools-httpstatus.pickup-services.com/random/"

r = requests.get(BASE_URL + POSSIBLE_STATUS_CODES)
try:
    handleCode(r)
except Exception as e:
    print(e)