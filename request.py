import requests


url = "https://api.covid19india.org/v4/min/data.min.json"
url1 = "https://keralastats.coronasafe.live/summary.json"
# url2  = "https://keralastats.coronasafe.live/latest.json"


result = requests.get(url=url)
result1 = requests.get(url = url1)

data = result.json()
data1 = result1.json()


li = ["confirmed","deceased","recovered"]
li1 = ["confirmed","deceased","recovered","vaccinated"]
kl =[]

districts = ["Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode"
            ,"Malappuram","Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad"]

districts_data = []

total_active = data1["summary"]["active"]
total_obs = data1["summary"]["total_obs"]


for i in li:
    kl.append(data1["delta"][i]) 
kl.append(total_active)
kl.append(total_obs)


for district in districts:
    l = []
    for i in li1:
        l.append(data["KL"]["districts"][district]["total"][i])
    districts_data.append(l)









