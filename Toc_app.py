import streamlit as st

# إعدادات الصفحة العامة بناءً على المقترح الفني
st.set_page_config(page_title="TOC Website Proposal", layout="wide")

# تخصيص التصميم بالألوان الهادئة (الأزرق/الأخضر) كما ورد في التصميم العام للمقترح
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية للتنقل (Sidebar)
st.sidebar.title("TOC Website")
page = st.sidebar.radio("انتقل إلى:", ["الرئيسية", "المشاريع", "التطوع", "اتصل بنا"])

# --- 1. الصفحة الرئيسية ---
if page == "الرئيسية":
    col1, col2 = st.columns([1, 4])
    with col1:
        st.subheader("Logo") 
    with col2:
        st.title("منظمة TOC الإنسانية")
        st.info("**قصة الشعار:** يرمز شعارنا إلى التضامن والإيمان بقوة العمل الجماعي لتحقيق تغيير إيجابي.")

    st.divider()
    st.header("من نحن؟")
    st.write("نحن منظمة تسعى لتحقيق العدالة الاجتماعية وتوفير الاحتياجات الأساسية.")
    
    col_v, col_g = st.columns(2)
    with col_v:
        st.subheader("الرؤية")
        st.write("أن نصبح منظمة رائدة في تقديم المساعدات الإنسانية وتحقيق العدالة الاجتماعية.")
    with col_g:
        st.subheader("أهدافنا")
        st.write("- تحسين ظروف المحتاجين.\n- تعزيز التعليم والصحة.\n- تقديم مساعدات طارئة.")

    st.subheader("ماذا نفعل؟")
    st.write("توزيع الغذاء، الرعاية الصحية، وتعليم الأطفال.")

    st.subheader("شركاؤنا وداعمونا")
    st.write("عرض شعارات المؤسسات الداعمة للمنظمة.")

    st.divider()
    # أزرار التفاعل (Call-to-Action) كما وردت في المقترح
    c1, c2, c3 = st.columns(3)
    c1.button("Donate Now / تبرع الآن", type="primary", use_container_width=True)
    c2.button("Join Us / انضم إلينا", use_container_width=True)
    c3.button("Learn About Projects / مشاريعنا", use_container_width=True)

# --- 2. صفحة المشاريع ---
elif page == "المشاريع":
    st.header("مشاريع المنظمة")
    tab1, tab2 = st.tabs(["المشاريع الحالية", "المشاريع السابقة"])
    
    with tab1:
        st.subheader("مشروع توزيع الغذاء في المناطق النائية")
        st.write("**الوصف:** تفاصيل الأهداف، المناطق المستهدفة، والجدول الزمني.")
        st.button("Contribute Now / ساهم الآن")

    with tab2:
        st.subheader("المشاريع المكتملة")
        st.write("عرض الصور والنتائج الملموسة والتقارير عن الأثر الذي تم تحقيقه.")

# --- 3. صفحة التطوع ---
elif page == "التطوع":
    st.header("انضم إلى فريق المتطوعين")
    st.write("التطوع هو فرصة للمساهمة في تغيير حياة الآخرين وتقديم العون لمن يحتاج.")
    
    st.subheader("لماذا تتطوع معنا؟")
    st.write("- إحداث تأثير مباشر.\n- تطوير المهارات الشخصية.\n- الحصول على شهادة تقدير.")
    
    st.subheader("فرص التطوع")
    st.info("**تطوع أونلاين:** كتابة محتوى، إدارة حملات رقمية.")
    st.success("**تطوع ميداني:** توزيع المساعدات في الميدان.")

# --- 4. اتصل بنا ---
elif page == "اتصل بنا":
    st.header("تواصل معنا")
    with st.form("contact"):
        st.text_input("الاسم")
        st.text_input("البريد الإلكتروني")
        st.text_area("الرسالة")
        st.form_submit_button("إرسال الرسالة")

    st.divider()
    st.write("📧 Email: info@tabakh.org")
    st.write("📞 Phone: 123-456-789")
    st.write("📍 Address: PORTSUDAN Street, City of Goodness")

# التذييل
st.sidebar.markdown("---")
st.sidebar.write("BY: ENG IBRAHIM MUSA") 
