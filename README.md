# 🤖 AI-Powered CRM Matching System

This project is an AI-driven CRM tool designed to:
- Generate an ideal customer persona based on a company's website and product.
- Match seller profiles against that persona using open-source similarity logic (RapidFuzz).
- Store data in MongoDB with FastAPI for backend API handling.

---

## 🧠 Features

🔹 **API 1: Generate Persona**  
Creates a persona from product, region, and optional company website.

🔹 **API 2: Match Profile**  
Matches a seller profile against existing personas and gives a similarity score.

🔹 **Database**  
MongoDB stores all persona and match data with timestamps.

🔹 **FastAPI Backend**  
Clean, scalable backend with automatic documentation via Swagger UI.

---

## ⚙️ Tech Stack

| Tool       | Purpose                    |
|------------|----------------------------|
| **FastAPI**  | Web API framework         |
| **MongoDB**  | NoSQL database            |
| **Pydantic** | Data validation/schemas   |
| **RapidFuzz**| Fuzzy text matching       |
| **Postman**  | API testing               |
| **Python-dotenv** | Env var handling     |

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/Swetha-Kirubananthan/ai_crm_project.git
cd ai_crm_project