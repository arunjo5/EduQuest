import os
import openai
import tiktoken

class OpenAISummarize(object):
    openai_key = ""

    def __init__(self, openai_key) -> None:
        self.openai_key = openai_key


    def count_tokens(self, text):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(text))


    def chunk_text(self, text, max_tokens=500):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokens = encoding.encode(text)
        chunks = []

        current_chunk = []
        current_token_count = 0

        for token in tokens:
            if current_token_count + 1 <= max_tokens:
                current_chunk.append(token)
                current_token_count += 1
            else:
                chunks.append(encoding.decode(current_chunk))
                current_chunk = [token]
                current_token_count = 1

        if current_chunk:
            chunks.append(encoding.decode(current_chunk))

        return chunks


    def summarize_text(self, text, max_chunk_size=500, max_combined_summary_size=4000):
        openai.api_key = self.openai_key
        model_engine = "text-davinci-003"
        prompt_template = "{}\n\nTl;dr (max 200 words)"

        def recursive_summarize(text):
            chunks = self.chunk_text(text, max_chunk_size)
            summaries = []

            for chunk in chunks:
                prompt = prompt_template.format(chunk)

                response = openai.Completion.create(
                    engine=model_engine,
                    prompt=prompt,
                    max_tokens=150,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )

                summary = response.choices[0].text.strip()
                summaries.append(summary)

            combined_summary = " ".join(summaries)

            if self.count_tokens(combined_summary) > max_combined_summary_size:
                return recursive_summarize(combined_summary)
            else:
                return combined_summary

        final_summary = recursive_summarize(text)

        cohesion_prompt = f"{final_summary}\n\nTl;dr (max 2 paragraphs)"

        response = openai.Completion.create(
            engine=model_engine,
            prompt=cohesion_prompt,
            temperature=0.7,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1,
        )

        rewritten_summary = response.choices[0].text.strip()

        return rewritten_summary
