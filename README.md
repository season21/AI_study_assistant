__🚀 AI Study Assistant__
**Multi-Output LLM System using LangChain & HuggingFace**



__🌟 Overview__

AI Study Assistant is an intelligent system that generates Notes, Quiz Questions, and Summaries from a single topic using Large Language Models.

Unlike traditional LLM apps, this project uses parallel chain execution to produce multiple outputs simultaneously, improving efficiency and user experience.


__🎯 Key Features__

✨ Multi-output generation (Notes + Quiz + Summary)
⚡ Parallel execution using RunnableParallel
🧠 Prompt-engineered pipelines
🤖 HuggingFace LLM integration (Flan-T5)
🌐 Simple UI with Streamlit
📦 Modular and scalable architecture




__🧠 Use Case__

📌 Ideal for students, self-learners, and exam preparation

Instead of switching between tools:

One for notes
One for quizzes
One for summaries

👉 This system does everything in one click


___🏗️ System Architecture__
                User Input (Topic)
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   Notes Chain     Quiz Chain     Summary Chain
        │               │               │
        └────── Parallel Execution ──────┘
                        │
                 Combined Output


__⚙️ Tech Stack__

Technology	Purpose
Python	Core programming
LangChain	LLM orchestration
HuggingFace	Model (Flan-T5)
Streamlit	User Interface
dotenv	Environment management


__📂 Project Structure__
AI-STUDY-ASSISTANT/
│── app.py                # Streamlit UI
│── study_chain.py        # Core LLM pipeline
│── requirements.txt      # Dependencies
│── .env                  # API keys (ignored)
│── .gitignore
│── README.md


__🔄 Workflow__
User enters a topic
Topic is passed to multiple prompt templates
Each prompt runs through the LLM
Outputs are generated in parallel
Results are displayed in UI



__📈 Future Enhancements__
🔍 Add RAG (Document-based Q&A)
📊 Add evaluation metrics (LangSmith)
🐳 Docker deployment
☁️ Cloud deployment (GCP / AWS)
💬 Add chat memory


**🧠 Key Learnings**
Built modular LLM pipelines using LangChain
Applied prompt engineering techniques
Implemented parallel execution for performance
Integrated HuggingFace LLM APIs


⭐ If you found this useful, give it a star!
