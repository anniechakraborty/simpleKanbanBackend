# Simple Kanban Board

## 📌 Project Overview

This is an [**Angular-based Kanban Board** application](https://github.com/anniechakraborty/simpleKanbanBoard) that allows users to create, manage, and track tasks. The application uses **Reactive Forms** for user input and integrates API data for task retrieval and updates. The application also implements user authentication and authorization, and route protection using **authGuard**.

The [backend](https://github.com/anniechakraborty/simpleKanbanBackend) of this application is written using **Python's Flask** framework, and the database is implemented using **MongoDB**. We have used RestAPIs to implement all the **CRUD** operations.

## 🚀 Features

- **User registration, login and proper authentication**
- **Create, Read, Update, and Delete (CRUD) Tasks**
- **Reactive Forms** for managing task input
- **API Integration** for fetching and updating tasks
- **Flask** used to implement the RestAPIs
- **MongoDB** is used to implement the database.

## 🛠️ Technologies Used

- **Angular 19** (CLI)
- **TypeScript**
- **Python 3.13.1** 
- **Flask**
- **JWT Tokens, Flask-Bcrypt** (to handle token generation for user authentication)
- **PyMongo** (for database connection)
- **Bootstrap 5** (for UI styling)
- **HttpClient** (to handle HTTP requests)
- **Reactive Forms** (for user input handling)
- **Guard** (an authGuard to protect the routes)

## 📦 Installation (frontend)

1. **Clone the repository:**
   ```sh
   git clone https://github.com/anniechakraborty/simpleKanbanBoard.git
   cd simpleKanbanBoard
   ```
2. **Install dependencies:**
   ```sh
   npm install
   ```
3. **Run the Angular app:**
   ```sh
   ng serve
   ```
4. Open the browser and go to `http://localhost:4200/`

## 📦 Installation (backend)

1. **Clone the repository:**
   ```sh
   git clone https://github.com/anniechakraborty/simpleKanbanBackend.git
   cd simpleKanbanBackend
   ```
2. **Create a Virtual Environment and activate it:**
   ```sh
   python -m venv venv
   venv/Scripts/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Python app:**
   ```sh
   py run.py
   ```


## 🔧 Usage

### **Register or Login as a user**

- Enter a unique username, email and password
- Click on 'Register' button to register
- If you are a returning user then click on Sign in and enter your email and password

### **Adding a Task**

- Fill in the **task title** and **description** in the form. Set the status.
- Click the **Add Task** button to save the task.

### **Viewing and Editing Tasks**

- Tasks are displayed in a list format under their respective status categories.
- Click on a task title to open a **modal window** with details.
- Edit the task by making changes in the form fields inside the modal.
- Save the changes by clicking on Save.

### **Deleting a Task**

- Click the **cross (X)** button on the right side of the task title to remove a task from the list. A confirmation prompt will appear before deletion to prevent accidental removals.

## 📜 License

This project is licensed under the **MIT License**.

## 📞 Contact

For any issues or suggestions, reach out via:

- 📧 Email: [chakrabortyannie20@gmail.com](mailto\:chakrabortyannie20@gmail.com)
- 🐙 GitHub: [https://github.com/anniechakraborty](https://github.com/anniechakraborty)

---