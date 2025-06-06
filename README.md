# Resume Parser with AI

This is a **Resume Parser** application built using **FastAPI**, with **Gemini 2.0 Flash** for intelligent resume parsing. The application extracts key information from resumes, provides upskilling recommendations, and suggests improvements based on the parsed data. Parsed data is stored in a **PostgreSQL** database safely with base6r encoding (Using **Neon DB**) for retrieval and display.

## Features
- **Resume Parsing**: Extracts details like name, skills, experience, education, and contact information and much more using Gemini 2.0 Flash API.
- **Upskilling Suggestions**: Provides tailored recommendations for skills enhancement based on parsed resume data.
- **Improvement Suggestions**: Offers actionable feedback to improve the resume content and structure.
- **Data Storage**: Saves parsed resume data to a PostgreSQL database (Neon DB).
- **Data Retrieval**: Displays stored resume data for review.
- **API Framework**: Built with FastAPI for efficient and scalable API endpoints.

## Tech Stack
- **Backend**: FastAPI (Python)
- **AI Model**: Gemini 2.0 Flash for resume parsing and suggestions
- **Database**: Serverless PostgreSQL (Neon DB)
- **Containerization**: Docker 

## Prerequisites
- Python 3.8+
- PostgreSQL Neon DB account and connection string
- Gemini 2.0 Flash API key
- Docker (optional, for containerized setup)

## Setup Instructions

### Without Docker
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/resume-parser-ai.git
   cd resume-parser-ai

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   venv\scripts\activate

3. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt

4. **Set Environment Variables: Create a .env file in the project root and add**:
   ```bash
    GEMINI_API_KEY=your_gemini_api_key
    PG_DB_URL=your_neon_db_connection_url

5. **Start the FastAPI Application**:
   ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000

6. **Access To The AppliCation**:
   
    - Open http://localhost:8000/ And You Can See The Application UI
    - Upload resumes and check the functionality.


### With Docker
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/resume-parser-ai.git
   cd resume-parser-ai

2. **Set Environment Variables: Create a .env file in the project root and add**:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key
   PG_DB_URL=your_neon_db_connection_url

3. **Build and Run the Docker Container**:
   ```bash
    docker-compose up --build

4. **Access To The AppliCation**:
    - Open http://localhost:8000/ And You Can See The Application UI
    - Upload resumes and check the functionality.
    - To Check the Log Checkout The file named --log-level info which is automatically created in the project directory

### ScreenShots :- 
Resume Uploading Tab :- 
![1sttab](https://github.com/user-attachments/assets/8679e514-b4de-445c-af0d-b859af0f282a)

Resume Parsing History Tab :- 
![2ndtab](https://github.com/user-attachments/assets/18eec6f4-6389-49fe-8625-3663650c5c84)

Resume Detail Tab :- 
![detail_tab](https://github.com/user-attachments/assets/1bdc24e8-821b-4aad-8840-70421823f528)



### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.



