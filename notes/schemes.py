from pydantic import BaseModel, Schema


class CreateNote(BaseModel):
    description: str = Schema(None, title="The description of the note", max_length=500)
    slug: str  # The slug field for get detail note
