SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `tiempo`;
DROP TABLE IF EXISTS `asignacion_emp`;
DROP TABLE IF EXISTS `proyecto`;
DROP TABLE IF EXISTS `empleado`;
DROP TABLE IF EXISTS `departamento`;
DROP TABLE IF EXISTS `usuarios`;
SET FOREIGN_KEY_CHECKS = 1;

-- 1. Departamento
CREATE TABLE `departamento` (
  `departamento_id` INT AUTO_INCREMENT PRIMARY KEY,
  `nombre` VARCHAR(200) NOT NULL UNIQUE,
  `descripcion` VARCHAR(200) NOT NULL,
  `gerente_emp_id` INT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Empleado
CREATE TABLE `empleado` (
  `empleado_id` INT AUTO_INCREMENT PRIMARY KEY,
  `run` VARCHAR(12) NOT NULL UNIQUE,
  `nombre` VARCHAR(100) NOT NULL,
  `direccion` VARCHAR(200) NOT NULL,
  `telefono` VARCHAR(20) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `salario` FLOAT NOT NULL,
  `departamento_id` INT NOT NULL,
  CONSTRAINT `fk_emp_depto` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`departamento_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Agregar relación circular del gerente al departamento
ALTER TABLE `departamento`
  ADD CONSTRAINT `fk_depto_gerente` FOREIGN KEY (`gerente_emp_id`) REFERENCES `empleado` (`empleado_id`) ON DELETE SET NULL ON UPDATE CASCADE;

-- 3. Proyecto
CREATE TABLE `proyecto` (
  `proyecto_id` INT AUTO_INCREMENT PRIMARY KEY,
  `nombre` VARCHAR(50) NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  `fecha_inicio` DATE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. Asignación (Tabla Intermedia)
CREATE TABLE `asignacion_emp` (
  `empleado_id` INT NOT NULL,
  `proyecto_id` INT NOT NULL,
  `rol` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`empleado_id`, `proyecto_id`),
  CONSTRAINT `fk_asig_emp` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`empleado_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_asig_proy` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`proyecto_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. Registro de Tiempo
CREATE TABLE `tiempo` (
  `tiempo_id` INT AUTO_INCREMENT PRIMARY KEY,
  `empleado_id` INT NOT NULL,
  `proyecto_id` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `horas` FLOAT NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  CONSTRAINT `fk_tiempo_emp` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`empleado_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_tiempo_proy` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`proyecto_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. Usuarios del sistema (Login)
CREATE TABLE `usuarios` (
  `user_id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(50) NOT NULL UNIQUE,
  `password` VARCHAR(12) NOT NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `apellidos` VARCHAR(200) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `tipo_usuario` VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;