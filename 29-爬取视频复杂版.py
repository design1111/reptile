
import requests

def get_iframe_src(url):
    resp = requests.get(url)
    print(resp.text)

def main(url):
    #1、拿到页面的源代码，找到iframe对应的url
    iframe_src = get_iframe_src(url)




if __name__ == '__main__':
    url = "https://www.meijuxi.com/play/31260-1-1.html"
    main(url)
