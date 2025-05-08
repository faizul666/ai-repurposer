def linkedin_prompt(text, tone="professional"):
    return f"""
You are a social media expert. Convert the following blog into a professional and engaging LinkedIn post in a {tone} tone:

{text}
"""

def tweet_prompt(text, tone="witty"):
    return f"""
Write a {tone} tweet summarizing the key idea from this blog post in under 280 characters:

{text}
"""

def insta_caption_prompt(text, tone="casual"):
    return f"""
Write a short, {tone} Instagram caption from this blog post with emojis and 3 relevant hashtags:

{text}
"""
