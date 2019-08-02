import peewee
import datetime
from typing import List

from fastapi import HTTPException
from db import database

from .response_schemes import ResponseListNotes


class Notes(peewee.Model):
    """
    Exposition table Notes in DB
    """
    id = peewee.PrimaryKeyField(unique=True, null=False)
    slug = peewee.CharField(max_length=100, unique=True)
    description = peewee.TextField(default='')

    count = peewee.IntegerField(default=0)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)
    is_published = peewee.BooleanField(default=True)

    @classmethod
    def get_list(cls) -> List[ResponseListNotes]:
        """
        Get list of notes from DB
        :return List[ResponseListNotes]:
        """
        result = []
        for row in cls.select():
            print(row.is_published)
            result.append(ResponseListNotes(
                description=row.description,
                slug=row.slug,
                count=row.count,
                created_date=str(row.created_date),
                is_published=row.is_published
            ))
        return result

    @classmethod
    def get_note_by_slug(cls, slug) -> ResponseListNotes:
        """
        Get note from DB filtering by slug
        :param slug:
        :return ResponseListNotes:
        """
        try:
            note = cls.get(Notes.slug == slug)
            note.count += 1
            note.save()
        except peewee.DoesNotExist:
            raise HTTPException(status_code=400, detail=f"Note with slug {slug} does not exist!")

        return ResponseListNotes(
            description=note.description,
            slug=note.slug,
            count=note.count,
            created_date=str(note.created_date),
            is_published=note.is_published
        )

    class Meta:
        database = database


if not Notes.table_exists():
    Notes.create_table(Notes)
