# Import du framework
from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata

# Routers (You'll create these later)
import routers.router_reservations, routers.router_user, routers.router_workspace  

# Initialisation de l'API
app = FastAPI(
    title="Reservify",
    description=api_description,
    openapi_tags=tags_metadata
)

# Router dédié aux Reservations (Workspace) - You'll create this router later
app.include_router(routers.router_reservations.router)
app.include_router(routers.router_workspace.router)
app.include_router(routers.router_user.router)





