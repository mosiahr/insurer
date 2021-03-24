import uuid


def generation_uuid(prefix):
    """
    Generate the UUID as a prefix and a 32-character hexadecimal string
    Example:
        gen_uuid('SM') => SMa41ea507e7a443f2a1a973ac141fb8f8
    """
    id = uuid.uuid4()
    return f"{prefix}{id.hex}"


def get_uuid_for_sms():
    return generation_uuid(prefix='SM')
