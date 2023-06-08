-- DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS task;

-- CREATE TABLE user (
--   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
--   username VARCHAR(255),
--   user_password VARCHAR(255),
--   user_email VARCHAR(255),
--   created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
-- );

CREATE TABLE task (
  task_id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_name TEXT NOT NULL,
  task_description VARCHAR(255),
  task_status VARCHAR(255),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Run this command flask --app todo init-db after making changes here
