create table if not exists user
(
    id        int auto_increment
        primary key,
    name      varchar(32) null,
    email     varchar(32) null,
    password  varchar(32) null,
    is_active tinyint(1)  null,
    constraint email
        unique (email)
);

create index ix_user_id
    on user (id);


