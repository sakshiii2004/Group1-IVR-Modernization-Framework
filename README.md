📖 Project Overview

This project replaces the traditional "Nurse Call Button" with an AI-powered Voice-Activated Triage System. Patients speak their requests, and the AI automatically routes them to the correct department (e.g., Housekeeping, Maintenance), reducing nurse workload.

⚠️ Problem Statement

The legacy manual buzzer system has three major flaws:
- No Context: Cannot distinguish between a request for water and a medical emergency.
- Wasted Time: Forces nurses to act as manual dispatchers for non-medical issues.
- Slow Response: Manual hand-offs delay service and lower patient satisfaction.

🎯 Objectives
- Direct Routing: Bypass the nursing station entirely for non-medical requests.
- Smart Tech: Utilize a Python (Flask) backend with Natural Language Understanding (NLU).
- Zero-Touch Workflow: Automatically generate service tickets and dispatch alerts.

🏗️ System Architecture

Built using one of two approaches:
- Phone-Based (Twilio): Twilio frontend converts voice to data; Flask backend processes NLU and triggers SMS/database updates.
- Web Simulator (Tablet): HTML/JS frontend captures browser audio; Flask backend extracts keywords, logs tickets, and responds via Text-to-Speech.
