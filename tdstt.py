try:
    import requests,time,os,sys,random,json
    from datetime import date
    from datetime import datetime
except:
    import os,sys
    os.system('pip install requests')
    import requests,time,random,json
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
    IP_addres = requests.get('http://dynupdate.no-ip.com/ip.php').text
    time.sleep(0.02)
    print(f"{do}╔════════════════════════════════════════════════════╗")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {vang}TOOL TDS TIKTOK                         {do}║")
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
def log(token):
    head = {
        "content-type":"application/json; charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","alt-svc": 'h3=":443"; ma=86400, h3-29=":443"; ma=86400','cf-cache-status': 'DYNAMIC','cf-ray': '70c2e6bc5fd63c34-HKG','content-encoding': 'br','content-type': 'application/json; charset=UTF-8','expect-ct': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"','nel': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}','report-to': '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=yHwEQlCTLU5mzOav1G%2FzMW6XAD7OIZUsyuOYLih%2Bb2EiaF3d0mYUAz4Js42OwP2BPsqr81h69xckJRKQ7bWlvrE3E%2BXhBQ8kkkrwfHrAGbub51iF9EufCvvS0uA8bHCklQ%3D%3D"}],"group":"cf-nel","max_age":604800}','server': 'cloudflare','strict-transport-security': 'max-age=0; includeSubDomains','vary': 'Accept-Encoding','x-content-type-options': 'nosniff','x-frame-options': 'SAMEORIGIN','x-powered-by': 'VPSSIM','x-xss-protection': '1; mode=block'
    }
    lg = requests.get("https://traodoisub.com/api/?fields=profile&access_token="+token,headers=head).json()
    try:
        if (lg['success'] == 200):
            print(xlacay+"LOGIN THÀNH CÔNG")
            time.sleep(1)
            return lg
    except:
        print(do+lg['error'])
        time.sleep(1)
        return 1
def logtds():    
    while True:
        if os.path.exists('token_tds_tiktok.txt'):
            with open('token_tds_tiktok.txt', 'r') as f:
                list = json.loads(f.read())
            print(xlacay+'NHẬP '+xlacay+'['+do+'1'+xlacay+']'+luc+' SỬ DỤNG TOKEN TDS '+vang+list["user"].upper())
            print(xlacay+'NHẬP '+xlacay+'['+do+'2'+xlacay+']'+luc+' NHẬP TOKEN TDS MỚi')
            chon = input(xlacay+'NHẬP LỰA CHỌN: '+trang)
            if chon == '1':

                return list
            elif chon == '2':
                os.remove('token_tds_tiktok.txt');
            else:
                print(do+'LỰA CHỌN KHÔNG XÁC ĐỊNH.')  
                continue
        elif not os.path.exists('token_tds_tiktok.txt'):
            while True:
                tk = input(xlacay+"NHẬP TOKEN TDS: "+trang)
                login = log(tk)
                if "error" in login:
                    print(do+"TOKEN TDS KO CHÍNH XÁC")
                    continue
                else:
                    user = login['data']["user"]
                    with open('token_tds_tiktok.txt', 'w') as f:
                        json.dump({"user":user, "token":tk}, f)
                    break
            try:
                with open('token_tds_tiktok.txt', 'r') as f:
                    list = json.loads(f.read())
                return list
                break
            except:
                os.remove('token_tds_tiktok.txt');
        
        
