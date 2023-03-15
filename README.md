## Readme: Using OpenAI's GPT model

This code demonstrates how to import OpenAI's API key and use their GPT model for text generation. 

### Importing OpenAI
At the beginning of the code, the `openai` module is imported to authenticate and authorize access to OpenAI's GPT model. 

### Using the GPT model
The `model` variable specifies the GPT model to be used for text generation. The code uses the `while` loop to listen for user input and generate text based on the input using OpenAI's GPT model. The generated text is stored in the `response` variable and is displayed to the user using the `print` statement.

### Parameters
The text generation process can be controlled using various parameters:

- `temperature` controls the "creativity" of the generated text. Higher temperatures lead to more varied and unexpected responses, while lower temperatures lead to more conservative and predictable responses.

- `top_p` controls the diversity of the generated text by setting a threshold for the cumulative probability of the most likely words.

- `max_tokens` sets the maximum number of tokens (words) that the GPT model will generate.

- `frequency_penalty` and `presence_penalty` control the frequency of repetition of words and phrases in the generated text.

### Running the code
To run the code, save it as a Python file with a `.py` extension and run it in a Python environment with the OpenAI package installed. Replace the `model` variable with the name of the GPT model you want to use and replace the `openai.api_key` with your own API key. When you run the code, it will prompt you for input and generate text based on your input.
