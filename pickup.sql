
CREATE TABLE RegisteredUser
(email VARCHAR(256) NOT NULL PRIMARY KEY,
 name VARCHAR(256) NOT NULL,
 wechat VARCHAR(256) NOT NULL UNIQUE,
 phone VARCHAR(256),
 residence VARCHAR(256) NOT NULL,
 age INTEGER NOT NULL,
 gender VARCHAR(256) NOT NULL,
 citizenship VARCHAR(256) NOT NULL,
 department_at_duke VARCHAR(256) NOT NULL,
 undergraduate VARCHAR(256),
 company VARCHAR(256));

CREATE TABLE Volunteer
(email VARCHAR(256) NOT NULL PRIMARY KEY REFERENCES RegisteredUser(email),
 available_time DATE NOT NULL,
 car_plate VARCHAR(256) NOT NULL REFERENCES Car(plate_number),
 driver_license VARCHAR(256) NOT NULL);

CREATE TABLE Flight
(flight_number VARCHAR(256) NOT NULL PRIMARY KEY,
 arrival time DATE NOT NULL,
 terminal VARCHAR(256) NOT NULL);

CREATE TABLE Car
(plate_number VARCHAR(256) NOT NULL PRIMARY KEY,
 capacity Integer NOT NULL);

CREATE TABLE NewStudent
(email VARCHAR(256) NOT NULL PRIMARY KEY REFERENCES RegisteredUser(email),
 flight VARCHAR(256) NOT NULL REFERENCES Flight(flight_number),
 luggage_checked_number INTEGER NOT NULL,
 luggage_carryon_number INTEGER NOT NULL,
 backpack_number INTEGER NOT NULL);

CREATE TABLE Pickup
(volunteer VARCHAR(256) NOT NULL REFERENCES Volunteer(email),
 newstudent VARCHAR(256) NOT NULL REFERENCES NewStudent(email),
 PRIMARY KEY(volunteer, newstudent))
