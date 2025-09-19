
BEGIN;
--
-- Create model DeployEnv
--
CREATE TABLE "auto_test_plt_deployenv"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"name" varchar(100) NOT NULL,
"hostname" varchar(100) NOT NULL,
"port" integer NOT NULL,
"status" bool NOT NULL,
"memo" text NULL,
"project_id" integer NOT NULL REFERENCES "auto_test_plt_project" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE INDEX "auto_test_plt_deployenv_project_id_9e29d08c" ON "auto_test_plt_deployenv" ("project_id");
COMMIT;
