import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
from sklearn.metrics import mean_squared_error

# Load the data
tdf = pd.read_csv("data/processed_electric_production.csv", parse_dates=["DATE"], index_col="DATE")

# Split the data into training and testing sets
train_data = tdf[:-6]
test_data = tdf[-6:]

# ARIMA Model
# Fit ARIMA model to the training data
arima_model = ARIMA(train_data["diff"].dropna(), order=(1, 0, 1))
res_arima = arima_model.fit()
print("ARIMA Model Summary:")
print(res_arima.summary())

# Forecast using ARIMA
arima_forecast = res_arima.forecast(steps=6)

# GARCH Model
# Fit GARCH model to the training data
garch_model = arch_model(train_data["diff"].dropna(), vol='Garch', p=1, q=1)
res_garch = garch_model.fit(disp='off')
print("\nGARCH Model Summary:")
print(res_garch.summary())

# Forecast using GARCH (volatility forecasting)
garch_forecast_variance = res_garch.forecast(horizon=6).variance.dropna()

# Evaluate ARIMA model
rmse_arima = np.sqrt(mean_squared_error(test_data["diff"].dropna(), arima_forecast))
print(f'\nARIMA Model RMSE: {rmse_arima}')

# Evaluate GARCH model (indirectly by comparing predicted volatility)
# Note: GARCH forecasts variance, not the actual time series values
# You might want to compare the predicted variance with the squared residuals of the test data
# This requires more sophisticated evaluation techniques depending on your goals
print("\nGARCH model evaluation is based on variance prediction, requires advanced evaluation techniques.")
