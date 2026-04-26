-- clubs
insert into club (name, year) values
('Chemistry Club', 2026),
('Cipher Design Enthusiasts', 2026),
('National Honor Society', 2026),
('Alpha Club', 2026),
('Chess Club', 2026),
('Art Club', 2025),
('Alpha Club', 2025),
('Chess Club', 2025);

-- students
insert into student (studentID, name) values
('689841389', 'Jesse Pinkman'),
('381568890', 'Alice Lovelace'),
('463467847', 'Bob Smith'),
('751262875', 'Eve Dropper'),
('777988757', 'Beta Prune'),
('243751057', 'Levy Rozman'),
('846190944', 'Andy Warhol');

-- faculty
insert into faculty (facultyID, name) values
('971413406', 'Mr. Torvalds'),
('228415060', 'Mrs. Green'),
('841562807', 'Mr. White'),
('461897099', 'Mr. Chad'),
('579031740', 'Mrs. Harmon');

-- budgets
insert into budget (clubName, clubYear, balance) values
('Chemistry Club', 2026, 200.00),
('Cipher Design Enthusiasts', 2026, 500.00),
('National Honor Society', 2026, 200.00),
('Alpha Club', 2026, 100.00),
('Chess Club', 2026, 80.00),
('Art Club', 2025, 200.00),
('Alpha Club', 2025, 100.00),
('Chess Club', 2025, 100.00);

-- advisor
insert into advisor (facultyID, clubName, clubYear) values
('841562807', 'Chemistry Club', 2026),
('971413406', 'Cipher Design Enthusiasts', 2026),
('228415060', 'National Honor Society', 2026), 
('461897099', 'Alpha Club', 2026),
('579031740', 'Chess Club', 2026),
('228415060', 'Art Club', 2025),
('841562807', 'Alpha Club', 2025),
('971413406', 'Chess Club', 2025);

-- memberships
insert into membership (studentID, clubName, clubYear) values
('689841389', 'Chemistry Club', 2026),
('689841389', 'Alpha Club', 2026),

('381568890', 'Cipher Design Enthusiasts', 2026),
('381568890', 'National Honor Society', 2026),

('463467847', 'Cipher Design Enthusiasts', 2026),
('463467847', 'National Honor Society', 2026),

('751262875', 'Cipher Design Enthusiasts', 2026),

('777988757', 'Alpha Club', 2026),
('777988757', 'Chess Club', 2026),
('777988757', 'Alpha Club', 2025),
('777988757', 'Chess Club', 2025),

('243751057', 'Chess Club', 2026),
('243751057', 'Chess Club', 2025),

('846190944', 'Art Club', 2025);

-- meetings
insert into meeting (clubName, clubYear, meetingDate, startTime, classroom, description, duration) values
('Chemistry Club', 2026, '2026-02-05', '15:00:00', 'SCI101', 'Outdoor lab experiment session', 90),
('Chemistry Club', 2026, '2026-02-19', '15:00:00', 'SCI101', 'Acid-base reactions practice', 90),

('Cipher Design Enthusiasts', 2026, '2026-02-06', '16:00:00', 'CS201', 'Cryptography security discussion', 75),
('Cipher Design Enthusiasts', 2026, '2026-02-20', '16:00:00', 'CS201', 'RSA implementation workshop', 75),

('National Honor Society', 2026, '2026-10-10', '14:00:00', 'AUD1', 'Volunteer planning session', 60),
('National Honor Society', 2026, '2026-11-14', '14:00:00', 'AUD1', 'Scholarship application review', 60),

('Alpha Club', 2026, '2026-03-01', '17:00:00', 'ROOM105', 'Leadership brainstorming session', 60),
('Alpha Club', 2026, '2026-03-15', '17:00:00', 'ROOM105', 'Team building exercises', 60),

('Chess Club', 2026, '2026-02-08', '16:30:00', 'LIB201', 'Opening theory discussion', 90),
('Chess Club', 2026, '2026-02-22', '16:30:00', 'LIB201', 'Practice matches', 90),

('Art Club', 2025, '2025-09-12', '15:30:00', 'ART105', 'Sketching fundamentals', 120),
('Art Club', 2025, '2025-10-03', '15:30:00', 'ART105', 'Watercolor techniques', 120),

('Alpha Club', 2025, '2025-09-20', '17:00:00', 'ROOM105', 'Intro leadership workshop', 60),

('Chess Club', 2025, '2025-09-25', '16:00:00', 'LIB201', 'Beginner tournament prep', 90);

-- transactions
insert into transactions (clubName, clubYear, transactionID, transactionDate, description, amount, transactiontype) values

('Chemistry Club', 2026, 'T10000001', '2026-02-05', 'Lab supplies purchase', 18.75, 'expense'),
('Chemistry Club', 2026, 'T10000002', '2026-02-19', 'Donation from alumni', 25.00, 'income'),

('Cipher Design Enthusiasts', 2026, 'T10000003', '2026-02-06', 'Encryption software license', 12.50, 'expense'),
('Cipher Design Enthusiasts', 2026, 'T10000004', '2026-02-20', 'Club fundraiser', 30.00, 'income'),

('National Honor Society', 2026, 'T10000005', '2026-10-10', 'Volunteer supplies', 22.00, 'expense'),
('National Honor Society', 2026, 'T10000006', '2026-11-14', 'Community donation', 40.00, 'income'),

('Alpha Club', 2026, 'T10000007', '2026-03-01', 'Team materials', 15.25, 'expense'),
('Alpha Club', 2026, 'T10000008', '2026-03-15', 'Membership dues', 35.00, 'income'),

('Chess Club', 2026, 'T10000009', '2026-02-08', 'Chess sets replacement pieces', 10.00, 'expense'),
('Chess Club', 2026, 'T10000010', '2026-02-22', 'Tournament entry fees covered', 20.00, 'income'),

('Art Club', 2025, 'T10000011', '2025-09-12', 'Paint and brushes', 19.99, 'expense'),
('Art Club', 2025, 'T10000012', '2025-10-03', 'Art show ticket sales', 50.00, 'income'),

('Alpha Club', 2025, 'T10000013', '2025-09-20', 'Leadership workshop materials', 14.50, 'expense'),

('Chess Club', 2025, 'T10000014', '2025-09-25', 'Beginner chess clocks', 16.00, 'expense');

