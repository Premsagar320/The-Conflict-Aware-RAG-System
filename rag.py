# ======================
# WORKING CONFLICT-AWARE RAG SYSTEM
# Using correct model name
# ======================

import google.generativeai as genai

# Configure Gemini API with your key
GEMINI_API_KEY = "AIzaSyAq0r7D807Pm7qujwLVzXtYnkyq8IctsQ8"
genai.configure(api_key=GEMINI_API_KEY)

print("✅ Gemini API configured successfully!")

# Define the company policies
documents = {
    "Employee Handbook v1": "At NebulaGears, we believe in complete freedom. All employees are eligible for the 'Work From Anywhere' program. You can work remotely 100% of the time from any location. No prior approval is needed.",
    
    "Manager Updates 2024": "Update to remote work policy: Effective immediately, remote work is capped at 3 days per week. Employees must be in the HQ office on Tuesdays and Thursdays. All remote days require manager approval.",
    
    "Intern Onboarding FAQ": "Welcome to the team! Please note that while full-time employees have hybrid options, interns are required to be in the office 5 days a week for the duration of their internship to maximize mentorship. No remote work is permitted for interns."
}

def ask_policy_question(question):
    """Ask policy questions with automatic conflict resolution"""
    
    prompt = f"""
USER QUESTION: "{question}"

COMPANY POLICIES:
1. EMPLOYEE HANDBOOK: {documents['Employee Handbook v1']}
2. MANAGER UPDATES: {documents['Manager Updates 2024']}
3. INTERN FAQ: {documents['Intern Onboarding FAQ']}

CONFLICT RESOLUTION RULES:
- Role-specific policies override general policies
- Intern rules beat employee rules for interns
- Be clear about which document provides the final answer

ANSWER FORMAT:
- First: Direct yes/no answer
- Then: Explain any policy conflicts
- Finally: Cite the source document

ANSWER:
"""
    
    try:
        # Use the correct model name from the available list
        model = genai.GenerativeModel("models/gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Test the system
print("🚀 Testing Conflict-Aware Policy System...\n")

# Test 1: Intern question (the main test case)
print("=" * 60)
print("TEST 1: Intern asking about remote work")
print("=" * 60)
result1 = ask_policy_question("I just joined as a new intern. Can I work from home?")
print("RESULT:")
print(result1)

# Test 2: Employee question
print("\n" + "=" * 60)
print("TEST 2: Employee asking about remote work")
print("=" * 60)
result2 = ask_policy_question("As a full-time employee, what are my remote work options?")
print("RESULT:")
print(result2)

# Test 3: Specific policy check
print("\n" + "=" * 60)
print("TEST 3: Policy details for managers")
print("=" * 60)
result3 = ask_policy_question("As a manager, how many remote days can I approve for my team?")
print("RESULT:")
print(result3)

print("\n" + "=" * 60)
print("✅ All tests completed!")
print("=" * 60)
