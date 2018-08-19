# That's useless, only for example purpose

drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  ip text not null,
  url text not null,
  cookie tetxt not null
);
