import page

user_name = "Helga"
password = "Helga"


def authorize (wait):
    page.login(wait).click()
    page.user(wait).send_keys(user_name)
    page.password(wait).send_keys(password)
    page.submit(wait).click()