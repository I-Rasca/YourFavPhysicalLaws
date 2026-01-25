import tkinter as tk
from tkinter import ttk, messagebox

#================= DATOS =================
laws = {
    "Law of Universal Gravitationl": {
        "formula": "F = G · (m₁ · m₂) / r²",
        "description": "Describe the force of attraction between two masses.",
        "example": "Explain why planets orbit around the Sun.",
        "parameters": ["m1 (kg)", "m2 (kg)", "r (m)"],
        "Unit": "N",
        "calculate": lambda m1, m2, r: 6.674e-11 * m1 * m2 / r**2
    },
    "Newton's Second Law": {
        "formula": "F = m · a",
        "description": "The force applied to an object is equal to its mass times its acceleration.",
        "example": "Pushing an empty cart is easier than pushing a loaded one.",
        "parameters": ["m (kg)", "a (m/s²)"],
        "Unit": "N",
        "calculate": lambda m, a: m * a
    },
    "Kinetic Energy": {
        "formula": "Ec = ½ · m · v²",
        "description": "Energy of a moving object.",
        "example": "Car in motion.",
        "parameters": ["m (kg)", "v (m/s)"],
        "Unit": "J",
        "calculate": lambda m, v: 0.5 * m * v**2
    },
    "Ohm's Law": {
        "formula": "V = I · R",
        "description": "Relate voltage, current, and resistance.",
        "example": "It is used to calculate the electrical consumption in a circuit.",
        "parameters": ["I (A)", "R (Ω)"],
        "Unit": "V",
        "calculate": lambda i, r: i * r
    }
}

entradas = []

#================= FUNCIONES =================
def mostrar_ley(event=None):
    for widget in frame_inputs.winfo_children():
        widget.destroy()
    entradas.clear()

    ley = combo.get()
    info = laws[ley]

    texto.set(
        f"📐 Formula:\n{info['formula']}\n\n"
        f"📖 {info['description']}\n\n"
        f"🔍 Example:\n{info['example']}"
    )

    for param in info["parameters"]:
        tk.Label(frame_inputs, text=param).pack()
        entry = tk.Entry(frame_inputs)
        entry.pack()
        entradas.append(entry)
def calculate():
    ley = combo.get()
    info = laws[ley]

    try:
        valores = [float(e.get()) for e in entradas]
        resultado = info["calculate"](*valores)
        unidad = info["Unit"] #agregado recien
        resultado_label.config(text=f"Outcome: {resultado:.4e} {unidad}") #modificado recien
    except ValueError:
        messagebox.showerror("Error", "Enter numbers only")

#================= GUI =================
root = tk.Tk()
root.title("Interactive Physical Laws")
root.geometry("520x600")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

tk.Label(
    root,
    text="📘 Famous Laws of Physics",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
).pack(pady=10)

combo = ttk.Combobox(root, values=list(laws.keys()), state="readonly", width=35)
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", mostrar_ley)
combo.current(0)

texto = tk.StringVar()
tk.Label(
    root,
    textvariable=texto,
    wraplength=480,
    justify="left",
    bg="#2d2d2d",
    fg="white",
    padx=10,
    pady=10
).pack(padx=10, pady=10, fill="x")

frame_inputs = tk.Frame(root, bg="#1e1e1e")
frame_inputs.pack(pady=5)

tk.Button(
    root,
    text="Calculating",
    command=calculate,
    bg="#4caf50",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=10)

resultado_label = tk.Label(
    root,
    text="Outcome:",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)
resultado_label.pack()

mostrar_ley()
root.mainloop()