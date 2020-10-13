
CREATE TABLE `rol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rol_UN` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1