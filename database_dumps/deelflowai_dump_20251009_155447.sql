-- DeelFlowAI Database Dump
-- Generated: 2025-10-09T15:54:47.294989
-- Source: db.sqlite3
-- Database: SQLite

-- Table: django_migrations
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1, 'contenttypes', '0001_initial', '2025-08-25 10:22:53.773375');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (2, 'auth', '0001_initial', '2025-08-25 10:22:53.869133');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (3, 'admin', '0001_initial', '2025-08-25 10:22:53.949764');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2025-08-25 10:22:54.007108');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2025-08-25 10:22:54.056378');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2025-08-25 10:22:54.113436');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2025-08-25 10:22:54.166238');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (8, 'auth', '0003_alter_user_email_max_length', '2025-08-25 10:22:54.221789');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (9, 'auth', '0004_alter_user_username_opts', '2025-08-25 10:22:54.264321');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (10, 'auth', '0005_alter_user_last_login_null', '2025-08-25 10:22:54.314825');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (11, 'auth', '0006_require_contenttypes_0002', '2025-08-25 10:22:54.349913');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2025-08-25 10:22:54.400138');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (13, 'auth', '0008_alter_user_username_max_length', '2025-08-25 10:22:54.449801');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2025-08-25 10:22:54.512259');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (15, 'auth', '0010_alter_group_name_max_length', '2025-08-25 10:22:54.552126');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (16, 'auth', '0011_update_proxy_permissions', '2025-08-25 10:22:54.595361');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2025-08-25 10:22:54.646803');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (18, 'deelflow', '0001_initial', '2025-08-25 10:22:54.688324');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (19, 'sessions', '0001_initial', '2025-08-25 10:22:54.762205');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (20, 'deelflow', '0002_alter_businessmetrics_ai_conversations', '2025-08-25 10:40:44.796278');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (21, 'deelflow', '0003_organization_user', '2025-09-04 05:40:38.547409');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (22, 'deelflow', '0004_user_password', '2025-09-04 06:23:15.660951');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (23, 'deelflow', '0005_permission_role', '2025-09-08 03:45:09.028500');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (24, 'deelflow', '0006_propertyaianalysis', '2025-09-09 16:13:33.582019');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (25, 'deelflow', '0007_visionanalysismetrics_voiceaicallmetrics', '2025-09-09 17:57:20.113091');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (26, 'deelflow', '0008_blockchaintxnmetrics_nlpprocessingmetrics', '2025-09-09 18:00:48.949777');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (27, 'deelflow', '0009_campaign_campaignperformance_campaignpropertystats_and_more', '2025-09-10 07:47:45.084729');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (28, 'deelflow', '0010_discoveredlead', '2025-09-15 06:43:04.655890');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (29, 'deelflow', '0011_outreachcampaign_campaignrecipient', '2025-09-15 06:48:11.364081');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (30, 'deelflow', '0012_remove_campaign_end_date_remove_campaign_start_date_and_more', '2025-09-22 08:36:28.724291');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (31, 'deelflow', '0013_alter_lead_options_lead_address_lead_city_lead_email_and_more', '2025-10-08 10:17:39.846259');

-- Table: sqlite_sequence
DROP TABLE IF EXISTS `sqlite_sequence`;
CREATE TABLE sqlite_sequence(name,seq);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('django_migrations', 31);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('django_admin_log', 21);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('django_content_type', 33);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('auth_permission', 132);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('auth_group', 0);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('auth_user', 5);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_activityfeed', 2);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_businessmetrics', 1);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_compliancestatus', 1);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_historicalmetrics', 1);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_organization', 7);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_user', 8);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_role', 4);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_propertyaianalysis', 1);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_campaign', 3);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_permission', 6);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_role_permissions', 2);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_lead', 4);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_deal', 3);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_property', 5);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_aianalysis', 3);
INSERT INTO `sqlite_sequence` (`name`, `seq`) VALUES ('deelflow_dealmilestone', 5);

