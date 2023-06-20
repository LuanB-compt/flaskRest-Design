CREATE TABLE Room (
    ID       integer  PRIMARY KEY NOT NULL,
    Capacity integer  NOT NULL,
    Filled   integer  DEFAULT 0
);

CREATE TABLE Student (
    ID            integer PRIMARY KEY NOT NULL ,
    Name_         text    NOT NULL,
    CPF           text    NOT NULL
);

CREATE TABLE Lecture (
    ID          integer       PRIMARY KEY NOT NULL,
    RoomID      integer       NOT NULL,
    UserID      integer       NOT NULL,
    FOREIGN KEY (RoomID)      REFERENCES Room(ID),
    FOREIGN KEY (ProfessorID) REFERENCES Professor(ID)
);