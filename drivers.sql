CREATE TABLE IF NOT EXISTS drivers (
    id integer PRIMARY KEY,
    name text NOT NULL,
    family_name text NOT NULL,
    plate_number text NOT NULL
)