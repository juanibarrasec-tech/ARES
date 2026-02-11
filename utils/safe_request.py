import requests
def get(url, t=10):
    try:
        return requests.get(url, timeout=t, headers={"User-Agent":"ARES"})
    except:
        return None
