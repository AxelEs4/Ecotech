SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `tiempo`;
DROP TABLE IF EXISTS `asignacion_emp`;
DROP TABLE IF EXISTS `proyecto`;
DROP TABLE IF EXISTS `empleado`;
DROP TABLE IF EXISTS `departamento`;
DROP TABLE IF EXISTS `usuarios`;
SET FOREIGN_KEY_CHECKS = 1;

-- 1. Tabla Usuarios (Autenticación y Sistema)
CREATE TABLE `usuarios` (
  `user_id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `apellidos` VARCHAR(200) NOT NULL,
  `correo` VARCHAR(100) NOT NULL UNIQUE,
  `tipo_usuario` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Tabla Departamento (Se crea antes de Empleado)
CREATE TABLE `departamento` (
  `departamento_id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `descripcion` VARCHAR(200) DEFAULT NULL,
  `gerente_emp_id` INT(11) DEFAULT NULL,
  PRIMARY KEY (`departamento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Tabla Empleado
CREATE TABLE `empleado` (
  `empleado_id` INT(11) NOT NULL AUTO_INCREMENT,
  `run` VARCHAR(12) NOT NULL UNIQUE,
  `nombre` VARCHAR(100) NOT NULL,
  `direccion` VARCHAR(200) DEFAULT NULL,
  `telefono` VARCHAR(20) DEFAULT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `salario` DECIMAL(12,2) NOT NULL,
  `departamento_id` INT(11) NOT NULL,
  PRIMARY KEY (`empleado_id`),
  CONSTRAINT `fk_emp_depto` FOREIGN KEY (`departamento_id`) 
    REFERENCES `departamento` (`departamento_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Relación circular de Gerente en Departamento
ALTER TABLE `departamento`
  ADD CONSTRAINT `fk_depto_gerente` FOREIGN KEY (`gerente_emp_id`) 
    REFERENCES `empleado` (`empleado_id`) ON DELETE SET NULL ON UPDATE CASCADE;

-- 4. Tabla Proyecto
CREATE TABLE `proyecto` (
  `proyecto_id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `descripcion` VARCHAR(200) DEFAULT NULL,
  `fecha_inicio` DATE NOT NULL,
  PRIMARY KEY (`proyecto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. Tabla Asignación de Empleados a Proyectos (Muchos a Muchos)
CREATE TABLE `asignacion_emp` (
  `empleado_id` INT(11) NOT NULL,
  `proyecto_id` INT(11) NOT NULL,
  `rol` VARCHAR(100) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  PRIMARY KEY (`empleado_id`, `proyecto_id`),
  CONSTRAINT `fk_asig_empleado` FOREIGN KEY (`empleado_id`) 
    REFERENCES `empleado` (`empleado_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_asig_proyecto` FOREIGN KEY (`proyecto_id`) 
    REFERENCES `proyecto` (`proyecto_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. Tabla Registro de Tiempo (Horas trabajadas)
CREATE TABLE `tiempo` (
  `tiempo_id` INT(11) NOT NULL AUTO_INCREMENT,
  `empleado_id` INT(11) NOT NULL,
  `proyecto_id` INT(11) NOT NULL,
  `fecha` DATE NOT NULL,
  `horas` DECIMAL(4,2) NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`tiempo_id`),
  CONSTRAINT `fk_tiempo_empleado` FOREIGN KEY (`empleado_id`) 
    REFERENCES `empleado` (`empleado_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_tiempo_proyecto` FOREIGN KEY (`proyecto_id`) 
    REFERENCES `proyecto` (`proyecto_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;