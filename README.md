### **Running Instructions**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/bhargavasai9999/uploadfile.git
   cd uploadfile
   ```

2. **Create and Activate a Virtual Environment**  
   ```bash
   python -m venv venv
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**  
   Create a `.env` file in the project root with the following:
   ```plaintext
   FLASK_APP=run.py
   FLASK_ENV=development
   DATABASE_URL=sqlite:///secure_file_sharing.db
   JWT_SECRET_KEY=your_secret_key
   
   ```

5. **Initialize the Database**  
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the Application**  
   ```bash
   flask run
   ```

7. **Access the Application**  
   Open your browser and navigate to:  
   `http://127.0.0.1:5000`
