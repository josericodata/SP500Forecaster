import streamlit as st
from helper import fetch_sp_tickers, fetch_stock_history, generate_stock_prediction
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="Stock Predictor", page_icon="📈")

# Sidebar
st.sidebar.header("User Input Features")
tickers = fetch_sp_tickers()

# Modify ticker display to include company names
ticker_options = [f"{symbol} - {name}" for symbol, name in tickers.items()]
selected_option = st.sidebar.selectbox("Select Stock Symbol", options=ticker_options)

# Extract the stock symbol (acronym) from the selected option
stock_symbol = selected_option.split(" - ")[0]
days_to_forecast = st.sidebar.slider("Select Prediction Range (Days)", 5, 180, 30)  # Expanded slider to 180 days
run_prediction = st.sidebar.button("Run Prediction")  # Button below the slider

# Main Section
st.header(f"Stock Data for {stock_symbol}")

try:
    # Fetch and display full historical stock data
    stock_data_full = fetch_stock_history(stock_symbol, period="max")

    # Plot Historical Data
    st.subheader("Historical Stock Prices")
    fig = go.Figure(
        data=[
            go.Scatter(
                x=stock_data_full.index,
                y=stock_data_full['Close'],
                mode='lines',
                name='Closing Price',
                line=dict(color='blue')
            )
        ]
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)

    # Check if prediction button is clicked
    if run_prediction:
        st.subheader("Stock Predictions")

        try:
            # Fetch 2 years of data for predictions
            stock_data_limited = fetch_stock_history(stock_symbol, period="2y")

            # Generate predictions using the limited data
            train, test, predictions, forecast = generate_stock_prediction(
                stock_symbol, forecast_days=days_to_forecast
            )

            # Plot Predictions
            prediction_fig = go.Figure()
            prediction_fig.add_trace(go.Scatter(x=train.index, y=train, mode='lines', name='Train', line=dict(color='blue')))
            prediction_fig.add_trace(go.Scatter(x=test.index, y=test, mode='lines', name='Test', line=dict(color='orange')))
            prediction_fig.add_trace(go.Scatter(x=test.index, y=predictions, mode='lines', name='Test Predictions', line=dict(color='green')))
            prediction_fig.add_trace(go.Scatter(x=forecast.index, y=forecast, mode='lines', name='Forecast', line=dict(color='red')))
            prediction_fig.update_layout(
                xaxis_title="Date",
                yaxis_title="Price (USD)",
                showlegend=True
            )
            st.plotly_chart(prediction_fig, use_container_width=True)

            # Display Closing Prices for Predicted Days
            st.subheader("Predicted Closing Prices")
            forecast_table = forecast.reset_index()
            forecast_table['index'] = forecast_table['index'].dt.strftime('%Y-%m-%d')  # Format the dates
            forecast_table.rename(columns={'index': 'Date', 0: 'Predicted Closing Price'}, inplace=True)
            st.write(forecast_table)

        except ValueError as ve:
            st.warning(str(ve))  # Friendly warning for insufficient data

        except Exception as e:
            st.error(f"Error generating predictions: {e}")

except ValueError as ve:
    st.warning(str(ve))  # Friendly warning for insufficient data

except Exception as e:
    st.error(f"Error fetching stock data: {e}")

