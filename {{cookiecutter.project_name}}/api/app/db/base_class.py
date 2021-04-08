from pydantic import Field


class Base:
    __name__: str

    # Generate __collectionname__ automatically
    def __collectionname__(cls) -> str:
        return cls.__name__.lower()
