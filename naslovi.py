class Kontakt:
    def __init__(self, first_name, last_name, email, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def polno_ime(self):
        return self.first_name, self.last_name

vsi_kontakti = []

answer = raw_input("Would you like to add a new contact?(y/n) ")
while answer.lower() == "y":
    ime = raw_input("Contact's First name: ")
    priimek = raw_input("Contact's Last name: ")
    email1 = raw_input("Contact's e-mail: ")
    gsm = raw_input("Contact's phone number: ")
    naslov = raw_input("Contact's address: ")
    oseba = Kontakt(first_name=ime, last_name=priimek, email=email1, phone=gsm, address=naslov)
    vsi_kontakti.append(oseba)
    question = raw_input("Would you like to continue with adding contacts (y/n) ")
    if question.lower() == "n":
        break

for vnos in vsi_kontakti:
    print vnos.first_name, vnos.last_name, vnos.email, vnos.phone, vnos.address








