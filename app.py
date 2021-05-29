from flask import Flask,render_template,url_for,json
import pandas as pd
import numpy as np
from request import *
app =Flask(__name__, template_folder='templates')


#Daily Cases
df = pd.read_csv('./model/prediction1.csv')
df = df.rename(columns={'ds':"Date","yhat":"Cases"})
df1 = df[["Date","Cases"]]
labels1 =[]
values1 = []
sum= 0
for ind in df1.index:
    labels1.append(df1["Date"][ind])
    values1.append(int(df1["Cases"][ind]))
    sum=sum + values1[ind]

diff1=int(0.08*sum)

#Cumilative Cases
df2 = pd.read_csv('./model/prediction2.csv')
df2 = df2.rename(columns={'ds':"Date","yhat":"Cases"})
df2 = df2[["Date","Cases"]]
labels2 =[]
values2 = []

for ind in df2.index:
    labels2.append(df2["Date"][ind])
    values2.append(int(df2["Cases"][ind]))


                            # DISTRICT WISE CASES
labels_dict ={"labels_d1":[], 
               "labels_d2":[],
               "labels_d3":[],
               "labels_d4":[],
               "labels_d5":[],
               "labels_d6":[],
               "labels_d7":[],
               "labels_d8":[],
               "labels_d9":[],
               "labels_d10":[],
               "labels_d11":[], 
               "labels_d12":[],
               "labels_d13":[],
               "labels_d14":[]}

values_dict = {"values_d1":[], 
               "values_d2":[],
               "values_d3":[],
               "values_d4":[],
               "values_d5":[],
               "values_d6":[],
               "values_d7":[],
               "values_d8":[],
               "values_d9":[],
               "values_d10":[],
               "values_d11":[], 
               "values_d12":[],
               "values_d13":[],
               "values_d14":[]}

# Function for reading csv
def read(filename):
    data = pd.read_csv(filename+'.csv')
    data = data.rename(columns={'ds':"Date","yhat":"Cases"})
    data = data[["Date","Cases"]]
    label=[]
    value=[]
    for ind in data.index:
        label.append(data["Date"][ind])
        value.append(int(data["Cases"][ind]))
    return [label,value] 
    


d1 = read("./model/prediction_d1")
d2 = read("./model/prediction_d2")
d3 = read("./model/prediction_d3")
d4 = read("./model/prediction_d4")
d5 = read("./model/prediction_d5")
d6 = read("./model/prediction_d6")
d7 = read("./model/prediction_d7")
d8 = read("./model/prediction_d8")
d9 = read("./model/prediction_d9")
d10 = read("./model/prediction_d10")
d11 = read("./model/prediction_d11")
d12 = read("./model/prediction_d12")
d13 = read("./model/prediction_d13")
d14 = read("./model/prediction_d14")


labels_dict["labels_d1"] = d1[0]
labels_dict["labels_d2"] = d2[0]
labels_dict["labels_d3"] = d3[0]
labels_dict["labels_d4"] = d4[0]
labels_dict["labels_d5"] = d5[0]
labels_dict["labels_d6"] = d6[0]
labels_dict["labels_d7"] = d7[0]
labels_dict["labels_d8"] = d8[0]
labels_dict["labels_d9"] = d9[0]
labels_dict["labels_d10"] = d10[0]
labels_dict["labels_d11"] = d11[0]
labels_dict["labels_d12"] = d12[0]
labels_dict["labels_d13"] = d13[0]
labels_dict["labels_d14"] = d14[0]



values_dict["values_d1"] = d1[1]
values_dict["values_d2"] = d2[1]
values_dict["values_d3"] = d3[1]
values_dict["values_d4"] = d4[1]
values_dict["values_d5"] = d5[1]
values_dict["values_d6"] = d6[1]
values_dict["values_d7"] = d7[1]
values_dict["values_d8"] = d8[1]
values_dict["values_d9"] = d9[1]
values_dict["values_d10"] = d10[1]
values_dict["values_d11"] = d11[1]
values_dict["values_d12"] = d12[1]
values_dict["values_d13"] = d13[1]
values_dict["values_d14"] = d14[1]

l1=[]
l2=[]

def sub(str):
    r=len(values_dict[str])
    diff= (values_dict[str][r-1])- (values_dict[str][r-8])
    l1.append(diff)
    hcare=int(0.08*diff)
    l2.append(hcare)


