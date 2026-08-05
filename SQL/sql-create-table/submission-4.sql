create table videos(id int,name text,created_at date,published Boolean);

create table cities(name text,population int,country text,is_capital boolean);

-- Do not modify below this line --
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'videos';
