def create_database_entry(patient_name, id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient


def print_database(db):
    locations = ["Room 1", "Room 4", "ER", "Post-Op"]
    for i, (patient, location) in enumerate(zip(db, locations)):
        print("{} - {} - {}".format(i, patient, location))


def print_patients_over_age(db, age):
    for patient in db:
        if patient[2] > age:
            print(patient[0])


def get_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient


def main():
    db = []
    x = create_database_entry("Ann Ables", 1, 30)
    db.append(x)
    x = create_database_entry("Bob Boyles", 2, 31)
    db.append(x)
    x = create_database_entry("Chris Chou", 3, 33)
    db.append(x)
    x = create_database_entry("David Dinkins", 4, 34)
    db.append(x)

    patient_id_tested = 2
    test_done = ("HDL", 65)

    patient = get_patient(db, patient_id_tested)
    patient[3].append(test_done)
    patient[3].append(test_done)
    print_database(db)


if __name__ == "__main__":
    main()