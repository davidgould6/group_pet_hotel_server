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

SELECT "pets"."id", "pets"."petName", "pets"."breed", "pets"."color", "pets"."isCheckedIn", "owners"."name" AS "ownerName"
FROM "pets"
JOIN "owners"
ON "pets"."owner_id" = "owners"."id";

SELECT "owners"."id", "owners"."name", COUNT("pets"."owner_id")
FROM "pets"
JOIN "owners"
ON "owners"."id" = "pets"."owner_id"
GROUP BY "owners"."id";