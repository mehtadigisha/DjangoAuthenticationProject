# Django Authentication Project

This project implements a user authentication system in Django, providing features such as login, signup, password reset, profile management, and more. Below are the details of the implemented functionalities:

---

## Features

### 1. Login Page
- **Fields**: 
  - Username/Email
  - Password
- **Links/Buttons**:
  - **Sign Up**: Redirects to the Signup page.
  - **Forgot Password**: Redirects to the Forgot Password page.

---

### 2. Sign Up Page
- **Fields**:
  - Username
  - Email
  - Password
  - Confirm Password
- **Validation**:
  - Passwords must match.
  - Email must be unique.
- **Link/Button**:
  - Back to the Login page.

---

### 3. Forgot Password Page
- **Fields**:
  - Email
- **Functionality**:
  - Sends an email with a password reset link to the entered email address.
- **Button**:
  - "Send Reset Instructions" to initiate the password reset process.

---

### 4. Change Password Page
- **Access**:
  - Requires authentication.
- **Fields**:
  - Old Password
  - New Password
  - Confirm New Password
- **Validation**:
  - Old password must match the current password.
  - New passwords must match.
- **Link/Button**:
  - Back to the Dashboard.

---

### 5. Dashboard
- **Access**:
  - Only accessible to authenticated users.
- **Features**:
  - Displays a personalized greeting: "Hi, username!".
  - Links to the **Profile Page** and **Change Password Page**.
  - Option to **Logout**.

---

### 6. Profile Page
- **Access**:
  - Requires authentication.
- **Displays**:
  - Username
  - Email
  - Date Joined
  - Last Updated
- **Links/Buttons**:
  - Back to the Dashboard.
  - Logout.

---

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
2. **Install Dependencies: Ensure you have Python and pip installed**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Database Migration**:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
4. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```
5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```
6. **Access the Application: Open http://127.0.0.1:8000 in your web browser**.

### Technology Stack
   - Backend: Django
   - Frontend: HTML, CSS, Bootstrap
   - Database: SQLite (default)

