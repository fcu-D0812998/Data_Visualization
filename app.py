import streamlit as st

# 設定頁面配置
st.set_page_config(
    page_title="德烜科技線上分析工具",
    page_icon="logoicon.ico",
    layout="wide"
)

# 主標題
st.title("🔬 德烜科技線上分析工具")

# 顯示公司標誌
try:
    st.image("logoicon.ico", width=200, caption="德烜科技標誌")
except:
    st.info("標誌圖片載入中...")

st.markdown("---")

# 簡介
st.markdown("""
目前功能：

- **表面特徵分析**：計算液滴潤濕角
- **Dimple 3D 視覺化**：3D 凹痕高度圖分析

請使用左側邊欄選擇您需要的功能。
""")
