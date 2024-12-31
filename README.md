# 📊 **SP500Forecaster**
### **Predicting S&P 500 Stocks with ML**

**SP500Forecaster is a machine learning-powered stock price prediction app specifically designed for S&P 500 companies. Built with Python and Streamlit, it leverages historical stock data to forecast future trends and empower investors with data-driven insights.**

## 🛠️ **How It's Built**

SP500Forecaster is built with the following core frameworks and tools:

- **Streamlit** - To create an intuitive web interface
- **Yahoo Finance API (YFinance)** - To fetch up-to-date financial data
- **Statsmodels** - To implement the AutoReg time-series forecasting model
- **Plotly** - To generate dynamic and interactive financial charts
- **Pandas** - To manipulate and process financial datasets

## 🧑‍💻 **How It Works**

1. The user selects a stock ticker from the S&P 500 list.
2. Historical stock data is retrieved using the Yahoo Finance API.
3. The AutoReg (Auto Regressive) model is trained on two years of historical data.
4. The model generates forecasts for the next 5–180 days.
5. Results are displayed with interactive charts and tables.

## ✨ **Key Features**

- **Real-time S&P 500 stock data** - Access accurate and up-to-date information.
- **Interactive charts** - View historical trends and future predictions visually.
- **Custom prediction ranges** - Forecast stock prices for 5 to 180 days.
- **Downloadable CSV** - Save prediction results for further analysis.
- **User-friendly interface** - Accessible for novice and experienced users alike.

## 🚀 **Getting Started**

### **Local Installation**

1. Clone the repository:
```bash
git clone https://github.com/user/SP500Forecaster.git
```
**Hint:** Replace `user` with `josericodata` in the URL above. I am deliberately asking you to pause here so you can support my work. If you appreciate it, please consider giving the repository a star or forking it. Your support means a lot—thank you! 😊

2. Create a virtual environment:
```bash
python3 -m venv venvStreamlit
```

3. Activate the virtual environment:
```bash
source venvStreamlit/bin/activate
```

4. Install requirements:
```bash
pip install -r requirements.txt
```

5. Navigate to the app directory:
```bash
cd streamlit_app
```

6. Run the app:
```bash
streamlit run 00_ℹ️_Info.py
```

The app will be live at ```http://localhost:8501```

## 🌟 **Future Enhancements**

Planned improvements and new features include:

- **Integration of advanced ML models** (e.g., LSTM, Prophet) for better prediction accuracy.
- **Multi-stock analysis** to compare performance across different stocks.
- **Sector-based insights** to understand trends within specific industries.
- **User accounts and history tracking** for tailored predictions and personalized experiences.

## 🔧 **Environment Setup**

The SP500Forecaster app is built and tested using the following software environment:

- **Operating System**: Ubuntu 22.04.5 LTS (Jammy)
- **Python Version**: Python 3.10.12

Ensure your environment matches or exceeds these versions for optimal performance.


## 📋 **Important Notes**

- **Data Requirements**: Stocks with less than two years of historical data will not be processed by the model.
- **Using the Stock Predictor**:
  1. Select a stock ticker from the dropdown menu.
  2. Choose the desired prediction range using the slider.
  3. Click the **Run Prediction** button to generate results.
  
## ⚠️ **Disclaimer**

**This app is designed to demonstrate my skills in data modeling and analytics, showcasing how data-driven insights can assist in building my portfolio as a data analyst. It is not intended to provide financial advice or investment guidance. The predictions are for illustrative purposes only and should not be relied upon for making financial decisions.**
