import streamlit as st
import os

st.set_page_config(page_title="🎵 Streamlit Music Player", layout="centered")

st.title("🎵 Streamlit Music Player")
st.caption("Browse and play preloaded songs from the music folder!")

# --- Music directory path ---
MUSIC_DIR = "music"

# List all audio files in MUSIC_DIR
audio_files = [
    f for f in os.listdir(MUSIC_DIR)
    if f.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a'))
]

if not audio_files:
    st.warning("No audio files found in the music directory!")
else:
    selected_file = st.selectbox("🎶 Select a song to play:", audio_files)
    audio_path = os.path.join(MUSIC_DIR, selected_file)
    
    # Read audio file bytes
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    st.markdown(f"**Now Playing:** `{selected_file}`")
    st.audio(audio_bytes, format=f"audio/{selected_file.split('.')[-1]}")

    # Display playlist
    st.subheader("📃 Playlist")
    for af in audio_files:
        st.write(f"• {af}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
