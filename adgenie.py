import streamlit as st
import openai
import os

st.set_page_config(page_title="AdGenie - AI Ad Assistant", layout="centered")

st.title("🤖 AdGenie - Ecommerce AI Assistant")
st.markdown("Generate high-converting ad copy, emails, and support messages for your brand.")

# Load OpenAI key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# User Inputs
brand = st.text_input("🛍️ Brand Name", "Oflicto")
product = st.text_input("📦 Product", "Massage Gun")
tone = st.selectbox("🎨 Tone", ["friendly", "luxury", "professional", "funny"])
audience = st.text_input("🎯 Target Audience", "fitness lovers")
customer_message = st.text_area("📩 Customer Query (for Support Reply)", "Where is my order? I placed it 5 days ago.")
name = st.text_input("🙋 Customer Name", "Rahul")

# Generate Button
if st.button("Generate AI Content"):
    system_prompt = f"""
You are AdGenie, an AI trained to generate ecommerce content including:
1. Ad Copy
2. Abandoned Cart Email
3. Upsell Email
4. Customer Support Reply
5. SMS Message

Use the brand: {brand}
Product: {product}
Tone: {tone}
Audience: {audience}
Customer Name: {name}
Customer Message: {customer_message}
Respond in a helpful and structured format.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": system_prompt}]
    )

    result = response['choices'][0]['message']['content']
    st.markdown("---")
    st.subheader("🧠 AI-Generated Output")
    st.markdown(result)
