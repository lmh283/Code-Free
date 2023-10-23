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
class TDS:
    name = ''
    def __init__(self, token, idacc):
        self.token = token
        self.idacc = idacc
        self.dem = 0
        self.tongxu = 0
    def CauHinh(self):
        chnick = requests.post(f"https://traodoisub.com/api/?fields=tiktok_run&id={self.idacc}&access_token={self.token}").json()
        if 'error' in chnick:
            print(f'{do}Cấu hình thất bại!!!   ',end='\r')
            exit()
        else:
            TDS.name = chnick['data']["uniqueID"]
            print(f"{xlacay}Cấu hình thành công     ")
    def DuyetNV(self,idnv):
        duyet = requests.post(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={idnv}&access_token={self.token}').json()
        return duyet['cache']
    def NhanXu(self):
        getxu = requests.post(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={self.token}').json()
        if 'data' in getxu:
                print(getxu)
                self.tongxu = self.tongxu + int((getxu['data']['msg'].split('+')[1]).split(' Xu')[0])
                print(xlacay+"═══════════════════════════════════════════════════════════════════════")
                print(syan+"ĐANG AUTO TIKTOK: "+trang+name+xlacay+" ║ "+trang+str(getxu['data']['msg'])+xlacay+" ║ "+syan+"TOTAL: "+vang+str(self.tongxu)+xlacay+" ║ "+syan+"TỔNG XU: "+trang+str(getxu['data']['xu']))
                print(xlacay+"═══════════════════════════════════════════════════════════════════════")
        else:
            print(f"{do}Lỗi nhận xu!!!    ")
            print(getxu)
    def LamJob(self):
        self.NhanXu()
        while True:
            getjob = requests.get(f'https://traodoisub.com/api/?fields=tiktok_follow&access_token={self.token}').json()
            if 'countdown' in getjob:
                countdown = getjob['countdown']
                for i in range(int(countdown)+20, 0, -1):
                    print(f'Thao tác quá nhanh vui lòng chậm lại, đợi {i} giây', end='\r')
                    time.sleep(1)
            else:
                for list in getjob['data']:
                    self.dem += 1
                    link = list['link']
                    idnv = list['id']
                    os.system(f"start {link}" if os.name == "nt" else f"termux-open {link}")
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(xlacay+"["+trang+"LMH_TOOL"+xlacay+"] "+" ["+vang+str(self.dem)+xlacay+"] "+" ["+trang+current_time+xlacay+"] "+" ["+vang+idnv+xlacay+"]")
                    dl(delay)
                    self.DuyetNV(idnv)
                    if (self.dem%10 == 0):
                        self.NhanXu()
                        
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
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {xlacay}Profile: {syan}lmhtool.ezzeblog.com   {do}║")
    time.sleep(0.02)
    print(f"{do}║  {xlacay}『{trang}H2M{xlacay}』 {syan}▶ {xlacay}IP hiện tại: {trang}{IP_addres}              {do}║")
    time.sleep(0.02)
    print(f"{do}╚════════════════════════════════════════════════════╝")
def LogTDS(token):
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
def SaveAcc():    
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
                login = (tk)
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
def dl(delay):
    for i in range(delay,0,-1):
        print(f'{syan}Vui lòng chờ {trang}{i}{syan} giây  ',end="\r")
        time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")
inten()
login1 = SaveAcc()
token = login1['token']
login2 = LogTDS(token)
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
apitds = TDS(token,idacc)
apitds.CauHinh()
delay = int(input(f'{xlacay}Nhập delay làm nhiệm vụ: {trang}'))
apitds.LamJob()