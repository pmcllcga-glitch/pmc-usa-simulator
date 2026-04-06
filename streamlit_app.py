import streamlit as st
import pandas as pd
from pathlib import Path

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA | Investment Portal", layout="wide")

# 2. 제목
st.title("🏢 PMC USA & Asia PCE: Modern Housing Solution")
st.markdown("---")

# 3. 사진 갤러리 (경로 인식 강화 버전)
st.subheader("📸 Project Visualization")

# 형님이 올리신 실제 파일명 (오타 방지)
images = [
    "pmc_layout.jpg1.jpg", "pmc_layout.jpg2.jpg", "pmc_layout.jpg3.jpg",
    "pmc_layout.jpg4.jpg", "pmc_layout.jpg5.jpg", "pmc_layout.jpg6.jpg"
]

# 사진 파일이 있는지 확인하고 띄우기
cols = st.columns(3)
current_dir = Path(__file__).parent

for idx, img_name in enumerate(images):
    img_path = current_dir / img_name
    with cols[idx % 3]:
        if img_path.exists():
            st.image(str(img_path), use_container_width=True, caption=f"PCE Detail {idx+1}")
        else:
            # 사진이 안 나올 때만 안내 문구를 띄웁니다.
            st.warning(f"'{img_name}' 찾는 중...")

st.markdown("---")

# 4. 수익 시뮬레이터 (사이드바)
st.sidebar.header("📊 Project Parameters")
units = st.sidebar.number_input("Total Units", min_value=1, value=100)
rent = st.sidebar.number_input("Monthly Rent ($)", min_value=1, value=2500)
# ⚠️ 중요: 아래 슬라이더를 0이 아닌 숫자로 움직여야 계산이 나옵니다!
saving_rate = st.sidebar.slider("PCE Tech Savings (%)", 0, 50, 20)

# 계산
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5

c1, c2 = st.columns(2)
with c1:
    st.metric("Estimated Cost Savings", f"${total_saving:,.0f}")
with c2:
    st.metric("Early Completion Benefit", f"${early_revenue:,.0f}")

# 5. 하단 정보
st.info("SAMSUNG C&T (EPC) | WITH PC (System) | PMC USA (Execution)")

# --- 디버깅용 (사진이 계속 안 나오면 여기 파일 목록을 보세요) ---
with st.expander("현장 자재(파일) 목록 확인"):
    files = [f.name for f in current_dir.glob("*")]
    st.write(files)
