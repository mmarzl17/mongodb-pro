import uuid
import random
from string import digits, ascii_uppercase, ascii_lowercase


def gen_random_string(count=24):
    char_seqs = digits + ascii_uppercase + ascii_lowercase
    random_chars = random.sample(char_seqs, count)
    return ''.join(random_chars)


def gen_uuid_str():
    return str(uuid.uuid4()).replace('-', '')

a = 16
print("uuid str: ", gen_uuid_str())
# a = gen_uuid_str()