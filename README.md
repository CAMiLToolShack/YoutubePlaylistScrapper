<h1>Scrapes data from youtube playlists.</h1> 

1. Create a YouTube playlist with videos to scrape
2. Copy the ID of the YouTube playlist. DO NOT COPY FULL LINK! To get ID copy information after 'link = ' in the URL
   For example: The ID for "https://www.youtube.com/playlist?list=PLvkXMNNLP7yuUoVibeBUqU1029kqLp6re" would be "PLvkXMNNLP7yuUoVibeBUqU1029kqLp6re"
3. To get the YouTube API key, create a Google Cloud service account and create a Youtube V3 API key
   Here's a more detailed tutorial: https://blog.hubspot.com/website/how-to-get-youtube-api-key
4. Pass information to class using .set_youtube_api_key()
5. use .scrape() after passing in all information
6. Make sure a 'transcripts/' directory exits in the local directory of python file
7. Finally, use ._write_to_docx() or ._write_to_csv() to output information into files
