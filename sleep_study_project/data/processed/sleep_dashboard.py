import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# تشكيل النصوص العربية
def reshape(text):
    return get_display(arabic_reshaper.reshape(text))

# تحميل البيانات
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "sleep_data_clean.csv"))

st.title(reshape("📊 دراسة تأثير النوم باستخدام بايثون"))

st.markdown(reshape("""
### نظرة عامة
تم جمع البيانات من استبيان يتناول عادات النوم وتأثيرها على المزاج والطاقة والتركيز، باستخدام Python وأدوات التحليل البياني.
"""))

# توزيع ساعات النوم
st.subheader(reshape("توزيع ساعات النوم"))

fig, ax = plt.subplots()
sns.histplot(df['ساعات_النوم'], kde=True, color="#3498db")
plt.xlabel(reshape("عدد الساعات"))
plt.ylabel(reshape("عدد المشاركين"))
st.pyplot(fig)

# العلاقة بين العمر وساعات النوم
st.subheader(reshape("العلاقة بين العمر وساعات النوم"))

fig2, ax2 = plt.subplots()
sns.regplot(x='العمر_الرقمي', y='ساعات_النوم', data=df,
            scatter_kws={'alpha': 0.6, 'color': '#2ecc71'},
            line_kws={'color': '#e74c3c', 'linewidth': 3})
plt.axhline(y=7, color='blue', linestyle='--', label=reshape("المستوى الموصى به"))
plt.legend()
plt.xlabel(reshape("العمر"))
plt.ylabel(reshape("ساعات النوم"))
st.pyplot(fig2)
