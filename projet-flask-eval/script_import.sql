-- Maison ty
create or replace view v_imp_maison as (
select distinct type_maison,duree_travaux,surface,description from importmaisontravaux i
where type_maison not in (select libelle from maison)
);

insert into maison (libelle, duree,surface,descriptions) select * from v_imp_maison;


-- travaux 
create view v_imp_travaux as (
select distinct type_travaux,unite,prix_unitaire,code_travaux from importmaisontravaux i
where type_travaux not in (select libelle from travaux)
);

insert into travaux (libelle,unite,pu,code) select * from v_imp_travaux;

-- maison_travaux
create view v_imp_maisontravaux as (
select m.idmaison,t.idtravaux,i.quantite from importmaisontravaux i 
join maison m on m.libelle  = i.type_maison
join travaux t on t.libelle = i.type_travaux
);

insert into maisontravaux (idmaison,idtravaux,quantite) select * from v_imp_maisontravaux;


-- Finition
create view v_imp_finition as (
select distinct finition,taux_finition from importdevis i
where finition not in (select libelle from finition)
);

insert into finition (libelle, augmentation) select * from v_imp_finition;


-- Devis
create view v_imp_devis as (
select m.idmaison,f.idfinition,i.client,i.date_debut,i.taux_finition,m.duree,i.date_devis,i.ref_devis,i.lieu from importdevis i
join maison m on m.libelle = i.type_maison
join finition f on f.libelle = i.finition
);

insert into devis (idmaison,idfinition,idclient,debuttravaux,augmentation,duree,datecreation,reference,lieu) select * from v_imp_devis;



-- Details Devis

create view v_imp_detaildevis as (
select d.iddevis,t.idtravaux,m.quantite,t.pu from importdevis i 
join devis d  on d.reference = i.ref_devis
join maisontravaux m on d.idmaison = m.idmaison
join travaux t on t.idtravaux = m.idtravaux
);

insert into detaildevis (iddevis,idtravaux,quantite,pu) select * from v_imp_detaildevis;


--Paiement
create view v_imp_paiement as (
select d.iddevis,i.montant,i.date_paiement,i.ref_paiement from importpaiement i
join devis d on d.reference = i.ref_devis
);

insert into paiement (iddevis,montant,dateheure,reference) select * from v_imp_paiement;