-- Table: auth_group_permissions
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Table: auth_user_groups
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Table: auth_user_user_permissions
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Table: django_admin_log
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (1, '1', 'Malware by 0 at 2025-08-25 10:35:43.953288+00:00', 1, '[{"added": {}}]', 7, 1, '2025-08-25 10:35:43.959104');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (2, '2', 'Ransomware by 1 at 2025-08-25 10:37:21.789413+00:00', 1, '[{"added": {}}]', 7, 1, '2025-08-25 10:37:21.792926');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (3, '1', 'Metrics on 2025-08-25', 1, '[{"added": {}}]', 8, 1, '2025-08-25 10:40:57.786759');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (4, '1', 'Metrics on 2025-08-25', 2, '[]', 8, 1, '2025-08-25 10:41:36.298803');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (5, '1', 'Compliance 96% (89.55%)', 1, '[{"added": {}}]', 9, 1, '2025-08-25 10:44:22.718149');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (6, '1', 'new_signups - 2025-08-25', 1, '[{"added": {}}]', 10, 1, '2025-08-25 10:53:10.415313');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (7, '1', 'new signups - 2025-08-25', 2, '[{"changed": {"fields": ["Metric type"]}}]', 10, 1, '2025-08-25 10:53:20.875103');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (8, '2', 'arpan58', 1, '[{"added": {}}]', 4, 1, '2025-08-29 13:05:33.588794');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (9, '2', 'arpan58', 2, '[{"changed": {"fields": ["First name", "Last name"]}}]', 4, 1, '2025-08-29 13:05:55.986778');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (10, '2', 'admin admin (arpansarkar@gmail.com)', 3, '', 11, 1, '2025-09-04 06:24:08.760957');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (11, '2', 'test admin org', 3, '', 12, 1, '2025-09-04 06:24:17.506585');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (12, '1', 'Metrics on 2025-08-25', 2, '[{"changed": {"fields": ["Total revenue"]}}]', 8, 5, '2025-09-15 16:57:50.866630');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (13, '7', 'Abhishake Saha (abhishake@gmail.com)', 1, '[{"added": {}}]', 11, 5, '2025-09-15 17:02:58.990986');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (14, '1', 'test', 1, '[{"added": {}}]', 25, 5, '2025-09-15 18:01:00.293076');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (15, '1', 'Lead 1 - qualified', 1, '[{"added": {}}]', 24, 5, '2025-09-15 18:01:05.188119');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (16, '1', 'Manage Roles', 1, '[{"added": {}}]', 14, 1, '2025-09-22 10:43:49.721028');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (17, '2', 'Manage Clients', 1, '[{"added": {}}]', 14, 1, '2025-09-22 10:44:11.835561');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (18, '3', 'Manage Campaigns', 1, '[{"added": {}}]', 14, 1, '2025-09-22 10:44:35.705178');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (19, '4', 'Manage Organization', 1, '[{"added": {}}]', 14, 1, '2025-09-22 10:45:05.205469');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (20, '5', 'Manage Leads', 1, '[{"added": {}}]', 14, 1, '2025-09-22 10:45:21.956173');
INSERT INTO `django_admin_log` (`id`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`, `action_time`) VALUES (21, '6', 'Manage Properties', 1, '[{"added": {}}]', 14, 1, '2025-09-22 10:45:36.999335');

-- Table: django_content_type
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (7, 'deelflow', 'activityfeed');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (8, 'deelflow', 'businessmetrics');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (9, 'deelflow', 'compliancestatus');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (10, 'deelflow', 'historicalmetrics');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (11, 'deelflow', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (12, 'deelflow', 'organization');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (13, 'deelflow', 'role');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (14, 'deelflow', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (15, 'deelflow', 'propertyaianalysis');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (16, 'deelflow', 'visionanalysismetrics');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (17, 'deelflow', 'voiceaicallmetrics');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (18, 'deelflow', 'blockchaintxnmetrics');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (19, 'deelflow', 'nlpprocessingmetrics');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (20, 'deelflow', 'campaignperformance');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (21, 'deelflow', 'campaignpropertystats');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (22, 'deelflow', 'channel');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (23, 'deelflow', 'channelresponserate');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (24, 'deelflow', 'lead');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (25, 'deelflow', 'campaign');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (26, 'deelflow', 'discoveredlead');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (27, 'deelflow', 'outreachcampaign');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (28, 'deelflow', 'campaignrecipient');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (29, 'deelflow', 'deal');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (30, 'deelflow', 'dealmilestone');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (31, 'deelflow', 'property');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (32, 'deelflow', 'aianalysis');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (33, 'deelflow', 'savedproperty');

-- Table: auth_permission
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (1, 1, 'add_logentry', 'Can add log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (2, 1, 'change_logentry', 'Can change log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (3, 1, 'delete_logentry', 'Can delete log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (4, 1, 'view_logentry', 'Can view log entry');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (5, 2, 'add_permission', 'Can add permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (6, 2, 'change_permission', 'Can change permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (7, 2, 'delete_permission', 'Can delete permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (8, 2, 'view_permission', 'Can view permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (9, 3, 'add_group', 'Can add group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (10, 3, 'change_group', 'Can change group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (11, 3, 'delete_group', 'Can delete group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (12, 3, 'view_group', 'Can view group');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (13, 4, 'add_user', 'Can add user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (14, 4, 'change_user', 'Can change user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (15, 4, 'delete_user', 'Can delete user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (16, 4, 'view_user', 'Can view user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (17, 5, 'add_contenttype', 'Can add content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (18, 5, 'change_contenttype', 'Can change content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (19, 5, 'delete_contenttype', 'Can delete content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (20, 5, 'view_contenttype', 'Can view content type');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (21, 6, 'add_session', 'Can add session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (22, 6, 'change_session', 'Can change session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (23, 6, 'delete_session', 'Can delete session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (24, 6, 'view_session', 'Can view session');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (25, 7, 'add_activityfeed', 'Can add activity feed');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (26, 7, 'change_activityfeed', 'Can change activity feed');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (27, 7, 'delete_activityfeed', 'Can delete activity feed');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (28, 7, 'view_activityfeed', 'Can view activity feed');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (29, 8, 'add_businessmetrics', 'Can add business metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (30, 8, 'change_businessmetrics', 'Can change business metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (31, 8, 'delete_businessmetrics', 'Can delete business metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (32, 8, 'view_businessmetrics', 'Can view business metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (33, 9, 'add_compliancestatus', 'Can add compliance status');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (34, 9, 'change_compliancestatus', 'Can change compliance status');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (35, 9, 'delete_compliancestatus', 'Can delete compliance status');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (36, 9, 'view_compliancestatus', 'Can view compliance status');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (37, 10, 'add_historicalmetrics', 'Can add historical metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (38, 10, 'change_historicalmetrics', 'Can change historical metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (39, 10, 'delete_historicalmetrics', 'Can delete historical metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (40, 10, 'view_historicalmetrics', 'Can view historical metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (41, 11, 'add_user', 'Can add user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (42, 11, 'change_user', 'Can change user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (43, 11, 'delete_user', 'Can delete user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (44, 11, 'view_user', 'Can view user');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (45, 12, 'add_organization', 'Can add organization');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (46, 12, 'change_organization', 'Can change organization');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (47, 12, 'delete_organization', 'Can delete organization');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (48, 12, 'view_organization', 'Can view organization');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (49, 13, 'add_role', 'Can add role');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (50, 13, 'change_role', 'Can change role');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (51, 13, 'delete_role', 'Can delete role');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (52, 13, 'view_role', 'Can view role');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (53, 14, 'add_permission', 'Can add permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (54, 14, 'change_permission', 'Can change permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (55, 14, 'delete_permission', 'Can delete permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (56, 14, 'view_permission', 'Can view permission');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (57, 15, 'add_propertyaianalysis', 'Can add property ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (58, 15, 'change_propertyaianalysis', 'Can change property ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (59, 15, 'delete_propertyaianalysis', 'Can delete property ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (60, 15, 'view_propertyaianalysis', 'Can view property ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (61, 16, 'add_visionanalysismetrics', 'Can add vision analysis metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (62, 16, 'change_visionanalysismetrics', 'Can change vision analysis metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (63, 16, 'delete_visionanalysismetrics', 'Can delete vision analysis metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (64, 16, 'view_visionanalysismetrics', 'Can view vision analysis metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (65, 17, 'add_voiceaicallmetrics', 'Can add voice ai call metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (66, 17, 'change_voiceaicallmetrics', 'Can change voice ai call metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (67, 17, 'delete_voiceaicallmetrics', 'Can delete voice ai call metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (68, 17, 'view_voiceaicallmetrics', 'Can view voice ai call metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (69, 18, 'add_blockchaintxnmetrics', 'Can add blockchain txn metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (70, 18, 'change_blockchaintxnmetrics', 'Can change blockchain txn metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (71, 18, 'delete_blockchaintxnmetrics', 'Can delete blockchain txn metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (72, 18, 'view_blockchaintxnmetrics', 'Can view blockchain txn metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (73, 19, 'add_nlpprocessingmetrics', 'Can add nlp processing metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (74, 19, 'change_nlpprocessingmetrics', 'Can change nlp processing metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (75, 19, 'delete_nlpprocessingmetrics', 'Can delete nlp processing metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (76, 19, 'view_nlpprocessingmetrics', 'Can view nlp processing metrics');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (77, 20, 'add_campaignperformance', 'Can add campaign performance');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (78, 20, 'change_campaignperformance', 'Can change campaign performance');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (79, 20, 'delete_campaignperformance', 'Can delete campaign performance');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (80, 20, 'view_campaignperformance', 'Can view campaign performance');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (81, 21, 'add_campaignpropertystats', 'Can add campaign property stats');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (82, 21, 'change_campaignpropertystats', 'Can change campaign property stats');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (83, 21, 'delete_campaignpropertystats', 'Can delete campaign property stats');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (84, 21, 'view_campaignpropertystats', 'Can view campaign property stats');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (85, 22, 'add_channel', 'Can add channel');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (86, 22, 'change_channel', 'Can change channel');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (87, 22, 'delete_channel', 'Can delete channel');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (88, 22, 'view_channel', 'Can view channel');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (89, 23, 'add_channelresponserate', 'Can add channel response rate');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (90, 23, 'change_channelresponserate', 'Can change channel response rate');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (91, 23, 'delete_channelresponserate', 'Can delete channel response rate');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (92, 23, 'view_channelresponserate', 'Can view channel response rate');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (93, 24, 'add_lead', 'Can add lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (94, 24, 'change_lead', 'Can change lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (95, 24, 'delete_lead', 'Can delete lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (96, 24, 'view_lead', 'Can view lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (97, 25, 'add_campaign', 'Can add campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (98, 25, 'change_campaign', 'Can change campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (99, 25, 'delete_campaign', 'Can delete campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (100, 25, 'view_campaign', 'Can view campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (101, 26, 'add_discoveredlead', 'Can add discovered lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (102, 26, 'change_discoveredlead', 'Can change discovered lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (103, 26, 'delete_discoveredlead', 'Can delete discovered lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (104, 26, 'view_discoveredlead', 'Can view discovered lead');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (105, 27, 'add_outreachcampaign', 'Can add outreach campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (106, 27, 'change_outreachcampaign', 'Can change outreach campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (107, 27, 'delete_outreachcampaign', 'Can delete outreach campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (108, 27, 'view_outreachcampaign', 'Can view outreach campaign');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (109, 28, 'add_campaignrecipient', 'Can add campaign recipient');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (110, 28, 'change_campaignrecipient', 'Can change campaign recipient');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (111, 28, 'delete_campaignrecipient', 'Can delete campaign recipient');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (112, 28, 'view_campaignrecipient', 'Can view campaign recipient');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (113, 29, 'add_deal', 'Can add deal');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (114, 29, 'change_deal', 'Can change deal');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (115, 29, 'delete_deal', 'Can delete deal');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (116, 29, 'view_deal', 'Can view deal');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (117, 30, 'add_dealmilestone', 'Can add deal milestone');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (118, 30, 'change_dealmilestone', 'Can change deal milestone');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (119, 30, 'delete_dealmilestone', 'Can delete deal milestone');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (120, 30, 'view_dealmilestone', 'Can view deal milestone');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (121, 31, 'add_property', 'Can add property');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (122, 31, 'change_property', 'Can change property');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (123, 31, 'delete_property', 'Can delete property');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (124, 31, 'view_property', 'Can view property');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (125, 32, 'add_aianalysis', 'Can add ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (126, 32, 'change_aianalysis', 'Can change ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (127, 32, 'delete_aianalysis', 'Can delete ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (128, 32, 'view_aianalysis', 'Can view ai analysis');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (129, 33, 'add_savedproperty', 'Can add saved property');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (130, 33, 'change_savedproperty', 'Can change saved property');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (131, 33, 'delete_savedproperty', 'Can delete saved property');
INSERT INTO `auth_permission` (`id`, `content_type_id`, `codename`, `name`) VALUES (132, 33, 'view_savedproperty', 'Can view saved property');

-- Table: auth_group
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);

-- Table: auth_user
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `first_name`) VALUES (1, 'pbkdf2_sha256$600000$Ag2xbqCPj7xNFQFzeXpq1l$eB4Fk87xnzspQa0ntRcL7cieds5V72ft5hMuOYy6vO0=', '2025-09-22 08:56:06.701174', 1, 'deelflow2025', '', 'arpan.s@vycentra.com', 1, 1, '2025-08-25 10:25:13.899988', '');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `first_name`) VALUES (2, 'pbkdf2_sha256$600000$NIihh0XYakej9bOIkF3zzj$S+mM7uEJd3TF/zLkRqR98uEIPMZga0mYEjyhb/kdmJ0=', NULL, 0, 'arpan58', 'Sarkar', '', 0, 1, '2025-08-29 13:05:33', 'Arpan');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `first_name`) VALUES (3, 'pbkdf2_sha256$600000$DtL8ZdRHLNV5JJ0dpSJTMv$ohPW0QWyLoxcDc1WGOfoI3kWn+ZuwG4H9DGsLSNhH0Q=', NULL, 1, 'arpans05', '', 'arpansarkar@vrxlab.com', 1, 1, '2025-09-01 11:34:31.402456', '');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `first_name`) VALUES (4, 'pbkdf2_sha256$600000$r3HfqhIIh8LKzX7xClZGOg$SqVpMFpttxBrTr9gZCSR1/+XSHpCSeFnwcwSS2wzp/Y=', NULL, 1, 'arpans', '', 'arpansarkar@vrxlab.com', 1, 1, '2025-09-01 11:44:32.592322', '');
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `first_name`) VALUES (5, 'pbkdf2_sha256$600000$jtwiPbzQflCI8oRpqepuOS$QpDxhzoaAFW8C6J6/mXF+MR0FtEKkodKQxP/C7Es15E=', '2025-09-15 16:57:27.527262', 1, 'Anirudha007', '', 'anirudha.das2551995@gmail.com', 1, 1, '2025-09-09 14:19:09.017706', '');

-- Table: deelflow_activityfeed
DROP TABLE IF EXISTS `deelflow_activityfeed`;
CREATE TABLE "deelflow_activityfeed" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL, "action_type" varchar(100) NOT NULL, "description" text NOT NULL, "timestamp" datetime NOT NULL);
INSERT INTO `deelflow_activityfeed` (`id`, `user_id`, `action_type`, `description`, `timestamp`) VALUES (1, 0, 'Malware', 'Rachel W., David M. activities', '2025-08-25 10:35:43.953288');
INSERT INTO `deelflow_activityfeed` (`id`, `user_id`, `action_type`, `description`, `timestamp`) VALUES (2, 1, 'Ransomware', 'Arpan S., Anirudha M. activities', '2025-08-25 10:37:21.789413');

-- Table: deelflow_compliancestatus
DROP TABLE IF EXISTS `deelflow_compliancestatus`;
CREATE TABLE "deelflow_compliancestatus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "compliance_percent" decimal NOT NULL, "audit_trail" text NOT NULL, "system_health" varchar(50) NOT NULL, "updated_at" datetime NOT NULL);
INSERT INTO `deelflow_compliancestatus` (`id`, `compliance_percent`, `audit_trail`, `system_health`, `updated_at`) VALUES (1, 96, 'ADMIN: Login successful
JANE.DOE: Login failed (wrong password)
KYC: Customer ID #102 verified
SYSTEM: Health status updated to Healthy', '89.55%', '2025-08-25 10:44:22.712762');

-- Table: deelflow_historicalmetrics
DROP TABLE IF EXISTS `deelflow_historicalmetrics`;
CREATE TABLE "deelflow_historicalmetrics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "metric_type" varchar(50) NOT NULL, "metric_value" decimal NOT NULL, "record_date" date NOT NULL);
INSERT INTO `deelflow_historicalmetrics` (`id`, `metric_type`, `metric_value`, `record_date`) VALUES (1, 'new signups', 4508, '2025-08-25');

-- Table: django_session
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('bpqeyia61yrxo8hvq8husv1cyjorfcbj', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1uqUP7:igABz19hoWoJVONB_e7mv_PMi7bq7YFBAHEae6LJl74', '2025-09-08 10:26:21.632011');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('j0p9p7nqcs9lxld7kytlw5wlmh2eonxo', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1utJwk:8RlFYrm8ZAMaCHmX6mAuOH_GAJmy7ului5s9vgopz_s', '2025-09-16 05:52:46.010661');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('h3ug9hstf5s3rkzxjg45j1mqsl3mot89', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1utMlk:m-BXlor8CMLUOo9aD9ziFOsRlM_o9Bu41m3CnLGGnBM', '2025-09-16 08:53:36.976394');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('i2hjcpntrof7xpbash9o3n5gr08xtyta', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1utpMI:DuLkCMRVs0WAp2I-xoXfSGMQsiGxcM1DbS_JG4G2_Eg', '2025-09-17 15:25:14.596410');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('aaznsdw2d8l3p7h29x8gf9lek6xz8gg8', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1uu2nx:LwyGIB3Wt1Z14ZE9Ntn7li1zQMO69SmxdvfmRNKdzYc', '2025-09-18 05:46:41.827382');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('6zyxpyurvvc6nx8troiks0mp3pbdoflu', '.eJxVjEEOwiAQRe_C2pDCQFtcuu8ZyMAMUjWQlHZlvLtt0oVu_3vvv4XHbc1-a7z4mcRVWHH53QLGJ5cD0APLvcpYy7rMQR6KPGmTUyV-3U737yBjy3udnDJWJ6vJBgygohvAUa-J0cUECTQEy5pHSggDs-5NBwZVp8a9MkZ8vu-bN9A:1uvzCG:2s6yKwakfmsWIx99ZBA_-NNM-OaDX9bV164j6VkxcAc', '2025-09-23 14:19:48.700282');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('45c2pnzid3ybttfod681bffppayux2lj', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1uwFWP:0m7R_VrcOq_hK3R6eqSSgLoVTGHEiyvkZXPvS30yGtw', '2025-09-24 07:45:41.425061');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('zqlii61ke52szjmfsze8qtzo7kdtttyo', '.eJxVjEEOwiAQRe_C2pDCQFtcuu8ZyMAMUjWQlHZlvLtt0oVu_3vvv4XHbc1-a7z4mcRVWHH53QLGJ5cD0APLvcpYy7rMQR6KPGmTUyV-3U737yBjy3udnDJWJ6vJBgygohvAUa-J0cUECTQEy5pHSggDs-5NBwZVp8a9MkZ8vu-bN9A:1uy23U:iZQ28XU4mySktQi6mZS9O14uzVQ7oQ0sE29Xcee9Vfc', '2025-09-29 05:47:12.319860');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('4oauyv7oafw8d1sp3f5hvqrbzjxvs53j', '.eJxVjEEOwiAQRe_C2pDCQFtcuu8ZyMAMUjWQlHZlvLtt0oVu_3vvv4XHbc1-a7z4mcRVWHH53QLGJ5cD0APLvcpYy7rMQR6KPGmTUyV-3U737yBjy3udnDJWJ6vJBgygohvAUa-J0cUECTQEy5pHSggDs-5NBwZVp8a9MkZ8vu-bN9A:1uyCW7:X-ho9Jgapve9JnnsiNO0dMvPqQc-D44xIE0LLeKAyWs', '2025-09-29 16:57:27.533310');
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES ('pkpurgf573bpv6t39k83hlgnsis77srs', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMJDv9bhjTg9oO8j22W-ept3WZke8KP-jg157peTncv4MaR_3W3upsEI3Qk5KTLFiiEVjQAYGTOYEkKyYAIklOKBLeO6u0Tq5EDwDs_QHW0TdM:1v0cL8:GtRoNHwviBDqtADk-y4qs6-f4olTM1SJEGYu0VQH6RI', '2025-10-06 08:56:06.738158');

-- Table: deelflow_businessmetrics
DROP TABLE IF EXISTS `deelflow_businessmetrics`;
CREATE TABLE "deelflow_businessmetrics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_revenue" decimal NOT NULL, "active_users" integer NOT NULL, "properties_listed" integer NOT NULL, "total_deals" integer NOT NULL, "monthly_profit" decimal NOT NULL, "voice_calls_count" integer NOT NULL, "report_date" date NOT NULL, "ai_conversations" decimal NOT NULL);
INSERT INTO `deelflow_businessmetrics` (`id`, `total_revenue`, `active_users`, `properties_listed`, `total_deals`, `monthly_profit`, `voice_calls_count`, `report_date`, `ai_conversations`) VALUES (1, 4.35, 14238, 3847, 47, 127500, 89, '2025-08-25', 48.2);

-- Table: deelflow_organization
DROP TABLE IF EXISTS `deelflow_organization`;
CREATE TABLE "deelflow_organization" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "uuid" char(32) NOT NULL UNIQUE, "name" varchar(255) NOT NULL, "slug" varchar(255) NOT NULL UNIQUE, "subscription_status" varchar(50) NOT NULL, "updated_at" datetime NOT NULL, "created_at" datetime NOT NULL);
INSERT INTO `deelflow_organization` (`id`, `uuid`, `name`, `slug`, `subscription_status`, `updated_at`, `created_at`) VALUES (1, 'bdc653918f284fbf81f792414f4fca33', 'test admin org', 'test-admin-org', 'new', '2025-09-04 06:05:36.501889', '2025-09-04 06:05:36.501889');
INSERT INTO `deelflow_organization` (`id`, `uuid`, `name`, `slug`, `subscription_status`, `updated_at`, `created_at`) VALUES (3, '0d24147a168d4426bf1fd7c3b1f427b0', 'test admin org', 'test-arpan-org', 'new', '2025-09-04 06:26:03.339160', '2025-09-04 06:26:03.339160');
INSERT INTO `deelflow_organization` (`id`, `uuid`, `name`, `slug`, `subscription_status`, `updated_at`, `created_at`) VALUES (4, '9f287ac6330c42519fbe5c3b036a5f27', 'Wipro', 'Wipro', 'new', '2025-09-09 14:29:48.951318', '2025-09-09 14:29:48.951318');
INSERT INTO `deelflow_organization` (`id`, `uuid`, `name`, `slug`, `subscription_status`, `updated_at`, `created_at`) VALUES (5, '2c43265273d34ac3b2383c73679fe4e5', 'goodcausesolutions', 'goodcausesolutions', 'new', '2025-09-15 05:42:17.101117', '2025-09-15 05:42:17.101117');
INSERT INTO `deelflow_organization` (`id`, `uuid`, `name`, `slug`, `subscription_status`, `updated_at`, `created_at`) VALUES (6, '9b5b921a80b14a6292a797fde910a288', 'vcentra', 'vcentra', 'new', '2025-09-15 16:54:24.519953', '2025-09-15 16:54:24.519953');
INSERT INTO `deelflow_organization` (`id`, `uuid`, `name`, `slug`, `subscription_status`, `updated_at`, `created_at`) VALUES (7, '9634f6cc68924e83a563dca8c0763e62', 'test super admin org', 'super_admin-garth-org', 'new', '2025-09-22 08:56:38.806026', '2025-09-22 08:56:38.806026');

-- Table: deelflow_user
DROP TABLE IF EXISTS `deelflow_user`;
CREATE TABLE "deelflow_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "uuid" char(32) NOT NULL UNIQUE, "email" varchar(254) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "phone" varchar(20) NULL, "role" varchar(50) NOT NULL, "level" integer NOT NULL, "points" integer NOT NULL, "is_verified" bool NOT NULL, "is_active" bool NOT NULL, "stripe_customer_id" varchar(100) NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "organization_id" integer NOT NULL REFERENCES "deelflow_organization" ("id") DEFERRABLE INITIALLY DEFERRED, "password" varchar(255) NOT NULL);
INSERT INTO `deelflow_user` (`id`, `uuid`, `email`, `first_name`, `last_name`, `phone`, `role`, `level`, `points`, `is_verified`, `is_active`, `stripe_customer_id`, `created_at`, `updated_at`, `organization_id`, `password`) VALUES (1, 'bbd013ae86224521bf064d8a7aacadcf', 'admin@gmail.com', 'admin', 'admin', '1234567890', 'admin', 1, 0, 0, 1, 'cus_SrKt16siewODxX', '2025-09-04 06:05:36.941160', '2025-09-04 06:05:36.941160', 1, '1992');
INSERT INTO `deelflow_user` (`id`, `uuid`, `email`, `first_name`, `last_name`, `phone`, `role`, `level`, `points`, `is_verified`, `is_active`, `stripe_customer_id`, `created_at`, `updated_at`, `organization_id`, `password`) VALUES (3, '42231c5f2e694d4abb64e4f63749a64f', 'arpansarkar@gmail.com', 'admin', 'admin', '1234567890', 'admin', 1, 0, 0, 1, 'cus_SrKt16siewODxX', '2025-09-04 06:26:03.776744', '2025-09-04 06:26:03.776744', 3, 'pbkdf2_sha256$600000$LJ9cZHmHEt5wvBvlQN2TdY$UwFRH0ZBub3GxqrCbycBJSdrx6K6un/23x1xXfDuCkE=');
INSERT INTO `deelflow_user` (`id`, `uuid`, `email`, `first_name`, `last_name`, `phone`, `role`, `level`, `points`, `is_verified`, `is_active`, `stripe_customer_id`, `created_at`, `updated_at`, `organization_id`, `password`) VALUES (4, '1beddf3f43814d958f944865020050c5', 'bappa.anirudha@gmail.com', 'Anirudha2', 'Das', '7908934723', 'staff', 1, 0, 0, 1, NULL, '2025-09-09 14:29:48.961001', '2025-09-09 14:29:48.961001', 4, 'pbkdf2_sha256$600000$Mcbep4mf88tlAqhAM8o3bw$PUicaWhU5dxcjJZW5EtE4fFZ884XSi1tzCjLIBEZps8=');
INSERT INTO `deelflow_user` (`id`, `uuid`, `email`, `first_name`, `last_name`, `phone`, `role`, `level`, `points`, `is_verified`, `is_active`, `stripe_customer_id`, `created_at`, `updated_at`, `organization_id`, `password`) VALUES (5, '9564a304de5f4bb6bee8954e52447c4b', 'tridha@gmail.com', 'Tridha', 'Das', '8845678334', 'staff', 1, 0, 0, 1, NULL, '2025-09-15 05:42:17.122282', '2025-09-15 05:42:17.122282', 5, 'pbkdf2_sha256$600000$dPQ7dzdFf6CiBRKHOILfpX$O1UvdXlCj/rZGBPT5eRBEiyKI7E8TCTW6NTpC1d8Rhs=');
INSERT INTO `deelflow_user` (`id`, `uuid`, `email`, `first_name`, `last_name`, `phone`, `role`, `level`, `points`, `is_verified`, `is_active`, `stripe_customer_id`, `created_at`, `updated_at`, `organization_id`, `password`) VALUES (6, 'b239500f777c49c198746fc937484b30', 'info@vcentra.com', 'clive', 'garth', '9800000000', 'staff', 1, 0, 0, 1, NULL, '2025-09-15 16:54:24.528757', '2025-09-15 16:54:24.528757', 6, 'pbkdf2_sha256$600000$SrnYwCyPFfMdcn1NNOVYNl$AJ+ZSp0Jv4sX1ymz4BL9Wc6FEREs4+qZaNNRgQqHN4A=');
INSERT INTO `deelflow_user` (`id`, `uuid`, `email`, `first_name`, `last_name`, `phone`, `role`, `level`, `points`, `is_verified`, `is_active`, `stripe_customer_id`, `created_at`, `updated_at`, `organization_id`, `password`) VALUES (7, 'c48875a271714736b742c602df6816f9', 'abhishake@gmail.com', 'Abhishake', 'Saha', '09800000000', 'user', 1, 0, 0, 1, NULL, '2025-09-15 17:02:58.987050', '2025-09-15 17:02:58.987050', 4, 'vcentra@123');
INSERT INTO `deelflow_user` (`id`, `uuid`, `email`, `first_name`, `last_name`, `phone`, `role`, `level`, `points`, `is_verified`, `is_active`, `stripe_customer_id`, `created_at`, `updated_at`, `organization_id`, `password`) VALUES (8, '2bde730d8b054f1da452d76d752fbc04', 'garthsmith@vycentra.com', 'Garth', 'Smith', '1234567890', 'super admin', 1, 0, 0, 1, 'cus_SrKt16siewODxX', '2025-09-22 08:56:39.243184', '2025-09-22 08:56:39.243184', 7, 'pbkdf2_sha256$600000$0lrQSIWrkzhc8C2ZM4cSdR$h6thQL2GiUOZv/xwKsdX4EZKEpwgd6b+bepyD4DQJKs=');

-- Table: deelflow_permission
DROP TABLE IF EXISTS `deelflow_permission`;
CREATE TABLE "deelflow_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE, "label" varchar(150) NOT NULL);
INSERT INTO `deelflow_permission` (`id`, `name`, `label`) VALUES (1, 'manage_roles', 'Manage Roles');
INSERT INTO `deelflow_permission` (`id`, `name`, `label`) VALUES (2, 'manage_client', 'Manage Clients');
INSERT INTO `deelflow_permission` (`id`, `name`, `label`) VALUES (3, 'manage_campaign', 'Manage Campaigns');
INSERT INTO `deelflow_permission` (`id`, `name`, `label`) VALUES (4, 'manage_org', 'Manage Organization');
INSERT INTO `deelflow_permission` (`id`, `name`, `label`) VALUES (5, 'manage_lead', 'Manage Leads');
INSERT INTO `deelflow_permission` (`id`, `name`, `label`) VALUES (6, 'manage_properties', 'Manage Properties');

-- Table: deelflow_role
DROP TABLE IF EXISTS `deelflow_role`;
CREATE TABLE "deelflow_role" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE, "label" varchar(150) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
INSERT INTO `deelflow_role` (`id`, `name`, `label`, `created_at`, `updated_at`) VALUES (1, 'manager', 'Manager', '2025-09-09 04:00:03.462405', '2025-09-22 08:43:29.554178');
INSERT INTO `deelflow_role` (`id`, `name`, `label`, `created_at`, `updated_at`) VALUES (2, 'Arpan', 'admin', '2025-09-22 10:35:18.357134', '2025-09-22 10:35:18.364634');
INSERT INTO `deelflow_role` (`id`, `name`, `label`, `created_at`, `updated_at`) VALUES (3, 'Anirudha', 'admin', '2025-09-22 10:42:26.098015', '2025-09-22 10:42:26.102884');
INSERT INTO `deelflow_role` (`id`, `name`, `label`, `created_at`, `updated_at`) VALUES (4, 'Abhishek', 'admin', '2025-09-22 10:48:05.325229', '2025-09-22 10:48:05.495331');

-- Table: deelflow_role_permissions
DROP TABLE IF EXISTS `deelflow_role_permissions`;
CREATE TABLE "deelflow_role_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "role_id" bigint NOT NULL REFERENCES "deelflow_role" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" bigint NOT NULL REFERENCES "deelflow_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO `deelflow_role_permissions` (`id`, `role_id`, `permission_id`) VALUES (1, 4, 1);
INSERT INTO `deelflow_role_permissions` (`id`, `role_id`, `permission_id`) VALUES (2, 4, 3);

-- Table: deelflow_propertyaianalysis
DROP TABLE IF EXISTS `deelflow_propertyaianalysis`;
CREATE TABLE "deelflow_propertyaianalysis" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "address" varchar(255) NOT NULL UNIQUE, "ai_confidence" real NOT NULL, "distress_level" real NOT NULL, "motivation" varchar(255) NOT NULL, "timeline" varchar(255) NOT NULL, "roi_percent" real NOT NULL, "cap_rate" real NOT NULL, "cash_flow" real NOT NULL, "market_stability_score" real NOT NULL, "comparables_confidence" real NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
INSERT INTO `deelflow_propertyaianalysis` (`id`, `address`, `ai_confidence`, `distress_level`, `motivation`, `timeline`, `roi_percent`, `cap_rate`, `cash_flow`, `market_stability_score`, `comparables_confidence`, `created_at`, `updated_at`) VALUES (1, '1247 Oak Street, Dallas, TX 75201', 58.0, 8.5, 'High – Divorce Settlement', '30–45 days', 12.7, 6.2, 540.0, 7.2, 90.0, '2025-09-09 17:43:43.747322', '2025-09-19 01:21:03.091215');

-- Table: deelflow_visionanalysismetrics
DROP TABLE IF EXISTS `deelflow_visionanalysismetrics`;
CREATE TABLE "deelflow_visionanalysismetrics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_analyses" integer NOT NULL, "accuracy_rate" real NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_voiceaicallmetrics
DROP TABLE IF EXISTS `deelflow_voiceaicallmetrics`;
CREATE TABLE "deelflow_voiceaicallmetrics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_calls" integer NOT NULL, "success_rate" real NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_blockchaintxnmetrics
DROP TABLE IF EXISTS `deelflow_blockchaintxnmetrics`;
CREATE TABLE "deelflow_blockchaintxnmetrics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_txns" integer NOT NULL, "success_rate" real NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_nlpprocessingmetrics
DROP TABLE IF EXISTS `deelflow_nlpprocessingmetrics`;
CREATE TABLE "deelflow_nlpprocessingmetrics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_processed" integer NOT NULL, "accuracy_rate" real NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_campaignperformance
DROP TABLE IF EXISTS `deelflow_campaignperformance`;
CREATE TABLE "deelflow_campaignperformance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "campaign_type" varchar(100) NOT NULL, "roi_percentage" decimal NOT NULL, "date_range" varchar(100) NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_campaignpropertystats
DROP TABLE IF EXISTS `deelflow_campaignpropertystats`;
CREATE TABLE "deelflow_campaignpropertystats" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "total_properties" integer NOT NULL, "distressed_properties" integer NOT NULL, "competition_level" varchar(50) NOT NULL, "avg_roi" decimal NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_channel
DROP TABLE IF EXISTS `deelflow_channel`;
CREATE TABLE "deelflow_channel" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL UNIQUE, "active" bool NOT NULL, "created_at" datetime NOT NULL);

-- Table: deelflow_channelresponserate
DROP TABLE IF EXISTS `deelflow_channelresponserate`;
CREATE TABLE "deelflow_channelresponserate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "channel_name" varchar(100) NOT NULL, "response_rate" decimal NOT NULL, "date_range" varchar(100) NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_discoveredlead
DROP TABLE IF EXISTS `deelflow_discoveredlead`;
CREATE TABLE "deelflow_discoveredlead" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "owner_name" varchar(255) NULL, "address" varchar(255) NOT NULL, "city" varchar(100) NULL, "state" varchar(50) NULL, "zipcode" varchar(20) NULL, "source" varchar(50) NOT NULL, "details" text NULL, "motivation_score" real NOT NULL, "property_condition" varchar(100) NULL, "financial_situation" varchar(100) NULL, "timeline_urgency" varchar(100) NULL, "negotiation_style" varchar(100) NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_outreachcampaign
DROP TABLE IF EXISTS `deelflow_outreachcampaign`;
CREATE TABLE "deelflow_outreachcampaign" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "description" text NULL, "channel" varchar(20) NOT NULL, "message_template" text NOT NULL, "scheduled_time" datetime NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Table: deelflow_campaignrecipient
DROP TABLE IF EXISTS `deelflow_campaignrecipient`;
CREATE TABLE "deelflow_campaignrecipient" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" varchar(50) NOT NULL, "response" text NULL, "sent_at" datetime NULL, "campaign_id" bigint NOT NULL REFERENCES "deelflow_outreachcampaign" ("id") DEFERRABLE INITIALLY DEFERRED, "lead_id" bigint NOT NULL REFERENCES "deelflow_discoveredlead" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Table: deelflow_campaign
DROP TABLE IF EXISTS `deelflow_campaign`;
CREATE TABLE "deelflow_campaign" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "status" varchar(20) NOT NULL, "created_at" datetime NOT NULL, "budget" decimal NULL, "campaign_type" varchar(100) NOT NULL, "channel" varchar(20) NOT NULL, "distress_indicators" varchar(500) NOT NULL, "email_content" text NULL, "geographic_scope_type" varchar(50) NOT NULL, "geographic_scope_values" varchar(500) NOT NULL, "location" varchar(255) NULL, "max_price" decimal NULL, "min_price" decimal NULL, "minimum_equity" decimal NULL, "property_type" varchar(100) NULL, "scheduled_at" datetime NULL, "subject_line" varchar(500) NULL, "use_ai_personalization" bool NOT NULL);
INSERT INTO `deelflow_campaign` (`id`, `name`, `status`, `created_at`, `budget`, `campaign_type`, `channel`, `distress_indicators`, `email_content`, `geographic_scope_type`, `geographic_scope_values`, `location`, `max_price`, `min_price`, `minimum_equity`, `property_type`, `scheduled_at`, `subject_line`, `use_ai_personalization`) VALUES (1, 'test', 'active', '2025-09-15 18:01:00.288269', NULL, 'new', 'email', '[]', NULL, 'zip', '[]', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0);
INSERT INTO `deelflow_campaign` (`id`, `name`, `status`, `created_at`, `budget`, `campaign_type`, `channel`, `distress_indicators`, `email_content`, `geographic_scope_type`, `geographic_scope_values`, `location`, `max_price`, `min_price`, `minimum_equity`, `property_type`, `scheduled_at`, `subject_line`, `use_ai_personalization`) VALUES (2, 'Summer Sale Campaign', 'active', '2025-09-22 08:55:18.469285', 5000, 'new', 'email', '[''Pre-foreclosure'', ''Tax Liens'']', 'Hello! Check out our special summer deals on properties in your area.', 'zip', '[''33101'', ''33102'', ''33103'']', 'Miami', 750000, 250000, 100000, 'Residential', '2025-09-25 10:00:00', 'Exclusive Summer Deals for Your Property!', 1);
INSERT INTO `deelflow_campaign` (`id`, `name`, `status`, `created_at`, `budget`, `campaign_type`, `channel`, `distress_indicators`, `email_content`, `geographic_scope_type`, `geographic_scope_values`, `location`, `max_price`, `min_price`, `minimum_equity`, `property_type`, `scheduled_at`, `subject_line`, `use_ai_personalization`) VALUES (3, 'IP List', 'inactive', '2025-09-23 13:04:53.488742', 1000, 'seller_finder', 'sms', '[''Tax Liens'']', 'safrtw4e', 'zip', '4354', 'tre', 31, 18, 21, 'est', '2025-09-08 15:08:00', 'rtyr', 1);

-- Table: deelflow_lead
DROP TABLE IF EXISTS `deelflow_lead`;
CREATE TABLE "deelflow_lead" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" varchar(20) NOT NULL, "responded" bool NOT NULL, "created_at" datetime NOT NULL, "address" varchar(255) NULL, "city" varchar(100) NULL, "email" varchar(254) NULL, "financial_situation" varchar(100) NULL, "motivation_score" real NOT NULL, "name" varchar(255) NOT NULL, "negotiation_style" varchar(100) NULL, "notes" text NULL, "phone" varchar(20) NULL, "property_condition" varchar(100) NULL, "source" varchar(50) NOT NULL, "state" varchar(50) NULL, "timeline_urgency" varchar(100) NULL, "updated_at" datetime NOT NULL, "zipcode" varchar(20) NULL, "campaign_id" bigint NULL REFERENCES "deelflow_campaign" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO `deelflow_lead` (`id`, `status`, `responded`, `created_at`, `address`, `city`, `email`, `financial_situation`, `motivation_score`, `name`, `negotiation_style`, `notes`, `phone`, `property_condition`, `source`, `state`, `timeline_urgency`, `updated_at`, `zipcode`, `campaign_id`) VALUES (2, 'new', 0, '2025-10-09 08:20:20.540697', '100 Buyer Street', 'New York', 'john.smith@email.com', 'pre_approved', 8.5, 'John Smith', 'collaborative', NULL, '+1-555-0101', 'excellent', 'website', 'NY', 'high', '2025-10-09 08:20:20.540697', '10002', NULL);
INSERT INTO `deelflow_lead` (`id`, `status`, `responded`, `created_at`, `address`, `city`, `email`, `financial_situation`, `motivation_score`, `name`, `negotiation_style`, `notes`, `phone`, `property_condition`, `source`, `state`, `timeline_urgency`, `updated_at`, `zipcode`, `campaign_id`) VALUES (3, 'new', 0, '2025-10-09 08:20:20.549232', '200 Seller Avenue', 'Los Angeles', 'sarah.johnson@email.com', 'qualified', 7.2, 'Sarah Johnson', 'competitive', NULL, '+1-555-0102', 'good', 'referral', 'CA', 'medium', '2025-10-09 08:20:20.549232', '90211', NULL);
INSERT INTO `deelflow_lead` (`id`, `status`, `responded`, `created_at`, `address`, `city`, `email`, `financial_situation`, `motivation_score`, `name`, `negotiation_style`, `notes`, `phone`, `property_condition`, `source`, `state`, `timeline_urgency`, `updated_at`, `zipcode`, `campaign_id`) VALUES (4, 'new', 0, '2025-10-09 08:20:20.555243', '300 Investor Blvd', 'Chicago', 'mike.wilson@email.com', 'cash_buyer', 9.1, 'Mike Wilson', 'aggressive', NULL, '+1-555-0103', 'excellent', 'social_media', 'IL', 'high', '2025-10-09 08:20:20.555243', '60602', NULL);

-- Table: deelflow_dealmilestone
DROP TABLE IF EXISTS `deelflow_dealmilestone`;
CREATE TABLE "deelflow_dealmilestone" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NOT NULL, "description" text NULL, "status" varchar(20) NOT NULL, "due_date" datetime NULL, "completed_date" datetime NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "deal_id" bigint NOT NULL REFERENCES "deelflow_deal" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO `deelflow_dealmilestone` (`id`, `title`, `description`, `status`, `due_date`, `completed_date`, `created_at`, `updated_at`, `deal_id`) VALUES (1, 'Initial Offer Submitted', 'Buyer submitted initial offer', 'completed', '2025-08-25 13:50:20.671736', '2025-08-25 13:50:20.671736', '2025-10-09 08:20:20.672735', '2025-10-09 08:20:20.672735', 1);
INSERT INTO `deelflow_dealmilestone` (`id`, `title`, `description`, `status`, `due_date`, `completed_date`, `created_at`, `updated_at`, `deal_id`) VALUES (2, 'Inspection Completed', 'Property inspection passed with minor issues', 'completed', '2025-09-04 13:50:20.671736', '2025-09-04 13:50:20.671736', '2025-10-09 08:20:20.680736', '2025-10-09 08:20:20.680736', 1);
INSERT INTO `deelflow_dealmilestone` (`id`, `title`, `description`, `status`, `due_date`, `completed_date`, `created_at`, `updated_at`, `deal_id`) VALUES (3, 'Closing Completed', 'Deal successfully closed', 'completed', '2025-09-09 13:50:20.671736', '2025-09-09 13:50:20.671736', '2025-10-09 08:20:20.688734', '2025-10-09 08:20:20.688734', 1);
INSERT INTO `deelflow_dealmilestone` (`id`, `title`, `description`, `status`, `due_date`, `completed_date`, `created_at`, `updated_at`, `deal_id`) VALUES (4, 'Contract Signed', 'Purchase agreement executed', 'completed', '2025-09-29 13:50:20.671736', '2025-09-29 13:50:20.671736', '2025-10-09 08:20:20.695734', '2025-10-09 08:20:20.695734', 2);
INSERT INTO `deelflow_dealmilestone` (`id`, `title`, `description`, `status`, `due_date`, `completed_date`, `created_at`, `updated_at`, `deal_id`) VALUES (5, 'Inspection Scheduled', 'Property inspection scheduled for next week', 'pending', '2025-10-16 13:50:20.671736', NULL, '2025-10-09 08:20:20.702735', '2025-10-09 08:20:20.702735', 2);

-- Table: deelflow_property
DROP TABLE IF EXISTS `deelflow_property`;
CREATE TABLE "deelflow_property" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "address" varchar(255) NOT NULL, "city" varchar(100) NOT NULL, "state" varchar(50) NOT NULL, "zipcode" varchar(20) NOT NULL, "property_type" varchar(20) NOT NULL, "price" decimal NOT NULL, "bedrooms" integer NULL, "bathrooms" real NULL, "square_feet" integer NULL, "lot_size" real NULL, "year_built" integer NULL, "description" text NULL, "images" text NOT NULL CHECK ((JSON_VALID("images") OR "images" IS NULL)), "status" varchar(20) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "ai_analysis_id" bigint NULL REFERENCES "deelflow_propertyaianalysis" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO `deelflow_property` (`id`, `address`, `city`, `state`, `zipcode`, `property_type`, `price`, `bedrooms`, `bathrooms`, `square_feet`, `lot_size`, `year_built`, `description`, `images`, `status`, `created_at`, `updated_at`, `ai_analysis_id`) VALUES (1, '123 Main Street', 'New York', 'NY', '10001', 'apartment', 750000, 3, 2.0, 1200, NULL, NULL, NULL, '[]', 'active', '2025-10-09 08:20:20.502680', '2025-10-09 08:20:20.502680', NULL);
INSERT INTO `deelflow_property` (`id`, `address`, `city`, `state`, `zipcode`, `property_type`, `price`, `bedrooms`, `bathrooms`, `square_feet`, `lot_size`, `year_built`, `description`, `images`, `status`, `created_at`, `updated_at`, `ai_analysis_id`) VALUES (2, '456 Oak Avenue', 'Los Angeles', 'CA', '90210', 'house', 1200000, 4, 3.0, 2000, NULL, NULL, NULL, '[]', 'active', '2025-10-09 08:20:20.510683', '2025-10-09 08:20:20.510683', NULL);
INSERT INTO `deelflow_property` (`id`, `address`, `city`, `state`, `zipcode`, `property_type`, `price`, `bedrooms`, `bathrooms`, `square_feet`, `lot_size`, `year_built`, `description`, `images`, `status`, `created_at`, `updated_at`, `ai_analysis_id`) VALUES (3, '789 Pine Street', 'Chicago', 'IL', '60601', 'condo', 450000, 2, 2.0, 900, NULL, NULL, NULL, '[]', 'pending', '2025-10-09 08:20:20.518687', '2025-10-09 08:20:20.518687', NULL);
INSERT INTO `deelflow_property` (`id`, `address`, `city`, `state`, `zipcode`, `property_type`, `price`, `bedrooms`, `bathrooms`, `square_feet`, `lot_size`, `year_built`, `description`, `images`, `status`, `created_at`, `updated_at`, `ai_analysis_id`) VALUES (4, '321 Elm Drive', 'Houston', 'TX', '77001', 'house', 350000, 3, 2.0, 1500, NULL, NULL, NULL, '[]', 'active', '2025-10-09 08:20:20.525688', '2025-10-09 08:20:20.525688', NULL);
INSERT INTO `deelflow_property` (`id`, `address`, `city`, `state`, `zipcode`, `property_type`, `price`, `bedrooms`, `bathrooms`, `square_feet`, `lot_size`, `year_built`, `description`, `images`, `status`, `created_at`, `updated_at`, `ai_analysis_id`) VALUES (5, '654 Maple Lane', 'Phoenix', 'AZ', '85001', 'townhouse', 280000, 2, 2.0, 1100, NULL, NULL, NULL, '[]', 'active', '2025-10-09 08:20:20.532683', '2025-10-09 08:20:20.532683', NULL);

-- Table: deelflow_deal
DROP TABLE IF EXISTS `deelflow_deal`;
CREATE TABLE "deelflow_deal" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "deal_type" varchar(20) NOT NULL, "status" varchar(20) NOT NULL, "offer_price" decimal NOT NULL, "final_price" decimal NULL, "commission" decimal NULL, "closing_date" datetime NULL, "notes" text NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "buyer_lead_id" bigint NULL REFERENCES "deelflow_lead" ("id") DEFERRABLE INITIALLY DEFERRED, "seller_lead_id" bigint NULL REFERENCES "deelflow_lead" ("id") DEFERRABLE INITIALLY DEFERRED, "property_id" bigint NOT NULL REFERENCES "deelflow_property" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO `deelflow_deal` (`id`, `deal_type`, `status`, `offer_price`, `final_price`, `commission`, `closing_date`, `notes`, `created_at`, `updated_at`, `buyer_lead_id`, `seller_lead_id`, `property_id`) VALUES (1, 'sale', 'closed', 750000, 745000, 22350, '2025-09-09 13:50:20.561246', 'Successful closing with minor price negotiation', '2025-10-09 08:20:20.632230', '2025-10-09 08:20:20.632230', 2, NULL, 1);
INSERT INTO `deelflow_deal` (`id`, `deal_type`, `status`, `offer_price`, `final_price`, `commission`, `closing_date`, `notes`, `created_at`, `updated_at`, `buyer_lead_id`, `seller_lead_id`, `property_id`) VALUES (2, 'sale', 'pending', 1200000, 1180000, 35400, '2025-10-24 13:50:20.562236', 'Under contract, awaiting inspection', '2025-10-09 08:20:20.640243', '2025-10-09 08:20:20.640243', 3, NULL, 2);
INSERT INTO `deelflow_deal` (`id`, `deal_type`, `status`, `offer_price`, `final_price`, `commission`, `closing_date`, `notes`, `created_at`, `updated_at`, `buyer_lead_id`, `seller_lead_id`, `property_id`) VALUES (3, 'sale', 'active', 450000, NULL, NULL, NULL, 'Initial offer submitted', '2025-10-09 08:20:20.647241', '2025-10-09 08:20:20.647241', 4, NULL, 3);

-- Table: deelflow_aianalysis
DROP TABLE IF EXISTS `deelflow_aianalysis`;
CREATE TABLE "deelflow_aianalysis" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "analysis_type" varchar(50) NOT NULL, "result" text NOT NULL CHECK ((JSON_VALID("result") OR "result" IS NULL)), "confidence_score" real NOT NULL, "processing_time" real NOT NULL, "created_at" datetime NOT NULL, "lead_id" bigint NULL REFERENCES "deelflow_lead" ("id") DEFERRABLE INITIALLY DEFERRED, "property_id" bigint NULL REFERENCES "deelflow_property" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO `deelflow_aianalysis` (`id`, `analysis_type`, `result`, `confidence_score`, `processing_time`, `created_at`, `lead_id`, `property_id`) VALUES (1, 'property_valuation', '"Property valued at $750,000 with 95% confidence"', 0.95, 2.3, '2025-10-09 08:20:20.653734', 2, 1);
INSERT INTO `deelflow_aianalysis` (`id`, `analysis_type`, `result`, `confidence_score`, `processing_time`, `created_at`, `lead_id`, `property_id`) VALUES (2, 'market_analysis', '"Strong market conditions, recommended listing price $1.2M"', 0.88, 3.1, '2025-10-09 08:20:20.660735', 3, 2);
INSERT INTO `deelflow_aianalysis` (`id`, `analysis_type`, `result`, `confidence_score`, `processing_time`, `created_at`, `lead_id`, `property_id`) VALUES (3, 'investment_potential', '"High ROI potential, estimated 12% annual return"', 0.92, 1.8, '2025-10-09 08:20:20.665735', 4, 3);

-- Table: deelflow_savedproperty
DROP TABLE IF EXISTS `deelflow_savedproperty`;
CREATE TABLE "deelflow_savedproperty" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "property_id" bigint NOT NULL REFERENCES "deelflow_property" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "deelflow_user" ("id") DEFERRABLE INITIALLY DEFERRED);
