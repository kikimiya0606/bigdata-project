(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> pwd

Path
----
C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project...


(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> ls


    디렉터리: C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigd
    ata-project-a-kiki


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2026-03-20  오전 10:03                kiki
d-----      2026-03-20  오전 10:03                venv
-a----      2026-03-20  오전 11:45             54 .env
-a----      2026-03-20  오전 10:21            157 .gitignore    
-a----      2026-03-13  오전 10:34           1854 requirements.t
                                                  xt


(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> cd kiki
(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki\kiki> cd ..
(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> mkdir kiki1


    디렉터리: C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigd 
    ata-project-a-kiki


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2026-03-20  오후 12:21                kiki1


(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> cat kiki/app.py
import streamlit as st
import pandas as pd
# ?섏씠吏 ?ㅼ젙
st.set_page_config(page_title="鍮낅뜲?댄꽣 遺꾩꽍 ?꾨줈?앺듃", page_icon="?뱤")
# ?쒕ぉ
st.title("鍮낅뜲?댄꽣 遺꾩꽍 ?꾨줈?앺듃")
st.write("泥?踰덉㎏ Streamlit ?깆엯?덈떎!")
# 援щ텇??
st.divider()
# 媛꾨떒???곗씠?고봽?덉엫 ?쒖떆
st.subheader("?섑뵆 ?곗씠??)
data = {
 "?대쫫": ["源泥좎닔", "?댁쁺??, "諛뺣???, "?뺤닔吏?, "理쒖???], 
 "?숇뀈": [3, 3, 3, 3, 3],
 "?꾧났": ["AI?뚰봽?몄썾??, "AI?뚰봽?몄썾??, "AI?뚰봽?몄썾??, "AI?뚰봽?몄썾??, "AI?뚰봽?몄썾??],
 "Python?먯닔": [85, 92, 78, 95, 88]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
# 媛꾨떒??李⑦듃
st.subheader("Python ?먯닔 李⑦듃")
st.bar_chart(df.set_index("?대쫫")["Python?먯닔"])
# ?ъ씠?쒕컮
st.sidebar.header("?ㅼ젙")
st.sidebar.write("???곸뿭? ?ъ씠?쒕컮?낅땲??")
name = st.sidebar.text_input("?대쫫???낅젰?섏꽭??)
if name:
 st.sidebar.write(f"?덈뀞?섏꽭?? {name}??")
(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> cp kiki/app.py
(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> rm app.py
(venv) PS C:\Users\6-112\Desktop\빅데이터분석프로그래밍\bigdata-project-a-kiki> rm -Recurse kiki1
