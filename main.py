from fastapi import FastAPI, Body
from starlette.responses import FileResponse, StreamingResponse
from ollama import Client

app = FastAPI()
ai  = Client(host='http://ollama:11434')

@app.get("/")
async def read_index():
    return FileResponse('/app/index.html')


@app.post("/define")
async def define(request = Body()):
    try:
        return StreamingResponse(
            response_generator(request['term']),
            media_type="text/event-stream",
        )
    except:
        return 'Введите валидный термин'

def response_generator(message):
    stream = ai.chat(
        model='llama3.1',
        messages=[
            {'role': 'system', 'content': 'Ты исполняешь роль учителя и наставника для подростка. Попробуй объяснить в доступной и понятной форме, то что я напишу тебе. Можно приводить примеры, и разбивать сложные идеи на более мелкие части, которые легче понять. Используй не больше 20 предложений. Не называй меня подростком при разговоре. Акцентрируйся больше на предмете объяснения'},
            {'role': 'user', 'content': message}
        ],
        stream=True,
    )
    for chunk in stream:
        yield chunk['message']['content']