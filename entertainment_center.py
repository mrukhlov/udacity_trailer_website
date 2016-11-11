import fresh_tomatoes
from media import Movie

almost_christmas = Movie('Almost Christmas', 'A dysfunctional family gathers together for their first Christmas since their mom died.', 'https://www.youtube.com/watch?v=-mw-Rhm8OIw', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjM1MTkwNTQ1Ml5BMl5BanBnXkFtZTgwNTc5ODgxOTE@._V1_SY1000_CR0,0,631,1000_AL_.jpg', '1h 52min', 'PG-13')
arrival = Movie('Arrival', 'A linguist is recruited by the military to assist in translating alien communications.', 'https://www.youtube.com/watch?v=AMgyWT075KY', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SY1000_CR0,0,640,1000_AL_.jpg', '1h 56min', 'PG-13')
shut_in = Movie('Shut In', 'A heart-pounding thriller about a widowed child psychologist who lives in an isolated existence in rural New England. Caught in a deadly winter storm, she must find a way to rescue a young boy before he disappears forever.', 'https://www.youtube.com/watch?v=LbCs-LTJqaM', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3MTAyMTE2MV5BMl5BanBnXkFtZTgwMzY5MzM0MDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg', '1h 31min', 'PG-13')
elle = Movie('Elle', 'A successful businesswoman gets caught up in a game of cat and mouse as she tracks down the unknown man who raped her.', 'https://www.youtube.com/watch?v=gM96ne-XiH0', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5NDI5MzA1OF5BMl5BanBnXkFtZTgwMTQzNTQwMDI@._V1_.jpg', '2h 10min', 'R')
love_witch = Movie('The Love Witch', 'A modern-day witch uses spells and magic to get men to fall in love with her, in a tribute to 1960s pulp novels and Technicolor melodramas.', 'https://www.youtube.com/watch?v=_1rMTHBSwuI', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5NDEyMjQwNV5BMl5BanBnXkFtZTgwNDQ1MjMwMDI@._V1_SY1000_CR0,0,672,1000_AL_.jpg', '2h', 'R')
doctor_strange = Movie('Doctor Strange', 'A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.', 'https://www.youtube.com/watch?v=HSzx-zryEgM', 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2ODA4MTM0M15BMl5BanBnXkFtZTgwNzE5OTYxMDI@._V1_SY1000_CR0,0,683,1000_AL_.jpg', '1h 55min', 'PG')

movies = [almost_christmas, arrival, shut_in, elle, love_witch, doctor_strange]

fresh_tomatoes.open_movies_page(movies)