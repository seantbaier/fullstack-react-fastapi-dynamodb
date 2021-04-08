from pydantic import BaseModel


# Shared properties
class ProjectBase(BaseModel):
    title: str


# Properties to receive on item creation
class ProjectCreate(ProjectBase):
    title: str


# Properties to receive on item update
class ProjectUpdate(ProjectBase):
    id: str


# Properties shared by models stored in DB
class ProjectInDBBase(ProjectBase):
    id: str
    title: str


# Properties to return to client
class Project(ProjectInDBBase):
    pass


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
