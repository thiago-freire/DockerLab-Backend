DROP TABLE NODOCKER;
DROP TABLE USUARIO;
DROP TABLE MAQUINA;

CREATE TABLE MAQUINA (
	id_maquina SERIAL PRIMARY KEY, 
	ip TEXT NOT NULL, 
	nome TEXT,
	usuario TEXT NOT NULL, 
	senha TEXT NOT NULL, 
	porta INTEGER NOT NULL,
    data_cadastro timestamp without time zone NOT NULL
);

CREATE TABLE USUARIO (
	id_usuario SERIAL PRIMARY KEY, 
	email TEXT NOT NULL, 
	nome TEXT,
	perfil TEXT NOT NULL,
    data_cadastro timestamp without time zone NOT NULL
);

CREATE TABLE NODOCKER (
	id SERIAL PRIMARY KEY, 
	nome TEXT NOT NULL,
	id_maquina INTEGER NOT NULL,
	id_usuario INTEGER NOT NULL,
	cpu_cores INTEGER NOT NULL,
	ram INTEGER NOT NULL,
	device INTEGER NOT NULL,
	network INTEGER NOT NULL,
    data_cadastro timestamp without time zone NOT NULL,
	FOREIGN KEY (id_maquina) REFERENCES Maquina (id_maquina),
	FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario)
);