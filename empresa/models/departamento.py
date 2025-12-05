from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

@dataclass
class Departamento:

    _numero: int
    _nome: str
    _cpf_gerente: Optional[str] = None
    _created_at: Optional[datetime] = None
    _updated_at: Optional[datetime] = None

    # Departamento -> JSON (dict)
    def to_dict(self) -> dict:
        return {
            'numero': self._numero,
            'nome': self._nome,
            'cpf_gerente': self._cpf_gerente,
            'created_at': self._created_at,
            'updated_at': self._updated_at
        }

    # JSON (dict) -> Departamento
    @classmethod
    def from_dict(cls, data: dict) -> 'Departamento':
        return Departamento(
            data.get('numero'),
            data.get('nome'),
            data.get('cpf_gerente'),
            data.get('created_at'),
            data.get('updated_at')
        )
    
    def __str__(self) -> str:
        return (
            f'Departamento(numero={self._numero}, nome={self._nome}, '
            f'cpf_gerente={self._cpf_gerente}, '
            f'created_at={self._created_at}, updated_at={self._updated_at})'
        )

    @property
    def numero(self) -> int:
        return self._numero
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def cpf_gerente(self) -> Optional[str]:
        return self._cpf_gerente
    
    @property
    def created_at(self) -> Optional[datetime]:
        return self._created_at
    
    @property
    def updated_at(self) -> Optional[datetime]:
        return self._updated_at
