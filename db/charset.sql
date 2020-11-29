USE akatsuki;
ALTER DATABASE akatsuki CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE posts_postimage CHANGE description description LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;
ALTER TABLE posts_postimage CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE accounts_othersinfo CHANGE bio bio LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;
ALTER TABLE accounts_othersinfo CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;