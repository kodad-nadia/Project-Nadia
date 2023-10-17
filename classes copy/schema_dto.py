from pydantic import BaseModel

# Pydantic model for reservations
class ReservationBase(BaseModel):
    workspace_id: str
    user_id: str
    date: str
    reserved: bool

class Reservation(ReservationBase):
    id: str

class ReservationNoID(ReservationBase):
    pass

# Pydantic model for workspaces
class WorkspaceBase(BaseModel):
    name: str
    capacity: int
    location: str

class Workspace(WorkspaceBase):
    id: str

class WorkspaceNoID(WorkspaceBase):
    pass

# Pydantic model for users
class UserBase(BaseModel):
    username: str
    email: str

class User(UserBase):
    id: str

class UserNoID(UserBase):
    pass
