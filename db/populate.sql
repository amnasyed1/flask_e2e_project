show databases;
use allergy;
show tables;

INSERT INTO patients (id, first_name, last_name, date_of_birth, gender) VALUES
('131313', 'Phillip', 'Duran', '1996-07-22', 'Male'),
('878787', 'Alan', 'Brown', '1967-08-06', 'Male'),
('101010', 'Mark', 'Dixon', '1980-12-22', 'Male'),
('181818', 'Renee', 'Garcia', '2021-03-28', 'Female'),
('636363', 'Joshua', 'Holmes', '1962-08-19', 'Male'),
('123456', 'Daniel', 'Rivera', '2016-10-26', 'Male'),
('127464', 'Rita', 'Perry', '1999-06-17', 'Female'), 
('765434', 'Joanne', 'Washington', '1989-03-29', 'Female'),
('041408', 'Nathan', 'Howard', '2013-06-23', 'Male'),
('190814', 'Alexandra', 'Barnett', '1970-08-11', 'Female');

INSERT INTO allergy_tests (id, patient_id, test_name, test_result, test_date) VALUES 
('20424475', '131313', 'Soy skin test', 'Positive', '2023-10-22'),
('58357624', '878787', 'Wheat skin test', 'Negative', '2023-09-26'),
('23975635', '101010', 'Sesame blood test', 'Negative', '2023-08-12'),
('57264953', '181818', 'Fish blood test', 'Positive', '2023-07-09'),
('83752358', '636363', 'Eggs blood test', 'Positive', '2023-10-01'),
('94856353', '123456', 'Wheat blood test', 'Negative', '2023-01-22'),
('76734924', '127464', 'Milk blood test', 'Positive', '2023-10-12'),
('37244245', '765434', 'Peanuts blood test', 'Negative', '2023-04-19'),
('87525748', '041408', 'Crustacean shellfish blood test', 'Positive', '2023-05-05'),
('10475625', '190814', 'Sesame skin test', 'Positive', '2023-03-27');