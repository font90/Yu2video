tkinter       # Incluido en las instalaciones estándar de Python, no es necesario incluir si se usa junto con Python.
yt-dlp==2023.10.7   # Para descargar videos, puedes actualizar a la última versión si es necesario.
Pillow==10.0.1     # Librería para procesar imágenes (PIL fork.)
pyperclip==1.8.2   # Manejador portapapeles
urllib3=2.0.7-python AguaComponent)="#">


### **Para Windows:**
1. **Descargar FFmpeg**:
    - Ve al sitio oficial de FFmpeg: [Hyperlink removed for security reasons]().
    - En la sección **Windows**, selecciona "Build from gyan.dev" o uno de los binarios recomendados directamente para Windows.
    - Descarga el archivo comprimido correspondiente (normalmente, un archivo ZIP).

2. **Extraer y configurar FFmpeg**:
    - Extrae el archivo ZIP descargado y coloca la carpeta donde desees (por ejemplo, `C:\ffmpeg`).
    - Dentro de esa carpeta, ubica el archivo ejecutable de FFmpeg en la ruta: `bin/ffmpeg.exe`.

3. **Configurar la variable de entorno `PATH`**:
    - Abre el **Panel de Control** de Windows y busca **Configuración avanzada del sistema**.
    - Ve a la pestaña **Opciones avanzadas** y haz clic en **Variables de entorno**.
    - En la lista de variables del sistema, busca `Path` y pulsa en **Editar**.
    - Añade la ruta donde se encuentra FFmpeg, por ejemplo: `C:\ffmpeg\bin`.
    - Pulsa **Aceptar** para guardar los cambios.

4. **Verificar la instalación**:
    - Abre la terminal de comandos (CMD) y escribe:

    - En el cmd de windows escribe
           ffmpeg -version

    -En caso de no poder instalar te dejo link de video de instalcion
    LINK https://www.youtube.com/watch?v=9TayWS6RiU4&ab_channel=Qubyts

    -En caso de usar linux
    LINK https://www.youtube.com/watch?v=Yo-gIvXQOOQ&ab_channel=InteligenteDigital


