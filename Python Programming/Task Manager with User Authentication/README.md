# ✅ Task Manager with User Authentication  

## 📌 Project Overview  
This project is a **Task Management System** that allows users to **register, log in, and manage their tasks securely**. Each user has their own task list, and only authenticated users can access and modify their tasks. The system features **user authentication, task creation, task tracking, and a menu-driven interface** for seamless task management.  

## 🎯 Features  
🔹 **User Authentication** – Secure login and registration with password hashing.  
🔹 **Task Management** – Users can **add, view, mark tasks as completed, and delete tasks**.  
🔹 **Persistent Storage** – All tasks and user credentials are stored in files.  
🔹 **Interactive Menu** – A user-friendly interface for managing tasks efficiently.  

## 🛠️ Steps Performed  

### **1️⃣ User Authentication**  
✅ **Registration** – Users create an account with a unique username and secure password.  
✅ **Login** – Users log in with their credentials before accessing the task manager.  

### **2️⃣ Task Management**  
✅ **Add a Task** – Users add tasks with a unique ID and default "Pending" status.  
✅ **View Tasks** – Displays all tasks for the logged-in user with task ID, description, and status.  
✅ **Mark Task as Completed** – Users can update task status from "Pending" to "Completed".  
✅ **Delete a Task** – Users can remove tasks from their task list.  

### **3️⃣ Interactive Menu**  
📌 The system presents a **menu** with options:  
- **[1] Add a Task**  
- **[2] View Tasks**  
- **[3] Mark Task as Completed**  
- **[4] Delete a Task**  
- **[5] Logout**  
The user selects an option, and the system processes the request until logout.  

## 📂 File Handling (Persistent Storage)  
📝 **User Credentials:** Stored securely in a file with password hashing.  
📝 **Tasks:** Each user's tasks are stored separately, ensuring privacy and persistence.  

## 🔍 Future Enhancements  
🚀 **Database Integration** – Replace file storage with SQLite or PostgreSQL for scalability.  
🚀 **Web Application** – Develop a web-based version using Flask or Django.  
🚀 **Email Notifications** – Send reminders for pending tasks.  