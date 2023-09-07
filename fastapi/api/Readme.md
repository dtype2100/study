# docker mysql
1. docker run -p 3307:3306 -e MYSQL_ROOT_PASSWORD=todos -e MYSQL_DATABASE=todos -d -v todos:/db --name todos mysql:8.0
2. docker ps
3. docker logs todos
4. docker volume ls
 
## MySQL 접속
1. docker exec -it todos bash 
2. mysql -u root -p 
 

## SQL
1. SHOW databases;
2. USE todos;
3. CREATE TABLE todo(
    id INT NOT NULL AUTO_INCREMENT,
    contents VARCHAR(256) NOT NULL,
    is_done BOOLEAN NOT NULL,
    PRIMARY KEY (id)
);
4. INSERT INTO todo (contents, is_done) VALUES ("FastAPI Section 0", true);
5. SELECT * FROM todo;