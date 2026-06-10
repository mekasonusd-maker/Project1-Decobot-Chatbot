# 🤖 DecoBot — Rule-Based AI Chatbot

**DecodeLabs Internship | Batch 2026 | Project 1**

---

## 📌 Project Overview

DecoBot is a rule-based AI chatbot built in Python as part of the 
DecodeLabs Batch 2026 internship program. This project demonstrates 
the foundational architecture of intelligent systems using 
deterministic logic — the same control layer used in real-world 
AI guardrail frameworks like NVIDIA NeMo and Meta's Llama Guard.

---

## 🧠 How It Works

The chatbot follows the **IPO Model**:

- **Input** → User types a message, which is sanitized using 
`.lower().strip()`
- **Process** → The cleaned input is matched against a dictionary 
knowledge base using O(1) lookup
- **Output** → The matched response is printed, or a fallback 
message is returned for unknown inputs

---

## ⚙️ Key Features

- ✅ 13 intents in the knowledge base
- ✅ Input sanitization (handles any casing or spacing)
- ✅ Dictionary-based lookup (O(1) efficiency vs O(n) if-elif ladder)
- ✅ Fallback response for unrecognized inputs
- ✅ Continuous loop with clean exit command
- ✅ Follows the White Box AI principle — fully traceable logic

---

## 🛠️ Tech Stack

- **Language:** Python 3.14
- **IDE:** Visual Studio Code
- **Concepts:** Control Flow, Dictionary Hash Maps, IPO Model, 
Deterministic AI

---

## 🚀 How to Run

1. Make sure Python is installed on your system
2. Clone this repository or download `chatbot.py`
3. Open terminal and navigate to the project folder
4. Run the command:
5. Start chatting! Type exit to quit.
💬 Sample Conversation
========================================
  DecoBot is Online. Type 'exit' to quit.
========================================
You: hello
DecoBot: Hi there! Welcome. How can I help you today?

You: what is ai
DecoBot: AI is the simulation of human intelligence by machines.

You: tell me a joke
DecoBot: Why do programmers prefer dark mode? Light attracts bugs!

You: exit
DecoBot: Shutting down. Goodbye!


Concepts Demonstrated
Concept
Implementation
IPO Model
Input sanitization → Dictionary lookup → Print response
Hash Map
Python dictionary for O(1) response retrieval
Infinite Loop
while True with break on exit command
Fallback Logic
.get() method with default response
Input Sanitization
.lower().strip() on every input
👨‍💻 Author
Emmanuel
DecodeLabs Internship — Batch 2026
---

Start with **Step 1** — tell me when you're on the GitHub homepage!

```bash
python chatbot.py
