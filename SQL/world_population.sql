use world ;
select *from city;
select distinct country code from city limit 10;
select count(*) from city;  -- count no of rows
select * from city limit 5; -- show first rows
select* from city order by population ;  -- order ascending
select * from city order by Population desc limit 25; -- order decending 
select * from city order by CountryCode,Name;
select * from city where name like 'ak%'; -- the name srtats with akk -- start with ak
select * from city where name like '%ak';-- end with ak
select * from city where name like '%ak%'; -- inbetween ak in the name
alter table city rename to city_dup;-- rename the name of folder
alter table city_dup rename to city;
select *from city where name like "z%" order by Population desc limit 10;
select * from countrylanguage;
select count(*) from countrylanguage where IsOfficial = "F" and Language like "English"; -- like and = are sililar here  "TASK"
select * From country order by region;
select * from country where Continent="Asia" order by Region , SurfaceArea desc ;
 


