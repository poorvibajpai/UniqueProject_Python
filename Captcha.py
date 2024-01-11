import random
import string
def generate_alpha_numeric_captcha(length=6):
    char = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(char) for _ in range(length))
    return captcha_text
generate_captcha = generate_alpha_numeric_captcha()
print(f"Generates captcha text : {generate_captcha}")