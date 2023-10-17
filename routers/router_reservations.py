import uuid
from fastapi import APIRouter, HTTPException
from classes.schema_dto import Reservation, ReservationNoID

router = APIRouter(
    tags=["Reservations"]
)

reservations = [
    Reservation(id=str(uuid.uuid4()), workspace_id="workspace1", user_id="user1", date="2023-10-17", reserved=True),
    Reservation(id=str(uuid.uuid4()), workspace_id="workspace2", user_id="user2", date="2023-10-18", reserved=False),
    Reservation(id=str(uuid.uuid4()), workspace_id="workspace3", user_id="user3", date="2023-10-19", reserved=True)
]

@router.get('/reservations')
async def get_reservations():
    return reservations

@router.post('/reservations')
async def create_reservation(givenReservation: ReservationNoID):
    new_reservation = Reservation(id=str(uuid.uuid4()), **givenReservation.dict())
    reservations.append(new_reservation)
    return new_reservation

@router.get('/reservations/{reservation_id}')
async def get_reservation_by_id(reservation_id: str):
    for reservation in reservations:
        if reservation.id == reservation_id:
            return reservation
    raise HTTPException(status_code=404, detail="Reservation not found")

@router.patch('/reservations/{reservation_id}')
async def modify_reservation(reservation_id: str, modified_reservation: ReservationNoID):
    for reservation in reservations:
        if reservation.id == reservation_id:
            reservation.workspace_id = modified_reservation.workspace_id
            reservation.user_id = modified_reservation.user_id
            reservation.date = modified_reservation.date
            reservation.reserved = modified_reservation.reserved
            return reservation
    raise HTTPException(status_code=404, detail="Reservation not found")

@router.delete('/reservations/{reservation_id}', status_code=204)
async def delete_reservation(reservation_id: str):
    for reservation in reservations:
        if reservation.id == reservation_id:
            reservations.remove(reservation)
            return
    raise HTTPException(status_code=404, detail="Reservation not found")



