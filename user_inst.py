import os, requests, random, time, threading
from user_agent import generate_user_agent as hh
from datetime import datetime

#~ ~~ ~ ~ ~ ~ ~ ~  ~
Y = '\033[1;33m'
R = '\033[1;31m'
F = '\033[2;32m'
X = '\033[1;33m'
M = '\x1b[1;37m'
B = '\033[2;36m'
#~ ~~ ~ ~ ~ ~ ~ ~  ~

os.system('cls' if os.name == 'nt' else 'clear')
token ="8610445580:AAHrJ1VHZQZ7mCTKqcFC3mcLzalT68AXEF4"
id ="7004521790"
os.system('cls' if os.name == 'nt' else 'clear')

#~ ~~ ~ ~ ~ ~ ~ ~  ~
good = 0
bad = 0
lock = threading.Lock()
url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"
#~ ~~ ~ ~ ~ ~ ~ ~  ~

#~ ~~ ~ ~ ~ ~ ~ ~  ~
def insta(username):
    global good, bad
    
    headers = {
        'User-Agent': str(hh()),
        'x-ig-www-claim': "hmac.AR0WGmLJRJqBWJqYazuS6CMjhBQRyjwVl4w1BlIlacfMPeLY",
        'x-web-session-id': "ig6ce1:tod8tb:j3ptcc",
        'sec-ch-ua-platform-version': "\"\"",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
        'sec-ch-prefers-color-scheme': "dark",
        'x-csrftoken': "zS4POkggxFgG96GKZeNyDErjKX9ewZRs",
        'sec-ch-ua-platform': "\"Linux\"",
        'x-ig-app-id': "936619743392459",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?0",
        'x-instagram-ajax': "1031870713",
        'x-asbd-id': "359341",
        'origin': "https://www.instagram.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.instagram.com/accounts/emailsignup/",
        'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        'Cookie': "datr=5-hMaRw4Pel0M7y-LABNZKrM; ig_did=902E4765-2E33-4902-81B3-57DF1ADDBFA1; mid=aUzo5wABAAG6N22X8kkBICKn1nNX; ps_l=1; ps_n=1; ig_nrcb=1; dpr=2.082077741622925; rur=\"RVA\\05480037786638\\0541799765860:01fedacb2fd25cee93d1bdbcf9bf822abba4fd995a74aec67ce5a126f3f0891380a1bac2\"; csrftoken=zS4POkggxFgG96GKZeNyDErjKX9ewZRs; wd=891x912"
    }

    payload = {
        'enc_password': "#PWD_INSTAGRAM_BROWSER:10:1768230349:AcVQAH2Z4aF1RiZ6tzOWRJNp6wIcs52sTn7HW5spGF67thUg4ST5G7mKt38im7FENuveHSZnsBHAkyAvvIBVPqAPSTnCvXWo0bvMF1kMOT8LB3g72S6qVE1Wx7ZGfj49ZZJWbl79ZGTvUocBVxkR",
        'email': "eanaan@gmail.com",
        'failed_birthday_year_count': "{}",
        'first_name': "ean",
        'username': username,
        'opt_into_one_tap': "false",
        'use_new_suggested_user_name': "true",
        'jazoest': "22824"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        EAN = response.text
        
        if 'dryrun_passed":true' in EAN:
            with lock:
                good += 1
            print(f"\r{F}       𝗧𝗿𝘂 : {good} - {X}𝗙𝗮𝗹𝘀𝗲 : {bad} - {M}𝘂𝘀𝗲𝗿 : {username}", end="")
            
            tlg = f'''
➖➖➖➖➖➖➖➖➖
- 𓏬  user insta available 

- 𓏬 𝐔𝐬𝐄𝐫 → {username}

- 𓏬 من شيلد 
➖➖➖➖➖➖➖➖➖
'''
            try:
                requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={tlg}")
            except:
                pass
        else:
            with lock:
                bad += 1
            print(f"\r{F}      True × {good} {X}False × {bad} {M}User × {username}", end="")
                
    except Exception as e:
        with lock:
            bad += 1
        print(f"\r{F}       True × {good} - {X}False × {bad} - {M}User × {username} - Error: {str(e)}", end="")

def randomusers():
    while True:
        v1 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
        v2 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
        v3 = ''.join(random.choice('1234567890') for i in range(1))
        v4 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
        v5 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
        v6 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
        v7 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
        all_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        simm = random.choice(all_chars)
        defr = random.choice(all_chars.replace(simm, ''))
        stru = simm * (6 - 1) + defr  
        hh = ''.join(random.sample(stru, 6))     
        
        user1 = v5+v6+'.'+v7+v4
        user2 = v5+'.'+v6+v7+v4
        user3 = v5+v6+'_'+v7+v4
        user4 = v5+'_'+v7+'_'+v1
        user5 = v5+'_'+v6+v7+'_'
        G = (user1, user2, user3, user4, user5)
        user = random.choice(G)
        insta(user)
        
Threads = []
for _ in range(5):
    t = threading.Thread(target=randomusers)
    t.start()
    Threads.append(t)

for thread in Threads:
    thread.join()
