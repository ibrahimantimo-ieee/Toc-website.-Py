import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة والهوية البصرية بناءً على المقترح
st.set_page_config(page_title="منظمة TOC الإنسانية", page_icon="🤝", layout="wide")

# 2. [span_5](start_span)إضافة لمسات جمالية CSS (الألوان الهادئة: الأزرق والأخضر)[span_5](end_span)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Cairo', sans-serif; text-align: right; }
    [span_6](start_span).main { background-color: #f0f8ff; } /* أزرق فاتح هادئ[span_6](end_span) */
    .stButton>button {
        width: 100%; border-radius: 20px; background-color: #4CAF50; [span_7](start_span)/* أخضر[span_7](end_span) */
        color: white; font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #388E3C; transform: scale(1.02); }
    .map-container { border-radius: 15px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# [span_8](start_span)دالة لإضافة الخريطة التفاعلية (إحداثيات بورتسودان كمثال[span_8](end_span))
def display_map():
    st.markdown("### 📍 موقعنا على الخريطة")
    df = pd.DataFrame({'lat': [19.6158], 'lon': [37.2164]})
    st.map(df, zoom=12, use_container_width=True)

# 3. [span_9](start_span)[span_10](start_span)[span_11](start_span)[span_12](start_span)شريط التنقل الجانبي (4 صفحات منفصلة)[span_9](end_span)[span_10](end_span)[span_11](end_span)[span_12](end_span)
with st.sidebar:
    st.title("منظمة TOC 🤝")
    page = st.radio("القائمة الرئيسية", ["🏠 الرئيسية", "📂 المشاريع", "🙋 التطوع", "📞 اتصل بنا"])
    st.markdown("---")
    [span_13](start_span)st.caption("BY: ENG IBRAHIM MUSA[span_13](end_span)")

# -[span_14](start_span)-- 1. الصفحة الرئيسية[span_14](end_span) ---
if page == "🏠 الرئيسية":
    col_l, col_r = st.columns([1, 3])
    [span_15](start_span)with col_l: st.subheader("LOGO") #[span_15](end_span)
    with col_r:
        st.title("منظمة TOC الإنسانية")
        [span_16](start_span)st.info(f"**قصة الشعار:** يرمز شعارنا إلى التضامن والإيمان بقوة العمل الجماعي لتحقيق تغيير إيجابي.[span_16](end_span)")

    st.divider()
    [span_17](start_span)st.header("✨ من نحن؟") #[span_17](end_span)
    [span_18](start_span)[span_19](start_span)st.write("نحن منظمة تسعى لتحقيق العدالة الاجتماعية وتوفير الاحتياجات الأساسية.[span_18](end_span)[span_19](end_span)")
    
    c1, c2 = st.columns(2)
    with c1:
        [span_20](start_span)st.success("**ماذا نفعل؟** توزيع الغذاء، الرعاية الصحية، وتعليم الأطفال.[span_20](end_span)")
    with c2:
        [span_21](start_span)st.warning("**أهدافنا:** تحسين ظروف المحتاجين وتقديم مساعدات طارئة.[span_21](end_span)")
    
    st.divider()
    # [span_22](start_span)[span_23](start_span)أزرار الانتقال السريع (Call-to-Action)[span_22](end_span)[span_23](end_span)
    col_a, col_b, col_c = st.columns(3)
    with col_a: st.button("❤️ تبرع الآن")
    with col_b: st.button("🤝 انضم إلينا")
    with col_c: st.button("🔍 مشاريعنا")
    
    display_map()

# -[span_24](start_span)-- 2. صفحة المشاريع[span_24](end_span) ---
elif page == "📂 المشاريع":
    st.title("🚀 مشاريعنا الميدانية")
    tab1, tab2 = st.tabs(["📍 المشاريع الحالية", "✅ المشاريع السابقة"])
    
    with tab1:
        [span_25](start_span)st.subheader("مشروع توزيع الغذاء في المناطق النائية[span_25](end_span)")
        [span_26](start_span)st.write("إيصال المساعدات للأسر الأكثر احتياجاً.[span_26](end_span)")
        st.button("💰 ساهم الآن")

    with tab2:
        [span_27](start_span)st.subheader("حصاد الإنجازات[span_27](end_span)")
        [span_28](start_span)st.write("عرض النتائج الملموسة والتقارير عن الأثر المحقق.[span_28](end_span)")
    
    display_map()

# -[span_29](start_span)-- 3. صفحة التطوع[span_29](end_span) ---
elif page == "🙋 التطوع":
    st.title("كن جزءاً من التغيير 🌍")
    [span_30](start_span)st.markdown("> التطوع فرصة للمساهمة في تغيير حياة الآخرين.[span_30](end_span)")
    
    [span_31](start_span)st.header("لماذا تتطوع معنا؟[span_31](end_span)")
    [span_32](start_span)st.write("* تأثير مباشر على المحتاجين.[span_32](end_span)")
    [span_33](start_span)st.write("* تطوير المهارات الشخصية والمهنية.[span_33](end_span)")
    [span_34](start_span)st.write("* شهادة تقدير عند الإكمال.[span_34](end_span)")
    
    col_on, col_off = st.columns(2)
    with col_on:
        [span_35](start_span)st.info("**تطوع أونلاين:** كتابة محتوى وحملات رقمية.[span_35](end_span)")
    with col_off:
        [span_36](start_span)st.success("**تطوع ميداني:** توزيع المساعدات في الميدان.[span_36](end_span)")
    
    display_map()

# -[span_37](start_span)-- 4. صفحة اتصل بنا[span_37](end_span) ---
elif page == "📞 اتصل بنا":
    st.title("نحن هنا للاستماع إليك 📧")
    
    form_col, info_col = st.columns([2, 1])
    with form_col:
        with st.form("contact"):
            [span_38](start_span)st.text_input("الأسم") #[span_38](end_span)
            [span_39](start_span)st.text_input("البريد الإلكتروني") #[span_39](end_span)
            [span_40](start_span)st.text_area("رسالتك") #[span_40](end_span)
            [span_41](start_span)st.form_submit_button("إرسال الرسالة 🚀") #[span_41](end_span)
    
    with info_col:
        [span_42](start_span)st.markdown("### معلومات التواصل[span_42](end_span)")
        st.markdown("📧 info@tabakh.org")
        st.markdown("📞 123-456-789")
        st.markdown("📍 شارع بورتسودان")
    
    display_map()
