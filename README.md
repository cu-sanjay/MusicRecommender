<p align="center">
  <a href="https://musicx.streamlit.app/" target="_blank">
    <img src="logo.png" alt="Icon" width="100">
  </a>
  
  <h1 align="center">Music Recommendation System</h1>
</p>



<p align="center">
  Simple and powerful music recommendation system using machine learning to suggest personalized music recommendations based on user preferences. and many customizations. Unlike traditional recommendation systems that often feel like opaque black boxes, this system aims to empower users by providing clear rationales behind each recommendation and allowing them to customize their experience according to their preferences.
</p>

## Features

### Core Features

- **Dual Recommendation Modes**: Users can switch between two modes:
  - **Trending Tracks**: Recommends popular songs.
  - **Hidden Gems**: Discovers less popular, underrated tracks.
  
- **Six Recommendation Types**:
  - By Artist
  - Lyrically Similar
  - Similar Energy
  - Similar Mood
  - Released Around the Same Time
  - Random
  
- **Customizable Preferences**: Users can toggle any combination of recommendation types and set the number of recommendations for each type (ranging from 1 to 10).

### User Experience (UX) Enhancements

- **Lyric Visibility**: Option to display or hide song lyrics.
- **YouTube Integration**: Direct access to YouTube videos for recommended songs.
- **Interactive Recommendations**: Clicking on a recommended song triggers further recommendations based on that selection.
- **Theme and Width Options**: Ability to switch between custom (pastel), light, and dark themes, as well as adjust the width of the main content area.
- **Convenient Navigation**: Hamburger menu provides access to additional features such as bug reporting, sharing the web app, viewing source code, reading about the project, and accessing credits.
- **Cross-Platform Compatibility**: Ensures a seamless experience across various devices with responsive design.

## Use Case Examples

- **User A**: Catch up with the latest hits by utilizing the "Keep up with what's trending" mode.
- **User B**: Explore lesser-known tracks with the "Discover hidden gems" mode.
- **User C**: Focus on energy and mood rather than lyrics by disabling "Lyrically Similar" recommendations.
- **User D**: Dive into the discography of a favorite artist by enabling "By Artist" recommendations.
- **User E**: Explore contemporary music by activating "Released Around the Same Time" recommendations.
- **User F**: Seek variety by increasing the number of recommendations for each type.
- **User G**: Opt for a minimalist approach with only one recommendation per type.
- **User H**: Embrace serendipity with random recommendations.
- **User I**: Explore music outside their usual taste with random recommendations.

## Technologies Used
- Programming Language: Python
- Data Science Libraries: Pandas, NumPy, Scikit-learn
- Web Framework: Streamlit 

## Local Setup

To run project locally:

1. Clone the repository.
2. Set up a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Run the Streamlit frontend using `streamlit run app.py`.

## Folder Organization

- `.github/workflows/test.yml`: CI pipeline for automated testing.
- `.streamlit/config.toml`: Custom theming for the frontend.
- `pickles`: Data used for recommendations.

## Testing and Continuous Integration (CI)

The core functionality of the recommender system is tested using pytest. GitHub Actions are configured to run these tests automatically upon code push or pull request.

## Continuous Deployment (CD)

The Streamlit frontend is hosted at [Streamlit MusicX](https://musicx.streamlit.app/). Changes pushed to the main branch trigger automatic updates to the site.

## Data Source
The music data used for training the recommendation system is sourced from the publicly available Audio Features and Lyrics of Spotify Songs: [This](https://www.kaggle.com/datasets/imuhammad/audio-features-and-lyrics-of-spotify-songs) dataset on Kaggle.
