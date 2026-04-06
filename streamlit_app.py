import streamlit as st
import pandas as pd
import os

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA Investment Portal", layout="wide", page_icon="🏢")

# 2. 메인 타이틀
st.title("🏢 PMC USA & Asia PCE: Modern Housing Solution")
st.markdown("---")

# 3. 홍보 이미지 갤러리 (이름 오류 방지 로직 추가)
st.subheader("📸 Project Visualization")

# 형님이 올리신 파일명 리스트
images = [
    "pmc_layout.jpg1.jpg", "pmc_layout.jpg2.jpg", "pmc_layout.jpg3.jpg",
    "pmc_layout.jpg4.jpg", "pmc_layout.jpg5.jpg", "pmc_layout.jpg6.jpg"
]

cols = st.columns(3)
for idx, img in enumerate(images):
    with cols[idx % 3]:
        if os.path.exists(img):
            st.image(img, use_container_width=True, caption=f"PCE Technical Detail {idx+1}")
        else:
            # 파일이 진짜 없는지, 이름이 틀린 건지 확인용 문구
            st.warning(f"사진 파일 '{img}'을(를) 찾을 수 없습니다. (재부팅 필요)")

st.markdown("---")

# 4. 수익 시뮬레이터
st.subheader("💰 Investment ROI Simulator")

with st.sidebar:
    st.header("Project Parameters")
    units = st.number_input("Total Units (총 가구 수)", min_value=1, value=100)
    rent = st.number_input("Monthly Rent ($)", min_value=1, value=2500)
    # 슬라이더 기본값을 20%로 설정해서 처음부터 숫자가 나오게 했습니다!
    saving_rate = st.slider("PCE Tech Savings (%)", 0, 50, 20)

total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5

c1, c2 = st.columns(2)
with c1:
    st.metric("Estimated Cost Savings", f"${total_saving:,.0f}")
with c2:
    st.metric("Early Completion Benefit", f"${early_revenue:,.0f}")

# 5. 상세 분석
st.table(pd.DataFrame({
    "Category": ["Units", "PCE Savings", "Early Completion", "Total Value"],
    "Value": [f"{units}", f"${total_saving:,.0f}", f"${early_revenue:,.0f}", f"${(total_saving + early_revenue):,.0f}"]
}))

st.info("SAMSUNG C&T (EPC) | WITH PC (System) | PMC USA (Execution)")
