
# Data Entry Application using Python and GUI

## Abstract

The Data Entry Application, developed using Python and the Tkinter library, is designed to facilitate the efficient collection, storage, retrieval, and export of student information. This application employs an SQLite database to store student data, ensuring persistence and ease of access. Key functionalities include:

1. **User Information Entry**: Allows users to input essential personal details such as first name, last name, title, age, nationality, and contact information (email, phone, and address). Validation checks ensure that email addresses and phone numbers are correctly formatted.

2. **Course Information Management**: Enables the entry of course-related details, including registration status, the number of completed courses, and the number of semesters attended.

3. **Terms and Conditions**: Ensures users acknowledge the terms and conditions before data submission.

4. **Data Operations**:
   - **Insert Data**: Facilitates the insertion of validated data into the SQLite database.
   - **View Data**: Displays all stored records in a tabular format using Tkinter's Treeview widget.
   - **Search Data**: Provides search functionality, allowing users to filter data based on specific criteria.
   - **Export Data**: Offers an option to export stored data to a CSV file for external use.

The intuitive graphical user interface (GUI) built with Tkinter makes the application user-friendly and accessible to users with varying levels of technical expertise. This project demonstrates effective use of object-oriented programming (OOP) concepts, exception handling, and GUI basics in Python, making it a robust solution for managing student information.

## Features

- **Graphical User Interface (GUI)**: Designed with Tkinter for ease of use.
- **SQLite Integration**: Utilizes an SQLite database to store and manage data.
- **Validation**: Ensures accurate data entry with validation for email and phone number.
- **Data Entry Forms**: Collects comprehensive user and course information.
- **Data Management**: Includes functionalities for viewing, searching, and exporting data.
- **Terms and Conditions**: Requires user acceptance before data submission.

## Installation

To run this application, ensure you have Python installed on your system. You can clone this repository and run the application using the following commands:

```bash
git clone [https://github.com/yourusername/data-entry-application.git](https://github.com/NagarajanSanthosh/Data-Entry-Application.git)
cd data-entry-application
python data_entry_application.py
```

## Requirements

- Python 3
- Tkinter
- SQLite3
- CSV

## Usage

1. **Run the Application**: Execute the Python script to start the application.
2. **Enter Data**: Fill in the forms with the required information and click "Enter Data" to save it to the database.
3. **View Data**: Click "View Data" to display all stored records.
4. **Search Data**: Use the "Search Data" functionality to filter records based on specific criteria.
5. **Export Data**: Click "Export Data" to save the records to a CSV file.

## License

This project is not licensed. Feel Free to copy.

## Contributing

Feel free to submit issues and pull requests. Please ensure that your code adheres to the project's style guidelines and passes all tests.

## Contact

For any questions or suggestions, you can reach out to me at [santhoshn2982@gmail.com](mailto:santhoshn2982@gmail.com).

