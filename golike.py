try:
    import requests,sys,os,time,json,random
    from datetime import date
    from datetime import datetime
except:
    import os,sys
    os.system('pip install requests')
    import requests,time,json,random
    from datetime import date
    from datetime import datetime
xanh= "\033[1;96m"
xlacay ="\033[1;32m"
den="\033[1;90m"
do="\033[1;31m"
luc="\033[1;92m"
vang="\033[1;93m"
xduong="\033[1;94m"
hong="\033[1;95m"
trang="\033[1;97m"
vang="\033[1;93m"
syan="\033[1;36m"
def inten():
    print(xanh+"                      _   _   ____    __  __ ")
    print(do+"                     | | | | |___ \  |  \/  |")
    print(vang+"                     | |_| |   __) | | |\/| |")
    print(hong+"                     |  _  |  / __/  | |  | |")
    print(syan+"                     |_| |_| |_____| |_|  |_|\n")
    print(xlacay+"                     ❚█══TOOL BY MINH HIEU══█❚")
    IP_addres = requests.get('http://dynupdate.no-ip.com/ip.php').text
    time.sleep(0.02)
    print(f"{do}╔════════════════════════════════════════════════════╗")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {vang}TOOL GOLIKE TIKTOK                      {do}║")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {xanh}Copyright: {trang}Lê Minh Hiếu                 {do}║")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {syan}Facebook: {trang}Lê Minh Hiếu                  {do}║")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {hong}GitHub: {trang}lmh283                          {do}║ ")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {xlacay}Profile: {do}http://lmhtool.ezzeblog.com/   {do}║")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {xlacay}IP hiện tại: {trang}{IP_addres}              {do}║")
    time.sleep(0.02)
    print(f"{do}╚════════════════════════════════════════════════════╝")
    time.sleep(0.02)
    print(f"{do}────────────────────────────────────────────────────────────")
def cc(title):
    for i in title:
        print(i,end='')
        time.sleep(0.02)
def login(author,t):
    head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": author,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
    try:
        account = requests.get("https://sv5.golike.net/api/tiktok-account",headers=head_login).json()
        if (account['status'] == 200):
            print(xlacay+"LOGIN THÀNH CÔNG                              ")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            return account
        else:
            return 1
    except:
        print(do+"GOLIKE ĐANG LỖI, VUI LÒNG QUAY LẠI SAU!!!           ")
        return 1
os.system("cls" if os.name == "nt" else "clear")
inten()
# print(xlacay+"["+do+"1"+xlacay+"]. Đăng nhập tài khoản GOLIKE lần trước   ")
# print(xlacay+"["+do+"2"+xlacay+"]. Đăng nhập tài khoản GOLIKE mới         ")
# select = int(input(xlacay+"Nhập "+do+"1"+xlacay+" hoặc "+do+"2"+xlacay+":  "+do))
# if (select == 2):
#     authorization = input(xduong+"Nhập Authorization: "+trang)
#     t = input(xduong+"Nhập T: "+trang)
#     account = login(authorization,t)
#     head_login = {
#         "Accept": "application/json, text/plain, */*",
#         "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
#         "Authorization": authorization,
#         "Content-Type": "application/json;charset=utf-8",
#         "Origin": "https://app.golike.net",
#         "Referer": "https://app.golike.net/",
#         'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
#         'Sec-Ch-Ua-Mobile':'?0',
#         'Sec-Ch-Ua-Platform':'"Windows"',
#         'Sec-Fetch-Dest':'empty',
#         'Sec-Fetch-Mode':'cors',
#         'Sec-Fetch-Site':'same-site',
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
#         "T": t
#     }
# elif (select == 1):
#     f = open("taikhoan.txt","r")
#     tam = f.readline()
#     authorization = tam.split("|")[0]
#     t = tam.split("|")[1]
#     head_login = {
#         "Accept": "application/json, text/plain, */*",
#         "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
#         "Authorization": authorization,
#         "Content-Type": "application/json;charset=utf-8",
#         "Origin": "https://app.golike.net",
#         "Referer": "https://app.golike.net/",
#         'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
#         'Sec-Ch-Ua-Mobile':'?0',
#         'Sec-Ch-Ua-Platform':'"Windows"',
#         'Sec-Fetch-Dest':'empty',
#         'Sec-Fetch-Mode':'cors',
#         'Sec-Fetch-Site':'same-site',
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
#         "T": t
#     }
#     account = login(authorization,t)
def NhapGoLike():
    while True:
        if os.path.exists('authorization.txt'):
            with open('authorization.txt', 'r') as f:
                list = json.loads(f.read())
            print(xlacay+'NHẬP '+xlacay+'['+do+'1'+xlacay+']'+luc+' SỬ DỤNG AUTHORIZATION CŨ')
            print(xlacay+'NHẬP '+xlacay+'['+do+'2'+xlacay+']'+luc+' NHẬP AUTHORIZATION MỚi')
            chon = input(xlacay+'NHẬP LỰA CHỌN: '+trang)
            if chon == '1':
                return list
            elif chon == '2':
                os.remove('authorization.txt');
            else:
                print(do+'LỰA CHỌN KHÔNG XÁC ĐỊNH.')  
                continue
        elif not os.path.exists('authorization.txt'):
            while True:
                author = input(xlacay+"NHẬP AUTHORIZATION: "+trang)
                t = input(xlacay+"NHẬP T: "+trang)
                log = login(author,t)
                if log == 1:
                    print(do+"AUTHORIZATION HOẶC T KO CHÍNH XÁC")
                    continue
                else:
                    with open('authorization.txt', 'w') as f:
                        json.dump({"authorization":author, "t":t}, f)
                    break
            try:
                with open('authorization.txt', 'r') as f:
                    list = json.loads(f.read())
                return list
                break
            except:
                os.remove('authorization.txt');
