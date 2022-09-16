
create table if not exists produtos (
	id serial primary key,
	descricao VARCHAR(100),
	ativo boolean
);


create table if not exists pedidos (
	id serial primary key,
	produto_id int,
	quantidade int,
	data_pedido date,
	CONSTRAiNT fk_produto
		FOREIGN KEY(produto_id)
			REFERENCES produtos(id)
);

-- drop table pedidos;

create table if not exists produtos (
	id serial primary key,
	descricao VARCHAR(100),
	ativo boolean,
)
