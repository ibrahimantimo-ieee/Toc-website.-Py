import streamlit as st

# [span_0](start_span)[span_1](start_span)إعدادات الصفحة العامة وفقاً للمقترح[span_0](end_span)[span_1](end_span)
st.set_page_config(page_title="TOC Website Proposal", layout="wide")

# [span_2](start_span)تخصيص الألوان (أزرق وأخضر هادئ) لتعكس الطبيعة الإنسانية[span_2](end_span)
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True) # تم تصحيح هذا السطر هنا

# --- القائمة الجانبية للتنقل ---
st.sidebar.title("TOC Proposal")
page = st.sidebar.radio("انتقل إلى الصفحات:", ["1. الصفحة الرئيسية", "2. صفحة المشاريع", "3. صفحة التطوع", "4. اتصل بنا"])

# --- 1. الصفحة الرئيسية ---
if page == "1. الصفحة الرئيسية":
    col1, col2 = st.columns([1, 4])
    with col1:
        [span_3](start_span)st.subheader("الشعار")[span_3](end_span)
    with col2:
        [span_4](start_span)st.title("منظمة TOC الإنسانية")[span_4](end_span)
        [span_5](start_span)st.info(f"**قصة الشعار:** يرمز شعارنا إلى التضامن والإيمان بقوة العمل الجماعي لتحقيق تغيير إيجابي.")[span_5](end_span)

    st.divider()
    [span_6](start_span)st.header("من نحن؟")[span_6](end_span)
    [span_7](start_span)[span_8](start_span)st.write("نحن منظمة تسعى لتحقيق العدالة الاجتماعية وتوفير الاحتياجات الأساسية.")[span_7](end_span)[span_8](end_span)
    
    col_vision, col_goals = st.columns(2)
    with col_vision:
        [span_9](start_span)st.subheader("الرؤية")[span_9](end_span)
        [span_10](start_span)st.write("أن نصبح منظمة رائدة في تقديم المساعدات الإنسانية.")[span_10](end_span)
    with col_goals:
        [span_11](start_span)st.subheader("أهدافنا")[span_11](end_span)
        [span_12](start_span)st.write("- تحسين ظروف المحتاجين.\n- تعزيز التعليم والصحة.\n- تقديم مساعدات طارئة.")[span_12](end_span)

    [span_13](start_span)st.subheader("ماذا نفعل؟")[span_13](end_span)
    [span_14](start_span)st.write("توزيع الغذاء، الرعاية الصحية، وتعليم الأطفال.")[span_14](end_span)

    [span_15](start_span)st.subheader("شركاؤنا وداعمونا")[span_15](end_span)
    [span_16](start_span)st.write("عرض شعارات المؤسسات الداعمة.")[span_16](end_span)

    st.divider()
    c1, c2, c3 = st.columns(3)
    [span_17](start_span)c1.button("Donate Now / تبرع الآن", type="primary", use_container_width=True)[span_17](end_span)
    [span_18](start_span)c2.button("Join Us / انضم إلينا", use_container_width=True)[span_18](end_span)
    [span_19](start_span)c3.button("Learn About Projects / مشاريعنا", use_container_width=True)[span_19](end_span)

# --- 2. صفحة المشاريع ---
elif page == "2. صفحة المشاريع":
    [span_20](start_span)st.header("مشاريع المنظمة")[span_20](end_span)
    [span_21](start_span)[span_22](start_span)tab1, tab2 = st.tabs(["المشاريع الحالية", "المشاريع السابقة"])[span_21](end_span)[span_22](end_span)
    
    with tab1:
        [span_23](start_span)st.subheader("مشروع توزيع الغذاء في المناطق النائية")[span_23](end_span)
        [span_24](start_span)st.write("**الوصف:** تفاصيل الأهداف، المناطق المستهدفة، والجدول الزمني.")[span_24](end_span)
        [span_25](start_span)st.button("Contribute Now / ساهم الآن")[span_25](end_span)

    with tab2:
        [span_26](start_span)st.subheader("المشاريع المكتملة")[span_26](end_span)
        [span_27](start_span)st.write("عرض النتائج الملموسة والتقارير عن الأثر الذي تم تحقيقه.")[span_27](end_span)

# --- 3. صفحة التطوع ---
elif page == "3. صفحة التطوع":
    [span_28](start_span)st.header("التطوع معنا")[span_28](end_span)
    [span_29](start_span)st.write("التطوع فرصة للمساهمة في تغيير حياة الآخرين.")[span_29](end_span)
    
    [span_30](start_span)st.subheader("لماذا تتطوع معنا؟")[span_30](end_span)
    [span_31](start_span)st.write("* تأثير مباشر على المحتاجين.\n* تطوير المهارات الشخصية.\n* الحصول على شهادة تقدير.")[span_31](end_span)
    
    [span_32](start_span)st.subheader("فرص التطوع")[span_32](end_span)
    [span_33](start_span)st.info("**تطوع أونلاين:** كتابة محتوى، حملات رقمية.")[span_33](end_span)
    [span_34](start_span)st.success("**تطوع ميداني:** توزيع المساعدات في الميدان.")[span_34](end_span)

# --- 4. اتصل بنا ---
elif page == "4. اتصل بنا":
    [span_35](start_span)st.header("تواصل معنا")[span_35](end_span)
    with st.form("contact_form"):
        [span_36](start_span)st.text_input("الاسم")[span_36](end_span)
        [span_37](start_span)st.text_input("البريد الإلكتروني")[span_37](end_span)
        [span_38](start_span)st.text_area("الرسالة")[span_38](end_span)
        [span_39](start_span)st.form_submit_button("Send Message / إرسال")[span_39](end_span)

    st.divider()
    [span_40](start_span)st.write("📧 info@tabakh.org | 📞 123-456-789")[span_40](end_span)
    [span_41](start_span)st.write("📍 PORTSUDAN Street, City of Goodness")[span_41](end_span)

st.sidebar.markdown("---")
[span_42](start_span)[span_43](start_span)st.sidebar.write("BY: ENG IBRAHIM MUSA")[span_42](end_span)[span_43](end_span)
