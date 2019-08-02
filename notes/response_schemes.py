from pydantic import BaseModel, Schema


class ResponseCreateNote(BaseModel):
    """
    Scheme for preparations response for creating new note
    """
    id: int


class ResponseListNotes(BaseModel):
    """
    Scheme for preparations response for get either one note or list of notes
    """
    slug: str
    description: str = Schema(None, title="The description of the note", max_length=500)
    count: int = Schema(0, title="The count visit in note", max_length=500)

    created_date: str
    is_published: bool
