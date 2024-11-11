import strawberry
from .type import Owner
from strawberry.types import Info

async def get_data__owner(info: Info, id: int) -> Owner:
    """Get owner by id"""
    #owner_dict = await get_dict__owner(info, id)
    owner_dict = Owner(info, id = 1)
    return owner_dict

async def get_data__owners(info: Info) -> list[Owner]:
    """Get all owners"""
    #owners_dict_list = await get_dict__owners(info)
    owners_dict_list = [Owner(id = 1, name = '鈴木一郎', postalCode = '1140034', address = '東京都北区上十条2-25-4'), Owner(id = 2, name = '鈴木二郎', postalCode = '1150056', address = '東京都北区赤羽2-25-4')]
    return owners_dict_list
