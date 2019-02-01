create database ria_iniciales;

use ria_iniciales;

create table clientes(
    nombre_c varchar(30) not null primary key,
    apepat_c varchar(20) not null,
    apemat_c varchar(20) not null,
    telefono_c varchar(10) not null,
    email varchar(50) not null
    )ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into clientes (nombre_c, apepat_c, apemat_c, telefono_c, email) values 
('Gabi', 'Curiel', 'Garcia', '7751017401', 'gabi@gmail.com'),
('Isaias', 'Aranda', 'Leal', '7751017401', 'chay@gmail.com'),
('Santiago', 'Garcia', 'Soto', '7751855159', 'santi@gmail.com');

create table productos(
    id_p varchar(5) not null primary key,
    nombre_p varchar(30) not null,
    existencias int not null,
    fecha_c date not null,
    precio double not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into productos(id_p, nombre_p, existencias, fecha_c, precio) values
('01ALP', 'Alpura', 10, '2019/01/10', 20.0),
('02CRE', 'Crema', 5, '2019/02/11', 13.0),
('03BON', 'Bonafon', 30, '2019/04/03', 7.0);

show tables;
select * from clientes;
describe clientes;

select* from productos;
describe productos;


create user 'ria'@'localhost' identified by 'ria.2019';
grant all privileges on ria_iniciales.* to 'ria'@'localhost';
flush privileges; 