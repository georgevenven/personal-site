DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS projects;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TEXT,
    title TEXT NOT NULL,
    readtime INTEGER,
    content TEXT NOT NULL,
    previewText TEXT,
    topic TEXT NOT NULL
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    previewText TEXT,
    content TEXT NOT NULL,
    topic TEXT NOT NULL
);
