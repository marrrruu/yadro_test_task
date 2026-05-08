import requests
from datetime import datetime

class HTTPStatusCodeError(Exception): 
    pass

def custom_log(level, message):
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{time_now} | {level} | {message}")

def make_request(code):
    url = f"https://httpstat.us/{code}"
    try:
        custom_log("INFO", f"Отправка запроса на {url}")
        response = requests.get(url, headers={"Accept": "application/json"}, timeout=5)
        recived_code = response.status_code
        
        if 100 <= recived_code < 400:
            custom_log("INFO", f"Статус-код: {recived_code} | Тело ответа: {response.text}")
            
        elif 400 <= recived_code < 600:
            raise HTTPStatusCodeError(f"Код ошибки: {recived_code} | Тело ответа: {response.text}")
            
    except HTTPStatusCodeError as e:
        custom_log("ERROR", f"Исключение сервера: {e}")
    except requests.exceptions.RequestException as e:
        custom_log("ERROR", f"Сетевая ошибка: {e}")

def main():
    status_codes = [100, 200, 300, 404, 500]
    for code in status_codes:
        make_request(code)

if __name__ == "__main__":
    main()
