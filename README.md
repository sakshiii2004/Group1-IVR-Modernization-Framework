📌 Project Overview

This project modernizes the traditional Nurse Call Button system into an AI-powered IVR (Interactive Voice Response) system using FastAPI and Twilio.

Patients can speak or press options, and the system intelligently routes requests to the appropriate department such as:

Housekeeping
Maintenance
IT Support
Nursing Station

This reduces manual workload on nurses and improves response efficiency.

⚠️ Problem Statement

The legacy manual buzzer system has major limitations:

No Context Awareness: Cannot differentiate between simple and critical requests
Manual Dispatching: Nurses handle all requests, even non-medical ones
Delayed Response: Increases response time and reduces patient satisfaction

🎯 Objectives

Smart Routing: Automatically route requests to correct departments
Voice + Key Input Support: Accept both speech and DTMF input
Automated Workflow: Reduce human intervention in non-critical tasks
Scalable Architecture: Build a cloud-ready IVR system

🏗️ System Architecture

User Call
  ↓
Twilio Voice API
  ↓
FastAPI Backend (Webhook)
  ↓
TwiML Response Generation
  ↓
User Interaction (Speech / Keypad)
  ↓
Intent Handling & Routing

⚙️ Tech Stack

Backend: FastAPI (Python)
Telephony: Twilio Voice API
Speech Handling: Twilio Speech Recognition
Testing: Pytest
Deployment: Render (Cloud Hosting)
Tunneling (Development): Ngrok

🔄 IVR Flow

1 User receives a call from Twilio
2 FastAPI /voice endpoint handles the request
3 System plays welcome message using Text-to-Speech
4 User responds via:
--Speech (e.g., "housekeeping")
--Keypad input (1, 2, 3, 4)
5 /handle-intent processes input
6 System routes to appropriate service
7 Submenu (if needed) is triggered
8 Confirmation message is played
9 Call ends

🧪 Testing

The system was tested using a multi-layer approach:

✔ Unit Testing
  Tested endpoints like /voice and /handle-intent
  Verified TwiML responses
  
✔ Integration Testing
  Simulated full IVR flows
  Verified routing between menus
  
✔ End-to-End Testing
  Tested using real Twilio calls
  Verified complete call experience
  
✔ Performance Testing
  Measured response time
  Ensured low latency

🚀 Deployment

The backend is deployed using Render for public access.
FastAPI hosted on cloud
HTTPS enabled
Twilio webhook configured to deployed URL

Note:
Due to Twilio trial limitations, calls can only be made to verified numbers.
The system is demonstrated using a reverse-call approach.

📂 Project Structure

backend.py → FastAPI IVR backend
test_ivr.py → Pytest test cases
trigger_call.py → Twilio call trigger script
requirements.txt → Dependencies
README.md → Documentation

🧠 Key Features

✔ Voice + keypad input support

✔ Dynamic TwiML generation

✔ Multi-level IVR menus

✔ Real-time request routing

✔ Scalable backend

🔮 Future Enhancements
1 Natural Language Understanding (NLU)
2 Multi-language support
3 Database integration
4 Dashboard for hospital staff
5 AI-based intent detection
