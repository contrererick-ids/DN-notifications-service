from fastapi import APIRouter, HTTPException
from app.schemas import NotificacionRequest
from app.services.sns_service import publicar_notificacion

router = APIRouter(prefix="/notificaciones", tags=["Notificaciones"])


@router.post("/", status_code=200)
def enviar_notificacion(payload: NotificacionRequest):
    try:
        publicar_notificacion(
            folio=payload.folio,
            cliente_id=payload.cliente_id,
            total=payload.total,
            url_descarga=payload.url_descarga,
        )
        return {"status": "ok", "message": f"Notificación enviada para folio {payload.folio}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al publicar en SNS: {str(e)}")
