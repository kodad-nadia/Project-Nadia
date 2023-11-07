from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from database.firebase import authSession
from firebase_admin import auth

router = APIRouter(tags=["Auth"], prefix='/auth')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(provided_token: str = Depends(oauth2_scheme)):
    decoded_token = auth.verify_id_token(provided_token)
    decoded_token['idToken'] = provided_token
    return decoded_token

@router.get('/me')
async def get_user_data(current_user: dict = Depends(get_current_user)):
    try:
        user = auth.get_user(current_user['sub'])  # Fetch user details based on sub (subject) ID
        user_data = {
            "user_id": user.uid,
            "email": user.email,
            # Add other user details as needed
        }
        return user_data
    except auth.UserNotFoundError:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        # Provide a generic error message for other potential errors
        raise HTTPException(status_code=500, detail="Error fetching user data")

# Additional routes for signup, login, etc.
