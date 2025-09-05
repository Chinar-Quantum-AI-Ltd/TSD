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

The notebooks primarily work with the following **financial datasets**:

- Stock price data.
- Commodity Prices.
- Foreign Exchnage rates.
- Inflation rates.
- Cryptocurrency price histories.
- Sales and Revenue datasets

## Repository structure

TSD/
│
├── Notebooks/                       # All Jupyter notebooks
│   ├── statistical_nb/              # Notebooks for forecasting with statistical methods
│   │   └── ... (notebooks here)
│   │
│   ├── Ml,Dl_nb/                    # Notebooks for forecasting with Machine Learning & Deep Learning methods
│   │   └── ... (notebooks here)
│   │
│   ├── statistical_and_ml_nb/       # Notebooks combining statistical & ML approaches
│   │   └── ... (notebooks here)
│   │
│   └── others/                      # Contains Other experiments
│       └── ... (notebooks here)
│
├── data/                            # General datasets
│   └── ... (csv, parquet, etc.)
│
├── financial_data/                  # Finance-related datasets
│   └── ... (stock, forex, etc.)
│
└── README.md                        # This guide

## License

MIT
