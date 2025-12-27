import streamlit as st

# 1. إعدادات الصفحة العامة (اسم الموقع وتنسيق العرض)
st.set_page_config(page_title="TOC Website", layout="wide")

# 2. تخصيص التصميم بالألوان الهادئة (الأزرق والأخضر) كما ورد في المقترح
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. شريط التنقل الجانبي (Sidebar) للوصول للصفحات الأربعة
st.sidebar.title("منظمة TOC")
page = st.sidebar.radio("انتقل إلى الصفحات:", ["الرئيسية", "المشاريع", "التطوع", "اتصل بنا"])

# --- الصفحة الأولى: الرئيسية ---
if page == "الرئيسية":
    col1, col2 = st.columns([1, 4])
    with col1:
        st.subheader("Logo")
    with col2:
        st.title("منظمة TOC الإنسانية")
        st.info("**قصة الشعار:** يرمز شعارنا إلى التضامن والإيمان بقوة العمل الجماعي لتحقيق تغيير إيجابي.")

    st.divider()
    st.header("من نحن؟")
    st.write("نحن منظمة تسعى لتحقيق العدالة الاجتماعية وتوفير الاحتياجات الأساسية من خلال رؤية طموحة.")
    
    col_v, col_g = st.columns(2)
    with col_v:
        st.subheader("رؤيتنا")
        st.write("أن نصبح منظمة رائدة في تقديم المساعدات الإنسانية وتحقيق العدالة الاجتماعية.")
    with col_g:
        st.subheader("أهدافنا")
        st.write("- تحسين ظروف المحتاجين.\n- تعزيز التعليم والصحة.\n- تقديم مساعدات طارئة.")

    st.divider()
    # أزرار التفاعل (Call-to-Action)
    c1, c2, c3 = st.columns(3)
    c1.button("تبرع الآن / Donate Now", type="primary", use_container_width=True)
    c2.button("انضم إلينا / Join Us", use_container_width=True)
    c3.button("تعرف على مشاريعنا", use_container_width=True)

# --- الصفحة الثانية: المشاريع ---
elif page == "المشاريع":
    st.header("مشاريع المنظمة")
    tab1, tab2 = st.tabs(["المشاريع الحالية", "المشاريع السابقة"])
    
    with tab1:
        st.subheader("مشروع توزيع الغذاء")
        st.write("**الوصف:** تفاصيل حول الأهداف والجدول الزمني.")
        st.button("ساهم الآن")

    with tab2:
        st.subheader("المشاريع المكتملة")
        st.write("تقرير الأثر الذي تحقق والنتائج الملموسة.")

# --- الصفحة الثالثة: التطوع ---
elif page == "التطوع":
    st.header("انضم إلى فريق المتطوعين")
    st.write("التطوع فرصة للمساهمة في تغيير حياة الآخرين.")
    
    st.subheader("لماذا تتطوع معنا؟")
    st.write("* إحداث تأثير مباشر.\n* تطوير المهارات.\n* الحصول على شهادة تقدير.")
    
    st.info("**تطوع أونلاين:** إدارة حملات رقمية.")
    st.success("**تطوع ميداني:** توزيع المساعدات.")

# --- الصفحة الرابعة: اتصل بنا ---
elif page == "اتصل بنا":
    st.header("تواصل معنا")
    with st.form("contact_form"):
        st.text_input("الاسم")
        st.text_input("البريد الإلكتروني")
        st.text_area("الرسالة")
        st.form_submit_button("إرسال الرسالة")

    st.divider()
    st.write("📧 info@tabakh.org | 📞 123-456-789")
    st.write("📍 شارع بورتسودان، مدينة الخير")

# تذييل الصفحة
st.sidebar.markdown("---")
st.sidebar.write("BY: ENG IBRAHIM MUSA")
