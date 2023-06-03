import json
import pytest

from src.crud import notes

def test_get_all_notes(test_app, monkeypatch):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    author = fields.ForeignKeyField('models.Users', related_name='notes')
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    
    test_data = [{"id": 1, "title": "title", "content": "content", "author": "author", "created_at": 12132432, "modified_at": 12343234}]
    async def mock_get_all():
        return test_data
    
    monkeypatch.setattr(notes, "get_notes", mock_get_all)

    
