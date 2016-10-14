import webbrowser

# class Video():
#     def _init_(self,video_title,video_duration):
#         self.title = video_title
#         self.duration =video_duration


# This class stores information about a movie
class Movie():
    # VALID_RATINGS = ["G","PG", "PG-13","R"]
    def _init_(self,movie_title,movie_storyline, poster_image,trailer_youtube):
        self.movie_title=movie_title
        self.storyline =movie_storyline
        self.poster_image_url =poster_image
        self.trailer_youtube_url =trailer_youtube

    # def show_trailer():
#
# class tvShow(Video):
#     # VALID_RATINGS = ["G","PG", "PG-13","R"]
#     def _init_(self,tvShow_season,tvShow_tv_station, tvShow_episode):
#         self.season =tvShow_season
#         self.tv_station =tvShow_tv_station
#         self.episode =tvShow_episode
#
#     def get_local_listing():
