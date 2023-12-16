from faker import Faker
from faker.providers import BaseProvider
from datetime import datetime, timedelta
import csv

class AllergyProvider(BaseProvider):
    allergies = [
        'Milk', 'Sesame', 'Peanuts', 'Tree nuts', 'Fish', 'Crustacean shellfish', 'Eggs',
        'Wheat', 'Soy'
    ]

    def allergy(self):
        return self.random_element(self.allergies)

# creating a faker instance and allergy provider
fake = Faker()
fake.add_provider(AllergyProvider)

def generate_fake_data(fake_id):
    # creating a fake name
    first_name = fake.first_name()
    last_name = fake.last_name()
    fake_name = f"{first_name} {last_name}"

    # creating fake date of birth within the specified range (1 to 65 years old)
    end_date = datetime.now() - timedelta(days=365 * 1)  # 1 year ago (to have one year olds)
    start_date = end_date - timedelta(days=365 * (65 - 1))  # 65 years ago (to have individuals up to 65 years old)
    fake_dob = fake.date_of_birth(tzinfo=None, minimum_age=1, maximum_age=65)

    # creating fake allergy data
    fake_allergy_1 = fake.allergy()
    fake_allergy_2 = fake.allergy()

    # dictionary for storing the fake data
    fake_data = {
        'ID': fake_id,
        'Name': fake_name,
        'Date_of_Birth': fake_dob,
        'Allergy_1': fake_allergy_1,
        'Allergy_2': fake_allergy_2
    }

    return fake_data

# csv file path
csv_file_path = 'patients_with_multiple_food_allergies.csv'

# fake data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Name', 'Date_of_Birth', 'Allergy_1', 'Allergy_2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # the header
    writer.writeheader()

    # the fake entries
    for fake_id in range(1, 401):  # Changed the range to 401 to generate 400 entries
        fake_entry = generate_fake_data(fake_id)
        writer.writerow({'ID': fake_entry['ID'], 'Name': fake_entry['Name'], 'Date_of_Birth': fake_entry['Date_of_Birth'], 'Allergy_1': fake_entry['Allergy_1'], 'Allergy_2': fake_entry['Allergy_2']})

print(f"Fake patient data with IDs, Names, DOB, and Food Allergies (Allergy_1 and Allergy_2) exported to {csv_file_path}")


