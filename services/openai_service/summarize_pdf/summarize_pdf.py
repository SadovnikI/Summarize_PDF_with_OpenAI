from openai import OpenAI
from fastapi import HTTPException
from config import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
)


async def summarize_text(text: str) -> str:
    """
    Summarize the given text using the OpenAI API.

    Args:
        text (str): The text to be summarized.

    Returns:
        str: The summarized text.
    """
    try:
        max_text_length = 4096 - 500
        truncated_text = text[:max_text_length]

        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=(
                "You are a highly skilled summarization expert. "
                "Please provide a concise and informative summary of the following text. "
                "Make sure to capture the main points and any critical details:\n\n"
                f"{truncated_text}\n\n"
                "Summary:"
            ),
            max_tokens=150,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n\n"]
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while summarizing the text: {e}")
