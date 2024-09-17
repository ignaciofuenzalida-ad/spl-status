import requests
import time


def main():
    urls = [
        "https://spl-worker.onrender.com",
        "https://spl-worker-1.onrender.com",
        "https://spl-worker-2.onrender.com",
        "https://spl-worker-3.onrender.com",
        "https://spl-worker-4.onrender.com",
        "https://spl-worker-5.onrender.com",
        "https://spl-worker-6.onrender.com",
        "https://spl-worker-7.onrender.com",
        "https://spl-worker-8.onrender.com",
        "https://spl-worker-9.onrender.com",
    ]
    while True:
        for url in urls:
            response = requests.get(f"{url}/health")
            print(f"URL: {url} - Status Code: {response.status_code}")
        time.sleep(60)  # Sleep for 1 minute


if __name__ == "__main__":
    main()
