import asyncio
import sys
import gradio as gr
from faster_whisper import WhisperModel
from webscrape import scraper
from vector_db import load_data, search_with_sources
from llm_interface import chat

ADMIN_MODE = "--admin" in sys.argv

whisper_model = WhisperModel("base", device="cpu", compute_type="int8")


def transcribe_audio(audio_path):
    if audio_path is None:
        return ""
    segments, _ = whisper_model.transcribe(audio_path)
    return "".join(seg.text for seg in segments).strip()


# chatbot settings
LLM_MODEL = "Mistral"
SYSTEM_PROMPT = "You are a concise chatbot about Stirling University. Answer only the question asked, using only relevant information from the provided context. Be brief and direct. Include citations about where you got your answers from."


def ask_question(message, history):
    # search the database for relevant info
    context, sources = search_with_sources(message)

    # get answer from the llm passing conversation history
    answer = chat(message, context, LLM_MODEL, SYSTEM_PROMPT, history=history)

    # format the sources as links
    source_links = "\n".join([f"- [{s['title'] or s['url']}]({s['url']})" for s in sources])
    full_answer = f"{answer}\n\n---\n**Sources:**\n{source_links}"

    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": full_answer},
    ]
    return history, ""


def do_search(query):
    context, sources = search_with_sources(query)
    results = ""
    for s in sources:
        results += f"### [{s['title'] or s['url']}]({s['url']})\n> {s['snippet']}\n\n"
    return results


def do_scrape():
    asyncio.run(scraper.main(chunk_size=1000))
    return "Scraping done."


def do_ingest():
    load_data("chunked_data.json")
    return "Ingestion done."


# build the ui
with gr.Blocks(title="Stirbot") as app:
    gr.Markdown("# Stirbot")

    with gr.Tab("Chat"):
        chat_history = gr.Chatbot(height=300)
        question = gr.Textbox(placeholder="Ask about Stirling University...")
        with gr.Row():
            send_btn = gr.Button("Send")
            clear = gr.Button("Clear")
        mic = gr.Audio(sources=["microphone"], type="filepath", label="Speak your question")

        question.submit(ask_question, [question, chat_history], [chat_history, question])
        send_btn.click(ask_question, [question, chat_history], [chat_history, question])
        clear.click(lambda: ([], ""), outputs=[chat_history, question])
        mic.stop_recording(transcribe_audio, inputs=mic, outputs=question)

    with gr.Tab("Search"):
        search_box = gr.Textbox(placeholder="Search...")
        search_btn = gr.Button("Search")
        results = gr.Markdown()

        search_btn.click(do_search, search_box, results)

    if ADMIN_MODE:
        with gr.Tab("Scrape"):
            gr.Markdown("Scrape the university website. This takes a while.")
            scrape_btn = gr.Button("Start Scrape")
            scrape_output = gr.Textbox(interactive=False)
            scrape_btn.click(do_scrape, outputs=scrape_output)

        with gr.Tab("Ingest"):
            gr.Markdown("Load scraped data into the vector database.")
            ingest_btn = gr.Button("Start Ingestion")
            ingest_output = gr.Textbox(interactive=False)
            ingest_btn.click(do_ingest, outputs=ingest_output)

if __name__ == "__main__":
    app.launch(share=False)
