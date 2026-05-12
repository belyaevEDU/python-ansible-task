import requests

def handleCode(response: requests.Response) -> None:
    code = response.status_code

    if 100 <= code and code < 400:
        print(f"Status code: {code}")
        body = response.content.decode()
        if body == "":
            body = "<No body>"
        print(f"Body: {body}\n")
    elif 400 <= code and code < 600:
        raise Exception(f"Exception raised. Status code: {code}\n")

# В соответствии документации httpstat
POSSIBLE_STATUS_CODES = "100-103,200-208,226,300-308,400-426,427-428,431,440,444,449-451,460,463,494-499,500-508,510-511" # Work out a way to handle 207
# Оригинальный сервис отключили из-за наплыва трафика (ссылка в README), поэтому использую зеркало
BASE_URL = "https://tools-httpstatus.pickup-services.com/random/"

for _ in range(5):
    r = requests.get(BASE_URL + POSSIBLE_STATUS_CODES)
    try:
        handleCode(r)
    except Exception as e:
        print(e)