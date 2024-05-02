import models
from sqlalchemy.orm import Session
import bcrypt


def _add_user_credential(email: str, password: str,dbsession:Session) -> models.Credential:
    password_hash = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode()
    credential = models.Credential(
        email=email, password_hash=password_hash)
    dbsession.add(credential)
    dbsession.commit()
    return credential


def create_user(firstname:str, lastname:str, phone:str, email:str, password:str, role='Booker')->models.Booker:
    with Session(models.engine) as dbsession:
        user_credential = _add_user_credential(email=email, password=password,dbsession = dbsession)
        user = models.Booker(firstname=firstname, lastname=lastname,
                             phone=phone, credential=user_credential.email, role=role)
        dbsession.add(user)
        dbsession.commit()
        return user
