drop table if exists emojis;
drop table if exists categories;
create table categories (
  id integer primary key autoincrement,
  emoji_name text not null,
  category text not null 
);
