import streamlit as st
from streamlit_extras.keyboard_text import key
import pandas as pd
import numpy as np
import re

from urllib.parse import urlparse, parse_qs

def main():
    # Create a text input box
    text_input = st.text_input("Enter a YouTube link:")

    # Check if the user has pressed Enter
    if st.button("Submit"):
        # Extract the video ID from the YouTube link
        url_parsed = urlparse(text_input)
        video_id = parse_qs(url_parsed.query).get('v')

        if video_id:
            video_id = video_id[0]  # Get the first (and only) value from the list
            # Display the YouTube video
            st.video(f"https://www.youtube.com/watch?v={video_id}")
        else:
            st.write("Invalid YouTube link.")

if __name__ == "__main__":
    main()