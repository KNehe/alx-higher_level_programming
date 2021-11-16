-- Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Inclding table first_table and field name
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table ALTER COLUMN name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
