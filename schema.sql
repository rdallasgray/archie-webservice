drop table if exists pois;
create table pois (
       id integer primary key autoincrement,
       name string not null,
       description string not null,
       thumbnail string,
       hi_res_image_url string,
       co_ordinates string not null      
);