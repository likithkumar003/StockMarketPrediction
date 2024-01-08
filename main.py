import streamlit as st
from datetime import date

import yfinance as yf
from altair.examples.pyramid import df
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME','INTC','NOK')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


#@st.cache
#def load_data(ticker):
    #data = yf.download(ticker, START, TODAY)
    #data.reset_index(inplace=True)
    #return data


#data_load_state = st.text('Loading data...')
#data = load_data(selected_stock)
#data_load_state.text('Loading data... done!')
if selected_stock=="GOOG":
    data=pd.read_csv('GOOG.csv')
    st.subheader('Raw data')
    st.write(data.tail())
elif selected_stock=="AAPL":
    data = pd.read_csv('AAPL(1).csv')
    st.subheader('Raw data')
    st.write(data.tail())
elif selected_stock=="MSFT":
    data = pd.read_csv('MSFT1.csv')
    st.subheader('Raw data')
    st.write(data.tail())
elif selected_stock=="GME":
    data = pd.read_csv('GME1.csv')
    st.subheader('Raw data')
    st.write(data.tail())
elif selected_stock=="INTC":
    data = pd.read_csv('INTC.csv')
    st.subheader('Raw data')
    st.write(data.tail())
elif selected_stock=="NOk":
    data = pd.read_csv('NOK.csv')
    st.subheader('Raw data')
    st.write(data.tail())


def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()


df_train = data[['Date', 'Close']]
df_train.fillna(0)
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)


st.subheader('Forecast data')
st.write(forecast.tail())

st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)


