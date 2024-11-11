import strawberry
from datetime import datetime

@strawberry.type
class Owner:
    id: int
    name: str
    name_kana: str = Field(..., pattern = r'^[ァ-ヴー]+$')
    postal_code: str = Field(..., pattern = r'^[0-9]{7}$')
    address: str
    address_building: str | None = None
    address_room_number: str | None = None
    tel: str = Field(..., pattern = r'^[0-9]{10,11}$')
    mail: str | None = Field(None, pattern = r'^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$')
    #bank_account: 
    remarks: str | None = None
    created_at: datetime
    updated_at: datetime
