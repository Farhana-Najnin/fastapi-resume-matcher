🚀 FastAPI Resume Matcher
----------------------------------------------------------------------------------------------------------------------------------------

I built this project to make resume screening smarter. Traditional systems often rely on keyword matching, which misses context and true skill alignment. This API uses NLP to understand resumes and job descriptions, giving a more meaningful match.

It’s a hands-on project where I combined Natural Language Processing, backend API development, and real-time deployment to create something practical for recruiters or anyone curious about AI-driven hiring tools.

🎯 Why I Built This
----------------------------------------------------------------------------------------------------------------------------------------

I wanted to go beyond simple keyword matching. With this project, I can:

Measure semantic similarity between resumes and job descriptions

Automatically extract technical skills from unstructured text

Highlight missing skills for a given role

Generate a clear match score (%) for easy evaluation

🧠 Key Features
----------------------------------------------------------------------------------------------------------------------------------------

Transformer-based semantic text matching

Automatic skill extraction from resumes

Identifies missing skills for job requirements

High-performance REST API using FastAPI

Interactive testing via Swagger UI

Public API access through Ngrok

🛠️ Tech Stack I Used
----------------------------------------------------------------------------------------------------------------------------------------

Python – My main programming language

FastAPI – For building a fast, reliable backend

SentenceTransformers (all-MiniLM-L6-v2) – For semantic embeddings

Scikit-learn – For cosine similarity calculations

Uvicorn – ASGI server to run FastAPI

Ngrok – To expose the API publicly

Google Colab – Quick experimentation environment

🔐 Setting Up the Environment
----------------------------------------------------------------------------------------------------------------------------------------

I use Ngrok for public API access, keeping the token secure in a .env file.

Create a .env file:
NGROK_AUTH_TOKEN= my_ngrok_auth_token_here

Load it in Python:
from dotenv import load_dotenv
import os
load_dotenv()
NGROK_TOKEN = os.getenv("NGROK_AUTH_TOKEN")

🌐 How the Public URL Works
----------------------------------------------------------------------------------------------------------------------------------------

When I run the FastAPI server, I use Ngrok to expose it publicly. The URL that Ngrok provides, like:

https://endurable-thwartedly-somer.ngrok-free.dev/docs


only works while the server is running.

📌 API Endpoint
----------------------------------------------------------------------------------------------------------------------------------------

POST /match

Request JSON:
{
  "resume": "Candidate resume text here",
  "job_description": "Job description text here"
}

Example Response:
{
  "match_score_percent": 86.75,
  "resume_skills": ["python", "tensorflow", "git"],
  "job_required_skills": ["python", "docker", "aws"],
  "missing_skills": ["docker", "aws"]
}

🏗️ Architecture
----------------------------------------------------------------------------------------------------------------------------------------

Client (Swagger UI / Postman)
        ↓
FastAPI Endpoint (/match)
        ↓
Text Cleaning & Normalization
        ↓
SentenceTransformer Embeddings
        ↓
Cosine Similarity Calculation
        ↓
Skill Extraction Engine
        ↓
Structured JSON Response

🚀 Where I See It Being Useful
----------------------------------------------------------------------------------------------------------------------------------------

Smarter automated resume screening

Modern Applicant Tracking Systems (ATS)

AI-powered HR tools

Talent intelligence analytics

🔮 What I Want to Add Next
----------------------------------------------------------------------------------------------------------------------------------------

Dynamic skill extraction using NER

Ranking multiple resumes for the same job

A frontend dashboard using React or Streamlit

Cloud deployment on AWS or GCP
