from fastapi import APIRouter

from models import ActorCreateRequestDto
from services import ActorService

controller = APIRouter(prefix="/actor")


@controller.post("/actor")
def actor_create(actor: ActorCreateRequestDto):
    return ActorService.create_actor(actor)
