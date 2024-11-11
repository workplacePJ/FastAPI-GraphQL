import strawberry
from datetime import datetime

@strawberry.type
class Owner:
    id: int
    name: str
    nameKana: str = Field(..., pattern = r'^[ァ-ヴー]+$')
    postalCode: str = Field(..., pattern = r'^[0-9]{7}$')
    address: str
    buildingName: str | None = None
    roomNumber: str | None = None
    tel: str = Field(..., pattern = r'^[0-9]{10,11}$')
    mail: str | None = Field(None, pattern = r'^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$')
    #bankAccount: 
    remarks: str | None = None
    createdAt: datetime
    updatedAt: datetime
