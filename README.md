# TSD Project

This project focuses on time series data analysis and preprocessing techniques. It explores various methods for analyzing time series data, handling non-stationarity, and predictive modeling techniques using both **statistical** and **machine learning** approaches.

---

##  What’s Inside

Following key concepts are covered here:

- **Exploratory Data Analysis (EDA)**  
  Techniques for visualizing, decomposing, and understanding temporal structures in financial time series.

  
- **Feature Engineering for Time Series**  
  Lag features, rolling statistics, seasonal indicators, and date-based encodings.
  

- **Statistical Forecasting Methods**  
 
  - ARIMA / SARIMA  
  - Facebook Prophet
  - Vector Auto Regression
  - Arch/Garch for volatility modeling
  - Single and Double Exponential Smoothing
  - Holt Winters Exponential Smoothing
  

- **Machine Learning Approaches**  

  - Random Forests
  - XGBoost
  - Long Short Term Memory


- **Model Optimization and Evaluation**  
  Grid-search-cv , Randomized-search-cv, Training with cross-validation, and performance metrics (MAE, RMSE, MAPE).


- **Additional concpets covered**
  - Grangers causality test
  - Parameter selection with AIC , BIC 

---

## Datasets

The notebooks primarily works with the following **financial datasets**:

- Stock price data.
- Commodity Prices.
- Foreign Exchnage rates.
- Inflation rates.
- Cryptocurrency price histories.
- Sales and Revenue datasets

---

## Time Series Learning Path – Notebooks Guide

The notebooks are organized into folders and  every notebook is  **independent** but best understood in  the following suggested order:

## 1. Statistical Methods (`statistical_nb`)

The `statistical_nb` folder provides the foundations of time series forecasting, starting from univariate analysis and moving toward more advanced statistical methods. These notebooks not only cover essential concepts and exploratory analysis, but also demonstrate best practices for applying forecasting models.

### Recommended Order of Study

1. **Start with univariate basics**

   * `univariate_tsa.ipynb`
   * `forecasting_inflation_rates_sarima.ipynb`

2. **Apply classical ARIMA/SARIMA**

   * `univariate_tsa_Arima_and_sarima.ipynb`

3. **Explore volatility models (GARCH)**

   * `volatility_modeling_with_Garch.ipynb`

4. **Extend to multivariate forecasting (VAR)**

   * `multivariate_forecasting_with_VAR.ipynb`

5. **Experiment with smoothing methods and Prophet**

   * `Exponential_Smoothing_with_Holt_WInters.ipynb`
   * `foracasting_with_fb_prophet.ipynb`

## 2. Machine Learning & Deep Learning (`Ml_Dl-nb`)

The `ml_dl_nb` folder introduces modern approaches to time series forecasting using machine learning and deep learning models.

1. **Begin with tree-based ML models (Random Forest, XGBoost) to understand feature-based forecasting**

   * `univariate_tsf_random_forest.ipynb`

2. **Deep learning with LSTMs to capture sequential and nonlinear temporal pattern**

   * `univariate_tsf_LSTM.ipynb`

## 3. Statistical + ML Combined (`statistical_and_ml.nb`)

This section shows how statistical and machine learning methods can be combined for multivariate forecasting, hence compare and integrate both approaches.


* `Multivariate_timeseries_VAR-and-Xgboost.ipynb`


---


## License

MIT
