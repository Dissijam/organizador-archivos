
import os
import shutil
from pathlib import Path

# Ajusta "Downloads" o "Descargas" según cómo se llame exactamente tu carpeta en el sistema
RUTA_DESCARGAS = Path.home() / "Downloads" 

# Diccionario de categorías y sus extensiones asociadas
EXTENSIONES = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".stl"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt", ".csv", ".xls"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores_Software": [".exe", ".msi", ".deb", ".AppImage", ".iso"],
    "Multimedia": [".mp4", ".mkv", ".avi", ".mp3", ".flac", ".wav", ".mov"]
}

def organizar_carpeta():
    if not RUTA_DESCARGAS.exists():
        print(f"No se encuentra la ruta: {RUTA_DESCARGAS}")
        return

    print(f"Organizando la carpeta: {RUTA_DESCARGAS}")
    
    # Recorrer todos los elementos de la carpeta de descargas
    for archivo in RUTA_DESCARGAS.iterdir():
        # Ignorar si es una carpeta, solo procesar archivos
        if archivo.is_file():
            ext = archivo.suffix.lower()
            movido = False
            
            # Buscar a qué categoría pertenece la extensión
            for categoria, exts in EXTENSIONES.items():
                if ext in exts:
                    carpeta_destino = RUTA_DESCARGAS / categoria
                    # Crear la carpeta de categoría si no existe
                    carpeta_destino.mkdir(exist_ok=True)
                    
                    destino_final = carpeta_destino / archivo.name
                    
                    # Si ya existe un archivo con el mismo nombre, añadir un número al final
                    contador = 1
                    while destino_final.exists():
                        destino_final = carpeta_destino / f"{archivo.stem}_{contador}{archivo.suffix}"
                        contador += 1
                        
                    # Mover el archivo
                    shutil.move(str(archivo), str(destino_final))
                    print(f"-> Movido: {archivo.name} a {categoria}/")
                    movido = True
                    break
            
            if not movido:
                # Opcional: puedes crear una carpeta "Otros" para lo que no encaje
                pass

    print("¡Organización completada con éxito!")

if __name__ == "__main__":
    organizar_carpeta()