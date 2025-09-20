BEGIN;
--
-- Alter field project on deployenv
--
-- (no-op)
--
-- Alter field create_user on project
--
CREATE TABLE "new__auto_test_plt_project"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"name" varchar(200) NOT NULL,
"create_time" datetime NOT NULL,
"describe" text NULL,
"status" bool NOT NULL,
"type" integer NOT NULL,
"update_time" datetime NOT NULL,
"version" varchar(100) NOT NULL,
"create_user" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__auto_test_plt_project" ("id", "name", "create_time", "describe", "status", "type", "update_time", "version", "create_user") SELECT "id", "name", "create_time", "describe", "status", "type", "update_time", "version", "create_user_id" FROM "auto_test_plt_project";
DROP TABLE "auto_test_plt_project";
ALTER TABLE "new__auto_test_plt_project" RENAME TO "auto_test_plt_project";
CREATE INDEX "auto_test_plt_project_create_user_bf2703bb" ON "auto_test_plt_project" ("create_user");
COMMIT;
