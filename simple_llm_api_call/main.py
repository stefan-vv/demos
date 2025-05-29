from openai import OpenAI

# Replace with a generated api key at https://platform.openai.com
# Keys are usually stored in .env files and retrieved as environment variables
API_KEY = 'USER_API_KEY'
MODEL_ID = 'gpt-4o-mini'

def handle_user_input():
    user_input = input('User prompt or question: ')
    return user_input if isinstance(user_input, str) and user_input else None

def send_request_to_model(user_input):
    client = OpenAI(api_key=API_KEY)

    response = client.responses.create(
        model=MODEL_ID,
        instructions='Provide professional answers.',
        input=user_input
    )
    print(response)
    return response

def main():
    # Chat context, optional
    chat_history = []
    print('Type "exit" to quit.')

    while True:
        user_input = handle_user_input()

        if user_input is None:
            print('Please provide a valid prompt or question.')
            continue

        if user_input == 'exit':
            break

        # Append the user input to the chat history
        chat_history.append({
            "role": "user",
            "content": user_input
        })

        model_output_text = None
        try:
            response = send_request_to_model(user_input)
            model_output_text = response.output_text
            print('Model response:\n'.format(model_output_text))
        except Exception as e:
            print('Exception sending request to model: {}'.format(e))

        if model_output_text is not None:
            # Append the model output to the chat history
            chat_history.append({
                "role": "assistant",
                "content": model_output_text
            })

if __name__ == '__main__':
    main()
