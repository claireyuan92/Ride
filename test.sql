INSERT INTO RegisteredUser VALUES('abc@duke.edu', 'abc', 'abcwechat', '9198080000', 'the swift', 22, 'male', 'China', 'ECE', 'Nanjing University', NULL);
--
--
INSERT INTO RegisteredUser VALUES('xyz@duke.edu', 'xyz', 'xyzwechat', '9198081111', 'the UA APT', 24, 'female', 'China', 'CS', 'Beijing University', NULL);
--
--
INSERT INTO RegisteredUser VALUES('123@duke.edu', '123', '123wechat', '9198083333', 'the pp APT', 23, 'female', 'China', 'CS', 'Tianjing University', NULL);
--
INSERT INTO RegisteredUser VALUES('456@duke.edu', '456', '456wechat', '9198083333', 'the belmont APT', 25, 'male', 'China', 'Econ', 'Shandong University', NULL);

--
--
--
INSERT INTO Car VALUES('NC2015', 2);
INSERT INTO Car VALUES('NC2009', 1);
--
--
--
INSERT INTO Volunteer VALUES('abc@duke.edu', '2015-09-28 10:00:00', 'NC2015', 'ABC123456789');
--
INSERT INTO Volunteer VALUES('456@duke.edu', '2015-09-29 12:00:00', 'NC2009', '456123456789');
--
--
--
INSERT INTO Flight VALUES('FLN123', '2015-09-28 11:00:00', 'F8');
--
INSERT INTO Flight VALUES('FLNxyz', '2015-09-30 13:00:00', 'N18');
--
--
--
INSERT INTO NewStudent VALUES('xyz@duke.edu', 'FLN123', 1, 1, 1);
--
--
INSERT INTO NewStudent VALUES('123@duke.edu', 'FLNxyz', 2, 1, 1);
--
--
--
SELECT * FROM NewStudent, RegisteredUser
WHERE  department_at_duke = 'CS' AND NewStudent.email = RegisteredUser.email;
