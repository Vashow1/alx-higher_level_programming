-- script that creates and gives privileges to the MySQL server user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON IF EXISTS `hbtn_0d_2` TO 'user_0d_2'@'localhost';
