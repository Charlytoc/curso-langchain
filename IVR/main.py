import asyncio
import tempfile
import openai
import sounddevice as sd
import numpy as np
import whisper

# Initialize Whisper model
whisper_model = whisper.load_model("base")

async def generate_speech_stream(text: str, model: str = "tts-1", voice: str = "alloy", output_format: str = "mp3", openai_client=None):
    try:    
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_format}") as temp_file:
            response = openai_client.audio.speech.create(
                model=model,
                voice=voice,
                input=text
            )

            response.stream_to_file(temp_file.name)

            total_duration = "3000" 

            current_chunk = 0
            max_chunks = 100 

            while current_chunk < max_chunks:
                
                await asyncio.sleep(0.1)  # Small delay to allow the file to be written
                with open(temp_file.name, "rb") as audio_file:
                    audio_file.seek(current_chunk * 25000)
                    print("Emitting chunk ", current_chunk)
                    chunk = audio_file.read(25000)
                    if not chunk:
                        break
                    yield chunk
                    current_chunk += 1

            print("Finished reading all chunks")
            yield {"total_duration": total_duration}

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        yield None

async def record_audio(duration: int = 5, sample_rate: int = 16000):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    print("Recording finished.")
    return audio

async def transcribe_audio(audio):
    print("Transcribing audio...")
    result = whisper_model.transcribe(audio)
    return result["text"]

async def generate_response(prompt: str, openai_client):
    print("Generating response...")
    response = openai_client.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

async def main():
    openai.api_key = "YOUR_OPENAI_API_KEY"
    openai_client = openai

    while True:
        audio = await record_audio()
        text = await transcribe_audio(audio)
        print(f"User said: {text}")

        response_text = await generate_response(text, openai_client)
        print(f"AI response: {response_text}")

        async for chunk in generate_speech_stream(response_text, openai_client=openai_client):
            if isinstance(chunk, dict) and "total_duration" in chunk:
                print(f"Total duration: {chunk['total_duration']}")
            else:
                # Here you would play the audio chunk
                pass

if __name__ == "__main__":
    asyncio.run(main())
