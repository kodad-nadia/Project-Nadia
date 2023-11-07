# Import du framework
from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata


# Routers 
import routers.router_reservations, routers.router_user, routers.router_workspace
import routers.router_auth, routers.router_stripe


# Initialisation de l'API
app = FastAPI(
    title="Reservify",
    description=api_description,
    openapi_tags=tags_metadata,
    docs_url='/'
)

# Router dédié aux Reservations (Workspace) 
app.include_router(routers.router_reservations.router)
app.include_router(routers.router_workspace.router)
app.include_router(routers.router_user.router)
app.include_router(routers.router_auth.router)
app.include_router(routers.router_stripe.router)



