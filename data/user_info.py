import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str


@dataclasses.dataclass
class UserAddress(User):
    company: str
    country: str
    country_id: int
    state_or_province: str
    state_id: int
    city: str
    address1: str
    address2: str
    zip_or_postal_code: str
    phone_number: str
    fax_number: str
