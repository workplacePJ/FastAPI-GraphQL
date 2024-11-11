import strawberry
from .type import Owner
from strawberry.types import Info

async def get_data__owner(info: Info, id: int) -> Owner:
    """Get owner by id"""
    #owner_dict = await get_dict__owner(info, id)
    owner_dict = Owner(
        id = 1,
        name = '鈴木一郎',
        name_kana = 'スズキイチロウ',
        postal_code = '1142345',
        address = '東京都板橋区赤坂1-32-12',
        address_building = null,
        address_room_number = null,
        tel = '09011111111',
        mail = 'info@jsx.com',
        remarks = null,
        created_at = datetime.now(),
        updated_at = datetime.now()
    )
    return owner_dict

async def get_data__owners(info: Info) -> list[Owner]:
    """Get all owners"""
    #owners_dict_list = await get_dict__owners(info)
    owners_dict_list = [
        Owner(
            id = 1,
            name = '鈴木一郎',
            name_kana = 'スズキイチロウ',
            postal_code = '1142345',
            address = '東京都板橋区赤坂1-32-12',
            address_building = null,
            address_room_number = null,
            tel = '09011111111',
            mail = 'info@jsx.com',
            remarks = null,
            created_at = datetime.now(),
            updated_at = datetime.now()
        ), 
        Owner(
            id = 2,
            name = '鈴木二郎',
            name_kana = 'スズキジロウ',
            postal_code = '1142345',
            address = '東京都板橋区赤坂1-32-12',
            address_building = null,
            address_room_number = null,
            tel = '09022222222',
            mail = 'info@jsx2.com',
            remarks = null,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
    ]
    return owners_dict_list
