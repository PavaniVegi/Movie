# import media file to inherit the movie object structure
import media
import fresh_tomatoes

# creating movie objects by usibg media class movie structure
toy_story = media.Movie(
    "Toy Story", 
    "Astory of boy and his toys comes into life.", 
    r"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/".
    ...."220px-Toy_Story.jpg",  
    r"https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )
avatar = media.Movie(
    "Avatar", 
    "A marine on an alien planet.", 
    r"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-".
    ...."Poster.jpg/220px-Avatar-Teaser-Poster.jpg", 
    r"https://www.youtube.com/watch?v=d1_JBMrrYw8"
    )
moana = media.Movie(
    "Moana", 
    "An adventurous teenager sails out on a daring mission to save her people", 
    r"https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Moana_Teaser_Poste".
    ..."r.jpg/220px-Moana_Teaser_Poster.jpg", 
    r"https://www.youtube.com/watch?v=M5dnZKrUpdA"
    )
wall_e = media.Movie(
    "WALL_E", 
    "A robot who is responsible for cleaning a waste-covered Earth meets ".
    ..."another robot and falls in love with her. Together, they set out on a".
    ..."journey that will alter the fate of mankind.", 
    r"https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/WALL-Eposter.jpg/".
    ..."220px-WALL-Eposter.jpg", 
    r"https://www.youtube.com/watch?v=ZisWjdjs-gM"
    )
kungfu_panda = media.Movie(
    "Kung Fu Panda 3", 
    "The Dragon Warrior, Po, has to deal with challenges galore when circums".
    ..."tances compel him to train a bunch of awkward pandas in martial arts".
    ..." so that they can trounce Kai, a wicked supernatural warrior.", 
    r"https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Kung_Fu_Panda_3_".
    ..."poster.jpg/220px-Kung_Fu_Panda_3_poster.jpg", 
    r"https://www.youtube.com/watch?v=10r9ozshGVE"
    )

# creating a list of all movie objects
movies = [toy_story, avatar, moana, wall_e, kungfu_panda]

# call open movies page to generate web page with movies objects
fresh_tomatoes.open_movies_page(movies)
