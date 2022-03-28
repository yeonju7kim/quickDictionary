import requests
import json
app_id = "78eb898b"
app_key = "6ff1512e21d50c1b61b4743364e1daf9"
language = "en-us"
word_id = "example"


def query_word(word_id):
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    mean_list = []
    json_data = json.loads(r.text)
    # ['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']
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
