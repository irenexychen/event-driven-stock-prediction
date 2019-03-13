# Event-Driven Stock Prediction
<sub>(_because anything without is only marginally better than predicting winning numbers_)<sub>


## //TODO
**Preparation Stage**
- ~obtain Kaggle market data~
- scrape news data
- store data with frequency, news source into database (mongodb?)
- scope possible models, write findings in Notes section

**Training Stage**
- test and retrain, rinse and repeat


**Finalizing Stage**
- simple UI to display ups and downs, overlapped with major news?
- get the bread, roll in the dough


### Data Source
Stock Market: https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs
New Source: find google scraper? 

**Data columns meaning**
- Open: starting price of the day for a particuliar stock
- Close: closing price of the day for a particuliar stock
- High: max price of the day
- Low: min price of the day
- Last: last price of the share of the day
- Volume: total trade quantity of the day, includes bought and sold shares
- Turnover/Lacs: number of times inventory has been turned over/sold and replaced in a year (high ratios implies either strong sales or insufficient inventory)

Note:
- the market is closed on weekends and public holidays
- profit/loss calculation determined by the closing price of the stock for the day


## Notes
General forecasting model process:
- split data into training, validation and testing set



### Time Series
Time dependent: hence, linear regression model's assumption about independent data points is false
Seasonal or periodic trends: trends based on particular time frame
Stationarity property: constant mean/variance over time, simplifies model for better results, a requirement for forecasting. Dickey-Fuller test to check for stationarity

Pandas has dedicated libraries for handling TS objects:
- datatime64[ns] 
- transformations to eliminate trend and seasonality, to obtain stationarity (i.e. log transform for positive trends, differencing, decomposing...)
- removing noise (aggregation, smoothing, polynomial fitting)
- weighted moving average, where more recent values are given a higher weight (exponentially weighted moving average)
- retransform back to a scaled value after prediction using ARIMA

Auto-Regressive Integrated Moving Averages (ARIMA): forecasting for a stationary time series is a linear equation, with terms p, q, and d (# of Auto-Regressive terms, # of Moving Average terms, # of differences)
- use autocorrelation function to determine AR terms,
- use partial autocorrelation function to determine MA terms
```
from statsmodels.tsa.stattools import acf, pacf
```

### Time Series Prediction Methods

**Linear Regression**
Determines the relationship between the independent variables (x=dates) and the dependent variable (y=price), based on weights (theta). Can add own features (i.e. is start of the week, is end of the week, is quarterly, is fiscal year...)

```
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)
```
Note: regression model overfits to the date and month column, instead of taking previous day's data into consideration 

**K-Nearest Neighbour (kNN)**
Find similarity between new data points and old data points based on independent variables
