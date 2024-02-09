import configparser

config = configparser.RawConfigParser()
config.read("D:\\Python Automation Practicals\\Pytest Practicals\\nopCommerce_Testing\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def get_email():
        email = config.get("login data","email")
        return email

    @staticmethod
    def get_password():
        password = config.get("login data","password")
        return password
