import pandas as pd
from fbprophet import Prophet
import numpy as np

df = pd.read_csv('sum_by_day.csv')
df1 = df[['date','confirmed']]
df1 = df1.rename(columns={"date":"ds","confirmed":"y"})
m=Prophet(interval_width=0.95)
m.fit(df1)
future = m.make_future_dataframe(periods=7)
forecast = m.predict(future)

index = forecast.index
number_of_rows = len(index)
result = forecast[forecast.index>number_of_rows-8]
final_result=result[['ds','yhat']]
final_result.to_csv('prediction.csv')
prediction = pd.read_csv('prediction.csv')


# final_result = result[['ds','yhat']]
# print(final_result)
# prediction = .to_csv('prediction.csv')
# df2 = pd.read_csv('prediction.csv')
# df2[['ds','yhat']].to_csv('prediction1.csv') 
# result = pd.read_csv('prediction1.csv')
# result.to_html('output.html')

