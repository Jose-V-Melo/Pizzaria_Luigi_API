from datetime import datetime
from sqlalchemy import update, delete
from sqlalchemy.orm import Session
import src.schemas.usuario as schemas
import src.infra.sqlalchemy.models.usuario as models

class RepositoryUsuario():
    
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome=usuario.nome,
            senha=usuario.senha,
            email=usuario.email,
            telefone=usuario.telefone,
            foto=usuario.foto,
        )

        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def read(self):
        usuarios = self.session.query(models.Usuario).all()
        return usuarios

    def update(self, id_usuario: int, usuario: schemas.Usuario):
        stmt = (
            update(models.Usuario).where(models.Usuario.id == id_usuario).
            values(
                nome=usuario.nome,
                senha=usuario.senha,
                email=usuario.email,
                telefone=usuario.telefone,
                foto=usuario.foto,
                updated_at=datetime.now()
            )
        )

        self.session.execute(stmt)
        self.session.commit()

    def delete(self, id: int):
        stmt = delete(models.Usuario).where(models.Usuario.id == id)

        self.session.execute(stmt)
        self.session.commit()