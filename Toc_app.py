import streamlit as st

# 1. إعدادات الصفحة العامة (اسم الموقع وتنسيق العرض)
st.set_page_config(page_title="TOC Website", layout="wide")

# 2. تخصيص الألوان (أزرق وأخضر هادئ) لتعكس الطبيعة الإنسانية للمنظمة
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; font-weight: bold; }
    .stTextInput>div>div>input { border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. شريط التنقل الجانبي (Sidebar) للوصول لجميع الصفحات
st.sidebar.title("القائمة الرئيسية")
page = st.sidebar.radio("انتقل إلى الصفحات:", ["الرئيسية", "المشاريع", "التطوع", "اتصل بنا"])

# --- الصفحة الأولى: الرئيسية ---
if page == "الرئيسية":
    col1, col2 = st.columns([1, 4])
    with col1:
        [span_3](start_span)st.subheader("الشعار") #[span_3](end_span)
    with col2:
        st.title("منظمة TOC الإنسانية")
        [span_4](start_span)st.info("**قصة الشعار:** يرمز شعارنا إلى التضامن والإيمان بقوة العمل الجماعي لتحقيق تغيير إيجابي.") #[span_4](end_span)

    st.divider()
    [span_5](start_span)st.header("من نحن؟") #[span_5](end_span)
    [span_6](start_span)[span_7](start_span)st.write("نحن منظمة تسعى لتحقيق العدالة الاجتماعية وتوفير الاحتياجات الأساسية من خلال رؤية طموحة.") #[span_6](end_span)[span_7](end_span)
    
    col_v, col_g = st.columns(2)
    with col_v:
        st.subheader("رؤيتنا")
        [span_8](start_span)st.write("أن نصبح منظمة رائدة في تقديم المساعدات الإنسانية وتحقيق العدالة الاجتماعية.") #[span_8](end_span)
    with col_g:
        [span_9](start_span)st.subheader("أهدافنا") #[span_9](end_span)
        [span_10](start_span)st.write("- تحسين ظروف المحتاجين.\n- تعزيز التعليم والصحة.\n- تقديم مساعدات طارئة.") #[span_10](end_span)

    [span_11](start_span)st.subheader("ماذا نفعل؟") #[span_11](end_span)
    [span_12](start_span)st.write("نركز أنشطتنا على توزيع الغذاء، الرعاية الصحية، وتعليم الأطفال.") #[span_12](end_span)

    [span_13](start_span)st.subheader("شركاؤنا وداعمونا") #[span_13](end_span)
    [span_14](start_span)st.write("✨ عرض شعارات الشركات والمؤسسات الداعمة للمنظمة.") #[span_14](end_span)

    st.divider()
    # أزرار التفاعل البارزة (CTA)
    [span_15](start_span)c1, c2, c3 = st.columns(3) #[span_15](end_span)
    [span_16](start_span)c1.button("تبرع الآن / Donate Now", type="primary", use_container_width=True) #[span_16](end_span)
    [span_17](start_span)c2.button("انضم إلينا / Join Us", use_container_width=True) #[span_17](end_span)
    c3.button("تعرف على مشاريعنا", use_container_width=True)

# --- الصفحة الثانية: المشاريع ---
elif page == "المشاريع":
    [span_18](start_span)st.header("مشاريع المنظمة") #[span_18](end_span)
    [span_19](start_span)[span_20](start_span)tab1, tab2 = st.tabs(["المشاريع الحالية", "المشاريع السابقة"]) #[span_19](end_span)[span_20](end_span)
    
    with tab1:
        [span_21](start_span)st.subheader("مشروع توزيع الغذاء في المناطق النائية") #[span_21](end_span)
        [span_22](start_span)st.write("**الوصف:** تفاصيل حول الأهداف، المناطق المستهدفة، والجدول الزمني.") #[span_22](end_span)
        [span_23](start_span)st.button("ساهم الآن / Contribute Now") #[span_23](end_span)

    with tab2:
        [span_24](start_span)st.subheader("المشاريع المكتملة") #[span_24](end_span)
        [span_25](start_span)st.write("عرض الصور والنتائج الملموسة والتقرير المفصل عن الأثر الذي تم تحقيقه.") #[span_25](end_span)

# --- الصفحة الثالثة: التطوع ---
elif page == "التطوع":
    [span_26](start_span)st.header("انضم إلى فريق المتطوعين") #[span_26](end_span)
    [span_27](start_span)st.write("التطوع فرصة للمساهمة في تغيير حياة الآخرين وتقديم العون.") #[span_27](end_span)
    
    [span_28](start_span)st.subheader("لماذا تتطوع معنا؟") #[span_28](end_span)
    [span_29](start_span)st.write("* إحداث تأثير مباشر.\n* تطوير المهارات.\n* الحصول على شهادة تقدير.") #[span_29](end_span)
    
    [span_30](start_span)st.subheader("فرص التطوع") #[span_30](end_span)
    [span_31](start_span)st.info("**تطوع أونلاين:** كتابة محتوى، حملات رقمية.") #[span_31](end_span)
    [span_32](start_span)st.success("**تطوع ميداني:** توزيع المساعدات في الميدان.") #[span_32](end_span)

# --- الصفحة الرابعة: اتصل بنا ---
elif page == "اتصل بنا":
    [span_33](start_span)st.header("تواصل معنا") #[span_33](end_span)
    [span_34](start_span)with st.form("contact_form"): #[span_34](end_span)
        st.text_input("الاسم")
        st.text_input("البريد الإلكتروني")
        st.text_area("الرسالة")
        [span_35](start_span)st.form_submit_button("إرسال الرسالة / Send Message") #[span_35](end_span)

    st.divider()
    [span_36](start_span)st.subheader("معلومات الاتصال") #[span_36](end_span)
    [span_37](start_span)st.write("📧 info@tabakh.org | 📞 123-456-789") #[span_37](end_span)
    [span_38](start_span)st.write("💬 واتساب: 987-654-321") #[span_38](end_span)
    [span_39](start_span)st.write("📍 شارع بورتسودان، مدينة الخير") #[span_39](end_span)

# تذييل الصفحة يحمل توقيعك
st.sidebar.markdown("---")
[span_40](start_span)st.sidebar.write("BY: ENG IBRAHIM MUSA") #[span_40](end_span)
 
