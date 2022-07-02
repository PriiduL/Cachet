CREATE TABLE IF NOT EXISTS trips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_start TEXT,
    date_end TEXT,
    driver_id INTEGER NOT NULL,
    do_you_like INTEGER NOT NULL,
    style INTEGER NOT NULL,
    condition INTEGER NOT NULL,
    behaviour INTEGER NOT NULL,
    avg_trip_score INTEGER NOT NULL
)