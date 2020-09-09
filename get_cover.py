import requests,json

def get_api(id,type):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
    if type == 'av':
        link = f'https://api.bilibili.com/x/web-interface/view?aid={id}'
    else:
        link = f'https://api.bilibili.com/x/web-interface/view?bvid={id}'
    getter = requests.get(link,headers=headers)
    get_json = json.loads(getter.content)
    return get_json

def json_rush(js):
    bvid = js['data']['bvid']
    avid = f"av{js['data']['bvid']}"
    cover_link = js['data']['pic']
    return {'bvid':bvid,'avid':avid,'cover_link':cover_link}

def get_type(ab_id):
    if ab_id[:2] =='AV' or ab_id[:2] =='av' or ab_id[:2] =='Av':
        return 'av'
    if ab_id[:2] =='BV' or ab_id[:2] =='bv' or ab_id[:2] =='Bv':
        return 'bv'

def fast_run(ab_id):
    json = json_rush(get_api(ab_id[2:],get_type(ab_id)))
    if 'cover_link' in json:
        return json['cover_link']

def run(ab_id):
    return json_rush(get_api(ab_id[2:],get_type(ab_id)))