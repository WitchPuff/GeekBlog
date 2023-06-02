-- Active: 1685674652344@@127.0.0.1@3306@blog
-- DROP TABLE kudos;
-- DROP TABLE comment;
-- DROP TABLE article;
-- DROP TABLE profile;
-- DROP TABLE auth;
-- DROP TABLE constant;
CREATE TABLE constant
	(
		category 	VARCHAR(50) UNIQUE NOT NULL
	);
CREATE TABLE auth
	(
		username	VARCHAR(15) UNIQUE NOT NULL,
		passwd		VARCHAR(15) NOT NULL,
		PRIMARY KEY (username, passwd)
	);

CREATE TABLE article
	(
		id			BIGINT PRIMARY KEY AUTO_INCREMENT,
		username	VARCHAR(15) NOT NULL,
		title		VARCHAR(20) NOT NULL,
		category	VARCHAR(50) NOT NULL,
		tags		VARCHAR(200),
		summary		VARCHAR(200),
		body		TEXT NOT NULL,
		post_date	DATETIME NOT NULL,
		last_update	DATETIME NOT NULL,
		FOREIGN KEY (username) REFERENCES auth (username) 
			ON DELETE CASCADE,
		FOREIGN KEY (category) REFERENCES constant (category)
			ON DELETE CASCADE
	 ) AUTO_INCREMENT = 0;

CREATE TABLE profile
	(	
		username	VARCHAR(15) PRIMARY KEY,
		sign		VARCHAR(50),
		pic			LONGBLOB,
		github		VARCHAR(50),
		FOREIGN KEY (username) REFERENCES auth (username)
			ON DELETE CASCADE
	);
INSERT INTO auth VALUES ('root','test');

INSERT INTO profile (username) VALUES ('root');
CREATE TABLE comment
	(
		id				BIGINT NOT NULL,
		username		VARCHAR(15) NOT NULL,
		content			VARCHAR(500) NOT NULL,
		comment_time	DATETIME NOT NULL,
		PRIMARY KEY (id, username, content, comment_time),
		FOREIGN KEY (id) REFERENCES article (id)
			ON DELETE CASCADE,
		FOREIGN KEY (username) REFERENCES auth (username)
			ON DELETE CASCADE
	);

CREATE TABLE kudos
	(
		id			BIGINT,
		username	VARCHAR(15) NOT NULL,
		PRIMARY KEY (id, username),
		FOREIGN KEY (id) REFERENCES article (id)
			ON DELETE CASCADE,
		FOREIGN KEY (username) REFERENCES auth (username)
			ON DELETE CASCADE
	);