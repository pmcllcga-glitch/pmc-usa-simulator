import streamlit as st
import pandas as pd
import os

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA Investment Portal", layout="wide")

# 2. 메인 타이틀
st.title("🏢 PMC USA & Asia PCE: Modern Housing Solution")
st.markdown("---")

# 3. 홍보 이미지 자동 갤러리 (이름이 틀려도 알아서 찾아냄!)
st.subheader("📸 Project Visualization")

# 현재 창고(폴더)에 있는 모든 파일 목록을 가져옵니다.
all_files = os.listdir('.')
# 그 중에서 pmc_layout으로 시작하는 사진 파일만 쏙 골라냅니다.
image_files = sorted([f for f in all_files if f.startswith('pmc_layout') and f.lower().endswith(('.jpg', '.jpeg', '.png'))])

if not image_files:
    st.warning("⚠️ 사진 파일을 찾지 못했습니다. 깃허브에 파일이 있는지 다시 한번 확인해주세요.")
else:
    # 사진을 3열로 예쁘게 배치
    cols = st.columns(3)
    for idx, img_name in enumerate(image_files):
        with cols[idx % 3]:
            st.image(img_name, use_container_width=True, caption=f"PCE Detail: {img_name}")

st.markdown("---")

# 4. 수익 시뮬레이터 (형님의 핵심 무기)
st.sidebar.header("📊 Project Parameters")
units = st.sidebar.number_input("Total Units", min_value=1, value=100)
rent = st.sidebar.number_input("Monthly Rent ($)", min_value=1, value=2500)
# ⚠️ 중요: 처음부터 숫자가 나오도록 기본값을 20%로 설정했습니다.
saving_rate = st.sidebar.slider("PCE Tech Savings (%)", 0, 50, 20)

# 계산 로직
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5

c1, c2 = st.columns(2)
with c1:
    st.metric("Estimated Cost Savings", f"${total_saving:,.0f}")
with c2:
    st.metric("Early Completion Benefit", f"${early_revenue:,.0f}")

# 5. 하단 정보
st.info("SAMSUNG C&T (EPC Governance) | WITH PC (System) | PMC USA (Execution)")

# --- 혹시 몰라서 만드는 비상용 파일 목록 ---
with st.expander("현장 자재(파일) 목록 확인 (문제가 생기면 클릭)"):
    st.write("현재 서버에 올라온 파일들입니다:")
    st.write(all_files)
