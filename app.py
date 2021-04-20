from flask import Flask,render_template,url_for,json
import pandas as pd
import numpy as np
app =Flask("__name__")

df = pd.read_csv('./model/prediction.csv')
df = df.rename(columns={'ds':"Date","yhat":"Cases"})
df1 = df[["Date","Cases"]]
labels =[]
values = []
for ind in df1.index:
    labels.append(df1["Date"][ind])
    values.append(int(df1["Cases"][ind]))




@app.route('/')
def index():
    return render_template("index.html",labels = labels,values=values)
if __name__=="__main__":
    app.run(debug=True)
