import random
import string

char = string.ascii_letters + string.digits
result = "" .join(random.choices(char, k= 6)) # change k size to increase the lenght of captcha 
print(f"you captcha code: {result}")
