from PyQt5 import  QtCore
from PyQt5.QtWidgets import QFrame, QPushButton, QHBoxLayout

def botenesAcciones():
    #crear un cotenedor para el boton dentro del item
    container_widget = QFrame()
    container_layout = QHBoxLayout(container_widget)

    #crear botones
    botonVer = QPushButton("VER", container_widget)
    botonActualizar = QPushButton("EDITAR", container_widget)
    botonEliminar = QPushButton("ELIMINAR", container_widget)

    botonVer.setCursor(QtCore.Qt.PointingHandCursor)
    botonActualizar.setCursor(QtCore.Qt.PointingHandCursor)
    botonEliminar.setCursor(QtCore.Qt.PointingHandCursor)

    botonVer.setFixedSize(120, 40)
    botonActualizar.setFixedSize(120, 40)
    botonEliminar.setFixedSize(120, 40)

    botonActualizar.setStyleSheet("QPushButton{ background-color:#1877f2; margin-bottom:2px;border-radius:10px;font-size:15px;color:#fff}"
                        "QPushButton:hover{background-color:#4267b2}")
    botonVer.setStyleSheet("QPushButton{ background-color:#B49C09; margin-bottom:2px;border-radius:10px;font-size:15px;color:#fff}"
                        "QPushButton:hover{background-color:#4267b2;}")
    botonEliminar.setStyleSheet("QPushButton{ background-color:#d34; margin-bottom:2px;border-radius:10px ;font-size:15px;color:#fff}"
                        "QPushButton:hover{background-color:#4267b2;}")

    container_layout.addWidget(botonVer)
    container_layout.addWidget(botonActualizar)
    container_layout.addWidget(botonEliminar)
    return container_widget
