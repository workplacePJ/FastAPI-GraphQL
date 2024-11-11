import strawberry
from datetime import datetime

@strawberry.type
class Owner:
    id: int
    name: str
    name_kana: str
    postal_code: str
    address: str
    address_building: str | None = None
    address_room_number_or_floor: str | None = None
    tel: str
    mail: str | None = None
    #bank_account: 
    remarks: str | None = None
    created_at: datetime
    updated_at: datetime



"""
@strawberry.type
class Owner:
    id: int
    name: str
    name_kana: str = field(..., pattern = r'^[ァ-ヴー]+$')
    postal_code: str = field(..., pattern = r'^[0-9]{7}$')
    address: str
    address_building: str | None = None
    address_room_number_or_floor: str | None = None
    tel: str = field(..., pattern = r'^[0-9]{10,11}$')
    mail: str | None = field(None, pattern = r'^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$')
    #bank_account: 
    remarks: str | None = None
    created_at: datetime
    updated_at: datetime
"""
