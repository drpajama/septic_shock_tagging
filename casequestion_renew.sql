truncate qshock_casequestion CASCADE;
ALTER SEQUENCE qshock_casequestion_id_seq RESTART WITH 1; 
UPDATE qshock_casequestion SET ID = DEFAULT;