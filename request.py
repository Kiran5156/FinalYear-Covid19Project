import requests


url = "https://api.covid19india.org/v4/min/data.min.json"
url1 = "https://keralastats.coronasafe.live/summary.json"
# url2  = "https://keralastats.coronasafe.live/latest.json"
url3 ="https://keralastats.coronasafe.live/vaccination_summary.json"

result = requests.get(url=url)
result1 = requests.get(url = url1)
result3 = requests.get(url =url3)

data = result.json()
data1 = result1.json()
data3 = result3.json()


li = ["confirmed","deceased","recovered"]
li1 = ["confirmed","deceased","recovered","vaccinated1"]
kl =[]
va=[]
qs=[]

kl1=[]

districts = ["Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode"
            ,"Malappuram","Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad"]

districts_data = []

total_active = data1["summary"]["active"]
total_obs = data1["summary"]["total_obs"]

ch_active= data1["delta"]["active"]
ch_obs = data1["delta"]["total_obs"]


total_vac= data3["summary"]["tot_vaccinations"]
first_d= data3["summary"]["tot_person_vaccinations"]
second_d= data3["summary"]["second_dose"]

hos_obs= data1["summary"]["hospital_obs"]
home_obs= data1["summary"]["home_obs"]
hos_tod= data1["summary"]["hospital_today"]
totalo= data1["summary"]["total_obs"]

for i in li:
    kl.append(data1["summary"][i]) 
kl.append(total_active)
kl.append(total_obs)

for i in li:
    kl1.append(data1["delta"][i]) 
kl1.append(ch_active)
kl1.append(ch_obs)


for district in districts:
    l = []
    for i in li1:
        l.append(data["KL"]["districts"][district]["total"][i])
    districts_data.append(l)
print(districts_data)

va.append(total_vac)
va.append(first_d)
va.append(second_d)

qs.append(hos_obs)
qs.append(home_obs)
qs.append(hos_tod)
qs.append(totalo)










