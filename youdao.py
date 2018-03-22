from urllib import request, parse
import time
import random
import hashlib
import json

def md5(value):
    m = hashlib.md5()
    m.update(bytes(value,encoding='utf-8'))
    return m.hexdigest()

base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

keyword = input('输入翻译：')
salt = int(time.time() * 1000) + random.randint(0,9)
sign = "fanyideskweb" + keyword + str(salt) + "aNPG!!u6sesA>hBAW1@(-"
sign = md5(sign)


data = {
    "action": "FY_BY_REALTIME",
    "client": "fanyideskweb",
    "doctype": "json",
    "from": "AUTO",
    "i": keyword,
    "keyfrom": "fanyi.web",
    "salt": salt,
    "sign": sign,
    "smartresult": "dict",
    "to": "AUTO",
    "typoResult": "false",
    "version": "2.1",
}
data = parse.urlencode(data)

headers = {
    "Host": "fanyi.youdao.com",
    "Connection": "keep-alive",
    "Content-Length": len(data),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "http://fanyi.youdao.com",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://fanyi.youdao.com/",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "OUTFOX_SEARCH_USER_ID=1013580002@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=216555653.08909458; fanyi-ad-id=39535; fanyi-ad-closed=1; JSESSIONID=aaaqzHsRj0pfddFyj8edw; UM_distinctid=160c4f0adef526-00416b6000ee1a-b7a103e-fa000-160c4f0adf0501; ___rl__test__cookies=1515132715362",
}

req = request.Request(url=base_url,data=bytes(data,'utf-8'),headers=headers)
response = request.urlopen(req)
data = response.read().decode('utf-8')
data = json.loads(data)
res = data['translateResult'][0][0]['tgt']

print(res)