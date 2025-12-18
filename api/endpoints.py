from fastapi import APIRouter
from api.protocol import (
    status_response,
    command_response,
    research_state
)

router = APIRouter()


@router.get("/status")
def status():
    """
    Jarvis: "Research kaha tak pahuncha?"
    """
    return status_response()


@router.post("/command")
def command(cmd: dict):
    """
    Jarvis: start / stop / focus / summarize
    """
    return command_response(cmd)


@router.get("/state")
def state():
    """
    Internal detailed state
    """
    return research_state()
