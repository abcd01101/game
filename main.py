import streamlit as st
import time

# 상태 변수 초기화
if '잔여시간' not in st.session_state:
    st.session_state.잔여시간 = 0
if 'cnt' not in st.session_state:
    st.session_state.cnt = 0
if 'running' not in st.session_state:
    st.session_state.running = False

# 타이머 시작 함수
def start_timer():
    st.session_state.잔여시간 = 5
    st.session_state.cnt = 0
    st.session_state.running = True
    st.session_state.timer_end_time = time.time() + 5

# 클릭 함수
def click():
    if st.session_state.running:
        st.session_state.cnt += 1

# 리셋 함수
def reset():
    st.session_state.cnt = 0

# 타이머 업데이트 함수
def update_timer():
    if st.session_state.running:
        time_left = int(st.session_state.timer_end_time - time.time())
        if time_left > 0:
            st.session_state.잔여시간 = time_left
        else:
            st.session_state.running = False
            st.session_state.잔여시간 = 0

# 타이머 상태 업데이트
update_timer()

# UI 레이아웃
st.title("주어진 시간동안 최대한 많이 클릭하세요!")

# 타이머 레이블
st.write(f"Time left: {st.session_state.잔여시간} seconds")

# 클릭 횟수 레이블
st.write(f"현재 횟수: {st.session_state.cnt}")

# 버튼 클릭 시 동작
col1, col2 = st.columns(2)
with col1:
    if not st.session_state.running:
        if st.button('Start Timer'):
            start_timer()
    else:
        st.button('Button', on_click=click)

with col2:
    if st.button('Reset', on_click=reset):
        reset()

# 최종 결과 표시
if not st.session_state.running and st.session_state.잔여시간 == 0:
    st.write(f"최종 횟수: {st.session_state.cnt}")
