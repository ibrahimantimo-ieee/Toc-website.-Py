import streamlit as st

# إعدادات الصفحة العامة وفقاً للمقترح
st.set_page_config(page_title="TOC Website Proposal", layout="wide")

# [span_4](start_span)تخصيص التصميم بالألوان الهادئة (الأزرق/الأخضر) المقترحة[span_4](end_span)
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# [span_5](start_span)[span_6](start_span)[span_7](start_span)[span_8](start_span)القائمة الجانبية للتنقل[span_5](end_span)[span_6](end_span)[span_7](end_span)[span_8](end_span)
st.sidebar.title("TOC Website Proposal")
page = st.sidebar.radio("انتقل إلى الصفحات:", ["1. الرئيسية", "2. المشاريع", "3. التطوع", "4. اتصل بنا"])

# -[span_9](start_span)-- 1. الصفحة الرئيسية[span_9](end_span) ---
if page == "1. الرئيسية":
    col1, col2 = st.columns([1, 4])
    with col1:
        [span_10](start_span)st.subheader("Logo")[span_10](end_span)
    with col2:
        [span_11](start_span)st.title("منظمة TOC الإنسانية")[span_11](end_span)
        [span_12](start_span)st.info("**قصة الشعار:** يرمز شعارنا إلى التضامن والإيمان بقوة العمل الجماعي لتحقيق تغيير إيجابي.")[span_12](end_span)

    st.divider()
    [span_13](start_span)st.header("من نحن؟")[span_13](end_span)
    [span_14](start_span)[span_15](start_span)st.write("نحن منظمة تسعى لتحقيق العدالة الاجتماعية وتوفير الاحتياجات الأساسية.")[span_14](end_span)[span_15](end_span)
    
    col_vision, col_goals = st.columns(2)
    with col_vision:
        [span_16](start_span)st.subheader("الرؤية")[span_16](end_span)
        [span_17](start_span)st.write("أن نصبح منظمة رائدة في تقديم المساعدات الإنسانية.")[span_17](end_span)
    with col_goals:
        [span_18](start_span)st.subheader("أهدافنا")[span_18](end_span)
        [span_19](start_span)st.write("- تحسين ظروف المحتاجين.\n- تعزيز التعليم والصحة.\n- تقديم مساعدات طارئة.")[span_19](end_span)

    [span_20](start_span)st.subheader("ماذا نفعل؟")[span_20](end_span)
    [span_21](start_span)st.write("توزيع الغذاء، الرعاية الصحية، وتعليم الأطفال.")[span_21](end_span)

    [span_22](start_span)st.subheader("شركاؤنا وداعمونا")[span_22](end_span)
    [span_23](start_span)st.write("عرض شعارات المؤسسات الداعمة.")[span_23](end_span)

    st.divider()
    # [span_24](start_span)[span_25](start_span)أزرار التفاعل الواضحة[span_24](end_span)[span_25](end_span)
    c1, c2, c3 = st.columns(3)
    c1.button("Donate Now / تبرع الآن", type="primary", use_container_width=True)
    c2.button("Join Us / انضم إلينا", use_container_width=True)
    c3.button("Learn About Projects / مشاريعنا", use_container_width=True)

# -[span_26](start_span)-- 2. صفحة المشاريع[span_26](end_span) ---
elif page == "2. المشاريع":
    [span_27](start_span)st.header("مشاريع المنظمة")[span_27](end_span)
    [span_28](start_span)[span_29](start_span)tab1, tab2 = st.tabs(["المشاريع الحالية", "المشاريع السابقة"])[span_28](end_span)[span_29](end_span)
    
    with tab1:
        [span_30](start_span)st.subheader("مشروع توزيع الغذاء في المناطق النائية")[span_30](end_span)
        [span_31](start_span)st.write("**الوصف:** تفاصيل الأهداف، المناطق المستهدفة، والجدول الزمني.")[span_31](end_span)
        [span_32](start_span)st.button("Contribute Now / ساهم الآن")[span_32](end_span)

    with tab2:
        [span_33](start_span)st.subheader("المشاريع المكتملة")[span_33](end_span)
        [span_34](start_span)st.write("عرض الصور والنتائج الملموسة والتقارير المفصلة.")[span_34](end_span)

# -[span_35](start_span)-- 3. صفحة التطوع[span_35](end_span) ---
elif page == "3. التطوع":
    [span_36](start_span)st.header("انضم إلى فريق المتطوعين")[span_36](end_span)
    [span_37](start_span)st.write("التطوع فرصة للمساهمة في تغيير حياة الآخرين.")[span_37](end_span)
    
    [span_38](start_span)st.subheader("لماذا تتطوع معنا؟")[span_38](end_span)
    [span_39](start_span)st.write("* إحداث تأثير مباشر.\n* تطوير المهارات.\n* الحصول على شهادة تقدير.")[span_39](end_span)
    
    [span_40](start_span)st.subheader("فرص التطوع المتاحة")[span_40](end_span)
    [span_41](start_span)st.info("**تطوع أونلاين:** كتابة محتوى، حملات رقمية.")[span_41](end_span)
    [span_42](start_span)st.success("**تطوع ميداني:** توزيع المساعدات في الميدان.")[span_42](end_span)

# -[span_43](start_span)-- 4. اتصل بنا[span_43](end_span) ---
elif page == "4. اتصل بنا":
    [span_44](start_span)st.header("تواصل معنا")[span_44](end_span)
    with st.form("contact"):
        [span_45](start_span)st.text_input("الاسم")[span_45](end_span)
        [span_46](start_span)st.text_input("البريد الإلكتروني")[span_46](end_span)
        [span_47](start_span)st.text_area("الرسالة")[span_47](end_span)
        [span_48](start_span)st.form_submit_button("Send Message / إرسال")[span_48](end_span)

    st.divider()
    [span_49](start_span)st.subheader("معلومات الاتصال")[span_49](end_span)
    [span_50](start_span)st.write("📧 info@tabakh.org | 📞 123-456-789")[span_50](end_span)
    [span_51](start_span)st.write("💬 WhatsApp: 987-654-321")[span_51](end_span)
    [span_52](start_span)st.write("📍 PORTSUDAN Street, City of Goodness")[span_52](end_span)

# [span_53](start_span)[span_54](start_span)تذييل الصفحة[span_53](end_span)[span_54](end_span)
st.sidebar.markdown("---")
[span_55](start_span)st.sidebar.write("BY: ENG IBRAHIM MUSA")[span_55](end_span)
