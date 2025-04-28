import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QSpinBox, QPushButton, QTableWidget,
    QTableWidgetItem, QCheckBox, QMessageBox
)
from PyQt5.QtCore import Qt

class TaskMate(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TaskMate")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        layout_utama = QVBoxLayout()

        label_judul = QLabel("TaskMate")
        label_judul.setAlignment(Qt.AlignCenter)

        label_judul.setStyleSheet("font-size: 24px; font-weight: bold; color: blue;")

        label_identitas = QLabel("Nama: Muhammad Ridho Fahru Rozy | NIM: F1D022076")
        label_identitas.setAlignment(Qt.AlignCenter)

        form_layout = QHBoxLayout()

        self.input_tugas = QLineEdit()
        self.input_tugas.setPlaceholderText("Masukkan nama tugas")

        self.combo_prioritas = QComboBox()
        self.combo_prioritas.addItems(["Susah", "Sedang", "Gampang"])

        self.combo_kategori = QComboBox()
        self.combo_kategori.addItems(["Pekerjaan", "Kuliah"])

        self.spin_durasi = QSpinBox()
        self.spin_durasi.setRange(1, 24)
        self.spin_durasi.setSuffix(" jam")

        self.btn_tambah = QPushButton("Tambah Tugas")
        self.btn_tambah.clicked.connect(self.tambah_tugas)

        form_layout.addWidget(self.input_tugas)
        form_layout.addWidget(self.combo_prioritas)
        form_layout.addWidget(self.combo_kategori)
        form_layout.addWidget(self.spin_durasi)
        form_layout.addWidget(self.btn_tambah)

        self.tabel_tugas = QTableWidget()
        self.tabel_tugas.setColumnCount(5)
        self.tabel_tugas.setHorizontalHeaderLabels(["Tugas", "Prioritas", "Kategori", "Durasi", "Selesai"])

        self.btn_hapus = QPushButton("Hapus Tugas Selesai")
        self.btn_hapus.clicked.connect(self.hapus_selesai)

        layout_utama.addWidget(label_judul)
        layout_utama.addWidget(label_identitas)
        layout_utama.addLayout(form_layout)
        layout_utama.addWidget(self.tabel_tugas)
        layout_utama.addWidget(self.btn_hapus)

        self.setLayout(layout_utama)

    def tambah_tugas(self):
        nama = self.input_tugas.text()
        prioritas = self.combo_prioritas.currentText()
        kategori = self.combo_kategori.currentText()
        durasi = self.spin_durasi.value()

        if nama.strip() == "":
            QMessageBox.warning(self, "Peringatan", "Nama tugas tidak boleh kosong.")
            return

        baris = self.tabel_tugas.rowCount()
        self.tabel_tugas.insertRow(baris)
        self.tabel_tugas.setItem(baris, 0, QTableWidgetItem(nama))
        self.tabel_tugas.setItem(baris, 1, QTableWidgetItem(prioritas))
        self.tabel_tugas.setItem(baris, 2, QTableWidgetItem(kategori))
        self.tabel_tugas.setItem(baris, 3, QTableWidgetItem(f"{durasi} jam"))

        cek = QCheckBox()
        self.tabel_tugas.setCellWidget(baris, 4, cek)

        self.input_tugas.clear()

    def hapus_selesai(self):
        baris_hapus = []
        for baris in range(self.tabel_tugas.rowCount()):
            cek = self.tabel_tugas.cellWidget(baris, 4)
            if cek and cek.isChecked():
                baris_hapus.append(baris)

        if not baris_hapus:
            QMessageBox.information(self, "Informasi", "Tidak ada tugas selesai untuk dihapus.")
            return

        konfirmasi = QMessageBox.question(
            self, "Konfirmasi", 
            "Apakah Anda yakin ingin menghapus tugas yang sudah selesai?", 
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            for baris in reversed(baris_hapus):
                self.tabel_tugas.removeRow(baris)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskMate()
    window.show()
    sys.exit(app.exec_())
