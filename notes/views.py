from typing import List
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from psycopg2 import errors
from .response_schemes import ResponseCreateNote, ResponseListNotes
from .schemes import CreateNote
from .models import Notes

notes_router = APIRouter()


@notes_router.post('/notes', status_code=HTTP_201_CREATED, response_model=ResponseCreateNote)
async def create_note(note: CreateNote):
    """
    Create new note in DB
    :param note:
    :return ResponseCreateNote:
    """
    # try:
    try:
        note = Notes.create(
            **note.dict()
        )

    except (errors.UniqueViolation, errors.InFailedSqlTransaction):
        from db import database
        database.commit()
        raise HTTPException(status_code=400,
                            detail=f"Record with slug -> {note.slug} is in DB. Field slug must be unique!")

    return {'id': note.id}


@notes_router.get('/notes', status_code=HTTP_200_OK, response_model=List[ResponseListNotes])
async def get_list_notes():
    """
    Get list if notes from DB
    :return List[ResponseListNotes]:
    """
    return Notes.get_list()


@notes_router.get('/notes/{slug}', status_code=HTTP_200_OK, response_model=ResponseListNotes)
async def get_detail_note(slug: str):
    """
    Get current note from db by slug
    :param slug:
    :return ResponseListNotes:
    """
    return Notes.get_note_by_slug(slug)
