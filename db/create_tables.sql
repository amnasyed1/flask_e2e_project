CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    date_of_birth DATE 
)


CREATE TABLE allergy_tests (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    test_result VARCHAR(100) NOT NULL,
    test_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);

