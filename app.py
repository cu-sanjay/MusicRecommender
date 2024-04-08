import streamlit as st
import pickle
import base64
import pandas as pd
from recommender import hybrid_recommend, get_metadata
from youtubesearchpython import VideosSearch

dataset_url = 'https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs'

st.set_page_config(
    page_title='Music Recommendation System', 
    page_icon='logo.png',
    menu_items={
    'Get Help': 'Dumboo Test By Yourself.',
    'Report a bug': 'https://github.com/cu-sanjay/MusicRecommender/issues',
    'About': "### Developed by Sanjay Choudhary ❤️\n#### Music Data sourced from [Kaggle](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs)"
    }
)
with open("cu_logo.jpg", "rb") as f:
  logo_data = base64.b64encode(f.read()).decode()
st.markdown(
  f"""
  <div style="text-align: center;">
    <img src="data:image/png;base64, {logo_data}" width="100" height="150">
    <h1>AI/ML Mini Project</h1>
    <h1>Music Recommendation System</h1>
  </div>
  """,
  unsafe_allow_html=True
)
def change_song(index):
    st.session_state['current_song_index'] = index

# Load the data from the pickled file
data = pickle.load(open('pickles/data.pkl', 'rb'))


# Dropdown to select a song
selected_song = st.selectbox("Select a song:", data['track_name'])

# Find the index of the selected song
if selected_song in data['track_name'].tolist():
    selected_index = data[data['track_name'] == selected_song].index[0]
else:
    selected_index = 0  # Default to the first song if the selected song is not found

# Change the current song index
change_song(selected_index)

# Sidebar with customizing options

st.sidebar.title('Choose:')

option1 = 'Popular songs'
option2 = 'Discover hidden songs'
mode = st.sidebar.selectbox('Your mode of recommendations', (option1, option2))
if(mode == option1):
    prioritisePopular = True
else:
    prioritisePopular = False

recommendations_count = st.sidebar.slider('Set number of songs', min_value=1, max_value=10, value=3)

st.sidebar.write('Choose Recommendation type') # options added later below when adding songs



# Main Content:


# Showing current song

current_song = get_metadata(st.session_state['current_song_index'])

st.write(f'## {current_song["track_name"]} - {current_song["track_artist"]}')

youtube_search = VideosSearch(f'## {current_song["track_name"]} - {current_song["track_artist"]}', limit = 1)
youtube_id = youtube_search.result()['result'][0]['id'] # getting youtube link
thumbnail_url = youtube_search.result()['result'][0]['thumbnails'][0]['url'] # getting youtube thumbnail

st.write(f'[![YouTube thumbnail]({thumbnail_url})](https://www.youtube.com/watch?v={youtube_id})')
st.write(f'[Hear on YouTube](https://www.youtube.com/watch?v={youtube_id})')

with st.expander('Show lyrics'):
    st.write(current_song['lyrics'])


# Retreiving and showing recommendations as per user's choices

recommendations = hybrid_recommend(st.session_state['current_song_index'], recommendations_count, prioritisePopular=prioritisePopular)

for recommendation_type, songs in recommendations.items():
    if not st.sidebar.checkbox(recommendation_type, value=True):
        continue
    if(len(songs) == 0): # do not show a recommendation type if it has no songs
        continue
    st.write(f'#### {recommendation_type.title()}')
    with st.container():
        for song in songs:
            st.write(f'- {song["track_name"]} - {song["track_artist"]}')
            st.button("listen", key=str(song['index'])+recommendation_type, on_click=change_song, args=(song['index'],))
