Community Clinic Patient Record System

1. Project Overview

The Community Clinic Patient Record System is a simple Python program developed for the PROG211 – Object-Oriented Programming 1 (OOP1) individual assignment.

The program helps demonstrate how a community clinic can organize basic patient records using Object-Oriented Programming (OOP). It uses classes, objects, attributes, methods, and a dictionary to store and manage multiple patient records.

The program allows users to add patient records, search for patients, display patient information, and update a patient’s condition.

Note: The patient records included in this program are fictional sample data for demonstration purposes only.

2. Project Objectives

The objectives of this project are to:

* Demonstrate the use of Object-Oriented Programming in Python.
* Create at least two classes.
* Use attributes and methods to manage patient information.
* Store multiple patient records using a dictionary.
* Demonstrate an instance method and a class method using @classmethod.
* Show how software can help solve a real-world problem.
* Consider privacy, accessibility, reusability, and Digital Public Goods (DPG) principles.

3. System Requirements

The system requires:

* Python 3.8 or later.
* Visual Studio Code or another Python code editor (optional).
* A computer with Python installed.
* No external Python libraries are required.

4. Project Files

The project contains the following files:

* patient_record_system.py — the main Python source code.
* README.md — documentation explaining the project.
* sample_output.txt — an example of the program output.

5. How to Run the Program

Follow these steps to run the program:

1. Install Python on your computer.
2. Open Visual Studio Code.
3. Open the folder containing patient_record_system.py.
4. Open the terminal in Visual Studio Code.
5. Check whether Python is installed by typing:
    python --version
6. Run the program by typing:
    python patient_record_system.py

If you are using Windows and the python command does not work, try:

py patient_record_system.py

Press Enter to execute the program.

6. Classes and Methods

A. Patient Class

The Patient class represents an individual patient record.

Attributes:

* patient_id — stores the patient’s unique identification number.
* name — stores the patient’s name.
* age — stores the patient’s age.
* condition — stores a description of the patient’s condition or visit.
* total_patients — a class attribute used to count the patient objects created.

Methods:

* update_record() — updates a patient’s condition and optionally their age.
* display_info() — displays the details of a patient.
* get_total_patients() — a class method that returns the total number of patient objects created.

B. Clinic Class

The Clinic class manages the clinic’s patient records.

Attributes:

* clinic_name — stores the name of the clinic.
* patients — a dictionary used to store patient objects using their patient IDs.

Methods:

* add_patient() — adds a patient record to the clinic.
* find_patient() — searches for a patient using their ID.
* display_all_patients() — displays all patient records.
* add_sample_records() — adds fictional sample records for demonstration.

7. Sample Patient Records

The program uses the following fictional sample records:

1. Patient ID: P001
    Name: Mariama Kamara
    Age: 28
    Condition: Malaria (sample)
2. Patient ID: P002
    Name: Abdul Sesay
    Age: 41
    Condition: Routine check-up (sample)
3. Patient ID: P003
    Name: Fatmata Conteh
    Age: 19
    Condition: Vaccination visit (sample)

The program displays the records, searches for patient P002, updates the patient’s condition to a follow-up appointment, and demonstrates how duplicate patient IDs are rejected.

8. Object-Oriented Programming Concepts Used

The project demonstrates several important OOP concepts.

Classes: The Patient and Clinic classes define the structure and behaviour of the system.

Objects: Patient objects are created from the Patient class.

Attributes: Attributes store information such as patient ID, name, age, and condition.

Instance Methods: Methods such as display_info() and update_record() operate on individual patient objects.

Class Method: The get_total_patients() method uses the @classmethod decorator to access the class-level patient count.

Dictionary: The clinic uses a dictionary to store and organize multiple patient records.

Data Validation: The program rejects duplicate patient IDs and checks that an updated age is not negative.

9. Digital Public Goods (DPG) Considerations

The project demonstrates some principles related to Digital Public Goods.

Open Source and Transparency: The Python source code can be shared, inspected, and improved. An appropriate open-source licence should be added if the project is published as open-source software.

Privacy and Security: The program uses fictional sample data. A real clinic system would require appropriate access controls, secure data storage, backups, and protection of confidential patient information.

Inclusivity and Accessibility: The system could be improved with clear instructions, readable messages, keyboard-friendly controls, and an accessible user interface.

Modularity and Reusability: The program separates patient information from clinic management by using two classes. This makes the code easier to understand, maintain, and extend.

This is an educational demonstration and is not a certified Digital Public Good or a production-ready medical system.

10. Limitations of the System

The current system has the following limitations:

* Patient records are stored only while the program is running.
* The system does not save records to a permanent database.
* It uses a command-line interface instead of a graphical interface.
* It does not include user login or role-based access control.
* It does not provide encryption or audit logs.
* It is not designed to store real patient information.

11. Future Improvements

The system could be improved by:

* Adding a menu that allows users to enter patient information interactively.
* Connecting the program to a database such as SQLite.
* Adding a login system and user permissions.
* Improving input validation and error handling.
* Developing a graphical or web-based interface.
* Adding automated tests.
* Implementing stronger privacy and security measures.

12. Conclusion

The Community Clinic Patient Record System demonstrates how Python and Object-Oriented Programming can be used to represent a real-world problem. By using the Patient and Clinic classes, the program can create, store, search, display, and update patient records.

The project demonstrates classes, objects, attributes, instance methods, a class method, and dictionary-based record storage. It also introduces important considerations involving privacy, accessibility, modularity, and Digital Public Goods principles.

Overall, this project provides a foundation for understanding how software can support basic record management in a community clinic.

13. Submission Checklist

Before submitting the assignment:

* Run patient_record_system.py and confirm that it works.
* Take screenshots showing the program running in the terminal.
* Include the Python source code.
* Include this README.md file.
* Include sample output if required by the lecturer.
* Upload the files to your GitHub repository.
* Submit the GitHub repository link according to the lecturer’s instructions.
