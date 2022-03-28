import requests
import json
from api_credential import *
language = "en-us"
word_id = "example"
import urllib.request


def query_word_Oxford(word_id):
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    mean_list = []
    json_data = json.loads(r.text)
    try:
        for r in json_data['results']:
            for l in r['lexicalEntries']:
                for e in l['entries']:
                    for s in e['senses']:
                        if 'definitions' in s:
                            d = s['definitions']
                            mean_list = mean_list + d
    except:
        mean_list.append("can not find")
    return mean_list

def query_word_Papago(word_id):
    encText = urllib.parse.quote(word_id)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return [json.loads(response_body)['message']['result']['translatedText']]

# query_word_Papago()