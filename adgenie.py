import streamlit as st
from openai import OpenAI

# Load the OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AdGenie - Ecommerce AI Assistant")

st.title("🤖 AdGenie - Ecommerce AI Assistant")
st.write("Generate high-converting ad copy, emails, and support messages for your brand.")

brand = st.text_input("🛍️ Brand Name", "Oflicto")
product = st.text_input("📦 Product", "Massage Gun")
tone = st.selectbox("🎨 Tone", ["friendly", "professional", "bold"])
audience = st.text_input("🎯 Target Audience", "fitness lovers")
query = st.text_area("📩 Customer Query (for Support Reply)", "Where is my order? I placed it 5 days ago.")
customer_name = st.text_input("🙋 Customer Name", "Rahul")

if st.button("Generate Replies"):
    with st.spinner("Thinking..."):
        system_prompt = (
            f"You are AdGenie, an ecommerce AI assistant for the brand '{brand}'. "
            f"Generate: \n1. Ad Copy\n2. Promotional Email\n3. Support Reply to customer '{customer_name}' "
            f"who asked: '{query}'\n\n"
            f"Product: {product}\nTone: {tone}\nTarget Audience: {audience}"
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # You can try "gpt-4" if available
                messages=[{"role": "system", "content": system_prompt}]
            )
            output = response.choices[0].message.content
            st.markdown("### ✨ Generated Content")
            st.write(output)
        except Exception as e:
            st.error(f"❌ Error: {e}")
