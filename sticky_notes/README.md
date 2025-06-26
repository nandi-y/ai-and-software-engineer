# Sticky Notes Application

This is a simple Sticky Notes application built using Django. The application allows users to create, read, update, and delete sticky notes. Each note consists of a title and content, providing a straightforward way to manage notes.

## Features

- Create new sticky notes
- View a list of all sticky notes
- Edit existing sticky notes
- Delete sticky notes
- User-friendly interface

## Project Structure

```
sticky_notes/
├── manage.py
├── sticky_notes/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── notes/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── notes/
│           ├── base.html
│           ├── note_list.html
│           ├── note_detail.html
│           ├── note_form.html
│           └── note_confirm_delete.html
├── static/
│   └── notes/
│       └── styles.css
├── diagrams/
│   ├── use_case_diagram.png
│   ├── sequence_diagram.png
│   └── class_diagram.png
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sticky_notes
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django
   ```

4. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Diagrams

The following diagrams are included to illustrate the design of the application:

- Use Case Diagram: `diagrams/use_case_diagram.png`
- Sequence Diagram: `diagrams/sequence_diagram.png`
- Class Diagram: `diagrams/class_diagram.png`

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to the project. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.