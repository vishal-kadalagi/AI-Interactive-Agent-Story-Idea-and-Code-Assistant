import google.generativeai as genai

API_KEY = "Enter your API Key"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_story(prompt):
    try:
        if not prompt or len(prompt.strip()) == 0:
            return "Please provide a story prompt to continue."
        prompt_text = f"Continue this story in exactly 4-5 short sentences, keeping it engaging and concise: {prompt}"
        response = model.generate_content(prompt_text)
        if response and hasattr(response, 'text'):
            return response.text.strip()
        return "Could not generate story continuation. Please try again."
    except Exception as e:
        return "An error occurred while generating the story. Please try again with a different prompt."

def generate_idea_feedback(idea):
    try:
        response = model.generate_content(f"Provide brief, constructive feedback for this idea: {idea}")
        return response.text
    except Exception as e:
        return "Great start! Consider its purpose and target audience."

def agent():
    while True:
        mode = input("Choose mode: story / idea / code / exit\n>>> ").strip().lower()

        if mode == "story":
            text = input("Start your story: ")
            continuation = generate_story(text)
            print("\nStory continuation:")
            print(continuation)

        elif mode == "idea":
            idea = input("Describe your idea: ")
            feedback = generate_idea_feedback(idea)
            print("\nFeedback:")
            print(feedback)

        elif mode == "code":
            code = input("Paste your code here:\n")
            if "print" not in code and "def" not in code:
                print("Add a function or print statement")
            elif ":" in code and "(" in code and ")" in code:
                print("Check indentation if there's an error")
            else:
                print("Check syntax: colons, brackets, indentation")

        elif mode == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid mode. Please choose again.")

if __name__ == "__main__":
    agent()