log = NhapGoLike()
authorization = log['authorization']
t = log['t']
account = login(authorization,t)
os.system("cls" if os.name == "nt" else "clear")
inten()
listid = []
listname = []
for i in range(len(account['data'])):
    id = account['data'][i]['id']
    listid.append(id)
    user_id = account['data'][i]['user_id']
    unique_username = account['data'][i]['unique_username']
    listname.append(unique_username)
    print(xlacay+"["+do+str(i)+xlacay+"]"+xduong+"   =>   "+vang+"ID: "+trang+str(id)+xduong+"   =>   "+trang+unique_username)
stt = int(input(xlacay+"Chọn tài khoản để auto: "+do))
print(xlacay+"["+do+"1"+xlacay+"]. CHỈ LÀM JOB FOLLOW")
print(xlacay+"["+do+"2"+xlacay+"]. CHỈ LÀM JOB TIM")
print(xlacay+"["+do+"3"+xlacay+"]. LÀM CẢ JOB FOLLOW VÀ TIM")
nv = int(input(syan+"Nhập lựa chọn: "+trang))
dlmin = int(input(xlacay+"Nhập delay min: "+trang))
dlmax = int(input(xlacay+"Nhập delay max: "+trang))
redo = int(input(xlacay+'Nhận lại xu bao nhiêu lần: '+trang))
tt = int(input(syan+'TIKTOK THƯỜNG NHẬP SỐ 1, TIKTOK NOW NHẬP SỐ 2: '+trang))
os.system("cls" if os.name == "nt" else "clear")
inten()
print(syan+"TOOL BY LMH")
print(syan+"TÀI KHOẢN ĐANG AUTO: "+trang+listname[stt]+" => "+syan+"ID:"+trang+str(listid[stt]))
print(f"{do}────────────────────────────────────────────────────────────")
tong = 0
total = 0
hd = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Authorization": authorization,
    "Content-Type": "application/json;charset=UTF-8",
    "referer": "https://app.golike.net/",
    "origin": "https://app.golike.net",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "T": t
}
head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": authorization,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
while True:
    time.sleep(1)
    print(syan+'ĐANG LẤY NHIỆM VỤ TIKTOK                        ',end="\r")
    # try:
    while True:
        try:
            time.sleep(1)
            getjob = requests.get("https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id="+str(listid[stt])+"&data=null",headers=head_login).json()
            link = getjob['data']['link']
            break
        except:
            if (getjob['status'] == 500):
                for i in range(30,0,-1):
                    print(do+"Bạn vui lòng chờ "+xlacay+str(i)+do+" để hệ thống tính toán lại!        ",end="\r")
                    time.sleep(1)
                continue
            else:
                continue
    success = 0
    id_job = getjob['data']['id']
    type_acction = getjob['data']['type']
    object_id = getjob['data']['object_id']
    try:
        if (nv == 1):
            if (type_acction != "follow"):
                print(do+"TOOL CHỈ LÀM NHIỆM VỤ FOLLOW, BỎ QUA JOB                                    ",end = "\r")
                dt1 = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","type": "{type_acction}","object_id": "{object_id}"}}'
                skipjob = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',data=dt1,headers=hd).json()
                if (skipjob['status'] == 200):
                    print(do+"BỎ QUA THÀNH CÔNG                                     ",end="\r")
                    time.sleep(1)
                continue
        elif (nv == 2):
            if (type_acction != "tim"):
                print(do+"TOOL CHỈ LÀM NHIỆM VỤ TIM, BỎ QUA JOB                                    ",end = "\r")
                dt1 = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","type": "{type_acction}","object_id": "{object_id}"}}'
                skipjob = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',data=dt1,headers=hd).json()
                if (skipjob['status'] == 200):
                    print(do+"BỎ QUA THÀNH CÔNG                                     ",end="\r")
                    time.sleep(1)
                continue
        elif (nv == 3):
            if (type_acction != "follow") and (type_acction != "tim"):
                print(do+"TOOL CHỈ LÀM NHIỆM VỤ FOLLOW VÀ TIM, BỎ QUA JOB                                    ",end = "\r")
                dt1 = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","type": "{type_acction}","object_id": "{object_id}"}}'
                skipjob = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',data=dt1,headers=hd).json()
                if (skipjob['status'] == 200):
                    print(do+"BỎ QUA THÀNH CÔNG                                     ",end="\r")
                    time.sleep(1)
                continue
        if (tt == 2):
            link1 = link.split("com/")[1]
            link2 = "https://now.tiktok.com/"+link1
            os.system(f"start {link2}" if os.name == "nt" else f"termux-open {link2}")
        else:
            os.system(f"start {link}" if os.name == "nt" else f"termux-open {link}")
        delay = random.randint(dlmin,dlmax)
        for i in range(10,0,-1):
            print(syan+'VUI LÒNG THỰC HIỆN '+type_acction+' TRONG '+trang+str(i)+syan+' GIÂY                                  ',end= "\r")
            time.sleep(1)
        dt = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","async": true,"data": null}}'
        print(syan+"ĐANG NHẬN TIỀN                                                         ",end = "\r")
        i = 0
        while (i<redo):
            print(f'{syan}ĐANG NHẬN TIỀN LẦN {trang}{i}                                  ', end='\r') 
            getxu = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',data=dt,headers=hd).json()
            if (getxu['status'] != 200):
                success = 0
                i = i + 1
                time.sleep(1)
                continue
            else:
                success = 1
                xu =  getxu['data']['prices']
                total = total + int(xu)
                break
        if (success == 1):
            tong = tong + 1 
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            title = vang+"["+trang+str(tong)+vang+"] ["+trang+current_time+vang+"] ["+do+type_acction+vang+"] ["+trang+str(id_job)+vang+"] ["+trang+"+"+str(xu)+vang+"]  "+syan+"=>  "+xlacay+"TOTAL "+vang+str(total)+xlacay+" VNĐ    \n" 
            cc(title)
            a = tong%10
            if (a == 0):
                print(syan+"═════════════════════════════════════════════════════════════════════")
        elif (success == 0):
            print(do+"JOB LỖI, BỎ QUA NHIỆM VỤ                                    ",end = "\r")
            dt1 = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","type": "{type_acction}","object_id": "{object_id}"}}'
            skipjob = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',data=dt1,headers=hd).json()
            if (skipjob['status'] == 200):
                print(do+"BÁO LỖI THÀNH CÔNG                                     ",end="\r")
        delay = random.randint(dlmin,dlmax)
        for i in range(delay,0,-1):
            print(syan+'VUI CHỜ '+trang+str(i)+syan+' GIÂY ĐỂ LÀM NHIỆM VỤ TIẾP THEO                       ',end= "\r")
            time.sleep(1)
    except:
        print(do+"JOB LỖI, BỎ QUA NHIỆM VỤ                                    ",end = "\r")
        dt1 = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","type": "{type_acction}","object_id": "{object_id}"}}'
        skipjob = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',data=dt1,headers=hd).json()
        if (skipjob['status'] == 200):
            print(do+"BÁO LỖI THÀNH CÔNG                                     ",end="\r")