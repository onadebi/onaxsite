from typing import Type
from onaxmain.models import ContactOptions
import json


class MessagesDto:
    def __init__(self, name, message, email, phone, contact_option: ContactOptions):
        if not name:
            raise ValueError("Name cannot be null, None, or empty")
        if not message:
            raise ValueError("Message cannot be null, None, or empty")
        if not email:
            raise ValueError("Email cannot be null, None, or empty")
        if not phone:
            raise ValueError("Phone cannot be null, None, or empty")
        if not contact_option:
            raise ValueError("Contact option cannot be null, None, or empty")

        self.message = message
        self.email = email
        self.phone = phone
        self.name = name
        self.contact_option = contact_option

    @classmethod
    def from_json(cls, json_str: str) -> Type['MessagesDto']:
        '''Returns MessagesDto object from json string'''
        json_data: dict = json.loads(json_str)
        name = json_data.get('name')
        message = json_data.get('message')
        email = json_data.get('email')
        phone = json_data.get('phone')
        contact_option = json_data.get('contact_option')

        if not name:
            raise ValueError("Name cannot be null, None, or empty")
        if not message:
            raise ValueError("Message cannot be null, None, or empty")
        if not email:
            raise ValueError("Email cannot be null, None, or empty")
        if not phone:
            raise ValueError("Phone cannot be null, None, or empty")
        if not contact_option:
            raise ValueError("Contact option cannot be null, None, or empty")

        return cls(
            name=name,
            message=message,
            email=email,
            phone=phone,
            contact_option=contact_option
        )