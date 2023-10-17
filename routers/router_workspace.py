import uuid
from fastapi import APIRouter, HTTPException
from classes.schema_dto import Workspace, WorkspaceNoID

router = APIRouter(
    tags=["Workspaces"]
)

workspaces = [
    Workspace(id=str(uuid.uuid4()), name="Workspace A", capacity=10, location="Location X"),
    Workspace(id=str(uuid.uuid4()), name="Workspace B", capacity=15, location="Location Y"),
    Workspace(id=str(uuid.uuid4()), name="Workspace C", capacity=20, location="Location Z")
]

@router.get('/workspaces')
async def get_workspaces():
    return workspaces

@router.post('/workspaces')
async def create_workspace(given_workspace: WorkspaceNoID):
    new_workspace = Workspace(id=str(uuid.uuid4()), **given_workspace.dict())
    workspaces.append(new_workspace)
    return new_workspace

@router.get('/workspaces/{workspace_id}')
async def get_workspace_by_id(workspace_id: str):
    for workspace in workspaces:
        if workspace.id == workspace_id:
            return workspace
    raise HTTPException(status_code=404, detail="Workspace not found")

@router.patch('/workspaces/{workspace_id}')
async def modify_workspace(workspace_id: str, modified_workspace: WorkspaceNoID):
    for workspace in workspaces:
        if workspace.id == workspace_id:
            workspace.name = modified_workspace.name
            workspace.capacity = modified_workspace.capacity
            workspace.location = modified_workspace.location
            return workspace
    raise HTTPException(status_code=404, detail="Workspace not found")

@router.delete('/workspaces/{workspace_id}', status_code=204)
async def delete_workspace(workspace_id: str):
    for workspace in workspaces:
        if workspace.id == workspace_id:
            workspaces.remove(workspace)
            return
    raise HTTPException(status_code=404, detail="Workspace not found")

