-- migrate:up
CREATE TYPE provider_type as ENUM('Github', 'Gitlab');

CREATE TABLE "user" (
    id serial primary key,
    login varchar(100),
    email varchar(100),
    twitter_username varchar(20),
    provider provider_type not null,
    query_date date not null default current_date
);

-- migrate:down
DROP TYPE provider_type
DROP TABLE "user";
