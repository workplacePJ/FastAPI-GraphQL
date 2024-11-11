import strawberry

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
    creatAt:
    

class CompanyBase(BaseModel):
    name: str
    postal_code: str = Field(..., pattern = r'^[0-9]{7}$')
    address: str
    building_name: str | None = None
    room_number: str | None = None
    tel: str
    fax: str
    #mail: str = Field(..., pattern = r'^$')
    #HP: str = Field(..., pattern = r'^$')
    #invoice_registration_number: str = Field(..., pattern = r'^$')
    #company_seal: str = Field(..., pattern = r'^$')
