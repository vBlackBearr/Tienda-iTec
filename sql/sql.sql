

-- Creación de la tabla partners
CREATE TABLE partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    details VARCHAR(255),
    direction VARCHAR(255),
    api_endpoint VARCHAR(255),
    props JSON,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla partners
INSERT INTO partners (name, details, direction, api_endpoint, props, enabled)
VALUES
    ('Partner 1', 'Details 1', 'Direction 1', 'http://api.example.com/partner1', '{"key": "value1"}', 1),
    ('Partner 2', 'Details 2', 'Direction 2', 'http://api.example.com/partner2', '{"key": "value2"}', 1),
    ('Partner 3', 'Details 3', 'Direction 3', 'http://api.example.com/partner3', '{"key": "value3"}', 1);

-- Creación de la tabla raw_materials
CREATE TABLE raw_materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    props JSON,
    stock INT,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla raw_materials
INSERT INTO raw_materials (name, description, props, stock, enabled)
VALUES
    ('Raw Material 1', 'Description 1', '{"key": "value1"}', 100, 1),
    ('Raw Material 2', 'Description 2', '{"key": "value2"}', 200, 1),
    ('Raw Material 3', 'Description 3', '{"key": "value3"}', 150, 1);

-- Creación de la tabla products
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    props JSON,
    stock INT,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla products
INSERT INTO products (name, description, props, stock, enabled)
VALUES
    ('Product 1', 'Description 1', '{"key": "value1"}', 50, 1),
    ('Product 2', 'Description 2', '{"key": "value2"}', 75, 1),
    ('Product 3', 'Description 3', '{"key": "value3"}', 60, 1);

-- Creación de la tabla raw_materials_partners (relación muchos a muchos entre raw_materials y partners)
CREATE TABLE raw_materials_partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raw_material_id INT,
    partner_id INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id),
    FOREIGN KEY (partner_id) REFERENCES partners(id)
);

-- Datos de prueba para la tabla raw_materials_partners
INSERT INTO raw_materials_partners (raw_material_id, partner_id, props, enabled)
VALUES
    (1, 1, '{"key": "value1"}', 1),
    (2, 2, '{"key": "value2"}', 1),
    (3, 3, '{"key": "value3"}', 1);

-- Creación de la tabla bom (Bill of Materials)
CREATE TABLE bom (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    raw_material_id INT,
    quantity INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id)
);

-- Datos de prueba para la tabla bom
INSERT INTO bom (product_id, raw_material_id, quantity, props, enabled)
VALUES
    (1, 1, 5, '{"key": "value1"}', 1),
    (1, 2, 3, '{"key": "value2"}', 1),
    (2, 3, 4, '{"key": "value3"}', 1);

-- Creación de la tabla sales
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    total DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla sales
INSERT INTO sales (date, total, props, enabled)
VALUES
    ('2023-01-15', 500.00, '{"key": "value1"}', 1),
    ('2023-02-20', 750.50, '{"key": "value2"}', 1),
    ('2023-03-25', 300.25, '{"key": "value3"}', 1);

-- Creación de la tabla products_sales (relación muchos a muchos entre products y sales)
CREATE TABLE products_sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    sale_id INT,
    quantity INT,
    subtotal DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (sale_id) REFERENCES sales(id)
);

-- Datos de prueba para la tabla products_sales
INSERT INTO products_sales (product_id, sale_id, quantity, subtotal, props, enabled)
VALUES
    (1, 1, 2, 100.00, '{"key": "value1"}', 1),
    (1, 2, 3, 150.75, '{"key": "value2"}', 1),
    (2, 3, 1, 75.25, '{"key": "value3"}', 1);


-- Tabla de roles
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(255) NOT NULL,
    enabled BOOLEAN DEFAULT TRUE
);


-- Valores de prueba para la tabla "roles"
INSERT INTO roles (role_name) VALUES
    ('Administrador'),
    ('Editor'),
    ('Usuario');


-- Tabla de usuarios
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role_id INT,
    enabled BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (role_id) REFERENCES roles(id)
);


-- Valores de prueba para la tabla "usuarios"
INSERT INTO users (username, password, email, role_id) VALUES
    ('admin', 'hashed_password_admin', 'admin@example.com', 1),
    ('editor', 'hashed_password_editor', 'editor@example.com', 2),
    ('usuario1', 'hashed_password_user1', 'usuario1@example.com', 3),
    ('usuario2', 'hashed_password_user2', 'usuario2@example.com', 3);