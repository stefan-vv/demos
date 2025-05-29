# Simple LLM API call script using OpenAI's chatGPT API

### Setup

1. Install python if not installed and make it available globally on the system, i.e. add to path/env vars
2. Run `autobuild/build_venv.py` in order to create a virtual environment and install dependencies
3. Log in and generate an API key at `https://platform.openai.com`
4. Open `main.py` and paste the API key by replacing the `API_KEY` global variable (**NOTE**: OpenAI credits are required to run it, i.e. it is paid)
5. Activate the local virtual environment and run the `main.py` file.

#### NOTES:
- The virtual environment is not strictly necessary in this case, it is a good practice if there aren't many dependencies
- If the `main.py` script is run without having an `API_KEY` or the account associated with the `API_KEY` does not have credits it will display an error.