os.system("cls" if os.name == "nt" else "clear")
inten()
login1 = logtds()
token = login1['token']
login2 = log(token)
name = login1['user']
xu = login2['data']['xu']
xudie = login2['data']['xudie']
os.system("cls" if os.name == "nt" else "clear")
inten()
print(vang+"═══════════════════════════════════════════════════════════════════════")
print(syan+"TÀI KHOẢN: "+vang+name)
print(syan+"SỐ XU HIỆN TẠI: "+trang+xu)
print(syan+"SỐ XU DIE: "+do+xudie)
print(vang+"═══════════════════════════════════════════════════════════════════════")
idacc = input(xlacay+"Nhập user tiktok cần auto: "+trang)
print(xlacay+"["+do+"1"+xlacay+"]. LÀM NHIỆM VỤ TIM")
print(xlacay+"["+do+"2"+xlacay+"]. LÀM NHIỆM VỤ FOLLOW")
nv = int(input(syan+"NHẬP LỰA CHỌN: "+trang))
chnick = requests.post("https://traodoisub.com/api/?fields=tiktok_run&id="+idacc+"&access_token="+token).json()
tongxu = 0
if (chnick['success'] == 200):
    head = {
        "content-type":"application/json; charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","alt-svc": 'h3=":443"; ma=86400, h3-29=":443"; ma=86400','cf-cache-status': 'DYNAMIC','cf-ray': '70c2e6bc5fd63c34-HKG','content-encoding': 'br','content-type': 'application/json; charset=UTF-8','expect-ct': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"','nel': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}','report-to': '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=yHwEQlCTLU5mzOav1G%2FzMW6XAD7OIZUsyuOYLih%2Bb2EiaF3d0mYUAz4Js42OwP2BPsqr81h69xckJRKQ7bWlvrE3E%2BXhBQ8kkkrwfHrAGbub51iF9EufCvvS0uA8bHCklQ%3D%3D"}],"group":"cf-nel","max_age":604800}','server': 'cloudflare','strict-transport-security': 'max-age=0; includeSubDomains','vary': 'Accept-Encoding','x-content-type-options': 'nosniff','x-frame-options': 'SAMEORIGIN','x-powered-by': 'VPSSIM','x-xss-protection': '1; mode=block'
    }
    print(chnick['data']['msg'], end="\n")
    uniqueID = chnick['data']['uniqueID']
    time.sleep(1)
    dlmin = int(input(xlacay+"Nhập delay min: "+trang))
    dlmax = int(input(xlacay+"Nhập delay max: "+trang))
    quantity = int(input(xlacay+"Sau bao nhiêu nhiệm vụ thì nhận xu: "))
    time.sleep(1)
    t = 0
    loi = 0
    while True:
        if (nv == 1):
            getjob = requests.get('https://traodoisub.com/api/?fields=tiktok_like&access_token='+token,headers=head).json()
            try:
                loi = getjob['fail_count']
                if (loi == 8):
                    print(do+str(getjob['error']))
                    quit()
            except:
                if (getjob == []):
                    print(do+"TẠM THỜI HẾT JOB                        ",end="\r")
                    time.sleep(2)
                    continue
                try:
                    list = len(getjob['data'])
                except:
                    getjob = requests.get('https://traodoisub.com/api/?fields=tiktok_like&access_token='+token,headers=head).json()
                    list = len(getjob['data'])
                for i in range(list):
                    id = getjob['data'][i]['id']
                    link = getjob['data'][i]['link']
                    type = getjob['data'][i]['type']
                    os.system(f"start {link}" if os.name == "nt" else f"termux-open {link}")
                    delay = random.randint(dlmin,dlmax)
                    for i in range(delay,-1,-1):
                        print(xlacay+'VUI LÒNG CHỜ '+do+str(i)+xlacay+" GIÂY     ",end="\r")
                        time.sleep(1)
                    try:
                        duyetxu = requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id='+id+'&access_token='+token).json()
                    except:
                        time.sleep(1)
                        duyetxu = requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id='+id+'&access_token='+token).json()
                    t = t + 1
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(xlacay+"["+trang+"LMH_TOOL"+xlacay+"] "+" ["+vang+str(t)+xlacay+"] "+" ["+trang+current_time+xlacay+"] "+" ["+vang+id+xlacay+"]")
                    tong = duyetxu['cache']
                    if (t%quantity == 0):
                        try:
                            getxu = requests.post("https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token="+token).json()
                            tongxu = tongxu + int((getxu['data']['msg'].split('+')[1]).split(' Xu')[0])
                        except:
                            getxu = requests.post("https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token="+token).json()
                            tongxu = tongxu + int((getxu['data']['msg'].split('+')[1]).split(' Xu')[0])
                        print(xlacay+"═══════════════════════════════════════════════════════════════════════")
                        print(syan+"ĐANG AUTO TIKTOK: "+trang+uniqueID+xlacay+" ║ "+trang+str(getxu['data']['msg'])+xlacay+" ║ "+syan+"TOTAL: "+vang+str(tongxu)+xlacay+" ║ "+syan+"TỔNG XU: "+trang+str(getxu['data']['xu']))
                        print(xlacay+"═══════════════════════════════════════════════════════════════════════")
                        if (getxu['data']['msg'] == '+0 Xu'):
                            loi = 1
                            break
                    else:
                        continue
        elif (nv == 2):
            getjob = requests.get('https://traodoisub.com/api/?fields=tiktok_follow&access_token='+token,headers=head).json()
            try:
                loi = getjob['fail_count']
                if (loi == 8):
                    print(do+str(getjob['error']))
                    quit()
            except:
                if (getjob == []):
                    print(do+"TẠM THỜI HẾT JOB                        ",end="\r")
                    time.sleep(2)
                    continue
                try:
                    list = len(getjob['data'])
                except:
                    getjob = requests.get('https://traodoisub.com/api/?fields=tiktok_follow&access_token='+token,headers=head).json()
                    list = len(getjob['data'])
                for i in range(list):
                    id = getjob['data'][i]['id']
                    link = getjob['data'][i]['link']
                    type = getjob['data'][i]['type']
                    os.system(f"start {link}" if os.name == "nt" else f"termux-open {link}")
                    delay = random.randint(dlmin,dlmax)
                    for i in range(delay,-1,-1):
                        print(xlacay+'VUI LÒNG CHỜ '+do+str(i)+xlacay+" GIÂY     ",end="\r")
                        time.sleep(1)
                    try:
                        duyetxu = requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id='+id+'&access_token='+token).json()
                    except:
                        time.sleep(1)
                        duyetxu = requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id='+id+'&access_token='+token).json()
                    t = t + 1
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(xlacay+"["+trang+"LMH_TOOL"+xlacay+"] "+" ["+vang+str(t)+xlacay+"] "+" ["+trang+current_time+xlacay+"] "+" ["+vang+id+xlacay+"]")
                    tong = duyetxu['cache']
                    if (t%quantity == 0):
                        try:
                            getxu = requests.post("https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token="+token).json()
                            tongxu = tongxu + int((getxu['data']['msg'].split('+')[1]).split(' Xu')[0])
                        except:
                            getxu = requests.post("https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token="+token).json()
                            tongxu = tongxu + int((getxu['data']['msg'].split('+')[1]).split(' Xu')[0])
                        print(xlacay+"═══════════════════════════════════════════════════════════════════════")
                        print(syan+"ĐANG AUTO TIKTOK: "+trang+uniqueID+xlacay+" ║ "+trang+str(getxu['data']['msg'])+xlacay+" ║ "+syan+"TOTAL: "+vang+str(tongxu)+xlacay+" ║ "+syan+"TỔNG XU: "+trang+str(getxu['data']['xu']))
                        print(xlacay+"═══════════════════════════════════════════════════════════════════════")
                        if (getxu['data']['msg'] == '+0 Xu'):
                            loi = 1
                            break
                    else:
                        continue
        if (loi == 1):
            print(do+'TÀI KHOẢN TIKTOK CỦA BẠN CÒN ỔN KHÔNG!!!  ')
            print(xlacay+"["+do+"1"+xlacay+"]. Chọn lại nhiệm vụ")
            print(xlacay+"["+do+"2"+xlacay+"]. Thay acc tiktok")
            print(xlacay+"["+do+"3"+xlacay+"]. ENTER để tiếp tục")
            chon = input(f'{syan}NHẬP LỰA CHỌN: {trang}')
            if chon == '1':
                print(xlacay+"["+do+"1"+xlacay+"]. LÀM NHIỆM VỤ TIM")
                print(xlacay+"["+do+"2"+xlacay+"]. LÀM NHIỆM VỤ FOLLOW")
                nv = int(input(syan+"NHẬP LỰA CHỌN: "+trang))
                loi = 0
            elif chon == '2':
                while True:
                    idacc = input(xlacay+"Nhập ID TIKTOK cần auto: "+trang)
                    chnick = requests.post("https://traodoisub.com/api/?fields=tiktok_run&id="+idacc+"&access_token="+token).json()
                    if (chnick['success'] == 200):
                        uniqueID = chnick['data']['uniqueID']
                        break
                    else:
                        print(do+'CẤU HÌNH THẤT BẠI, VUI LÒNG NHẬP LẠI     \r')
                        time.sleep(1)
                        continue
                loi = 0
            elif chon == '3':
                loi = 0
                continue
else:
    print(do+"Cấu Hình Thất Bại         ")
    quit()