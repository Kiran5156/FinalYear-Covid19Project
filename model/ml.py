import pandas as pd
from fbprophet import Prophet
import numpy as np


#State wise Daily

dfsd = pd.read_csv('state_wise_daily.csv')
dfsd1 = dfsd[['Date_YMD','Status','KL']]
dfsd2 = dfsd1[dfsd1['Status']== 'Confirmed']
dfsd3 = dfsd2[['Date_YMD','KL']]
dfsd3 = dfsd3.rename(columns={"Date_YMD":"ds","KL":"y"})

m = Prophet(#growth="linear",

	# seasonality_mode= "multiplicative", 
	# changepoint_prior_scale= 30,
	# seasonality_prior_scale= 35,
	# holidays_prior_scale= 20,
	daily_seasonality= False,
	weekly_seasonality= False,
	yearly_seasonality= False,
	).add_seasonality(
		name= 'monthly',
		period=30.5,
		fourier_order= 55
	).add_seasonality(
		name= "daily",
		period= 7,
		fourier_order= 20
	).add_seasonality(
		name= "yearly",
		period= 365.25,
		fourier_order= 20
	).add_seasonality(
		name= "quarterly",
		period= 365.25/4,
		fourier_order= 5,
		prior_scale=15)
m.fit(dfsd3)
future = m.make_future_dataframe(periods=7)

forecast1 = m.predict(future)
forecast1["yhat"] = np.where(forecast1["yhat"]<0,0,forecast1["yhat"])

index1 = forecast1.index
number_of_rows = len(index1)
result = forecast1[forecast1.index>number_of_rows-8]
final_result=result[['ds','yhat']]
final_result.to_csv('prediction1.csv')


######################
#Summary graph
dfsda = dfsd1[dfsd1['Status']== 'Confirmed']
dfsdb = dfsd1[dfsd1['Status']== 'Recovered']
dfsdc = dfsd1[dfsd1['Status']== 'Deceased']

final_result=dfsda[['Date_YMD','KL']]
final_result.to_csv('dailyCon.csv')

final_result=dfsdb[['Date_YMD','KL']]
final_result.to_csv('dailyRec.csv')

final_result=dfsdc[['Date_YMD','KL']]
final_result.to_csv('dailyDec.csv')



#########################################################################################################
#State Wise Cumulative

dfs = pd.read_csv('states.csv')
dfa= dfs[dfs['State']== 'Kerala']
dfs1 = dfa[['Date','Confirmed']]
dfs1 = dfs1.rename(columns={"Date":"ds","Confirmed":"y"})
m=Prophet(interval_width=0.95)
m.fit(dfs1)
future = m.make_future_dataframe(periods=7)
forecast2 = m.predict(future)
forecast2["yhat"] = np.where(forecast2["yhat"]<0,0,forecast2["yhat"])


result = forecast2
final_result=result[['ds','yhat']]
final_result.to_csv('prediction2.csv')



#########################################################################################################
#District wise Cumulative

df=pd.read_csv(r"districts.csv") 
df_new = df[df['State'] == 'Kerala'] 
  
df1 = df_new[df_new['District']=='Alappuzha']
df2 = df_new[df_new['District']=='Ernakulam']
df3 = df_new[df_new['District']=='Idukki']
df4 = df_new[df_new['District']=='Kannur']
df5 = df_new[df_new['District']=='Kasaragod']
df6 = df_new[df_new['District']=='Kollam']
df7 = df_new[df_new['District']=='Kottayam']
df8 = df_new[df_new['District']=='Kozhikode']
df9 = df_new[df_new['District']=='Malappuram']
df10 = df_new[df_new['District']=='Palakkad']
df11 = df_new[df_new['District']=='Pathanamthitta']
df12 = df_new[df_new['District']=='Thiruvananthapuram']
df13 = df_new[df_new['District']=='Thrissur']
df14 = df_new[df_new['District']=='Wayanad']

dfd1 = df1[['Date','Confirmed']]
dfd1 = dfd1.rename(columns={"Date":"ds","Confirmed":"y"})

dfd2 = df2[['Date','Confirmed']]
dfd2 = dfd2.rename(columns={"Date":"ds","Confirmed":"y"})

dfd3 = df3[['Date','Confirmed']]
dfd3 = dfd3.rename(columns={"Date":"ds","Confirmed":"y"})

dfd4 = df4[['Date','Confirmed']]
dfd4 = dfd4.rename(columns={"Date":"ds","Confirmed":"y"})

dfd5 = df5[['Date','Confirmed']]
dfd5 = dfd5.rename(columns={"Date":"ds","Confirmed":"y"})

dfd6 = df6[['Date','Confirmed']]
dfd6 = dfd6.rename(columns={"Date":"ds","Confirmed":"y"})

dfd7 = df7[['Date','Confirmed']]
dfd7 = dfd7.rename(columns={"Date":"ds","Confirmed":"y"})

dfd8 = df8[['Date','Confirmed']]
dfd8 = dfd8.rename(columns={"Date":"ds","Confirmed":"y"})

dfd9 = df9[['Date','Confirmed']]
dfd9 = dfd9.rename(columns={"Date":"ds","Confirmed":"y"})

