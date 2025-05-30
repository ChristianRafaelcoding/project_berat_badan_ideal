import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from tkinter import messagebox as msg
import os

class BeratBadanIdealApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Berat Badan Ideal")

        frame = ttk.Frame(self.root, padding=15)
        frame.pack()

        frame_calc = ttk.LabelFrame(frame, text="Input Data", padding=15)
        frame_calc.grid(row=0, column=0, padx=10, pady=10)


        ttk.Label(frame_calc, text="Tinggi Badan (cm)").grid(row=0, column=0, sticky="w")
        self.entry_tinggi = ttk.Entry(frame_calc, bootstyle="info")
        self.entry_tinggi.grid(row=1, column=0, padx=5, pady=5)


        ttk.Label(frame_calc, text="Jenis Kelamin").grid(row=0, column=1, sticky="w", padx=10)
        self.kelamin = ttk.Combobox(
            frame_calc, bootstyle="info",
            values=["Laki-laki", "Perempuan"],
            state="readonly", width=12
        )
        self.kelamin.current(0)
        self.kelamin.grid(row=1, column=1, padx=10, pady=5)
        self.kelamin.bind("<<ComboboxSelected>>", self.update_gambar)

      
        ttk.Button(
            frame_calc, text="Hitung Berat Badan Ideal",
            bootstyle="success", command=self.hitung_bbi
        ).grid(row=2, column=0, columnspan=2, pady=15)

 
        self.label_hasil = ttk.Label(frame, text="", justify="left", font=("Helvetica", 10))
        self.label_hasil.grid(row=1, column=0, sticky="w", padx=10)

     
        self.gambar_label = ttk.Label(frame)
        self.gambar_label.grid(row=0, column=1, rowspan=2, padx=15)

   
        self.load_images()
        self.update_gambar()

    def load_images(self):
        base_dir = os.path.dirname(__file__)
        laki_path = os.path.join(base_dir, "img", "Laki.png")
        perempuan_path = os.path.join(base_dir, "img", "Perempuan.png")

        self.img_laki = ImageTk.PhotoImage(Image.open(laki_path).resize((100, 100)))
        self.img_perempuan = ImageTk.PhotoImage(Image.open(perempuan_path).resize((100, 100)))

    def update_gambar(self, event=None):
        if self.kelamin.get() == "Perempuan":
            self.gambar_label.configure(image=self.img_perempuan)
        else:
            self.gambar_label.configure(image=self.img_laki)

    def hitung_bbi(self):
        try:
            tinggi = float(self.entry_tinggi.get())
            jenis_kelamin = self.kelamin.get()

            if tinggi <= 0:
                self.label_hasil.config(text="Tinggi harus lebih dari 0 cm")
                return

            if jenis_kelamin == "Laki-laki":
                bbi = (tinggi - 100) - 0.1 * (tinggi - 100)
                keterangan = "Berat badan ideal laki-laki"
            else:
                bbi = (tinggi - 100) - 0.15 * (tinggi - 100)
                keterangan = "Berat badan ideal perempuan"

            hasil = (
                f"Hasil Perhitungan Berat Badan Ideal\n"
                f"Tinggi Badan   : {tinggi:.2f} cm\n"
                f"Jenis Kelamin  : {jenis_kelamin}\n"
                f"Berat Badan Ideal : {bbi:.2f} kg\n"
                f"Keterangan    : {keterangan}"
            )
            self.label_hasil.config(text=hasil)

        except ValueError:
            self.label_hasil.config(text="Masukkan angka valid untuk tinggi badan!")

# Jalankan aplikasi
root = ttk.Window(themename="superhero")  # kamu bisa ganti tema sesuai selera
app = BeratBadanIdealApp(root)
root.mainloop()
