CREATE TABLE IF NOT EXISTS trips (
    id integer PRIMARY KEY,
    date_start text,
    date_end text,
    driver_id integer NOT NULL,
    do_you_like integer NOT NULL,
    style integer NOT NULL,
    condition integer NOT NULL,
    behaviour integer NOT NULL
)