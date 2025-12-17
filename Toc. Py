import streamlit as st

# إعدادات الصفحة العامة وفقاً للمقترح
st.set_page_config(page_title="TOC Website Proposal", layout="wide")

# تخصيص الألوان (أزرق وأخضر هادئ) كما ورد في التصميم العام
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    .stTextInput>div>div>input { border-color: #add8e6; }
    </style>
    """, unsafe_allow_index=True)

# --- القائمة الجانبية للتنقل ---
st.sidebar.title("TOC Proposal")
page = st.sidebar.radio("انتقل إلى الصفحات:", ["1. الصفحة الرئيسية", "2. صفحة المشاريع", "3. صفحة التطوع", "4. اتصل بنا"])

# --- 1. الصفحة الرئيسية ---
if page == "1. الصفحة الرئيسية":
    # القسم العلوي
    col1, col2 = st.columns([1, 4])
    with col1:
        st.subheader("الشعار")
    with col2:
        st.title("منظمة TOC الإنسانية")
        st.info("**قصة الشعار:** يرمز شعارنا إلى التضامن والإيمان بقوة العمل الجماعي لتحقيق تغيير إيجابي.")

    st.divider()

    # القسم الأوسط
    st.header("من نحن؟")
    st.write("نحن منظمة تسعى لتحقيق العدالة الاجتماعية وتوفير الاحتياجات الأساسية.")
    
    col_vision, col_goals = st.columns(2)
    with col_vision:
        st.subheader("الرؤية")
        st.write("أن نصبح منظمة رائدة في تقديم المساعدات الإنسانية.")
    with col_goals:
        st
