import requests
import json
import matplotlib.pyplot as plt
tsquares = []
rsquares = []
tx = []
rx = []
url="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-069?Authorization=" + "ENTER YOUR API KEY HERE" + "&elementName=T,PoP6h"
htmlfile = requests.get(url)
#print(htmlfile.text)
data = json.loads(htmlfile.text)
locationSelect = int(input("新北市選擇地區\n0:瑞芳區 1:三重區 2:平溪區 3:淡水區 4:石門區 5:泰山區 6:新店區 7:萬里區 8:蘆洲區 9:永和區 \
    \n10:貢寮區 11:深坑區 12:鶯歌區 13:坪林區 14:板橋區 15:八里區 16:土城區 17:三芝區 18:汐止區 19:新莊區 \
    \n20:金山區 21:林口區 22:中和區 23:雙溪區 24:五股區 25:三峽區 26:樹林區 27:烏來區 28:石碇區\n"))
print(data["records"]["locations"][0]["location"][locationSelect]["locationName"],end = " ")
print(data["records"]["locations"][0]["location"][0]["weatherElement"][0]["description"]) # 溫度
print(data["records"]["locations"][0]["location"][0]["weatherElement"][1]["description"]) # 6小時降雨機率
for n in range(24):
    dataTime = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][0]["time"][n]["dataTime"][8:13]
    value = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][0]["time"][n]["elementValue"][0]["value"]
    print(f"{dataTime}H  {value}度")
    tsquares.append(int(value))
    tx.append(dataTime[:2]+"_"+dataTime[3:5]+"H")
for n in range(11):
    startTime = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][1]["time"][n]["startTime"][8:13]
    endTime = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][1]["time"][n]["endTime"][8:13]
    valuerain = data["records"]["locations"][0]["location"][locationSelect]["weatherElement"][1]["time"][n]["elementValue"][0]["value"]
    print(f"{startTime}H ~ {endTime}H  {valuerain}")
    rsquares.append(int(valuerain))
    rx.append(startTime[:2]+"_"+startTime[3:5]+"H")
plt.subplot(2,1,1)
plt.plot(tx,tsquares, "m-")
#plt.title("Temperture", fontsize=24)
#plt.xlabel("Data Time (Day_Hour)", fontsize=14)
plt.ylabel("Temperture", fontsize=14)
plt.tick_params(axis="x", labelsize=5)
plt.subplot(2,1,2)
plt.plot(rx,rsquares, "b-")
plt.axis([0,10,0,100])
#plt.title("Rain", fontsize=24)
plt.xlabel("Data Time (Day_Hour)", fontsize=14)
plt.ylabel("Probability of Precipitation(%)", fontsize=14)
plt.tick_params(axis="x", labelsize=5)
plt.show()
