-- Crear la base de datos
CREATE DATABASE AsistenteDB;
GO

USE AsistenteDB;
GO

-- Crear tablas de ejemplo
CREATE TABLE Clientes (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Email VARCHAR(100)
);
GO

CREATE TABLE Pedidos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    ClienteId INT FOREIGN KEY REFERENCES Clientes(Id),
    Fecha DATE,
    Monto DECIMAL(10,2)
);
GO

-- Insertar datos de ejemplo
INSERT INTO Clientes (Nombre, Apellido, Email) VALUES
('Juan', 'Pérez', 'juan.perez@example.com'),
('María', 'Gómez', 'maria.gomez@example.com');
GO

INSERT INTO Pedidos (ClienteId, Fecha, Monto) VALUES
(1, '2023-01-15', 150.00),
(2, '2023-02-20', 200.00);
GO
