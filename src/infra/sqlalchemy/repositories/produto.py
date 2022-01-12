from sqlalchemy.orm import Session
import src.schemas.produto as schemas
import src.infra.sqlalchemy.models.produto as models

class RepositoryProduto():
    
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            vlr_unit=produto.vlr_unit,
            tamanho=produto.tamanho,
            descricao=produto.descricao,
            ingredientes=produto.ingredientes,
            categoria_id=produto.categoria_id
        )

        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def list(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def get():
        pass

    def delete():
        pass