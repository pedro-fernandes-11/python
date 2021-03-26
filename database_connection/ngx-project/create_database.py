import pyodbc
import names
from random import randint
import random
import datetime

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=PC-GAMERM-41;"
                      "Database=projetoNGX;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()

states = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins'
    }


def create_table_clientes():
    try:
        cursor.execute(f'drop table clientes')
    except Exception as e:
        print("Não da pra dropar clientes: não existe")

    cursor.execute(
        f'create table clientes'
        '(id_cliente integer not null,'
        'first_name varchar(15) not null,'
        'last_name varchar(15) not null,'
        'dt_nascimento date not null,'
        'dt_cadastro date not null)'
    )

    cursor.commit()

    try:
        cursor.execute('alter table clientes drop constraint PK_cliente')
    except Exception as e:
        print("Não da pra dropar PK_cliente: não existe")

    cursor.execute(
        'alter table clientes add constraint PK_cliente primary key(id_cliente)'
    )

    cursor.commit()


def insert_data_into_clientes(number):
    for i in range(1, number + 1):
        now = datetime.datetime.now()
        random_day_nascimento = str(randint(1900, now.year - 18)) + '-' + str(randint(1, 12)) \
                                + '-' + str(randint(1, 30))
        random_day_cadastro = str(randint(int(random_day_nascimento.split('-')[0]), now.year))\
                              + '-' + str(randint(1, 12)) + '-' + str(randint(1, 30))
        insert_into = f"INSERT INTO clientes VALUES (?,?,?,?,?)"
        try:
            cursor.execute(insert_into, (i, names.get_first_name(),
                           names.get_last_name(),
                           random_day_nascimento, random_day_cadastro)
                           )
        except Exception as e:
            print(e)
            cursor.execute(insert_into, (i, names.get_first_name(),
                           names.get_last_name(),
                           '01-01-2000', '01-01-2010')
                           )

        cursor.commit()


def create_table_produtos():
    try:
        cursor.execute(f'drop table produtos')
    except Exception as e:
        print("Não da pra dropar produtos: não existe")

    cursor.execute(
        f'create table produtos'
        '(id_produto integer not null,'
        'nm_produto varchar(25) not null,'
        'preço_produto decimal(7, 2) not null)'
    )

    cursor.commit()

    try:
        cursor.execute('alter table produtos drop constraint PK_produto')
    except Exception as e:
        print("Não da pra dropar PK_produto: não existe")

    cursor.execute(
        'alter table produtos add constraint PK_produto primary key(id_produto)'
    )

    cursor.commit()


def insert_data_into_produtos():
    nm_produtos = ["Celular IPhone", "Celular Samsung", "Celular Xiaomi", "Celular LG", "Celular Motorola",
                   "Celular Mobicel", "Notebook Lenovo", "Notebook Positivo", "Notebook Acer", "Notebook Dell"]
    for each in nm_produtos:
        price = random.uniform(1000, 9999)
        insert_into = f"INSERT INTO produtos VALUES (?,?,?)"
        cursor.execute(insert_into, (nm_produtos.index(each) + 1, each, round(price, 2)))
        cursor.commit()


def create_table_estados():
    try:
        cursor.execute(f'drop table estados')
    except Exception as e:
        print("Não da pra dropar estados: não existe")

    cursor.execute(
        f'create table estados'
        '(cd_estado char(2) not null,'
        'nm_estado varchar(20) not null)'
        )

    cursor.commit()

    try:
        cursor.execute('alter table estados drop constraint PK_estado')
    except Exception as e:
        print("Não da pra dropar PK_estado: não existe")

    cursor.execute(
        'alter table estados add constraint PK_estado primary key(cd_estado)'
    )

    cursor.commit()


def insert_data_into_estados(states_inside_estados):
    insert_into = f"INSERT INTO estados VALUES (?,?)"

    for each_cd, each_nm in states_inside_estados.items():
        cursor.execute(insert_into, (each_cd, each_nm))


def create_table_vendas():
    try:
        cursor.execute(f'drop table vendas')
    except Exception as e:
        print("Não da pra dropar vendas: não existe")

    cursor.execute(
        f'create table vendas'
        '(id_venda integer not null,'
        'id_produto integer not null,'
        'id_cliente integer not null,'
        'cd_estado char(2) not null)'
        )

    cursor.commit()

    try:
        cursor.execute('alter table vendas drop constraint PK_venda')
        cursor.execute('alter table vendas drop constraint FK_cliente')
    except Exception as e:
        print("Não da pra dropar PK_venda: não existe")

    # Primary key
    cursor.execute(
        'alter table vendas add constraint PK_venda primary key(id_venda)'
    )

    # Foreign key
    cursor.execute(
        'alter table vendas add constraint FK_produto foreign key(id_produto) references produtos(id_produto)'
    )
    cursor.execute(
        'alter table vendas add constraint FK_cliente foreign key(id_cliente) references clientes(id_cliente)'
    )
    cursor.execute(
        'alter table vendas add constraint FK_estado foreign key(cd_estado) references estados(cd_estado)'
    )

    cursor.commit()


def insert_data_into_vendas(number, states_inside_vendas):
    insert_into = f"INSERT INTO vendas VALUES (?,?,?,?)"
    cd_estados = list(states_inside_vendas.keys())
    for i in range(1, number + 1):
        cursor.execute(insert_into, (i, randint(1, 10), randint(1, 100), cd_estados[randint(0, 26)]))
        cursor.commit()


create_table_produtos()
insert_data_into_produtos()

create_table_clientes()
insert_data_into_clientes(100)

create_table_estados()
insert_data_into_estados(states)

create_table_vendas()
insert_data_into_vendas(500, states)

conn.close()