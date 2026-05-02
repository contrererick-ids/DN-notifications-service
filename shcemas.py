from pydantic import BaseModel


class NotificacionRequest(BaseModel):
    folio: str
    cliente_id: int
    total: float
    url_descarga: str
