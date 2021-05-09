from flask import Flask,render_template,url_for,json
import pandas as pd
import numpy as np
app =Flask("__name__")


#Daily Cases
df = pd.read_csv('./model/prediction1.csv')
df = df.rename(columns={'ds':"Date","yhat":"Cases"})
df1 = df[["Date","Cases"]]
labels1 =[]
values1 = []
for ind in df1.index:
    labels1.append(df1["Date"][ind])
    values1.append(int(df1["Cases"][ind]))


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
    data = pd.read_csv('./model/'+filename+'.csv')
    data = data.rename(columns={'ds':"Date","yhat":"Cases"})
    data = data[["Date","Cases"]]
    label=[]
    value=[]
    for ind in data.index:
        label.append(data["Date"][ind])
        value.append(int(data["Cases"][ind]))
    return [label,value] 
    


d1 = read("prediction_d1")
d2 = read("prediction_d2")
d3 = read("prediction_d3")
d4 = read("prediction_d4")
d5 = read("prediction_d5")
d6 = read("prediction_d6")
d7 = read("prediction_d7")
d8 = read("prediction_d8")
d9 = read("prediction_d9")
d10 = read("prediction_d10")
d11 = read("prediction_d11")
d12 = read("prediction_d12")
d13 = read("prediction_d13")
d14 = read("prediction_d14")


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

# li1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]

# for x in data:
#     for i in li1:
#         labels_dict["labels_"+i] = d+i

























@app.route('/')
def index():
    return render_template("index.html",labels = labels1,values=values1,labels2=labels2,values2=values2)



@app.route('/districtwisecases')
def district():
    return render_template('districts.html',labels=labels_dict,values=values_dict)



if __name__=="__main__":
    app.run(debug=True)