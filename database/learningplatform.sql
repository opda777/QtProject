/*
 Navicat Premium Data Transfer

 Source Server         : 6655
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : learningplatform

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 23/11/2020 15:28:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for administrators
-- ----------------------------
DROP TABLE IF EXISTS `administrators`;
CREATE TABLE `administrators`  (
  `admin_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '管理员账号',
  `admin_password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '登录密码',
  `power` tinyint(0) NOT NULL COMMENT '权限',
  PRIMARY KEY (`admin_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of administrators
-- ----------------------------

-- ----------------------------
-- Table structure for comment_emp
-- ----------------------------
DROP TABLE IF EXISTS `comment_emp`;
CREATE TABLE `comment_emp`  (
  `com_id` int(0) NOT NULL AUTO_INCREMENT COMMENT '评价编号',
  `employee_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '职员账号',
  `admin_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '管理员账号',
  `Info` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '评价内容',
  `level` tinyint(0) NULL DEFAULT NULL COMMENT '评价等级',
  PRIMARY KEY (`com_id`) USING BTREE,
  INDEX `FK_COMMENT_EMP_REFERENCE_ADMIN`(`admin_id`) USING BTREE,
  INDEX `FK_COMMENT_EMP_REFERENCE_EMPLOYEE`(`employee_id`) USING BTREE,
  CONSTRAINT `FK_COMMENT_EMP_REFERENCE_ADMIN` FOREIGN KEY (`admin_id`) REFERENCES `administrators` (`admin_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_COMMENT_EMP_REFERENCE_EMPLOYEE` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comment_emp
-- ----------------------------

-- ----------------------------
-- Table structure for courses
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses`  (
  `course_id` int(0) NOT NULL AUTO_INCREMENT COMMENT '课程号',
  `employee_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '职员账号',
  `course_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程名',
  `tags` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程标签',
  `info` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程内容',
  `totaltime` float NULL DEFAULT NULL COMMENT '学时',
  `pic_path` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程封面',
  `price` float NULL DEFAULT NULL COMMENT '课程价格',
  `member_num` int(0) NULL DEFAULT NULL COMMENT '学习人数',
  PRIMARY KEY (`course_id`) USING BTREE,
  INDEX `FK_CLASS_REFERENCE_EMPLOYEE`(`employee_id`) USING BTREE,
  CONSTRAINT `FK_CLASS_REFERENCE_EMPLOYEE` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of courses
-- ----------------------------
INSERT INTO `courses` VALUES (1, '1@emp.com', 'UE4蓝图', 'UE4', NULL, NULL, 'path1', NULL, NULL);
INSERT INTO `courses` VALUES (2, '1@emp.com', 'UE4 C++', 'UE4', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `courses` VALUES (3, '1@emp.com', 'UE4 场景编辑', 'UE4', NULL, NULL, NULL, NULL, NULL);
INSERT INTO `courses` VALUES (4, '2@emp.com', 'Unity入门', 'Unity', NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for courses_messages
-- ----------------------------
DROP TABLE IF EXISTS `courses_messages`;
CREATE TABLE `courses_messages`  (
  `message_id` int(0) NOT NULL AUTO_INCREMENT COMMENT '留言编号',
  `course_id` int(0) NULL DEFAULT NULL COMMENT '课程号',
  `employee_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '职员账号',
  `mem_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '会员账号',
  `message_info` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '留言内容',
  `message_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '发布时间',
  `reply_info` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '回复内容',
  `reply_time` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '回复时间',
  PRIMARY KEY (`message_id`) USING BTREE,
  INDEX `FK_CLASS_MESSAGE_REFERENCE_CLASS`(`course_id`) USING BTREE,
  INDEX `FK_CLASS_MESSAGE_REFERENCE_EMPLOYEE`(`employee_id`) USING BTREE,
  INDEX `FK_CLASS_MESSAGE_REFERENCE_MEMBER`(`mem_id`) USING BTREE,
  CONSTRAINT `FK_CLASS_MESSAGE_REFERENCE_CLASS` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_CLASS_MESSAGE_REFERENCE_EMPLOYEE` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_CLASS_MESSAGE_REFERENCE_MEMBER` FOREIGN KEY (`mem_id`) REFERENCES `members` (`mem_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of courses_messages
-- ----------------------------
INSERT INTO `courses_messages` VALUES (5, 1, '1@emp.com', '1@qq.com', '好课程', '2020-11-22 20:17:55', '谢谢', '2020-11-23 14:17:17');
INSERT INTO `courses_messages` VALUES (6, 1, NULL, '1@qq.com', '留言', '2020-11-22 20:19:23', NULL, '2020-11-22 20:19:23');

-- ----------------------------
-- Table structure for employees
-- ----------------------------
DROP TABLE IF EXISTS `employees`;
CREATE TABLE `employees`  (
  `employee_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '职员账号',
  `emp_password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '登录密码',
  `idc` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '身份证号',
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '职员名',
  `sex` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '性别',
  `birthday` datetime(0) NULL DEFAULT NULL COMMENT '生日',
  `emall` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '邮箱',
  `icon` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '头像',
  `department` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '部门',
  `salary` float NULL DEFAULT NULL COMMENT '薪水',
  PRIMARY KEY (`employee_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employees
-- ----------------------------
INSERT INTO `employees` VALUES ('1@emp.com', '111', NULL, 'ue4', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `employees` VALUES ('2@emp.com', '222', NULL, 'unity', NULL, NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for learning
-- ----------------------------
DROP TABLE IF EXISTS `learning`;
CREATE TABLE `learning`  (
  `mem_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '会员账号',
  `course_id` int(0) NOT NULL COMMENT '课程号',
  `learnedTime` float NULL DEFAULT NULL COMMENT '学习时长',
  `isCollected` tinyint(1) NULL DEFAULT NULL COMMENT '是否收藏',
  `score` float NULL DEFAULT NULL COMMENT '成绩',
  PRIMARY KEY (`mem_id`, `course_id`) USING BTREE,
  INDEX `FK_CLASS_LEARNING_REFERENCE_CLASS`(`course_id`) USING BTREE,
  CONSTRAINT `FK_CLASS_LEARNING_REFERENCE_CLASS` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_LEARNING_REFERENCE_MEMBER` FOREIGN KEY (`mem_id`) REFERENCES `members` (`mem_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of learning
-- ----------------------------

-- ----------------------------
-- Table structure for members
-- ----------------------------
DROP TABLE IF EXISTS `members`;
CREATE TABLE `members`  (
  `mem_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '会员账号',
  `mem_password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '登录密码',
  `idc` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '身份证号',
  `mem_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '会员名',
  `sex` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '性别',
  `birthday` datetime(0) NULL DEFAULT NULL COMMENT '生日',
  `telephone` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '手机号',
  `icon` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '头像',
  `vip_level` int(0) NULL DEFAULT NULL COMMENT '会员等级',
  `balance` float NULL DEFAULT NULL COMMENT '充值余额',
  PRIMARY KEY (`mem_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of members
-- ----------------------------
INSERT INTO `members` VALUES ('1@qq.com', '111111', NULL, 'opda', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `members` VALUES ('2@qq.com', '222222', NULL, 'lcy', NULL, NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for mlevel
-- ----------------------------
DROP TABLE IF EXISTS `mlevel`;
CREATE TABLE `mlevel`  (
  `vip_Level` int(0) NOT NULL,
  `discount` float NULL DEFAULT NULL,
  PRIMARY KEY (`vip_Level`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of mlevel
-- ----------------------------

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news`  (
  `news_id` int(0) NOT NULL AUTO_INCREMENT COMMENT '新闻号',
  `employee_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '职员账号',
  `title` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '新闻标题',
  `info` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '新闻内容',
  `views` int(0) NULL DEFAULT NULL COMMENT '浏览数',
  `picture` varchar(260) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '图片',
  PRIMARY KEY (`news_id`) USING BTREE,
  INDEX `FK_NEWS_REFERENCE_EMPLOYEE`(`employee_id`) USING BTREE,
  CONSTRAINT `FK_NEWS_REFERENCE_EMPLOYEE` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of news
-- ----------------------------

-- ----------------------------
-- Table structure for news_messages
-- ----------------------------
DROP TABLE IF EXISTS `news_messages`;
CREATE TABLE `news_messages`  (
  `message_id` int(0) NOT NULL AUTO_INCREMENT COMMENT '留言编号',
  `mem_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '会员账号',
  `employee_id` char(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '职员账号',
  `news_id` int(0) NULL DEFAULT NULL COMMENT '新闻号',
  `message_info` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '留言内容',
  `message_date` datetime(0) NULL DEFAULT NULL COMMENT '发布时间',
  `reply_info` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '回复内容',
  `reply_date` datetime(0) NULL DEFAULT NULL COMMENT '回复时间',
  PRIMARY KEY (`message_id`) USING BTREE,
  INDEX `FK_NEWS_MESSAGE_REFERENCE_EMPLOYEE`(`employee_id`) USING BTREE,
  INDEX `FK_NEWS_MESSAGE_REFERENCE_MEMBER`(`mem_id`) USING BTREE,
  INDEX `FK_NEWS_MESSAGE_REFERENCE_NEWS`(`news_id`) USING BTREE,
  CONSTRAINT `FK_NEWS_MESSAGE_REFERENCE_EMPLOYEE` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_NEWS_MESSAGE_REFERENCE_MEMBER` FOREIGN KEY (`mem_id`) REFERENCES `members` (`mem_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_NEWS_MESSAGE_REFERENCE_NEWS` FOREIGN KEY (`news_id`) REFERENCES `news` (`news_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of news_messages
-- ----------------------------

-- ----------------------------
-- Table structure for order_details
-- ----------------------------
DROP TABLE IF EXISTS `order_details`;
CREATE TABLE `order_details`  (
  `order_id` int(0) NOT NULL COMMENT '订单号',
  `course_id` int(0) NOT NULL COMMENT '课程号',
  PRIMARY KEY (`order_id`, `course_id`) USING BTREE,
  INDEX `FK_ORDER_DETAILS_REFERENCE_CLASS`(`course_id`) USING BTREE,
  CONSTRAINT `FK_ORDER_DETAILS_REFERENCE_CLASS` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_ORDER_DETAILS_REFERENCE_ORDER` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_details
-- ----------------------------

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `order_id` int(0) NOT NULL AUTO_INCREMENT COMMENT '订单号',
  `mem_id` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '会员账号',
  `order_datetime` datetime(0) NOT NULL COMMENT '下单时间',
  `order_state` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '订单状态',
  `amount` float NOT NULL COMMENT '订单金额',
  `payway` tinyint(0) NULL DEFAULT NULL COMMENT '支付方式',
  `comment` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '评价',
  PRIMARY KEY (`order_id`) USING BTREE,
  INDEX `FK_ORDER_REFERENCE_MEMBER`(`mem_id`) USING BTREE,
  CONSTRAINT `FK_ORDER_REFERENCE_MEMBER` FOREIGN KEY (`mem_id`) REFERENCES `members` (`mem_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------

-- ----------------------------
-- Table structure for resource
-- ----------------------------
DROP TABLE IF EXISTS `resource`;
CREATE TABLE `resource`  (
  `resource_id` int(0) NOT NULL AUTO_INCREMENT,
  `course_id` int(0) NULL DEFAULT NULL COMMENT '课程号',
  `resource_name` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '资源名称',
  `resource_type` tinyint(0) NULL DEFAULT NULL COMMENT '资源种类 0：视频（在线观看），1：课件（下载）',
  `localPath` varchar(260) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '保存路径',
  PRIMARY KEY (`resource_id`) USING BTREE,
  INDEX `FK_Reference_17`(`course_id`) USING BTREE,
  CONSTRAINT `FK_Reference_17` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of resource
-- ----------------------------
INSERT INTO `resource` VALUES (1, 1, NULL, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
