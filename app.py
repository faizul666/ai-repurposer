import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import linkedin_prompt, tweet_prompt, insta_caption_prompt

# Load API key
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

st.set_page_config(page_title="AI Content Repurposer", page_icon="✨")
st.title("🪄 Blog-to-Social AI Repurposer")
st.markdown("Turn a blog post into a Tweet, LinkedIn post, and Instagram caption using free AI!")

blog_text = st.text_area("📄 Paste your blog post here", height=300)
tone = st.selectbox("🎨 Choose a tone", ["professional", "witty", "casual", "motivational"])

if st.button("✨ Generate Social Posts"):
    if not blog_text.strip():
        st.warning("Please paste a blog post first.")
    else:
        with st.spinner("Generating content..."):

            def get_response(prompt):
                response = client.chat.completions.create(
                    model="mistralai/mistral-7b-instruct",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content.strip()

            outputs = {
                "LinkedIn": get_response(linkedin_prompt(blog_text, tone)),
                "Twitter": get_response(tweet_prompt(blog_text, tone)),
                "Instagram": get_response(insta_caption_prompt(blog_text, tone))
            }

        for platform, content in outputs.items():
            st.subheader(f"📣 {platform} Post")
            st.code(content, language="markdown")
