import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    
)

logger = logging.getLogger(__name__)

class HTTPStatusCodeError(Exception): 
    pass

def make_request(code):
    url = f"https://httpstat.us/{code}"
    try:
        logger.info(f"Send request to {url}")
        response = requests.get(url, headers={"Accept": "application/json"}, timeout=5)
        received_code = response.status_code
        
        if 100 <= received_code < 400:
            logger.info(f"Status-code: {received_code} | Response body: {response.text}")
            
        elif 400 <= received_code < 600:
            raise HTTPStatusCodeError(f"Error-code: {received_code} | Response body: {response.text}")
            
    except HTTPStatusCodeError as e:
        logger.error(f"Service exception: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {e}")

def main():
    status_codes = [100, 200, 300, 404, 500]
    for code in status_codes:
        make_request(code)

if __name__ == "__main__":
    main()