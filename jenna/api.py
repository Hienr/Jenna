import config
from googleapiclient.discovery import build


class YouTubeAPI:
    def __init__(self):
        self._youtube = build(config.YOUTUBE_API_SERVICE_NAME, config.YOUTUBE_API_VERSION,
            developerKey=config.DEVELOPER_KEY)
    
    def search_by_keyword(self, keyword):
        search_response = self._youtube.search().list(
            q=keyword,
            part="id,snippet",
            maxResults=25
        ).execute()

        videos = {}

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos[search_result["id"]["videoId"]] = "%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["videoId"])
        return videos