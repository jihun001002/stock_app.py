import streamlit as st

st.title("미국 주식 매매 타이밍 추천")
st.write("500만 원으로 시작하는 미국 주식 매매 타이밍 분석기")

# 예제 코드 (나중에 지표 분석 추가 가능)
st.write("🚀 주가 분석 기능은 곧 추가될 예정입니다!")
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 🌟 Streamlit 앱 제목
st.title("📈 실시간 주식 분석 앱")

# 🔹 사용자 입력 (티커 심볼)
ticker = st.text_input("조회할 주식의 티커 심볼을 입력하세요 (예: AAPL, TSLA, 005930.KQ)", "AAPL")

# 🔹 데이터 불러오기
data = yf.Ticker(ticker)
hist = data.history(period="6mo")

# 🔹 주가 차트 출력
st.subheader(f"{ticker} 주가 차트")
fig, ax = plt.subplots()
ax.plot(hist.index, hist["Close"], label="종가", color="blue")
ax.set_xlabel("날짜")
ax.set_ylabel("주가 ($)")
ax.legend()
st.pyplot(fig)

# 🔹 기본 정보 출력
st.subheader(f"{ticker} 기본 정보")
st.write(data.info)

# 🔹 최근 뉴스 출력
st.subheader(f"{ticker} 관련 뉴스")
news = data.news
for n in news[:5]:  # 최근 5개 뉴스만
    st.write(f"🔹 [{n['title']}]({n['link']})")

# 🔹 배당금 정보 출력
st.subheader(f"{ticker} 배당금 정보")
st.write(data.dividends.tail(5))  # 최근 5개 배당금 기록

