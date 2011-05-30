-- MySQL dump 10.11
--
-- Host: localhost    Database: lobby
-- ------------------------------------------------------
-- Server version	5.0.51b-community-nt

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data_affiliatedorgs`
--

DROP TABLE IF EXISTS `data_affiliatedorgs`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `data_affiliatedorgs` (
  `filing_id` varchar(45) default NULL,
  `affiliated_orgname` varchar(255) default NULL,
  `affiliated_orgcountry` varchar(45) default NULL,
  `affiliated_orgppbcountry` varchar(45) default NULL,
  `id` int(10) unsigned NOT NULL auto_increment,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7649 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `data_agencies`
--

DROP TABLE IF EXISTS `data_agencies`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `data_agencies` (
  `filing_id` varchar(45) default NULL,
  `gov_entity_name` varchar(255) default NULL,
  `id` int(10) unsigned NOT NULL auto_increment,
  PRIMARY KEY  USING BTREE (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=316654 DEFAULT CHARSET=latin1 COMMENT='InnoDB free: 6144 kB';
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `data_foreignentity`
--

DROP TABLE IF EXISTS `data_foreignentity`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `data_foreignentity` (
  `filing_id` varchar(45) default NULL,
  `foreign_entity_name` varchar(255) default NULL,
  `foreign_entity_country` varchar(45) default NULL,
  `foreign_entity_ppbcountry` varchar(45) default NULL,
  `foreign_entity_status` varchar(45) default NULL,
  `foreign_entity_ownpercentage` varchar(45) default NULL,
  `foreign_entity_contribution` varchar(45) default NULL,
  `id` int(10) unsigned NOT NULL auto_increment,
  PRIMARY KEY  (`id`),
  KEY `FK_data_foreignentity_1` (`filing_id`),
  CONSTRAINT `FK_data_foreignentity_1` FOREIGN KEY (`filing_id`) REFERENCES `data_lobby` (`filing_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2214 DEFAULT CHARSET=latin1 COMMENT='InnoDB free: 6144 kB';
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `data_issues`
--

DROP TABLE IF EXISTS `data_issues`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `data_issues` (
  `filing_id` varchar(45) NOT NULL,
  `issue_code` varchar(45) default NULL,
  `specific_issue` blob,
  `id` int(10) unsigned NOT NULL auto_increment,
  PRIMARY KEY  USING BTREE (`id`),
  KEY `filing_id` USING BTREE (`filing_id`),
  CONSTRAINT `FK_data_issues_1` FOREIGN KEY (`filing_id`) REFERENCES `data_lobby` (`filing_id`)
) ENGINE=InnoDB AUTO_INCREMENT=245346 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `data_lobby`
--

DROP TABLE IF EXISTS `data_lobby`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `data_lobby` (
  `filing_id` varchar(45) NOT NULL default '',
  `year` varchar(4) default NULL,
  `received` varchar(45) default NULL,
  `amount` varchar(45) default NULL,
  `type` varchar(45) default NULL,
  `period` varchar(45) default NULL,
  `registrant_id` varchar(45) default NULL,
  `registrant_name` varchar(255) character set latin1 collate latin1_bin default NULL,
  `address` blob,
  `registrant_country` varchar(45) default NULL,
  `registrant_ppbcountry` varchar(45) default NULL,
  `client_name` varchar(255) default NULL,
  `client_id` varchar(45) default NULL,
  `client_status` varchar(45) default NULL,
  `contact_fullname` varchar(45) character set latin1 collate latin1_bin default NULL,
  `client_country` varchar(45) default NULL,
  `client_ppbcountry` varchar(45) default NULL,
  `client_state` varchar(45) default NULL,
  `client_ppbstate` varchar(45) default NULL,
  `id` int(10) unsigned NOT NULL auto_increment,
  PRIMARY KEY  USING BTREE (`id`),
  KEY `filing_id` (`filing_id`)
) ENGINE=InnoDB AUTO_INCREMENT=144634 DEFAULT CHARSET=latin1 COMMENT='InnoDB free: 8192 kB';
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `data_lobbyists`
--

DROP TABLE IF EXISTS `data_lobbyists`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `data_lobbyists` (
  `filing_id` varchar(45) default NULL,
  `lobbyist_name` varchar(45) default NULL,
  `lobbyist_status` varchar(45) default NULL,
  `lobbyist_indicator` varchar(45) default NULL,
  `official_position` varchar(255) default NULL,
  `id` int(10) unsigned NOT NULL auto_increment,
  PRIMARY KEY  (`id`),
  KEY `filing_id` (`filing_id`),
  CONSTRAINT `FK_data_lobbyists_1` FOREIGN KEY (`filing_id`) REFERENCES `data_lobby` (`filing_id`)
) ENGINE=InnoDB AUTO_INCREMENT=415413 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2008-10-02  0:46:12
