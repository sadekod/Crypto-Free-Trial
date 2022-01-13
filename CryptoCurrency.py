import time
from binance.client import Client
import numpy as np
import requests
gAAAAABh4JZELrrJ0UN6xBTKucvC_i6--aDEaPvIDk7GDSyAUJhdnCEGKOlSFFUBwzu2OeeMD0kZTnAUarCKwOgIY9lzgDuCYWZa4sWYkQrOuE5QdewkgpDT-MDi0LJjNyeasvl5yHBEXaaDRTREUYeqOgrFpZfoVEYW-Dsj1imP0NISHlaPRqptFPLUPTpHaZXWQL2iD3CdMhuAXvpyUSEkw2sDPxjOGCJWoW_VLRxZc_7lh59hAhl2sNXDirR8IvGF9k8jcGJo3Ke0ZCz3hZiT8wBlOrpDEjHk4R6ct1BKGqVNRMU9reLianaIsp0ksH-Uwy8wu3gG
        url_req = "https://api.telegram.org/bot" + key + "/sendMessage" + "?chat_id=" + secret + "&text=" + text
        requests.get(url_req)
    def __init__(self, file):
        self.connect(file)
    def connect(self, file):
        lines = [line.rstrip('\n') for line in open(file)]
        key = lines[0]
        secret = lines[1]
        self.client = Client(key, secret)
