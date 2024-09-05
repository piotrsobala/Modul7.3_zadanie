
from faker import Faker

# Klasa bazowa
class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email_adress):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_adress = email_adress

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

    def contact(self):
        print(f"Wybieram numer +48 {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")

# Klasa dziedzicząca
class BusinessContact(BaseContact):
    def __init__(self, position, company_name, work_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.work_phone_number = work_phone_number

    def contact(self):
        print(f"Wybieram numer +48 {self.work_phone_number} i dzwonię do {self.first_name} {self.last_name}")

# Funkcja do tworzenia losowych wizytówek
def create_contacts(contact_type, quantity):
    fake = Faker()
    contacts = []

    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email_adress = fake.email()

        if contact_type == 'base':
            contact = BaseContact(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email_adress=email_adress
            )
        elif contact_type == 'business':
            position = fake.job()
            company_name = fake.company()
            work_phone_number = fake.phone_number()
            contact = BusinessContact(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email_adress=email_adress,
                position=position,
                company_name=company_name,
                work_phone_number=work_phone_number
            )
        else:
            raise ValueError("Nieznany typ wizytówki. Użyj 'base' lub 'business'.")

        contacts.append(contact)

    return contacts

# Funkcja do obsługi input i generowania wizytówek
def main():
    contact_type = input("Podaj rodzaj wizytówki ('base' lub 'business'): ").strip().lower()
    quantity = int(input("Podaj ilość wizytówek: "))

    contacts = create_contacts(contact_type, quantity)

    for contact in contacts:
        contact.contact()
        print(f"Długość labela: {contact.label_length}\n")

# Uruchomienie programu
if __name__ == "__main__":
    main()
