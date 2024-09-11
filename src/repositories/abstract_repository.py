from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, filters):
        raise NotImplementedError

    @abstractmethod
    async def get_all_in(self, **in_filters):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, id):
        raise NotImplementedError
    
    @abstractmethod
    async def get_count(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, id):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, id):
        raise NotImplementedError
