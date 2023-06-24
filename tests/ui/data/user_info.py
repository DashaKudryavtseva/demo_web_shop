import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str


class UserAddress(User):
    company: str
    country: str
    state_or_province: str
    city: str
    address1: str
    address2: str
    zip_or_postal_code: str
    phone_number: str
    fax_number: str
