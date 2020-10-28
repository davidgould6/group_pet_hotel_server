--Where our sql queries will be
CREATE TABLE "pets"(
"id" serial PRIMARY KEY,
"owner_id" INT NOT NULL,
"petName" VARCHAR (100) NOT NULL,
"breed" VARCHAR (100) NOT NULL,
"color" VARCHAR (100) NOT NULL,
"isCheckedIn" BOOLEAN DEFAULT false
);
CREATE TABLE "owners"(
"id" serial PRIMARY KEY,
"name" VARCHAR (100) NOT NULL
);
INSERT INTO "owners"("name") VALUES ('David'), ('Gabriel'), ('Ashley');
INSERT INTO "pets" ("owner_id", "petName", "breed", "color") 
VALUES 
('1', 'Jake', 'adorbs', 'white'), 
('2', 'Icarus', 'St. Bernard', 'brown and white'), 
('3', 'Boo', 'cat', 'greyish');