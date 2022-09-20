
create table if not exists produtos (
	id serial primary key,
	descricao VARCHAR(100),
	ativo boolean
);


create table pedidos (
	id_pedido serial primary key,
	id_integracao bigint,
	quantidade double precision,
	id_produto bigint,
	valor_produto double precision,
	observacao varchar(200),
	valor_total_pedido double precision,
	data_pedido timestamp,
	CONSTRAINT fk_produto
		FOREIGN KEY(id_produto)
			REFERENCES produtos(id)
);
-- drop table pedidos;

create table if not exists produtos (
	id serial primary key,
	descricao VARCHAR(100),
	ativo boolean,
)
