from fastapi import FastAPI, File, UploadFile
import uvicorn
import tempfile
import os
import whisper

app = FastAPI(title="Servicio de Transcripción con Whisper")

# Cargar el modelo una sola vez al inicio
model = whisper.load_model("tiny")   # antes era "base"

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Guardar archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # Transcribir con Whisper
        result = model.transcribe(tmp_path, language="es")
        texto = result["text"]
    except Exception as e:
        texto = f"Error al transcribir: {e}"
    finally:
        # Eliminar archivo temporal
        os.unlink(tmp_path)

    return {"text": texto}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
