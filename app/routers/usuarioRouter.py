from fastapi import status, HTTPException, Depends, APIRouter, Response
from typing import List, Optional
from data.conexao import get_db 
from sqlalchemy.orm import Session
import services.usuarioService as service
from schemas.usuarioSchema import UsuarioBase, UsuarioInformacoes
router = APIRouter(
)

@router.get("/usuario/", response_model=List[UsuarioBase])
async def listar_usuarios(db: Session = Depends(get_db)):
    lista_usuarios = service.get_all(db)
    if not lista_usuarios:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return lista_usuarios

@router.post("/usuarios/", response_model=UsuarioInformacoes)
async def criar_usuario(usuario: UsuarioInformacoes, db: Session = Depends(get_db)):
    novo_usuario = service.post_user(db, usuario) 
    if not novo_usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado") 
    return novo_usuario