import re

def validate_nuber_phone(nuber_phone):
        # return re.findall(r'(\+375|80|375).*?(\d{2}).*?(\d{3}).*?(\d{2}).*?(\d{2})', nuber_phone)
        return "".join(re.findall(r'(\+375|80|375).*?(\d{2}).*?(\d{3}).*?(\d{2}).*?(\d{2})', nuber_phone)[0])
        

# t = validate_nuber_phone("8029 225-71-68")
print(validate_nuber_phone("+37529 225 71-68"))
# print("".join(t[0]))