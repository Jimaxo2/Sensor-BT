# Importa Tkinter para desplegar la ventana
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")  # Usa el backend de Tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import time

# -----------------------------
# CONFIGURA TU PUERTO SERIAL
# -----------------------------
SERIAL_PORT = "COM6"   # Cambia por tu puerto serial del ESP32
BAUD_RATE = 115200

# -----------------------------
# FUNCIÓN DE LECTURA SERIAL
# -----------------------------
def read_serial_data():
    """Lee una línea desde el puerto serial y la devuelve como float (o None si no es válida)."""
    try:
        line = ser.readline().decode("utf-8").strip()
        if line:
            return float(line)  # Convierte a número
    except (ValueError, UnicodeDecodeError):
        return None
    return None

# -----------------------------
# FUNCIÓN DE ACTUALIZACIÓN DEL GRAFICO
# -----------------------------
def update_graph():
    global x_data, y_data

    # Lee el nuevo valor desde el puerto serial
    new_value = read_serial_data()
    if new_value is not None:
        x_data.append(time.time() - start_time)  # segundos desde el inicio
        y_data.append(new_value)

        # Mantén solo los últimos 20 puntos
        if len(x_data) > 20:
            x_data.pop(0)
            y_data.pop(0)

        # Limpia y redibuja
        ax.clear()
        ax.plot(x_data, y_data, marker="o", color="blue")
        ax.set_title("Datos seriales en vivo")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Valor")
        ax.grid(True)

        canvas.draw()

    # Programa la siguiente actualización
    root.after(1000, update_graph)  # cada 1 segundo

# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
if __name__ == "__main__":
    # Conexión serial
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    except serial.SerialException as e:
        print(f"Error serial: {e}")
        exit(1)

    start_time = time.time()
    x_data, y_data = [], []

    # Ventana de Tkinter
    root = tk.Tk()
    root.title("Gráfico de datos seriales en vivo")
    root.geometry("600x400")

    # Figura de Matplotlib
    fig = Figure(figsize=(5, 3), dpi=100)
    ax = fig.add_subplot(111)

    # Inserta la figura en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Actualiza cada segundo
    root.after(1000, update_graph)

    # Maneja el cierre
    def on_close():
        ser.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()