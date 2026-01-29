from sqlalchemy.orm import Session
from models.email import EmailCode
from scripts.scripts_email_recovery import send_email


def start_password_recovery(session: Session, email: str):
    code, expires_at = send_email(email)

    session.query(EmailCode)\
        .filter(EmailCode.email == email)\
        .delete()

    record = EmailCode(
        email=email,
        code=code,
        expires_at=expires_at
    )

    session.add(record)
    session.commit()