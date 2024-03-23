from openai import OpenAI

DEFAULT_PERSONALITY = "an experienced chef"
DEFAULT_CONDITIONS = [
    "A client will provide one of the following inputs: a dish name, a list of one or more ingredients, or a recipe for a dish.",
    "If your client tells you a dish name, you should provide a detailed recipe for that dish.",
    "If your client provides you with an input that is an ingredient, or a list of ingredients, just respond with the name of any one dish that you know that includes those ingredients. In this case, you should limit your response just the name of the dish.",
    "If your client tells you a recipe for a dish, you should criticize the recipe and suggest improvements.",
    "If your client tells you anything else, you should deny the request and ask to try again.",
]
DEFAULT_MODEL = "gpt-3.5-turbo"


class ChefGPT:
    def __init__(
        self,
        personality=DEFAULT_PERSONALITY,
        conditions=DEFAULT_CONDITIONS,
        model=DEFAULT_MODEL,
    ):
        self.client = OpenAI()
        self.messages = [
            {
                "role": "system",
                "content": f"You are {personality}. You always try to be as clear as possible and provide the best possible answers for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
            }
        ]
        for condition in conditions:
            self.messages.append(
                {
                    "role": "system",
                    "content": condition,
                }
            )
        self.messages.append(
            {
                "role": "system",
                "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
            }
        )
        self.model = model

    def query(self, text):
        self.messages.append({"role": "user", "content": text})
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        return collected_messages
