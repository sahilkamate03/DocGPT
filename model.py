import openai

# Set up your OpenAI API key
openai.api_key = "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"

# List all fine-tuned models
models = openai.Model.list(fine_tuned=True)

# Print the name and ID of each model
for model in models['data']:
    print(model)
