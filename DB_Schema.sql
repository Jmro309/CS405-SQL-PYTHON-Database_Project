-- club
create table club (
    name varchar(100),
    year int check(year between 1900 and 2100),
    primary key (name, year)
);

-- student
create table student (
    studentID char(9) primary key,
    name varchar(100)
);

-- faculty
create table faculty (
    facultyID char(9) primary key,
    name varchar(100)
);

-- budget
create table budget (
    clubName varchar(100),
    clubYear int,
    balance decimal(10,2),
    primary key (clubName, clubYear),
    foreign key (clubName, clubYear)
        references club(name, year)
        on delete cascade
);

-- meeting
create table meeting (
    clubName varchar(100),
    clubYear int,
    meetingDate date,
    startTime time,
    classroom varchar(50),
    description varchar(250),
    duration int check (duration > 0),
    primary key (clubName, clubYear, meetingDate, startTime),
    foreign key (clubName, clubYear)
        references club(name, year)
        on delete cascade
);

-- field trip
create table fieldtrip (
    clubName varchar(100),
    clubYear int,
    destination varchar(100),
    tripDate date,
    tripTime time,
    description varchar(250),
    primary key (clubName, clubYear, destination, tripDate),
    foreign key (clubName, clubYear)
        references club(name, year)
        on delete cascade
);

-- transactions
create table transactions (
    clubName varchar(100),
    clubYear int,
    transactionID char(9),
    transactionDate date,
    description varchar(250),
    amount decimal(10,2),
    transactiontype varchar(50),
    primary key (clubName, clubYear, transactionID),
    foreign key (clubName, clubYear)
        references club(name, year)
        on delete cascade
);

-- membership (join relationship)
create table membership (
    studentID char(9),
    clubName varchar(100),
    clubYear int,
    primary key (studentID, clubName, clubYear),
    foreign key (studentID)
        references student(studentID)
        on delete cascade,
    foreign key (clubName, clubYear)
        references club(name, year)
        on delete cascade
);

-- advisor (faculty advises club)
create table advisor (
    facultyID char(9),
    clubName varchar(100),
    clubYear int,
    primary key (facultyID, clubName, clubYear),
    foreign key (facultyID)
        references faculty(facultyID)
        on delete cascade,
    foreign key (clubName, clubYear)
        references club(name, year)
        on delete cascade
);