import streamlit as st

st.set_page_config(page_title="🎵 Streamlit Music Player", layout="centered")

st.title("🎵 Streamlit Music Player")
st.caption("Upload your music files, build a playlist, and enjoy!")

# --- Upload Section ---
st.sidebar.header("📁 Upload Music")
uploaded_files = st.sidebar.file_uploader(
    "Upload audio files (MP3, WAV, FLAC, etc.)",
    type=["mp3", "wav", "ogg", "flac", "m4a"],
    accept_multiple_files=True
)

# --- Volume Control ---
volume = st.sidebar.slider("🔊 Volume (simulated)", 0, 100, 80)

# --- Playlist and Playback ---
if uploaded_files:
    file_names = [file.name for file in uploaded_files]
    selected_file_name = st.selectbox("🎶 Select a song to play:", file_names)

    # Find the selected file object
    selected_file = next(file for file in uploaded_files if file.name == selected_file_name)

    # Display selected song and audio player
    st.markdown(f"**Now Playing:** `{selected_file.name}`")
    audio_bytes = selected_file.read()
    st.audio(audio_bytes, format=selected_file.type)

    # Display Playlist Table
    st.subheader("📃 Playlist")
    for file in uploaded_files:
        st.write(f"• {file.name}")
else:
    st.info("Upload some audio files to get started 🎧")

# --- Footer ---
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
