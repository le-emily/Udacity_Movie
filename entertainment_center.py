import fresh_tomatoes
import media

toy_story =media.Movie("Toy Story", "A story of a boy and toys that come to life", "https://en.wikipedia.org/wiki/Toy_Story","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar=media.Movie("Avatar","A marine on an alien planet","https://en.wikipedia.org/wiki/Avatar_(2009_film)", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_dark_knight = media.Movie("The Dark Knight", "A man dressed as a bat works undercover as a hero","https://en.wikipedia.org/wiki/The_Dark_Knight_(film)", "https://www.youtube.com/watch?v=qY3UkAHufLY" )

tangled = media.Movie("Tangled","A woman tries to discover who she really is with the help of a man and a horse", "https://en.wikipedia.org/wiki/Tangled", "https://www.youtube.com/watch?v=pyOyBVXDJ9Q")

frozen =media.Movie("Frozen","https://en.wikipedia.org/wiki/Frozen_(2013_film)","https://www.youtube.com/watch?v=TbQm5doF_Uc")

the_godfather = movie.Movie("The Godfather",
                           "Every time he tries to get out, they pull him back in",
                           "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=YBrs0wvkPls")

the_princess_bride = movie.Movie("The Princess Bride",
                                 "Hello. My name is Inigo Montoya. You killed my father. Prepare to die",
                                 "http://ia.media-imdb.com/images/M/MV5BMTkzMDgyNjQwM15BMl5BanBnXkFtZTgwNTg2Mjc1MDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                                 "https://www.youtube.com/watch?v=VYgcrny2hRs")


movies = [toy_story,avatar,the_dark_knight,tangled,frozen,the_godfather,the_princess_bride]

fresh_tomatoes.open_movies_page(movies)
