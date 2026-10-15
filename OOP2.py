"""
PROG211 - Object-Oriented Programming 1
Project: Community Clinic Patient Record System

Demonstrates:
- Classes and objects
- Attributes and methods
- Dictionary data structure
- Instance methods
- Class method using @classmethod
"""


class Patient:
    """Represent a patient record."""

    total_patients = 0

    def __init__(self, patient_id, name, age, condition):
        self.patient_id = str(patient_id)
        self.name = name
        self.age = int(age)
        self.condition = condition

        Patient.total_patients += 1

    def update_record(self, name=None, age=None, condition=None):
        """Update patient information."""

        if name is not None and name.strip():
            self.name = name.strip()

        if age is not None:
            if int(age) < 0:
                raise ValueError("Age cannot be negative.")
            self.age = int(age)

        if condition is not None and condition.strip():
            self.condition = condition.strip()

    def display_info(self):
        """Display patient information."""

        return (
            f"Patient ID: {self.patient_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Condition: {self.condition}"
        )

    @classmethod
    def get_total_patients(cls):
        """Return the number of Patient objects created."""
        return cls.total_patients


class Clinic:
    """Manage patient records."""

    def __init__(self, clinic_name):
        self.clinic_name = clinic_name

        # Dictionary stores patient records by patient ID.
        self.patients = {}

    def add_patient(self, patient):
        """Add a patient while preventing duplicate IDs."""

        if patient.patient_id in self.patients:
            raise ValueError(
                f"Patient ID {patient.patient_id} already exists."
            )

        self.patients[patient.patient_id] = patient

    def find_patient(self, patient_id):
        """Find a patient using the patient ID."""

        return self.patients.get(str(patient_id))

    def display_all_patients(self):
        """Display all patient records."""

        if not self.patients:
            print("No patient records are available.")
            return

        print(f"\n{self.clinic_name} - Patient Records")
        print("-" * 60)

        for patient in self.patients.values():
            print(patient.display_info())

    def add_sample_records(self):
        """Add fictional records for demonstration."""

        samples = [
            Patient(
                "P001", "Mariama Kamara", 28,
                "Malaria (sample)"
            ),
            Patient(
                "P002", "Abdul Sesay", 41,
                "Routine check-up (sample)"
            ),
            Patient(
                "P003", "Fatmata Conteh", 19,
                "Vaccination visit (sample)"
            ),
        ]

        for patient in samples:
            self.add_patient(patient)


def main():
    """Run the clinic record system."""

    clinic = Clinic("Community Health Clinic")

    clinic.add_sample_records()

    print("=" * 60)
    print("COMMUNITY CLINIC PATIENT RECORD SYSTEM")
    print("=" * 60)

    print("All records are fictional sample data.")

    print(
        "\nPatient objects created:",
        Patient.get_total_patients()
    )

    # Display all records
    clinic.display_all_patients()

    # Search for a patient
    print("\nSearching for patient ID P002...")

    found = clinic.find_patient("P002")

    if found:
        print("Record found:")
        print(found.display_info())
    else:
        print("No record found.")

    # Update a patient record
    print("\nUpdating sample record P002...")

    if found:
        found.update_record(
            condition="Follow-up appointment (sample)"
        )

        print(found.display_info())

    # Test duplicate ID protection
    print("\nTesting duplicate-ID protection...")

    try:
        duplicate = Patient(
            "P001", "Duplicate Example", 30, "Sample"
        )

        clinic.add_patient(duplicate)

    except ValueError as error:
        print("Validation message:", error)

    print(
        "\nFinal patient count in clinic:",
        len(clinic.patients)
    )

    print("Program completed successfully.")


if __name__ == "__main__":
    main()