
CREATE TABLE partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    details VARCHAR(255),
    direction VARCHAR(255),
    api_endpoint VARCHAR(255),
    props JSON,
    enabled BOOLEAN
);


CREATE TABLE raw_materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    partner_id INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (partner_id) REFERENCES partners(id)
);


CREATE TABLE raw_materials_stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raw_material_id INT,
    stock INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id)
);


CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    props JSON,
    enabled BOOLEAN
);


CREATE TABLE products_stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    stock INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES products(id)
);


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

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    total DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN
);


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
