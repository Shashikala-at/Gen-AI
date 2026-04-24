from openai import OpenAI

# Create client using API key
client = OpenAI(api_key="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")

# Function for Zero-Shot Prompting
def zero_shot_prompt():
    print("\nZERO SHOT PROMPTING")


    prompt = """Classify the sentiment of the following sentence as Positive or Negative:
    'The product quality is amazing and I love it.'"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    print("Prompt:", prompt)
    print("Response:", response.output[0].content[0].text)


# Function for One-Shot Prompting
def one_shot_prompt():
    print("\nONE SHOT PROMPTING")

    prompt = """
Example:
Sentence: I love this phone
Sentiment: Positive

Now classify:
Sentence: This laptop is very slow
Sentiment:
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    print("Prompt:", prompt)
    print("Response:", response.output[0].content[0].text)


# Function for Few-Shot Prompting
def few_shot_prompt():
    print("\nFEW SHOT PROMPTING")

    prompt = """
Sentence: I love this product
Sentiment: Positive

Sentence: This service is terrible
Sentiment: Negative

Sentence: The experience was wonderful
Sentiment: Positive

Now classify:
Sentence: The food was awful
Sentiment:
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    print("Prompt:", prompt)
    print("Response:", response.output[0].content[0].text)


# Main Program
def main():
    print("PROMPT ENGINEERING APPLICATION USING LLM")

    # Run different prompt techniques
    zero_shot_prompt()
    one_shot_prompt()
    few_shot_prompt()


# Execute program
if __name__ == "__main__":
    main()