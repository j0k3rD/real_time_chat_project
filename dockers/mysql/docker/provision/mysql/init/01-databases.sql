CREATE DATABASE IF NOT EXISTS `chat_real_time`;
CREATE DATABASE IF NOT EXISTS `user_real_time`;

GRANT ALL ON `chat_real_time`.* TO 'root'@'%';
GRANT ALL ON `user_real_time`.* TO 'root'@'%'; 