
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

def hybrid_forecast(df, column="close", periods=1):
    arima_model = ARIMA(df[column], order=(5,1,0))
    arima_fit = arima_model.fit()
    arima_forecast = arima_fit.forecast(periods)

    prophet_df = df.rename(columns={column: "y", "ds": "ds"})
    prophet_model = Prophet(daily_seasonality=True)
    prophet_model.fit(prophet_df)
    future = prophet_model.make_future_dataframe(periods=periods)
    prophet_forecast = prophet_model.predict(future)["yhat"].iloc[-periods:]

    combined_forecast = 0.6 * arima_forecast.values + 0.4 * prophet_forecast.values
    return combined_forecast
