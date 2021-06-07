import requests
import json
continueFind = "Y"
while continueFind == "Y":
    url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-069?Authorization=' + 'ENTER YOUR API KEY HERE' + '&format=JSON&elementName=WeatherDescription'
    htmlfile = requests.get(url)
    data = json.loads(htmlfile.text)
    locationSelect = int(input("新北市選擇地區\n0:瑞芳區 1:三重區 2:平溪區 3:淡水區 4:石門區 5:泰山區 6:新店區 7:萬里區 8:蘆洲區 9:永和區 \
    \n10:貢寮區 11:深坑區 12:鶯歌區 13:坪林區 14:板橋區 15:八里區 16:土城區 17:三芝區 18:汐止區 19:新莊區 \
    \n20:金山區 21:林口區 22:中和區 23:雙溪區 24:五股區 25:三峽區 26:樹林區 27:烏來區 28:石碇區\n"))
    #for locationSelect in range(29):
    print(data["records"]["locations"][0]["location"][locationSelect]["locationName"],end = " ")
    print(data["records"]["locations"][0]["location"][0]["weatherElement"][0]["description"])
    for n in range(24):
        startTime = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][0]["time"][n]["startTime"][5:13]
        endTime = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][0]["time"][n]["endTime"][5:13]
        value = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][0]["time"][n]["elementValue"][0]["value"]
        print(f"{startTime}H ~ {endTime}H  {value}")
    continueFind = input("要繼續查詢請輸入 Y :")
