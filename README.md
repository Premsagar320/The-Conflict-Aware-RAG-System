# The-Conflict-Aware-RAG-System
 building a local RAG (Retrieval Augmented Generation) system that answers employee questions. 

Conflict-Aware RAG System using Google Gemini + ChromaDB
1. Introduction

This project implements a Conflict-Aware Retrieval Augmented Generation (RAG) system for answering company policy questions.
The fictional company NebulaGears has three documents that contain contradictory policies, making normal RAG retrieval unreliable.

The goal is to build a system that:

Retrieves the relevant policy text.

Detects conflicts between documents.

Applies role-based override logic to provide the correct final policy.

Uses Google Gemini Flash 2.0 as the LLM.

Tech Stack
LLM

Google Gemini Flash 2.0

Accessed via google-generativeai

Vector Store

ChromaDB (Local)

Embeddings

Google text-embedding-004 (recommended)
or

SentenceTransformers (all-MiniLM-L6-v2)

Dataset Overview

The system uses three documents:

Document A — employee_handbook_v1.txt

“At NebulaGears, all employees may work remotely 100% of the time from any location.”

Document B — manager_updates_2024.txt

“Remote work is capped at 3 days/week, with mandatory office attendance Tuesdays & Thursdays.”

Document C — intern_onboarding_faq.txt

“Interns must be onsite 5 days/week. No remote work allowed.”

Conflict Logic (Core Innovation)

The key challenge:
A normal similarity search will rank Document A highest for the query
“Can I work from home as an intern?”
because of shared keywords: work, home, remote, employee.

To solve this, I applied role-based conflict resolution:

Rules Used

Role-specific policies override general policies.

Intern rules override employee rules.

Newest document overrides older documents when roles match.

This logic is encoded inside the Gemini prompt so the model resolves conflicts reliably.

Python Code Implemented

This submission includes a fully working conflict-aware policy reasoning system using Gemini Flash 2.0.
The model is instructed to:

Compare documents

Detect contradictions

Determine which policy applies to the user

Cite the final ruling’s source

All three test queries produce correct answers.

Cost Analysis (for scaling)
Gemini Flash 2.0 Pricing (approx.)

Input: $0.10 per 1M tokens

Output: $0.40 per 1M tokens

Scenario

10,000 documents ingested (once)

5,000 employee queries per day

Approximate Cost

Average query: 1K tokens (input + output)

Cost per query ≈ $0.0005

Daily cost = 5000 × 0.0005 = $2.50/day

Yearly cost ≈ $900, extremely affordable for an enterprise RAG system.
