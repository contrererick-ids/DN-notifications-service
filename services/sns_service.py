import os
import boto3
from dotenv import load_dotenv

load_dotenv()

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
AWS_REGION = os.getenv("AWS_REGION")

sns_client = boto3.client(
    "sns",
    region_name=AWS_REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
)


def publicar_notificacion(folio: str, cliente_id: int, total: float, url_descarga: str):
    mensaje = (
        f"Se ha generado una nueva nota de venta.\n\n"
        f"Folio: {folio}\n"
        f"Cliente ID: {cliente_id}\n"
        f"Total: ${total:.2f}\n\n"
        f"Descarga tu nota en el siguiente enlace (válido por 1 hora):\n{url_descarga}"
    )

    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=mensaje,
        Subject=f"Nueva Nota de Venta - {folio}",
    )
