from requests import HTTPError
import requests as req
import random as ran
import json,asyncio,re

with open('/home/reep_c/code/python/dc_bot_rumi/json/setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class func:
    
    def catch_pic(self,keyword=None,random=False) ->str:
        session=req.session()
        proxies={
        'http':'http://127.0.0.1:51837',
        'https':'https://127.0.0.1:51837'
        }         

        headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "refer": "https://www.pixiv.com/",
        'PHPSESSID':jdata['PHPSESSID'],
        }
        
        global false,null,true
        false='False'
        null='None'
        true='True'
        rn=lambda:ran.randint(1000000,200000000) 
        try:
            final=rn() if random else keyword
            if not random:
                url=f'https://www.pixiv.net/ajax/search/artworks/{keyword}?'
                response_1=session.get(url,headers=headers)
                response_1=eval(response_1.content)['body']['illustManga']['data']
                datas=response_1
                pic_id=[]
                
                for data in datas:
                    if 'id' in data:
                        pic_id.append(data['id'])
            
                final=ran.choice(pic_id)
                pic_id.clear()
            pic_url=f'https://www.pixiv.net/artworks/{final}'
            response=req.get(pic_url)
            while response.status_code!=200:
                final=rn()
                pic_url=f'https://www.pixiv.net/artworks/{final}'
                response=req.get(pic_url)
                
            embed_url=f'https://pixiv.cat/{final}.jpg'
            return pic_url,embed_url
        except HTTPError as error:
            raise error
        

if __name__=='__main__':
    def random_test():
        print(func().catch_pic(random=True))
    
    def keyword_test():
        print(func().catch_pic(keyword=str(input('enter your keyword:'))))
    
    choose=int(input('0 or 1:'))
    if choose:
        keyword_test()
    else:
        random_test(random=True)
