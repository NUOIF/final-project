-- MySQL dump 10.13  Distrib 8.0.23, for osx10.16 (x86_64)
--
-- Host: localhost    Database: projectDB
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `_groups`
--

DROP TABLE IF EXISTS `_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `_groups` (
  `id_groups` int NOT NULL,
  `name_Groups` varchar(45) DEFAULT NULL,
  `idea_Groups` varchar(45) DEFAULT NULL,
  `idea_fescription` varchar(45) DEFAULT NULL,
  `idea_speciallty` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_groups`),
  KEY `id_Groups_fk` (`id_groups`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `_groups`
--

LOCK TABLES `_groups` WRITE;
/*!40000 ALTER TABLE `_groups` DISABLE KEYS */;
INSERT INTO `_groups` VALUES (1,'M75','management graduate projects','managing the graduate projects','web application');
/*!40000 ALTER TABLE `_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add committees charis',7,'add_committeescharis'),(26,'Can change committees charis',7,'change_committeescharis'),(27,'Can delete committees charis',7,'delete_committeescharis'),(28,'Can view committees charis',7,'view_committeescharis'),(29,'Can add doctors',8,'add_doctors'),(30,'Can change doctors',8,'change_doctors'),(31,'Can delete doctors',8,'delete_doctors'),(32,'Can view doctors',8,'view_doctors'),(33,'Can add evaluation',9,'add_evaluation'),(34,'Can change evaluation',9,'change_evaluation'),(35,'Can delete evaluation',9,'delete_evaluation'),(36,'Can view evaluation',9,'view_evaluation'),(37,'Can add examiners',10,'add_examiners'),(38,'Can change examiners',10,'change_examiners'),(39,'Can delete examiners',10,'delete_examiners'),(40,'Can view examiners',10,'view_examiners'),(41,'Can add groups',11,'add_groups'),(42,'Can change groups',11,'change_groups'),(43,'Can delete groups',11,'delete_groups'),(44,'Can view groups',11,'view_groups'),(45,'Can add projects',12,'add_projects'),(46,'Can change projects',12,'change_projects'),(47,'Can delete projects',12,'delete_projects'),(48,'Can view projects',12,'view_projects'),(49,'Can add students',13,'add_students'),(50,'Can change students',13,'change_students'),(51,'Can delete students',13,'delete_students'),(52,'Can view students',13,'view_students'),(53,'Can add department',14,'add_department'),(54,'Can change department',14,'change_department'),(55,'Can delete department',14,'delete_department'),(56,'Can view department',14,'view_department'),(57,'Can add department',15,'add_department'),(58,'Can change department',15,'change_department'),(59,'Can delete department',15,'delete_department'),(60,'Can view department',15,'view_department'),(61,'Can add examiners',16,'add_examiners'),(62,'Can change examiners',16,'change_examiners'),(63,'Can delete examiners',16,'delete_examiners'),(64,'Can view examiners',16,'view_examiners'),(65,'Can add doctors',17,'add_doctors'),(66,'Can change doctors',17,'change_doctors'),(67,'Can delete doctors',17,'delete_doctors'),(68,'Can view doctors',17,'view_doctors'),(69,'Can add groups',18,'add_groups'),(70,'Can change groups',18,'change_groups'),(71,'Can delete groups',18,'delete_groups'),(72,'Can view groups',18,'view_groups'),(73,'Can add students',19,'add_students'),(74,'Can change students',19,'change_students'),(75,'Can delete students',19,'delete_students'),(76,'Can view students',19,'view_students'),(77,'Can add department',20,'add_department'),(78,'Can change department',20,'change_department'),(79,'Can delete department',20,'delete_department'),(80,'Can view department',20,'view_department'),(81,'Can add evaluation',21,'add_evaluation'),(82,'Can change evaluation',21,'change_evaluation'),(83,'Can delete evaluation',21,'delete_evaluation'),(84,'Can view evaluation',21,'view_evaluation'),(85,'Can add groups',22,'add_groups'),(86,'Can change groups',22,'change_groups'),(87,'Can delete groups',22,'delete_groups'),(88,'Can view groups',22,'view_groups'),(89,'Can add examiners',23,'add_examiners'),(90,'Can change examiners',23,'change_examiners'),(91,'Can delete examiners',23,'delete_examiners'),(92,'Can view examiners',23,'view_examiners'),(93,'Can add projects',24,'add_projects'),(94,'Can change projects',24,'change_projects'),(95,'Can delete projects',24,'delete_projects'),(96,'Can view projects',24,'view_projects');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$bEFqtTyNcHhy$+VvCoNC8KNFJ+FrwPglyW4EDV54QRBGVAv0uQPsFuSc=','2021-02-18 11:25:15.560112',1,'h3','','','',1,1,'2021-02-18 11:24:50.846476'),(2,'pbkdf2_sha256$216000$YfFgdzRmja3b$1/kjyVuuRiXKp2K+nPwuLLbve91Z8X96Q40YWsQ80fY=','2021-02-20 18:14:03.960621',1,'hamad','','','',1,1,'2021-02-20 18:12:57.170698');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `committees_charis`
--

DROP TABLE IF EXISTS `committees_charis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `committees_charis` (
  `id_committees_charis` int NOT NULL,
  `name_committees_charis` varchar(45) DEFAULT NULL,
  `passwords` varchar(45) DEFAULT NULL,
  `id_department_fk` int DEFAULT NULL,
  PRIMARY KEY (`id_committees_charis`),
  KEY `id_committees_charis_fk` (`id_committees_charis`),
  KEY `id_depart_fk_idx` (`id_department_fk`),
  CONSTRAINT `id_depart_fk` FOREIGN KEY (`id_department_fk`) REFERENCES `department` (`id_department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `committees_charis`
--

LOCK TABLES `committees_charis` WRITE;
/*!40000 ALTER TABLE `committees_charis` DISABLE KEYS */;
INSERT INTO `committees_charis` VALUES (1,'sultan','123',1),(2,'faisal','123',2),(3,'mohammed','123',3);
/*!40000 ALTER TABLE `committees_charis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `id_department` int NOT NULL,
  `name_department` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_department`),
  KEY `id_department_fk` (`id_department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'CS'),(2,'IT'),(3,'IS');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-02-20 18:14:29.853933','1','CS',1,'[{\"added\": {}}]',15,2),(2,'2021-02-20 18:15:22.435928','12','saleh',1,'[{\"added\": {}}]',17,2),(3,'2021-02-20 18:22:53.622374','12','saleh',1,'[{\"added\": {}}]',17,2),(4,'2021-02-20 19:53:00.535134','1','CS',1,'[{\"added\": {}}]',20,2),(5,'2021-02-20 19:53:48.571138','2','IT',1,'[{\"added\": {}}]',20,2),(6,'2021-02-20 19:54:00.003940','3','IS',1,'[{\"added\": {}}]',20,2),(7,'2021-02-20 19:55:43.721541','1','sultan',1,'[{\"added\": {}}]',7,2),(8,'2021-02-20 19:56:02.797469','2','faisal',1,'[{\"added\": {}}]',7,2),(9,'2021-02-20 19:56:24.768254','3','mohammed',1,'[{\"added\": {}}]',7,2),(10,'2021-02-20 20:00:24.066578','1','1',1,'[{\"added\": {}}]',22,2),(11,'2021-02-20 20:00:57.875036','438006941','438006941',1,'[{\"added\": {}}]',19,2),(12,'2021-02-20 20:01:37.473342','438010648','438010648',1,'[{\"added\": {}}]',19,2),(13,'2021-02-20 20:02:17.963174','438000519','438000519',1,'[{\"added\": {}}]',19,2),(14,'2021-02-20 20:03:03.512011','438009200','438009200',1,'[{\"added\": {}}]',19,2),(15,'2021-02-20 20:03:48.129277','12','saleh',2,'[{\"changed\": {\"fields\": [\"Id groups fk\"]}}]',17,2),(16,'2021-02-20 20:04:48.650730','3','3',1,'[{\"added\": {}}]',23,2),(17,'2021-02-20 20:05:07.244131','12','saleh',2,'[{\"changed\": {\"fields\": [\"Id examiners fk\"]}}]',17,2),(18,'2021-02-20 20:05:25.853950','12','saleh',2,'[]',17,2),(19,'2021-02-20 20:17:44.209145','2','2',1,'[{\"added\": {}}]',23,2),(20,'2021-02-20 20:18:00.317775','3','3',2,'[{\"changed\": {\"fields\": [\"Name examiners\"]}}]',23,2),(21,'2021-02-20 20:18:46.191704','1','1',1,'[{\"added\": {}}]',21,2),(22,'2021-02-20 20:19:00.364603','2','2',1,'[{\"added\": {}}]',21,2),(23,'2021-02-20 20:35:04.907560','2','saleh',1,'[{\"added\": {}}]',17,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'committeeChairs','committeescharis'),(14,'committeeChairs','department'),(8,'committeeChairs','doctors'),(9,'committeeChairs','evaluation'),(10,'committeeChairs','examiners'),(11,'committeeChairs','groups'),(12,'committeeChairs','projects'),(13,'committeeChairs','students'),(5,'contenttypes','contenttype'),(20,'Department','department'),(15,'doctors','department'),(17,'doctors','doctors'),(16,'doctors','examiners'),(18,'doctors','groups'),(21,'Evaluation','evaluation'),(23,'Examiners','examiners'),(22,'Groups','groups'),(24,'projects','projects'),(6,'sessions','session'),(19,'students','students');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-02-18 11:22:39.085082'),(2,'auth','0001_initial','2021-02-18 11:22:39.181248'),(3,'admin','0001_initial','2021-02-18 11:22:39.368098'),(4,'admin','0002_logentry_remove_auto_add','2021-02-18 11:22:39.426862'),(5,'admin','0003_logentry_add_action_flag_choices','2021-02-18 11:22:39.435032'),(6,'contenttypes','0002_remove_content_type_name','2021-02-18 11:22:39.492824'),(7,'auth','0002_alter_permission_name_max_length','2021-02-18 11:22:39.526836'),(8,'auth','0003_alter_user_email_max_length','2021-02-18 11:22:39.548109'),(9,'auth','0004_alter_user_username_opts','2021-02-18 11:22:39.557511'),(10,'auth','0005_alter_user_last_login_null','2021-02-18 11:22:39.591163'),(11,'auth','0006_require_contenttypes_0002','2021-02-18 11:22:39.593763'),(12,'auth','0007_alter_validators_add_error_messages','2021-02-18 11:22:39.602735'),(13,'auth','0008_alter_user_username_max_length','2021-02-18 11:22:39.640466'),(14,'auth','0009_alter_user_last_name_max_length','2021-02-18 11:22:39.678461'),(15,'auth','0010_alter_group_name_max_length','2021-02-18 11:22:39.699776'),(16,'auth','0011_update_proxy_permissions','2021-02-18 11:22:39.708652'),(17,'auth','0012_alter_user_first_name_max_length','2021-02-18 11:22:39.743798'),(18,'sessions','0001_initial','2021-02-18 11:22:39.758848'),(19,'committeeChairs','0001_initial','2021-02-20 18:07:37.908255'),(20,'doctors','0001_initial','2021-02-20 18:07:38.101946'),(21,'Department','0001_initial','2021-02-20 18:59:47.416660'),(22,'Evaluation','0001_initial','2021-02-20 18:59:47.477923'),(23,'Examiners','0001_initial','2021-02-20 18:59:47.502203'),(24,'Groups','0001_initial','2021-02-20 18:59:47.568619'),(25,'committeeChairs','0002_auto_20210220_1858','2021-02-20 18:59:47.700956'),(26,'doctors','0002_auto_20210220_1858','2021-02-20 18:59:47.879508'),(27,'projects','0001_initial','2021-02-20 18:59:47.885566'),(28,'students','0001_initial','2021-02-20 18:59:47.890055');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('07l2soqnh1bjhkky4onofssq3rl5afo6','.eJxVjMsOwiAQRf-FtSEUKDN16d5vIDM8pGogKe3K-O_apAvd3nPOfQlP21r81tPi5yjOYhCn340pPFLdQbxTvTUZWl2XmeWuyIN2eW0xPS-H-3dQqJdvzQZHdqDQEAYmQg1WJRhUNhGUoQguW1asnUUd7WQZx4xTRjDgDFvx_gDQ0Tch:1lChQp:yuX8MlUVc48sbqRULEa5ypaJPVOjW0KZoKw7TTbH0IU','2021-03-04 11:25:15.564004'),('l7yf27f5za868ugkh7knqdgj8bli6v1e','.eJxVjEEOwiAQRe_C2hCGKQO4dO8ZCAxUqoYmpV0Z765NutDtf-_9lwhxW2vYelnClMVZaHH63VLkR2k7yPfYbrPkua3LlOSuyIN2eZ1zeV4O9--gxl6_NUdChV6XYWTPA0SnSZO1o1KciShDQXDeZWQN1qAxjpz1UEAhECXx_gDBizZe:1lDWlX:pKio-RkR6OewLLvlmo0Y9OyoLLV_dumacNGGXUsZJLQ','2021-03-06 18:14:03.966145');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `id_Doctors` int NOT NULL,
  `name_Doctors` varchar(45) DEFAULT NULL,
  `passwords` varchar(45) DEFAULT NULL,
  `id_department_fk` int DEFAULT NULL,
  `id_Groups_fk` int DEFAULT NULL,
  `id_Examiners_fk` int DEFAULT NULL,
  PRIMARY KEY (`id_Doctors`),
  KEY `id_department_fk_idx` (`id_department_fk`),
  KEY `id_Groups_fk_idx` (`id_Groups_fk`),
  KEY `id_Examiners_fk_idx` (`id_Examiners_fk`),
  CONSTRAINT `id_department_fk` FOREIGN KEY (`id_department_fk`) REFERENCES `department` (`id_department`),
  CONSTRAINT `id_Examiners_fk` FOREIGN KEY (`id_Examiners_fk`) REFERENCES `examiners` (`id_Examiners`),
  CONSTRAINT `id_Groups` FOREIGN KEY (`id_Groups_fk`) REFERENCES `_groups` (`id_groups`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (2,'saleh','123',1,1,2),(12,'saleh','123',1,1,3);
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors_doctors`
--

DROP TABLE IF EXISTS `doctors_doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors_doctors` (
  `id_Doctors` int NOT NULL,
  `name_Doctors` varchar(45) DEFAULT NULL,
  `passwords` varchar(45) DEFAULT NULL,
  `id_department_fk` int DEFAULT NULL,
  `id_Examiners_fk` int DEFAULT NULL,
  `id_Groups_fk` int DEFAULT NULL,
  PRIMARY KEY (`id_Doctors`),
  KEY `doctors_doctors_id_department_fk_e6ee7269_fk_doctors_d` (`id_department_fk`),
  KEY `doctors_doctors_id_Examiners_fk_daa4ac9c_fk_examiners` (`id_Examiners_fk`),
  KEY `doctors_doctors_id_Groups_fk_1ec4368a_fk_doctors_g` (`id_Groups_fk`),
  CONSTRAINT `doctors_doctors_id_department_fk_e6ee7269_fk_doctors_d` FOREIGN KEY (`id_department_fk`) REFERENCES `doctors_department` (`id_department`),
  CONSTRAINT `doctors_doctors_id_Examiners_fk_daa4ac9c_fk_examiners` FOREIGN KEY (`id_Examiners_fk`) REFERENCES `examiners` (`id_Examiners`),
  CONSTRAINT `doctors_doctors_id_Groups_fk_1ec4368a_fk_doctors_g` FOREIGN KEY (`id_Groups_fk`) REFERENCES `doctors_groups` (`id_groups`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors_doctors`
--

LOCK TABLES `doctors_doctors` WRITE;
/*!40000 ALTER TABLE `doctors_doctors` DISABLE KEYS */;
INSERT INTO `doctors_doctors` VALUES (12,'saleh','123',1,NULL,NULL);
/*!40000 ALTER TABLE `doctors_doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation`
--

DROP TABLE IF EXISTS `evaluation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluation` (
  `id_Evaluation` int NOT NULL,
  `gread_evaluation` varchar(45) DEFAULT NULL,
  `id_Examiners_fk` int DEFAULT NULL,
  `id_Groups_fk` int DEFAULT NULL,
  PRIMARY KEY (`id_Evaluation`),
  KEY `id_Evaluation_fk` (`id_Evaluation`),
  KEY `id_grops_fk_idx` (`id_Groups_fk`),
  KEY `id_Examiners_fkk_idx` (`id_Examiners_fk`),
  CONSTRAINT `id_Examiners_fkk` FOREIGN KEY (`id_Examiners_fk`) REFERENCES `examiners` (`id_Examiners`),
  CONSTRAINT `id_grops_fk` FOREIGN KEY (`id_Groups_fk`) REFERENCES `_groups` (`id_groups`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation`
--

LOCK TABLES `evaluation` WRITE;
/*!40000 ALTER TABLE `evaluation` DISABLE KEYS */;
INSERT INTO `evaluation` VALUES (1,'90',2,1),(2,'90',3,1);
/*!40000 ALTER TABLE `evaluation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examiners`
--

DROP TABLE IF EXISTS `examiners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examiners` (
  `id_Examiners` int NOT NULL,
  `name_Examiners` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_Examiners`),
  KEY `id_Examiners` (`id_Examiners`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examiners`
--

LOCK TABLES `examiners` WRITE;
/*!40000 ALTER TABLE `examiners` DISABLE KEYS */;
INSERT INTO `examiners` VALUES (2,'saleh'),(3,'saleh');
/*!40000 ALTER TABLE `examiners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `id_Projects` int NOT NULL,
  `name_projects` varchar(45) DEFAULT NULL,
  `filled_projects` varchar(45) DEFAULT NULL,
  `descriotion_projects` varchar(45) DEFAULT NULL,
  `id_Groups_fk` int DEFAULT NULL,
  PRIMARY KEY (`id_Projects`),
  KEY `id_Group_fkk_idx` (`id_Groups_fk`),
  CONSTRAINT `id_Group_fkk` FOREIGN KEY (`id_Groups_fk`) REFERENCES `_groups` (`id_groups`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id_Students` int NOT NULL,
  `name_Students` varchar(45) DEFAULT NULL,
  `passwords` varchar(45) DEFAULT NULL,
  `id_Groups_fk` int DEFAULT NULL,
  `id_department_fk` int DEFAULT NULL,
  PRIMARY KEY (`id_Students`),
  KEY `id_Groups_fk_idx` (`id_Groups_fk`),
  CONSTRAINT `id_depratment_fk` FOREIGN KEY (`id_Students`) REFERENCES `department` (`id_department`),
  CONSTRAINT `id_Groups_fk` FOREIGN KEY (`id_Groups_fk`) REFERENCES `_groups` (`id_groups`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (438000519,'Naif','123',1,1),(438006941,'Hamad','123',1,1),(438009200,'Faisal','123',1,1),(438010648,'Mohammed','123',1,1);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-21 20:42:58
