DO $$ 
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'db_user') THEN
        CREATE USER db_user WITH PASSWORD 'dbpassword123';
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'db_name') THEN
        CREATE DATABASE db_name;
    END IF;
END $$;

GRANT ALL PRIVILEGES ON DATABASE db_name TO db_user;