create table admin(
    id serial primary key,
    email varchar(50),
    password varchar(50)
);
insert into admin(email,password) values('admin@gmail.com', 'admin');

create table finition(
    idfinition serial primary key,
    libelle varchar(30),
    augmentation double precision
);


create table travaux(
    idtravaux serial primary key,
    libelle varchar(100),
    unite varchar(20),
    pu double precision,
    code varchar(20)
);

create table maison(
    idmaison serial primary key,
    libelle varchar(30),
    duree double precision,
    surface double precision
);

create table maisontravaux(
    idmaisontravaux serial primary key,
    idmaison int,
    idtravaux int,
    quantite double precision,
    foreign key(idmaison) references maison(idmaison),
    foreign key(idtravaux) references travaux(idtravaux)
);

create table devis(
    iddevis serial primary key,
    idmaison int,
    idfinition int,
    idclient varchar(20),
    debuttravaux date,
    augmentation double precision,
    duree double precision,
    datecreation date,
    reference varchar(20),
    lieu VARCHAR(50),
    foreign key(idmaison) references maison(idmaison),
    foreign key(idfinition) references finition(idfinition)
);

create table paiement(
    idpaiement serial primary key,
    iddevis int,
    montant double precision,
    dateheure date,
    reference varchar(50),
    foreign key(iddevis) references devis(iddevis)
);

create table detaildevis(
    iddetailsdevis serial primary key,
    iddevis int,
    idtravaux int,
    quantite double precision,
    pu double precision,
    foreign key(iddevis) references devis(iddevis),
    foreign key(idtravaux) references travaux(idtravaux)
);




-- Insertion des données dans la table 'finition'
INSERT INTO finition (libelle, augmentation) VALUES 
('Peinture standard', 0),
('Peinture premium', 30),
('Revêtement mural', 50);

-- Insertion des données dans la table 'travaux'
INSERT INTO travaux (libelle, unite, pu, code) VALUES
('Peinture des murs', 'm²', 25.00,  'TRV001'),
('Pose de carrelage', 'm²', 30.00,  'TRV002'),
('Installation de cuisine', 'unité', 2500.00, 'TRV003');

-- Insertion des données dans la table 'maison'
INSERT INTO maison (libelle, duree, surface) VALUES
('Maison principale', 6, 150),
('Maison de vacances', 4, 100);

-- Insertion des données dans la table 'maisontravaux'
INSERT INTO maisontravaux (idmaison, idtravaux, quantite) VALUES
(9, 1, 200),
(10, 2, 120),
(9, 1, 150),
(10, 3, 1);








create view V_mtdevistrav as (
    select d.iddevis,sum(d.quantite*d.pu) as montant from detaildevis d
    group by d.iddevis
);

create or replace view V_mtdevispaye as (
    select de.iddevis,case when vu.montant is null then 0 else vu.montant end as montant from devis de
    left join
    (select d.iddevis,sum(d.montant) as montant from paiement d
    group by d.iddevis) vu on de.iddevis = vu.iddevis
);

create or replace view v_devis as (
    select vu.*,(vu.total - vu.paye) as reste from ( 
    select d.idclient,d.iddevis,m.libelle as maison, f.libelle as finition, d.datecreation, (tot.montant + (tot.montant*d.augmentation/100)) as total,
    paye.montant as paye,
    d.debuttravaux as debut,
    Date(d.debuttravaux + (d.duree || ' days')::interval) AS fin
    from devis d
    join maison m on m.idmaison = d.idmaison
    join finition f on f.idfinition = d.idfinition
    join V_mtdevistrav tot on tot.iddevis = d.iddevis
    join V_mtdevispaye paye on paye.iddevis = d.iddevis
    ) vu
);


create or replace view v_detailsdevise as (
    select ROW_NUMBER() OVER () AS ligne, iddevis,mt.quantite,mt.idtravaux,t.libelle,t.pu,t.unite,quantite*t.pu as valeur  
    from devis as d 
    join maison as m on d.idmaison=m.idmaison 
    join maisontravaux as mt on mt.idmaison=d.idmaison  
    join travaux as t on t.idtravaux=mt.idtravaux 
    group by iddevis,mt.quantite,mt.idtravaux,t.libelle,t.pu,t.unite,valeur
);
--  iddevis | quantite | idtravaux |               libelle               | pu | unite  | valeur


create view v_board as (
select sum(total) as total, sum(paye) as paye, sum(reste) as reste from v_devis
);

CREATE TABLE moi (
    num INT PRIMARY KEY,
    libelle VARCHAR(255)
);

INSERT INTO moi (num, libelle) VALUES 
(1, 'Janvier'),
(2, 'Février'),
(3, 'Mars'),
(4, 'Avril'),
(5, 'Mai'),
(6, 'Juin'),
(7, 'Juillet'),
(8, 'Août'),
(9, 'Septembre'),
(10, 'Octobre'),
(11, 'Novembre'),
(12, 'Décembre');

CREATE TABLE annee (
    annee INT PRIMARY KEY
);

-- Insertion des données de 2019 à 2024
INSERT INTO annee (annee) VALUES 
(2019),
(2020),
(2021),
(2022),
(2023),
(2024);

create or replace view histogramme as (
select ROW_NUMBER() OVER () AS ligne,vu1.*,moi.libelle,case when vu2.montant is null then 0 else vu2.montant end as montant from 
(select annee.annee, moi.num as moi from annee cross join moi) vu1
left join 
(select vu.annee,vu.moi,sum(vu.montant) as montant from (
select EXTRACT(YEAR FROM datecreation) as annee,EXTRACT(MONTH FROM datecreation) as moi,v_devis.total as montant from v_devis
) vu
group by vu.annee, vu.moi
) vu2 on vu2.annee = vu1.annee and vu2.moi = vu1.moi
join moi on moi.num = vu1.moi
);


alter table maison add descriptions varchar(100)