-- Create the table in the image
CREATE TABLE nurses(
	Emp_id INT NOT NULL,
    Nurse_name TEXT NOT NULL,
    Status TEXT NOT NULL,
    PRIMARY KEY (Emp_id)
);

-- Create the employees table
CREATE TABLE IF NOT EXISTS doctors(
    Emp_id INT NOT NULL,
    Name TEXT NOT NULL,
    Status TEXT NOT NULL,
    PRIMARY KEY (Emp_id)
);

INSERT INTO nurses (Emp_id, Nurse_name, Status)
VALUES
    (2001, 'Naman Nanda', 'Available'),
    (2002, 'Mohit Marada', 'Available'),
    (2003, 'Panda Bhai', 'Available'),
    (2004, 'Sayak Roy', 'Available'),
    (2005, 'Gowtham', 'Available');
    
INSERT INTO doctors (Emp_id, Name, Status)
VALUES
    (1001, 'Ayush Garg', 'Assigned'),
    (1002, 'Harsh Aswani', 'Assigned'),
    (1003, 'Muntazir Jahangir', 'Assigned'),
    (1004, 'Yashvardhan Gera', 'Available'),
    (1005, 'Dhaivat Vipat', 'Available');