dfd10 = df10[['Date','Confirmed']]
dfd10 = dfd10.rename(columns={"Date":"ds","Confirmed":"y"})

dfd11 = df11[['Date','Confirmed']]
dfd11 = dfd11.rename(columns={"Date":"ds","Confirmed":"y"})

dfd12 = df12[['Date','Confirmed']]
dfd12 = dfd12.rename(columns={"Date":"ds","Confirmed":"y"})

dfd13 = df13[['Date','Confirmed']]
dfd13 = dfd13.rename(columns={"Date":"ds","Confirmed":"y"})

dfd14 = df14[['Date','Confirmed']]
dfd14 = dfd14.rename(columns={"Date":"ds","Confirmed":"y"})



m=Prophet(interval_width=0.95)
m.fit(dfd1)
future = m.make_future_dataframe(periods=7)
forecast_d1 = m.predict(future)
forecast_d1["yhat"] = np.where(forecast_d1["yhat"]<0,0,forecast_d1["yhat"])
result = forecast_d1
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d1.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd2)
future = m.make_future_dataframe(periods=7)
forecast_d2 = m.predict(future)
forecast_d2["yhat"] = np.where(forecast_d2["yhat"]<0,0,forecast_d2["yhat"])
result = forecast_d2
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d2.csv')

m=Prophet(interval_width=0.95)
m.fit(dfd3)
future = m.make_future_dataframe(periods=7)
forecast_d3 = m.predict(future)
forecast_d3["yhat"] = np.where(forecast_d3["yhat"]<0,0,forecast_d3["yhat"])
result = forecast_d3
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d3.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd4)
future = m.make_future_dataframe(periods=7)
forecast_d4 = m.predict(future)
forecast_d4["yhat"] = np.where(forecast_d4["yhat"]<0,0,forecast_d4["yhat"])
result = forecast_d4
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d4.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd5)
future = m.make_future_dataframe(periods=7)
forecast_d5 = m.predict(future)
forecast_d5["yhat"] = np.where(forecast_d5["yhat"]<0,0,forecast_d5["yhat"])
result = forecast_d5
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d5.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd6)
future = m.make_future_dataframe(periods=7)
forecast_d6 = m.predict(future)
forecast_d6["yhat"] = np.where(forecast_d6["yhat"]<0,0,forecast_d6["yhat"])
result = forecast_d6
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d6.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd7)
future = m.make_future_dataframe(periods=7)
forecast_d7 = m.predict(future)
forecast_d7["yhat"] = np.where(forecast_d7["yhat"]<0,0,forecast_d7["yhat"])
result = forecast_d7
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d7.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd8)
future = m.make_future_dataframe(periods=7)
forecast_d8 = m.predict(future)
forecast_d8["yhat"] = np.where(forecast_d8["yhat"]<0,0,forecast_d8["yhat"])
result = forecast_d8
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d8.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd9)
future = m.make_future_dataframe(periods=7)
forecast_d9 = m.predict(future)
forecast_d9["yhat"] = np.where(forecast_d9["yhat"]<0,0,forecast_d9["yhat"])
result = forecast_d9
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d9.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd10)
future = m.make_future_dataframe(periods=7)
forecast_d10 = m.predict(future)
forecast_d10["yhat"] = np.where(forecast_d10["yhat"]<0,0,forecast_d10["yhat"])
result = forecast_d10
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d10.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd11)
future = m.make_future_dataframe(periods=7)
forecast_d11 = m.predict(future)
forecast_d11["yhat"] = np.where(forecast_d11["yhat"]<0,0,forecast_d11["yhat"])
result = forecast_d11
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d11.csv')



m=Prophet(interval_width=0.95)
m.fit(dfd12)
future = m.make_future_dataframe(periods=7)
forecast_d12 = m.predict(future)
forecast_d12["yhat"] = np.where(forecast_d12["yhat"]<0,0,forecast_d12["yhat"])
result = forecast_d12
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d12.csv')


m=Prophet(interval_width=0.95)
m.fit(dfd13)
future = m.make_future_dataframe(periods=7)
forecast_d13 = m.predict(future)
forecast_d13["yhat"] = np.where(forecast_d13["yhat"]<0,0,forecast_d13["yhat"])
result = forecast_d13
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d13.csv')



m=Prophet(interval_width=0.95)
m.fit(dfd14)
future = m.make_future_dataframe(periods=7)
forecast_d14 = m.predict(future)
forecast_d14["yhat"] = np.where(forecast_d14["yhat"]<0,0,forecast_d14["yhat"])
result = forecast_d14
final_result=result[['ds','yhat']]
final_result.to_csv('prediction_d14.csv')

###################################################################
#Testing graph
data1 = pd.read_csv('GoK Dashboard  Official Kerala COVID-19 Statistics.csv',index_col=0)
data = data1.reindex(index=data1.index[::-1])
data = data.reset_index()
data.dropna(inplace=True)

final_result=data[['Date','Processed in 24hr(2pm-2pm)']]
final_result.to_csv('testingD.csv')

final_result=data[['Date','Tot. Sent']]
final_result.to_csv('testingC.csv')









