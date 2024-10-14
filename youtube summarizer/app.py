import streamlit as st
from dotenv import load_dotenv
load_dotenv() #load all the environment variables
import google.generativeai as genai

import os

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
# genai.init(project=os.getenv("GOOGLE_API_KEY"), location='asia-south1')

prompt = "You are Youtube video summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points withinn 200-250 words. The transcript text will be appended here: "

#getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript = transcript + " " + i["text"]

        return transcript

    except Exception as e:
        raise e

#getting the summary based on prompt from google generatiev ai
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

st.title("Youtube Transcript to detailed Notes Converted")
youtube_link = st.text_input("Enter Youtube link: ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"hhtp://img.youtube.com/vi/{video_id}/0.jpg", use_column_width = True)

if st.button("Get Detailed notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("#Detailed Notes: ")
        st.write(summary)
