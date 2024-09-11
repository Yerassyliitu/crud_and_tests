import pytest
from datetime import date
from unittest.mock import AsyncMock, MagicMock
from pydantic import BaseModel
from src.services import BaseService
from src.repositories.abstract_repository import AbstractRepository


class EntityModel(BaseModel):
    id: int
    name: str


def mapper(idk):
    return EntityModel(
        id=idk.id, 
        name=idk.name
    )


@pytest.fixture
def mock_repo():
    repo = AsyncMock(spec=AbstractRepository)
    return repo


@pytest.fixture
def base_service(mock_repo):
    return BaseService(base_repo=mock_repo)


@pytest.mark.asyncio
async def test_create_entity(base_service, mock_repo):
    entity = EntityModel(id=1, name="Test Entity")
    mock_repo.add_one.return_value = 1
    mock_repo.get_one.return_value = entity

    result = await base_service.create_entity(entity)
    
    assert mapper(result) == entity
    mock_repo.add_one.assert_called_once_with(data=entity.model_dump())
    mock_repo.get_one.assert_called_once_with(id=1)


@pytest.mark.asyncio
async def test_get_entity(base_service, mock_repo):
    entity = EntityModel(id=1, name="Test Entity")
    mock_repo.get_one.return_value = entity

    result = await base_service.get_entity(id=1)

    assert mapper(result) == entity
    mock_repo.get_one.assert_called_once_with(id=1)


@pytest.mark.asyncio
async def test_get_entities(base_service, mock_repo):
    entity = EntityModel(id=1, name="Test Entity")
    mock_repo.get_all.return_value = [(entity,)]

    result = await base_service.get_entities()
    result = [mapper(row) for row in result]
    assert result == [entity]
    mock_repo.get_all.assert_called_once()


@pytest.mark.asyncio
async def test_get_count(base_service, mock_repo):
    mock_repo.get_count.return_value = 10

    result = await base_service.get_count()

    assert result == 10
    mock_repo.get_count.assert_called_once()


@pytest.mark.asyncio
async def test_update_entity(base_service, mock_repo):
    entity = EntityModel(id=1, name="Updated Entity")
    mock_repo.edit_one.return_value = entity

    result = await base_service.update_entity(entity, id=1)

    assert mapper(result) == entity
    mock_repo.edit_one.assert_called_once_with(id=1, data=entity.model_dump())


@pytest.mark.asyncio
async def test_delete_entity(base_service, mock_repo):
    mock_repo.delete_one.return_value = True

    result = await base_service.delete_entity(id=1)

    assert result is True
    mock_repo.delete_one.assert_called_once_with(id=1)
