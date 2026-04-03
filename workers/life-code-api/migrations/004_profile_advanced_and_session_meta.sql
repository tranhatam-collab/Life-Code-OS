ALTER TABLE user_profiles ADD COLUMN avatar_url TEXT;
ALTER TABLE user_profiles ADD COLUMN locale TEXT;
ALTER TABLE user_profiles ADD COLUMN notification_prefs_json TEXT;

ALTER TABLE user_sessions ADD COLUMN device_label TEXT;
ALTER TABLE user_sessions ADD COLUMN ip_address TEXT;
ALTER TABLE user_sessions ADD COLUMN user_agent TEXT;
