import re

def validate_nuber_phone(nuber_phone):
        return re.findall(r'(\d{4}-\d\d-\d\d)', nuber_phone)
        # return "".join(re.findall(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', nuber_phone))
        

t = validate_nuber_phone("2246-57-16")
# print(validate_nuber_phone("2023-01-28"))
print(t[0])