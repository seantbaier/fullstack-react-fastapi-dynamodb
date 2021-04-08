from pydantic import BaseModel


# Shared properties
class OrganizationBase(BaseModel):
    name: str


# Properties to receive on item creation
class OrganizationCreate(OrganizationBase):
    name: str


# Properties to receive on item update
class OrganizationUpdate(OrganizationBase):
    id: str


# Properties shared by models stored in DB
class OrganizationInDBBase(OrganizationBase):
    id: str
    name: str


# Properties to return to client
class Organization(OrganizationInDBBase):
    pass


# Properties properties stored in DB
class OrganizationInDB(OrganizationInDBBase):
    pass
