from typing import List
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.categoria import RepositoryCategoria
from src.infra.sqlalchemy.repositories.produto import RepositoryProduto
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.schemas.usuario import Usuario, UsuarioSimples
from src.schemas.categoria import Categoria
from src.schemas.produto import Produto
from src.infra.sqlalchemy.repositories.usuario import RepositoryUsuario

app = FastAPI()

origins = [
    "https://192.168.100.18:4000",
    "https://pizzarialuigi.ddns.net",
    "http://localhost:4000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples)
def signup(usuario: Usuario, db: Session = Depends(get_db)):
    produto_criado = RepositoryUsuario(db).create(usuario)
    return produto_criado

@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    produtos = RepositoryUsuario(db).read()
    return produtos

@app.put('/usuarios/{id_usuario}', status_code=status.HTTP_200_OK, response_model=Usuario)
def editar_usuario(id_usuario, usuario: Usuario, db: Session = Depends(get_db)):
    RepositoryUsuario(db).update(id_usuario, usuario)
    return usuario

@app.delete('/usuarios/{id_usuario}', status_code=status.HTTP_200_OK)
def excluir_usuario(id_usuario, db: Session = Depends(get_db)):
    RepositoryUsuario(db).delete(id_usuario)
    return {"mensagem": "usuário excluído com sucesso!"}





@app.post('/categorias', status_code=status.HTTP_201_CREATED, response_model=Categoria)
def criar_categoria(categoria: Categoria, session: Session = Depends(get_db)):
    categoria_criada = RepositoryCategoria(session).create(categoria)
    return categoria_criada

@app.get('/categorias', response_model=List[Categoria])
def listar_categorias(session: Session = Depends(get_db)):
    categorias = RepositoryCategoria(session).list()
    return categorias








@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositoryProduto(session).create(produto)
    return produto_criado

@app.get('/produtos', response_model=List[Produto])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositoryProduto(session).list()
    return produtos