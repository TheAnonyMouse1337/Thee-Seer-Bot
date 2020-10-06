CREATE TABLE IF NOT EXISTS userdata (
    UserId integer PRIMARY KEY,
    Infraction integer DEFAULT 0,
    Invites integer DEFAULT 0,
    Date text DEFAULT CURRENT_TIMESTAMP
);