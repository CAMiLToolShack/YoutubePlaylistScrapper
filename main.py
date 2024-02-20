import YoutubePlaylistScrapper

Scrapper = YoutubePlaylistScrapper.YoutubePlaylistScrapper("Put your playlist id here.")
Scrapper.set_youtube_api_key("Put your API key here.")
Scrapper.scrape()
Scrapper._write_to_docx()
Scrapper._write_to_csv()