sub("values_d1")
sub("values_d2")
sub("values_d3")
sub("values_d4")
sub("values_d5")
sub("values_d6")
sub("values_d7")
sub("values_d8")
sub("values_d9")
sub("values_d10")
sub("values_d11")
sub("values_d12")
sub("values_d13")
sub("values_d14")




#Summary Graph
dfc1 = pd.read_csv('./model/dailyCon.csv')
dfc1 = dfc1.rename(columns={'Date_YMD':"Date","KL":"Cases"})
dfc2 = dfc1[["Date","Cases"]]
labelsc =[]
valuesc = []
for ind in dfc2.index:
    labelsc.append(dfc2["Date"][ind])
    valuesc.append(int(dfc2["Cases"][ind]))



dfr1 = pd.read_csv('./model/dailyRec.csv')
dfr1 = dfr1.rename(columns={'Date_YMD':"Date","KL":"Cases"})
dfr2 = dfr1[["Date","Cases"]]
labelsr =[]
valuesr = []
for ind in dfr2.index:
    labelsr.append(dfr2["Date"][ind])
    valuesr.append(int(dfr2["Cases"][ind]))

dfde1 = pd.read_csv('./model/dailyDec.csv')
dfde1 = dfde1.rename(columns={'Date_YMD':"Date","KL":"Cases"})
dfde2 = dfde1[["Date","Cases"]]
labelsde =[]
valuesde = []
for ind in dfde2.index:
    labelsde.append(dfde2["Date"][ind])
    valuesde.append(int(dfde2["Cases"][ind]))

#Testing Graph

dft1 = pd.read_csv('./model/testingD.csv')
dft1 = dft1.rename(columns={'Date':"Date","Processed in 24hr(2pm-2pm)":"Cases"})
dft2 = dft1[["Date","Cases"]]
labelst1 =[]
valuest1 = []
for ind in dft2.index:
    labelst1.append(dft2["Date"][ind])
    valuest1.append(int(dft2["Cases"][ind]))

dftc1 = pd.read_csv('./model/testingC.csv')
dftc1 = dftc1.rename(columns={'Date':"Date",'Tot. Sent':"Cases"})
dftc2 = dftc1[["Date","Cases"]]
labelstc =[]
valuestc = []
for ind in dftc2.index:
    labelstc.append(dftc2["Date"][ind])
    valuestc.append(int(dftc2["Cases"][ind]))

dftpr1 = pd.read_csv('./model/testingTPR.csv')
dftpr1 = dftpr1.rename(columns={'Date':"Date",'Test Positivity Rate (TPR)':"Cases"})
dftpr2 = dftpr1[["Date","Cases"]]
labelstp =[]
valuestp = []
for ind in dftc2.index:
    labelstp.append(dftpr2["Date"][ind])
    valuestp.append(dftpr2["Cases"][ind])

df7tpr1 = pd.read_csv('./model/testingTPR7.csv')
df7tpr1 = df7tpr1.rename(columns={'Date':"Date",'TPR last 7 day avg.':"Cases"})
df7tpr2 = df7tpr1[["Date","Cases"]]
labelstp7 =[]
valuestp7 = []
for ind in dftc2.index:
    labelstp7.append(df7tpr2["Date"][ind])
    valuestp7.append(df7tpr2["Cases"][ind])






@app.route('/')
def index():
    return render_template("index.html",labels = labels1,values=values1,sum=sum,diff1=diff1,labels2=labels2,values2=values2,labelsc=labelsc,valuesc=valuesc,
    labelsr=labelsr,valuesr=valuesr,labelsde=labelsde,valuesde=valuesde,labelst1 = labelst1,valuest1=valuest1,
    labelstc = labelstc,valuestc=valuestc,kl_data=kl,va_data=va,qs_data=qs,labelstp= labelstp,valuestp= valuestp,
    labelstp7= labelstp7, valuestp7= valuestp7,kl1_data=kl1)



@app.route('/districtwisecases')
def district():
    return render_template('districts.html',labels=labels_dict,values=values_dict,list1=l1,list2=l2,
    districts_data=districts_data,districts=districts,li = li1)



if __name__=="__main__":
    app.run(debug=True)