#import needed modules
import datetime as dt
import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
import matplotlib.dates as mdates

#open the file as a dataframe and detect the dates
source = 'C:/Users/Mario/Downloads/Database Python.xlsx'
df=pd.read_excel(source)
df['Date'] = pd.to_datetime(df['Date'])
df['year']=df['Date'].dt.strftime("%Y")
df['month']=df['Date'].dt.strftime("%m")
df['day']=df['Date'].dt.strftime("%d")

#Plot the two stocks price series against each other to get a visual representation
df.set_index('Date',inplace=True)
fig, ax = plt.subplots()
plt.plot(df['AAPL'])
plt.plot(df['MSFT'])
plt.ylabel('Price')
plt.xlabel('Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.show()

#It looks like the prices are not that clearly correlated to a degree, even if they generally move in the same direction.
#In order to understand how strong is the correlation we can use an easy way to get a clearer visual representation of this 
#by using a Seaborn “jointplot” as follows:

sns.jointplot(df['AAPL'], df['MSFT'] ,color='b')
plt.show()

#We can see from the information provided in the jointplot that the correlation between the two stock prices start strong 
#but then becomes weaker over time. This does not set the pair up as a potentially good fit for a mean reversion strategy.
#What we need to do now is create the spread series between the two prices by running a linear regression analysis between 
#the two price series.


#run Odinary Least Squares regression to find hedge ratio and then create spread series with 2std from mean to see
#if the ratio moves around the mean

df1 = pd.DataFrame( {'y':df['AAPL'],'x':df['MSFT']} )
est = sm.OLS( df1.y,df1.x )
est = est.fit()
df1['hr'] = -est.params[0]
df1['spread'] = df1.y + ( df1.x * df1.hr )
plt.plot( df1.spread , color='b' )
df1['Mean']=df1["spread"].mean()
plt.plot( df1.Mean , 'k--' )
df1['Up']=df1['Mean']+df1["spread"].std()*2
plt.plot( df1.Up , 'k--' )
df1['Down']=df1['Mean']-df1["spread"].std()*2
plt.plot( df1.Down , 'k--' )
plt.show()

#So, it does not look mean reverting but just to be sure we could run some statistical tests on the spread series to get a better idea. 
#The test we will be using is the Augmented Dickey Fuller test.

ADF = ts.adfuller( df1.spread )
print ( 'Augmented Dickey Fuller test statistic =',ADF[0] )
print ( 'Augmented Dickey Fuller p-value =',ADF[1] )
print ( 'Augmented Dickey Fuller 1%, 5% and 10% test statistics =',ADF[4] )

#ADF outcome

#Augmented Dickey Fuller test statistic = -1.8672634997621598
#Augmented Dickey Fuller p-value = 0.3476145738802513
#Augmented Dickey Fuller 1%, 5% and 10% test statistics = {'1%': -3.43209221904862, '5%': -2.8623098163208853, '10%': -2.5671797837779753}

#Discussion
#From this we can see that the test statistic of -1.867 is smaller in absolute terms than the 10% test statistic of -2.568 
#and the 5% test statistic of -2.864, and the 1% test statistic of -3.436, meaning we can reject the null hypothesis that there is a unit root in the spread time series.
#Therefore, the spread between the two stock prices is not mean reverting, at both the 10%, 5% level of significance, and at the 1% level.
#The p-value of 0.3476 means that we can reject the null hypothesis up to the 34.76% significance level. That’s pretty bad in terms of statistical significance, 
#and from this we can be pretty certain that the spread series does not in fact possess mean reverting qualities.

#Conclusions
#From our study of the two variables over the last 15 years, we were able to demonstrate that the spread between the stock price of Apple and Microsoft does not follow 
#a mean reverting path also highlighting a strong correlation at the beginning that has become weak as time passed by. This can also be explained by the differences in 
#innovating process of the two companies. Indeed, while Apple has grown at a fastest pace introducing new technologies and devices in a faster way, Microsoft has used 
#an approach more focused on improving its existing products and services resulting in less disruptive strategy hence lagging behind Apple. This has also resulted in a growing
#investing preference towards Cupertino’s firm rather than Microsoft.
