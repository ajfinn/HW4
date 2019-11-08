USE f19_msci3300;
DROP TABLE IF EXISTS finn_moviesApp;
CREATE TABLE finn_moviesApp(
movie_id int(11) NOT NULL AUTO_INCREMENT,
movie_name varchar(255),
PRIMARY KEY (movie_id)
)ENGINE=InnoDB AUTO_INCREMENT=1;

INSERT INTO finn_moviesApp(movie_name)
VALUES ('Akira'),
	('Joker'),
    ('Mandy'),
    ('Pulp Fiction'),
    ('Shrek'),
    ('Shrek 2')
