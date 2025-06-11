import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🤖 AdGenie - Ecommerce AI Assistant")
st.write("Generate high-converting ad copy, emails, and support messages for your brand.")

brand = st.text_input("🛍️ Brand Name", "Oflicto")
product = st.text_input("📦 Product", "Massage Gun")
tone = st.text_input("🎨 Tone", "friendly")
audience = st.text_input("🎯 Target Audience", "fitness lovers")
customer_query = st.text_area("📩 Customer Query (for Support Reply)", "Where is my order? I placed it 5 days ago.")
customer_name = st.text_input("🙋 Customer Name", "Rahul")

if st.button("✨ Generate Content"):
    system_prompt = f'''
You are AdGenie, an AI assistant that generates ecommerce ad copy, emails, and customer support replies in a {tone} tone.

Generate the following content for the brand "{brand}" and product "{product}" targeting "{audience}":

1. Ad Copy
2. Abandoned Cart Email
3. Upsell Email
4. Support Reply to "{customer_query}" from {customer_name}
5. SMS Message (Thank You type)
    '''

    with st.spinner("Generating..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": system_prompt}]
        )
        result = response.choices[0].message.content
        st.markdown("### 📝 Generated Content")
        st.markdown(result)
