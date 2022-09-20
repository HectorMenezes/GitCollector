-- migrate:up
CREATE TABLE Provider (
    id serial primary key,
    name varchar(30)
);

CREATE TABLE User (
    id serial primary key,
    login varchar(100),
    email varcahr(100),
    twitter_username varchar(20),
    provider int,
    FOREIGN KEY (provider) REFERENCES Provider(id)
);

-- migrate:down
DROP TABLE User;
DROP TABLE Provider;
