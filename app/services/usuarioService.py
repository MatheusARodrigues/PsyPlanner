from models.usuario import Usuario
from schemas.usuarioSchema import UsuarioInformacoes
from sqlalchemy.orm import Session

def get_all(db: Session):
    return db.query(Usuario).all()

def post_user(db: Session, usuario: UsuarioInformacoes):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        return None
    
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=usuario.senha_hash,
        telefone=usuario.telefone,
        ativo=usuario.ativo,
        data_criacao=usuario.data_criacao
    )
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return novo_usuario