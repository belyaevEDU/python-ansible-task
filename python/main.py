import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def handle_code(response: requests.Response) -> None:
    response.raise_for_status() # raises HTTPError in case of 4xx-5xx

    code = response.status_code
    body = response.content.decode()
    if body == "":
        body = "<No body>"
    logging.info(f"Status code: {code}. Body: {body}")

# Оригинальный сервис отключили из-за наплыва трафика (ссылка в README), поэтому использую зеркало
BASE_URL = "https://tools-httpstatus.pickup-services.com/random/"

# В соответствии документации httpstatus
# Исключен код 100 Continue из-за известной лимитации http.client внутри питона, из-за которого программа зависает при встрече этого кода статуса
POSSIBLE_STATUS_CODES = "101-103,200-208,226,300-308,400-426,427-428,431,440,444,449-451,460,463,494-499,500-508,510-511"

def main():
    for _ in range(5):
        r = requests.get(BASE_URL + POSSIBLE_STATUS_CODES, timeout=5, allow_redirects=False)
        try:
            handle_code(r)
        except requests.HTTPError as e:
            logger.error(f"Exception: {e}")

if __name__ == "__main__":
    main()