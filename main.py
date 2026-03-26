from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
import tempfile

app = FastAPI(title="Servicio de Transcripción")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Endpoint que recibe un archivo de audio y devuelve una transcripción.
    Por ahora devuelve un texto de prueba.
    Más tarde se conectará con Voicebox/Whisper.
    """
    # Guardar el archivo temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    # Simular procesamiento (en la versión final, llamar a Whisper)
    # Por ahora devolvemos un texto de ejemplo
    resultado = {
        "text": "Transcripción de prueba. Este es el texto reconocido a partir del audio."
    }

    # Eliminar archivo temporal
    os.unlink(tmp_path)

    return resultado

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)