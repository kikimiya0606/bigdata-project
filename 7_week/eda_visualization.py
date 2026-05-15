"""
CSIC 2010 EDA (1만 vs 6만)
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from urllib.parse import unquote
import os
import re

# ============================================================
# 페이지 설정
# ============================================================
st.set_page_config(
    page_title="CSIC 2010 웹 공격 EDA",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 CSIC 2010 웹 공격 데이터 탐색적 분석")
st.markdown("**1만 vs 6만 데이터 비교 분석**")

# ============================================================
# 데이터 로드 (⭐ 수정됨)
# ============================================================
@st.cache_data
def load_data():
    base = os.path.dirname(__file__)

    df_small = pd.read_csv(os.path.join(base, "csic2010_requests.csv"))
    df_full = pd.read_csv(os.path.join(base, "csic2010_requests_org.csv"))

    return df_small, df_full

df_small, df_full = load_data()

# ============================================================
# ⭐ 데이터 선택 (핵심)
# ============================================================
data_option = st.radio(
    "데이터 선택",
    ("1만 데이터", "6만 데이터")
)

if data_option == "1만 데이터":
    df = df_small.copy()
else:
    df = df_full.copy()

# ============================================================
# 전처리
# ============================================================
df["url_decoded"] = df["url"].apply(lambda x: unquote(str(x), encoding="latin-1"))
df["body_decoded"] = df["body"].fillna("").apply(lambda x: unquote(str(x), encoding="latin-1"))
df["full_text"] = df["url_decoded"] + " " + df["body_decoded"]
df["url_length"] = df["url_decoded"].str.len()
df["body_length"] = df["body_decoded"].str.len()
df["is_attack"] = (df["label"] == "Anomalous").astype(int)

# ============================================================
# 사이드바
# ============================================================
st.sidebar.header("📊 데이터 기본 정보")
st.sidebar.write(f"선택: {data_option}")
st.sidebar.metric("전체 HTTP 요청", f"{len(df):,}건")
st.sidebar.metric("정상 (Normal)", f"{(df['label']=='Normal').sum():,}건")
st.sidebar.metric("공격 (Anomalous)", f"{(df['label']=='Anomalous').sum():,}건")
st.sidebar.metric("공격 비율", f"{df['is_attack'].mean()*100:.1f}%")

method_dist = df["method"].value_counts()
st.sidebar.markdown("---")
st.sidebar.subheader("HTTP 메서드")
for method, count in method_dist.items():
    st.sidebar.text(f"{method}: {count:,}건")

# ============================================================
# 탭
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 분포 분석",
    "📏 길이 분석",
    "🔑 공격 키워드",
    "📄 HTTP 요청 뷰어"
])

# ─── 탭 1 ─────────────────
with tab1:
    st.header("정상 vs 공격 분포")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(
            values=df["label"].value_counts().values,
            names=df["label"].value_counts().index,
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        cross = pd.crosstab(df["method"], df["label"]).reset_index()
        cross_melted = cross.melt(
            id_vars="method", var_name="label", value_name="count"
        )
        fig = px.bar(
            cross_melted,
            x="method", y="count", color="label",
            barmode="group"
        )
        st.plotly_chart(fig, use_container_width=True)

# ─── 탭 2 ─────────────────
with tab2:
    st.header("URL 길이 분석")

    fig = px.box(
        df,
        x="label", y="url_length",
        color="label"
    )
    st.plotly_chart(fig, use_container_width=True)

# ─── 탭 3 ─────────────────
with tab3:
    st.header("공격 키워드 분석")

    keywords = ["select", "script", "../", "drop"]

    results = []
    for kw in keywords:
        normal = df[df["label"] == "Normal"]["full_text"].str.contains(kw, case=False).sum()
        attack = df[df["label"] == "Anomalous"]["full_text"].str.contains(kw, case=False).sum()

        results.append({
            "키워드": kw,
            "정상": normal,
            "공격": attack
        })

    result_df = pd.DataFrame(results)
    st.dataframe(result_df)

# ─── 탭 4 ─────────────────
with tab4:
    st.header("HTTP 요청 샘플")

    normal = df[df["label"] == "Normal"].iloc[0]
    attack = df[df["label"] == "Anomalous"].iloc[0]

    st.write("정상 요청")
    st.text(normal["url"][:120])

    st.write("공격 요청")
    st.text(attack["url"][:120])