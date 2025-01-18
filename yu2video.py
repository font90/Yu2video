import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from yt_dlp import YoutubeDL
from PIL import Image, ImageTk
import pyperclip  # Para manejar el portapapeles
import urllib.request
from io import BytesIO


# Función para descargar el video
def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Advertencia", "Por favor, introduce una URL.")
        return

    try:
        # Configuración para descargar el video
        folder = filedialog.askdirectory(title="Selecciona la carpeta de destino")
        if not folder:
            messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta.")
            return

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
        }

        status_label.config(text="Descargando...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Éxito", "¡El video se ha descargado correctamente!")
        status_label.config(text="Descarga completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Función para mostrar la miniatura del video
def fetch_thumbnail():
    """
    Fetches and displays the thumbnail image and title from a provided YouTube URL.
    This function utilizes the YoutubeDL library to extract video information and then
    fetches and previews the thumbnail image and title in the GUI. If the URL field is
    empty or an error occurs during the process, appropriate error messages are displayed
    using message boxes. Expects a valid YouTube URL to function correctly.

    :param url: The YouTube video URL retrieved from the GUI's input field. Should not
        be empty and must be properly formatted.

    :raises ValueError: If the provided URL is empty.
    :raises Exception: If there's a failure in downloading or processing the
        thumbnail content or video information due to invalid URL or network issues.

    :return: None. This function directly updates the GUI elements to display the
    """
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Advertencia", "Por favor, introduce una URL.")
        return

    try:
        with YoutubeDL({"quiet": True}) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            thumbnail_url = info_dict.get('thumbnail', '')
            title = info_dict.get('title', '')

        if thumbnail_url:
            with urllib.request.urlopen(thumbnail_url) as response:
                data = response.read()

            # Mostrar la imagen miniatura con PIL
            image = Image.open(BytesIO(data))
            image = image.resize((200, 150), Image.LANCZOS)
            img = ImageTk.PhotoImage(image)

            # Asignar la miniatura y el título en la interfaz
            thumbnail_label.config(image=img)
            thumbnail_label.image = img
            title_label.config(text=title)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener la miniatura: {e}")


# Función para pegar contenido desde el portapapeles
def paste_from_clipboard():
    url_entry.delete(0, tk.END)
    url_entry.insert(0, pyperclip.paste())


# Crear ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")
root.geometry("600x500")

# Desactivar el redimensionado de la ventana
root.resizable(False, False)

# Imagen de fondo
bg_image = Image.open("background.jpg")  # Coloca aquí tu imagen de fondo
bg_image = bg_image.resize((600, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)


bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Encabezado
header_label = tk.Label(
    root, text="Descargador de YouTube", font=("Arial", 20, "bold"), bg="#ffa500", fg="white"
)
header_label.pack(pady=20)

# Entrada de URL
url_entry = tk.Entry(root, width=50, font=("Arial", 14))
url_entry.pack(pady=10)

# Agregar un menú contextual para pegar desde el ratón
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Pegar", command=paste_from_clipboard)


def show_context_menu(event):
    menu.post(event.x_root, event.y_root)


url_entry.bind("<Button-3>", show_context_menu)  # Agregar función al clic derecho

# Botón para obtener miniatura
thumbnail_button = tk.Button(
    root,
    text="Obtener Miniatura",
    command=fetch_thumbnail,
    bg="#2196F3",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    borderwidth=3,
)
thumbnail_button.pack(pady=10)

# Etiqueta para mostrar la miniatura
thumbnail_label = tk.Label(root, bg="white")
thumbnail_label.pack(pady=10)

# Etiqueta de título
title_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#4CAF50", bg="white")
title_label.pack()

# Botón para descargar el video
download_button = tk.Button(
    root,
    text="Descargar Video",
    command=download_video,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    borderwidth=3,
)
download_button.pack(pady=20)

# Barra de progreso (opcional para un futuro añadido)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=15)

# Etiqueta de estado
status_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
status_label.pack()

# Ejecutar aplicación
root.mainloop()
