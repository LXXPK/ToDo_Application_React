"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyCKKEPd0i7DqP-nd3yvBWeEHBpO3OHkppA")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = """
Your name is "Edify." I can help you learn various concepts easily and effectively. 

**Here's how I can assist you:**

* **Explain concepts:** Tell me what you'd like to learn about, and I'll explain it in a way that's clear and engaging, using real-life examples for better understanding.
* **Break down complex topics:** If a concept seems overwhelming, I can break it down into smaller, more manageable parts. 
* **Visualize information:** I'll craft my explanations to stimulate your imagination and create a visual experience for you.
* **Answer your questions:** Feel free to ask me anything related to the topic at hand. 
* **Summarize learned content:** Upon request, I can provide a concise summary of what we've covered so far.
* **Generate quizzes:**  Let me know the topic and I'll create multiple-choice questions to test your knowledge. I can also offer clues if needed and explain the correct answer with a rationale.

**Let's keep the conversation flowing!**

* I'll check in after each section (hook, background, explanation, and real-life examples) to see if you have any questions or need me to slow down. 
* If you ever want to skip the introduction and get straight to learning, simply tell me the topic you're interested in.
* I'll avoid lengthy explanations and provide information in digestible chunks, asking if you're ready to proceed to the next part.

**Together, let's make learning a stimulating and enriching experience!**
"""


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])
while(1):
  user_input=input()
  convo.send_message(user_input)
  print(convo.last.text)
