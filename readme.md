# OpenAI Simple Chat
This project demonstrates the use of OpenAI's API to generate text completions in a simple web-based chat application. The application has two versions - Flask and Streamlit - that allows users to interact with a chatbot and generate responses based on their input. The chatbot uses the OpenAI API to generate text completions based on a given prompt and topic.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Forks](https://img.shields.io/github/forks/hipnologo/openai_simple_chat)](https://github.com/hipnologo/openai_simple_chat/network/members)
[![Stars](https://img.shields.io/github/stars/hipnologo/openai_simple_chat)](https://github.com/hipnologo/openai_simple_chat/stargazers)
[![Issues](https://img.shields.io/github/issues/hipnologo/openai_simple_chat)](https://github.com/hipnologo/openai_simple_chat/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/hipnologo/openai_simple_chat)](https://github.com/hipnologo/openai_simple_chat/graphs/contributors)

## Getting Started
To use this application, you will need to sign up for an API key from OpenAI, which you can do [here](https://beta.openai.com/signup/). Once you have an API key, you can set it as an environment variable on your system. 

### Flask
To run the Flask application, simply clone the repository and run the openai_simple_chat.py file. The application will be available at http://localhost:5000/.

### Streamlit
To run the Streamlit application, you need to have the streamlit library installed on your system. You can install it using pip install streamlit. Then, navigate to the streamlit directory and run streamlit run openai_simple_chat_streamlit.py. The application will be available at http://localhost:8501.

## Using the Application
The application has two main pages: the home page, where you can enter a topic and select a prompt, and the answer page, where the generated text completion will be displayed. The home page also has a form to download the answer as a markdown file.

## Built With
* [Flask](https://flask.palletsprojects.com/) - A micro web framework for Python
* [Streamlit](https://streamlit.io/) - An open-source app framework for machine learning and data science teams
* [OpenAI](https://beta.openai.com/) - A platform for training and deploying machine learning models

## Author
* **Fábio Carvalho** - [Fábio Carvalho](https://github.com/hipnologo)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Thanks to OpenAI for providing the API and the models used in this application
* Inspiration for this project came from the desire to explore the capabilities of GPT-3 and its use in web applications.
