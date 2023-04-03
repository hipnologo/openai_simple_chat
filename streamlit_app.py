import openai
import streamlit as st
import os

# Set the Model of use
LAST_GPT = True

# Set OpenAI API key
if 'api_key' not in globals():
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
else:
    try:
        api_key = st.text_input("Add your OpenAI API Key")
        openai.api_key = api_key
    except Exception as e:
        st.warning("No OpenAI API Key has been found")

# Define the function to generate responses
def generate_response(message_log, prompt):
    if not message_log:
        # Return a default message if the conversation history is empty
        return "Hi, how can I help you today?"

    try:
        if LAST_GPT == True:
            ### gpt-3.5-turbo model
            messages = [dict(role="user", content=prompt)]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,  # The last message in the conversation history as the prompt
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.3, # The "creativity" of the generated response (higher temperature = more creative)
                presence_penalty=2
            )
            message = response['choices'][0]['message']['content']
        else:
            ### text-davinci-003 model
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.3,
                presence_penalty=2
            )
            message = response.choices[0].text.strip()

        # Add the chatbot's response to the conversation history
        message_log.append({"role": "assistant", "content": message})
        return message

    except Exception as e:
        st.warning(f"An error occurred while processing your request: {e}")
        return None

# Set up the Streamlit app
st.title("Chat with an AI")
if 'message_log' not in st.session_state:
    st.session_state['message_log'] = []

# Get the user input and generate responses
user_input = st.text_input("You:")
if user_input:
    prompt = st.session_state['message_log'][-1]["content"] if st.session_state['message_log'] else ""
    st.session_state['message_log'].append({"role": "user", "content": user_input})
    ai_response = generate_response(st.session_state['message_log'], prompt)

# Display the conversation history
if st.session_state['message_log']:
    st.write("---")
    for message in st.session_state['message_log']:
        if message["role"] == "user":
            st.write("You: " + message["content"])
        else:
            st.write("AI: " + message["content"])
    st.write("---")
