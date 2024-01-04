#!/usr/bin/env python3.8
__author__ = 'InfSub'
__contact__ = 'ADmin@TkYD.ru'
__copyright__ = 'Copyright (C) 2023-2024, [LegioNTeaM] InfSub'
__date__ = '2024/01/04'
__deprecated__ = False
__email__ = 'ADmin@TkYD.ru'
__maintainer__ = 'InfSub'
__status__ = 'Production'
__version__ = '1.5.28'


from dataslots import dataslots
from dataclasses import dataclass
import platform
import re
from exceptions import CantGetIdentityPC
from set_logger_settings import *

py_logger.info(f'Loading module {__name__}...')


'''
for compatibility with older Windows 7 PCs, the dataclass(slots=true) parameter has been replaced with dataslots()
'''
# @dataclass(slots=True, frozen=True)


@dataslots
@dataclass(frozen=True)
class IdentityPC:
    pc_name: str
    city_abbr: str
    shop_number: str
    pc_type: str
    pc_number: str
    department_abbr: str


def get_identity_pc(host_name: str = '') -> IdentityPC:
    """
    The function returns a named tuple with the identification data of the PC.
    :param host_name: this parameter is used for testing, should be empty by default.
    :return: Named tuple with the identification data of the PC.
    """
    identity = _get_named_identity_pc(host_name)
    return IdentityPC(
        identity.pc_name,
        identity.city_abbr,
        identity.shop_number,
        identity.pc_type,
        identity.pc_number,
        identity.department_abbr
    )


def _get_named_identity_pc(host_name: str) -> IdentityPC:
    host_name = _get_host_name(host_name)
    return _parse_host_name(host_name)


def _get_host_name(host_name: str) -> str:
    """
    This is a function to get PC name from system properties.
    :param host_name: this parameter is used for testing, should be empty by default.
    :return: Host Name
    """
    host_name = platform.node() if host_name.strip() == '' else host_name
    return host_name


def _parse_host_name(host_name: str) -> IdentityPC:
    py_logger.debug(f"HostName: {host_name}")
    find_result = re.match(r'(^[a-z]{3})(?:-(\d{2}))?-(pc|nb)(\d{2})-([a-z]{3}$)', host_name, re.I)
    if find_result is None:
        if __name__ == '__main__':
            exit(f'Error: Elements of IdentityPC is not found in HostName: {host_name}')

        py_logger.exception(f'Error: Elements of IdentityPC is not found in HostName: {host_name}')
        raise CantGetIdentityPC

    identity_keys = {
        "pc_name": 0,
        "city_abbr": 1,
        "shop_number": 2,
        "pc_type": 3,
        "pc_number": 4,
        "department_abbr": 5
    }

    return IdentityPC(
        pc_name=find_result.group(identity_keys['pc_name']),
        city_abbr=find_result.group(identity_keys['city_abbr']),
        shop_number=find_result.group(identity_keys['shop_number'])
        if find_result.group(identity_keys['shop_number'])
        is not None else '01',
        pc_type=find_result.group(identity_keys['pc_type']),
        pc_number=find_result.group(identity_keys['pc_number']),
        department_abbr=find_result.group(identity_keys['department_abbr']),
    )


# for test this class:
if __name__ == '__main__':
    print(f'TST-01-NB10-Adm: {get_identity_pc("TST-01-NB10-Adm")}')
    print(f'Empty parameter: {get_identity_pc()}')
