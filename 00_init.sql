CREATE TABLE currencies (
    id SERIAL PRIMARY KEY,
    currency VARCHAR(255),
    date_ TIMESTAMP,
    price FLOAT
);