if __name__ == '__main__':
    CryptoListCount = 0
    i = 0
    filename = 'BinanceData.txt'
    connection = BinanceConnection(filename)
    symbolList = []
    PumpList = []
    with open('CryptoList.txt') as file:
        lines2 = file.readlines()
        lines2 = [line1.rstrip() for line1 in lines2]
        CryptoListCount = len(lines2)
        symbolList.append(lines2)
    symbol = symbolList
    limit = 200
    gAAAAABh4JaWXTc5F3OrZpGsmDVS_bs1K6bKVAMGBXiVw861X6_9ZPvm5fQYFJn1Y__3otoKBIXvzT0odpFnhos5n7lqqQCqS4dhOrpZTTeqHmm9GqKyYT1q8Re7WY4AbMOQndt3OEh2Pe0z4184fbW_Lq3_x4pxNmLS
        url = requests.get('https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol[0][i] + '')
        data = url.json()
        GünlükFiyatDegisimi = float(data['priceChangePercent'])
        if (degisim > 0.2) or (degisim2 > 0.2):
            if GünlükFiyatDegisimi < 55:
                BinanceConnection.send_msg(
                                "PUMP: " + str(symbol[0][i]) + "\nCHANGE1: " + str(degisim) + "\nCHANGE1: " + str(
                                    degisim2) + "\nPRICE: " + str(Change3MinuteClose[-1]) + "\nPRICE CHANGE: " + str(
                                    GünlükFiyatDegisimi))
        i = i + 1
        print(i)
        if (i == CryptoListCount):
            time.sleep(2)
            i = 0
from datetime import datetime
import twint
import requests
import googletrans
from googletrans import Translator
gAAAAABh4JbbIkabo7h6jB0F24Wfsr0HSWUv_rZ3EakPsaUTFzhYDqrJZc9VaN06jgqa_r_GSD9huhoSZKsNi-a1_pNpbUSSiWE1bE4qqPTS-lhAIVFxyQQ-RnBnsVerP0TjDRuDOUpRCi3xwgpnlq1lwo59qr207T24xxfeh2GT8UgLiZxeWNjWXrq_S9rg3yWDpwxMXGFoiPUo80HDlbfhqHw4I8YR3OlZOBdNG1jryr4ZmtaqIl_IVJwagd2TskfSC-qXmzUDZ0DVdeZwhmE1i3Y4iRV3BMFEcEc__5i14VSWZKrBd53oQ-eCcGMnZZTV19Oj_uSmVLt7ZRMuKQenVv0tHdxH6nOC4VwwBqxVaVRfLzu33vfOTKznzqi_3gLBra1t0Hqq9DuYmZD3amLv54S0xKq8kKnFFYrKdGIgVlUtpsxJuwBpOKfdkXs-RhvF_y4p73tBk_9ncfTeL5ufTzEg8sAduO_vDQvbhlUXyYCsUe1YQOknjT1MY8V9tVUM38sjeKyO
    listTweet = []
    listUsers = []
    listUsersFenomen = []
    listUsersTweetsDate=[]
    KeywordValueList=['KISA','HEDEF','%']
while True:
    config = twint.Config()
    config.Search = str(symbolList[0][CryptoCount2])
    config.Store_object = True
    config.Limit = 10
    twint.run.Search(config)
    tweets_as_objects = twint.output.tweets_list
    for i in tweets_as_objects:
        if i.likes_count > 30:
            date_time_obj=str(i.datetime)
            ReplacedValue = date_time_obj.replace('Türkiye Standart Saati', '')
            gAAAAABh4JcXa8avabw-djOFRNO2VlAjzM1OiJkbrcZ9VPZnwQf_8Glq6BuczXHJjKsqZULfkcZ77Y18SFkGDs4Gv2ibRu4SLeZOOKkXbJySib0PQpRxbc4mCpyh_IbXnMQKFrVEER27fPJSydR3w_jpSdUfKkvG4nBmCmyVB7_wrn2xcskDSr1nBe5lUpL5pIaYdUMzz6vIVMwhU4IvKShSiogm5pTojedF-YXX3M13cexuKs32-FO2T_V8xTTHieG9rQXe26lvaCxbffAMTE4ZcGCEWvjQBChjnpSpbhc_CBuMHKdNtFtLz89Qz_HSMPLjjVLG483CqKVW50c18IFVpJAXiUQGgYDjjJCpPieW3i4Y8WN9oCLfTkg0V_R4s8W4wIwBjQBcwC6ZvggBMTe29CneWcfVn7hdNSDdnKWpGAuJdDUbDDqmGzRfPUBjGeQEELzeWkeIaWET2bmdU05iJSF4sX-Wsvw6qbhTlZeCE1jGZ5--7gjqaopoT1isu_267IShfoKFUH1hLbrB9JHB1ble0MDF-2aWkEeKnN4AbdhSGsvUG8G5eN0muIpdIdKFRZArqWHP359ISQuIcmcDzxXL9gYttRDi0VLBsIf-1MuRM6mo3KOyOsV5p89G9W4fofgl4giwjnYlrLU-B1y9hVkAKoi-_XFtIRFgoMQLFx9QMvjmMDDCO1xfSyuFA72nECNEgGMY
    if len(listUsersTweetsDate) > 0:
        date_time_obj = str(listUsersTweetsDate[-1])
        ReplacedValue=date_time_obj.replace('Türkiye Standart Saati','')
        ReplacedValue=ReplacedValue.replace('-','/')
        ReplacedValue=ReplacedValue.rstrip()
        date_time_obj = datetime.strptime(ReplacedValue, '%Y/%m/%d %H:%M:%S')
        MinuteValue=int(date_time_obj.hour)
        DayValue=int(date_time_obj.day)
        NowDatetime=datetime.now().hour
        NowDateDay=datetime.now().day
        if MinuteValue == NowDatetime and DayValue == NowDateDay:
            for i in range(len(listUsersTweetsDate)):
                listTweetValue=listTweet[i]
                TweetValue=str(listTweetValue).replace('#','')
                TweetValue=TweetValue.upper()
                gAAAAABh4Jd4deYM3u0XHNtqC6Oqn3SznIbFSIHx7TyMnfA-6aRjOVQFKBO_Ijy9FZw2uov7_-ltXXs3PpFq4a-pfBLeV9dyI3X80Ze8HzJAf7EW7BZtFLwKoxtQXwN_6ryP8ivlCggEWHNmqXQdUnbNtwcq-bqENzsKzRnHdxpbtbB06GUzHx5Ai6L7SqWB2zKn94nRj_jYwJKtLy7xTQ-NToBhJtf4Qc3Cq4oM3RaT5kUhcwQhqT-2v9KRtz-myH8DisCQnztzsCwW3rTs0o296hPJndorzeIimxifqSm4L_XjnjBfTV-VUQVHRIZy1eVjKSOPYbQH0Kql_Lir0P32IWXz5McJfxSjgsdpIAcN7S9WvmJk51Ecqh32Rpo3LKObUiqwim1CS01qZGkLYNFwXUv-wSupXxzeXvQAxCTT6zlGiCn3cirsbk9ytYg2k-L2B-aNeOXrlYtTuVpO04fJ8CoVWvgnvpXdUsMtZXst2NuSERPLAjD16Hloqoy7qGq9ILZTKFl8h3ysKff4V5wnfaks7x4fc-pFyfxHhtzzzDtECKH3aYBiTIKSetEyF3kIfSshqtIN6ndbg0R8S5AeGEoZ3nHwgb7Gsnc0FmPO0-8s2AdKlNw-Tst1kDnhhvHg9NcjIYK_r501pVUN8xYCyIdqtVhbhVA8HOHd3uQZH3aamMwz45M42896OuzfUQpmGtMavHu1BU6Ym8EpYi4JJBeINzMEaUUXivbHxjqPSsYCNKO86fwPAMUWSXv28l7QOUbvF-F-sGHpcbk1CjEkkhqOCjVQ6FMDzgvbdquPiQm1Rv-8bHrcd-Kl_nXUTU39EK6oozuG1VeHl9HSuaRtN3R8uUTtEZjNb9lKdSFXtO1KvWlyyrON68kiEFy1m8V-HQ8E8UgIQgFdn1uOIHt-VkebqoE-LK0SqRuMlU-eEKSV8p1aemuCOyfWFW_lcKuSQ8ZwuLXNmqyxSKyO69LSpSJS-Fpok-VIk_SXR8tjxlN-ocMNAP8uxZyz-ZriZk5ogX1GeZWKDolVzNnnEAYlfQI-uHMqC8wPcvM6L_oGd5ac3szA6EcIyIBIJnHt6IFgQFIxUQ5Ob9VehFwUQnLYnj3pMQRnqvgt-GmGnSkyEgXxO_MCHW3_TKEX48kwWrcfkz5Fl6skOZGPoEegr6OMMeKwsQsBrJKnXKYaYGbmikJ8sOfvITVevw5hPCJ9dbzas0APvN_Cki3AMUt2AEsFeRxv1eCs4eVlOi3Tt9Xk45MGDjCAjNbax63PiBHiQ4SAJlRYeVVRw2btZF-t5YyY1IaslBs_uS3IzA_hOmqZcuu3U6bM8U9sK7Ibt6tD3Ah7J4uWgQUfv1KZb5Txyb9GxaWAg1lAN0fKkRmN94AFWwrvxIpuiMnYvG1EZxq-rkNJuR7-9N7zGZoER4pfiQxkGnAIvXDXeFMxuc5lQHcUiB4ft6_qQzZLNuDFz5S6mZu3UuGxcttKimozhRMmEaSb6oQAjHT_wA
        else:
            pass
    listUsersTweetsDate.clear()
    listUsers.clear()
    listTweet.clear()
    listUsersFenomen.clear()
    tweets_as_objects.clear()
    CryptoCount = CryptoCount + 1
    CryptoCount2=CryptoCount2+1
    if (CryptoCount2 == CryptoListCount):
        CryptoCount2 = 0
gAAAAABh4Je10SB1W6-jtN__atR0oFyqLnfFOwuoO5J4V2m8nz5TuTZH0XuSVOAiyPac7oMp6eLWKWUx5o-ZN_DNbUs3fPSY4z00pp8l3BgVmRI5Xb20JJKsDlCUihGIbuSDt6ab7IiH41IlXjuMvkj3kemDvGjHthTkkryVjxNBr1eP1jPBxAcQGMw1dunJPzfb9529pIGdfDQRQpXFZP4vcQYYTMN7XRh8CNf7s30zQN4zo9UEK6A7cynE1zU2JfUrP90Y55WqYvUFP8mVv6WOGMtFroFJI7cgCe36YU4yUrZKIdGvlDsfRz5aloJJDpe5UkRM9iIHrCbvANbZE5hXFGzyAPlOLX6gbBGQTAsSlthVXN_qzgmEFP8ZfIBTUdERl9J61u3hyPzQd4HQMdtdrURstdFTmN4GuC3lpEkS_cA_M0rK8Y-6d6YMULlRH7445WlCRe8Y8VAqdHpqp_9KOfXmqhgEcdaiPBveMTBbWYXZiocnT8JCCYjKtgsJzOExl4_Sh1FVdMNNmn4GQwOAUMZI3DewmRYe5e8qt77XJqsipdwgRXz_R-zWkpoUoPE4yr-vewOZrlQNmUD0lW2InYIK5ORqCcGfwqsZMA3Ee36bWubUAug2FlkMBJ11QPv1tsskh88G4XImIKxN5_ZI031K_oqwn4S_sETUJcu6nDUNE5KumE_B6KvZMezsKehX9WRne2KqXhAoTl2-lo35XPqdQ40isXz4FgfLd6nXDIrlxR7zBHczZCRq0kBP2IU1tfbb1o5Bg0pmmE9ANfYqsIzeQfGf6K3K6K2FYKvshDgALc1Qi6BHbdUkxSu7I2jTY3TRy6k83r3eaNJbskXkXQm_bODhzXXrx3yPDfDbYm4iu5bfjoORSlFXec0gkZbqUnvSnXUgvA8qU6dpZ3muB8qZs79qmC-6Mj1EiH9N3pdkeLzeqet33mMpVxatWmktxdXbBYy5WuWhGYsHKlK_yIBXIy0oQij-0A28Dkt065pLPKIQ2YT08lBsV3SiKy9Q6Pb6F1lx5i-rZcmJy27koTHOjjKCVw==
create_symbols_list('USDT')