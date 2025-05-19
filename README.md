# 🧠 Code Sutra – Flask App with MySQL Docker Setup

Code Sutra is a lightweight, Dockerized two-tier application that demonstrates the integration of a Flask backend with a MySQL database. It allows users to submit messages, store them in a database, and view them via a web frontend.

---

## 📦 Prerequisites

Make sure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/) (optional, for cloning)

---

## 🚀 Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/code-sutra.git
   cd code-sutra
   ```

2. Create a `.env` file to store your MySQL environment variables:

   ```bash
   touch .env
   ```

3. Add the following to your `.env` file:

   ```env
   MYSQL_HOST=mysql
   MYSQL_USER=your_username
   MYSQL_PASSWORD=your_password
   MYSQL_DB=your_database
   ```

---

## ▶️ Usage with Docker Compose

1. Build and run the containers:

   ```bash
   docker-compose up --build
   ```

2. Access the app in your browser:

   - Frontend: [http://localhost](http://localhost)
   - Backend API: [http://localhost:5000](http://localhost:5000)

3. Initialize the `messages` table in MySQL:

   ```sql
   CREATE TABLE messages (
       id INT AUTO_INCREMENT PRIMARY KEY,
       message TEXT
   );
   ```

4. Use the form on the frontend or hit `/insert_sql` route to store messages.

---

## 🧩 Running Without Docker Compose

### Step 1: Build the Flask image

```bash
docker build -t flaskapp .
```

### Step 2: Create a custom Docker network

```bash
docker network create twotier
```

### Step 3: Start MySQL container

```bash
docker run -d \
    --name mysql \
    -v mysql-data:/var/lib/mysql \
    --network=twotier \
    -e MYSQL_DATABASE=mydb \
    -e MYSQL_ROOT_PASSWORD=admin \
    -p 3306:3306 \
    mysql:5.7
```

### Step 4: Start Flask app container

```bash
docker run -d \
    --name flaskapp \
    --network=twotier \
    -e MYSQL_HOST=mysql \
    -e MYSQL_USER=root \
    -e MYSQL_PASSWORD=admin \
    -e MYSQL_DB=mydb \
    -p 5000:5000 \
    flaskapp:latest
```

---

## 🧹 Cleanup

To stop and remove containers:

```bash
docker-compose down
```

---

## ⚠️ Notes

- Replace placeholders in `.env` with real credentials.
- For production deployments, secure your app and database.
- Always validate and sanitize user inputs to prevent SQL injection.
- Check Docker logs for troubleshooting:
  
  ```bash
  docker logs flaskapp
  docker logs mysql
  ```

---

## 📫 Contact

Built with ❤️ by [Sameer Gupta](https://github.com/SameerGupta-Dev)
