-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`patron`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`patron` (
  `PAT_ID DECIMAL(10,0)` INT NOT NULL,
  `PAT_FNAME (20)` VARCHAR(45) NULL,
  `PAT_LNAME (20)` VARCHAR(45) NULL,
  `PAT_TYPE (10)` VARCHAR(45) NULL,
  `Checkout_CHECK_NUM DECIMAL (15,0)` INT NULL,
  PRIMARY KEY (`PAT_ID DECIMAL(10,0)`),
  INDEX `fk_patron_Checkout_idx` (`Checkout_CHECK_NUM DECIMAL (15,0)` ASC) VISIBLE,
  CONSTRAINT `fk_patron_Checkout`
    FOREIGN KEY (`Checkout_CHECK_NUM DECIMAL (15,0)`)
    REFERENCES `mydb`.`Checkout` (`CHECK_NUM DECIMAL (15,0)`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`author` (
  `AU_ID DECIMAL (7,0)` INT NOT NULL,
  `AU_FNAME` VARCHAR(30) NULL,
  `AU_LNAME` VARCHAR(30) NULL,
  `AU_BIRTHYEAR DECIMAL (4,0)` VARCHAR(45) NULL,
  PRIMARY KEY (`AU_ID DECIMAL (7,0)`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`writes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`writes` (
  `BOOK_NUM DECIMAL (10,0)` INT NOT NULL,
  `AU_ID DECIMAL (7,0)` VARCHAR(45) NULL,
  `author_AU_ID DECIMAL (7,0)` INT NOT NULL,
  PRIMARY KEY (`BOOK_NUM DECIMAL (10,0)`, `author_AU_ID DECIMAL (7,0)`),
  INDEX `fk_writes_author1_idx` (`author_AU_ID DECIMAL (7,0)` ASC) VISIBLE,
  CONSTRAINT `fk_writes_author1`
    FOREIGN KEY (`author_AU_ID DECIMAL (7,0)`)
    REFERENCES `mydb`.`author` (`AU_ID DECIMAL (7,0)`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`book`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`book` (
  `BOOK_NUM DECIMAL (10,0)` INT NOT NULL,
  `BOOK_TITLE` VARCHAR(120) NULL,
  `BOOK_YEAR DECIMAL (4,0)` VARCHAR(45) NULL,
  `BOOK_COST DECIMAL (8,2)` VARCHAR(45) NULL,
  `BOOK_SUBJECT` VARCHAR(120) NULL,
  `PAT_ID DECIMAL (10,0)` VARCHAR(45) NULL,
  `patron_PAT_ID DECIMAL(10,0)` INT NULL,
  `writes_BOOK_NUM DECIMAL (10,0)` INT NULL,
  PRIMARY KEY (`BOOK_NUM DECIMAL (10,0)`, `writes_BOOK_NUM DECIMAL (10,0)`),
  INDEX `fk_book_patron1_idx` (`patron_PAT_ID DECIMAL(10,0)` ASC) VISIBLE,
  INDEX `fk_book_writes1_idx` (`writes_BOOK_NUM DECIMAL (10,0)` ASC) VISIBLE,
  CONSTRAINT `fk_book_patron1`
    FOREIGN KEY (`patron_PAT_ID DECIMAL(10,0)`)
    REFERENCES `mydb`.`patron` (`PAT_ID DECIMAL(10,0)`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_book_writes1`
    FOREIGN KEY (`writes_BOOK_NUM DECIMAL (10,0)`)
    REFERENCES `mydb`.`writes` (`BOOK_NUM DECIMAL (10,0)`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Checkout`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Checkout` (
  `CHECK_NUM DECIMAL (15,0)` INT NOT NULL,
  `BOOK_NUM DECIMAL (10,0)` VARCHAR(45) NULL,
  `PAT_ID DECIMAL(10,0)` VARCHAR(45) NULL,
  `CHECK_OUT_DATE DATE` VARCHAR(45) NULL,
  `CHECK_DUE_DATE DATE` VARCHAR(45) NULL,
  `CHECK_IN_DATE DATE` VARCHAR(45) NULL,
  `book_BOOK_NUM DECIMAL (10,0)` INT NOT NULL,
  PRIMARY KEY (`CHECK_NUM DECIMAL (15,0)`),
  INDEX `fk_Checkout_book1_idx` (`book_BOOK_NUM DECIMAL (10,0)` ASC) VISIBLE,
  CONSTRAINT `fk_Checkout_book1`
    FOREIGN KEY (`book_BOOK_NUM DECIMAL (10,0)`)
    REFERENCES `mydb`.`book` (`BOOK_NUM DECIMAL (10,0)`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
