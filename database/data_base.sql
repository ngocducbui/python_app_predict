-- final_project.`user` definition

CREATE DATABASE final_project

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `date-of-birth` date NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` enum('0','1') NOT NULL,
  `image` longblob,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_un` (`username`)
)
