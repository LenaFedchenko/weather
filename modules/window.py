from PyQt6.QtWidgets import QLabel, QMainWindow,QFrame ,QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from modules.app import app 
import requests, os, json
import dotenv
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtGui import QPixmap,QImage



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.WIDTH_WINDOW = 1024
        self.HEIGHT_WINDOW  = 800

        # получаем обьект экрана
        primary_screen = app.primaryScreen()
        # получаем размеры экрана
        screen_size = primary_screen.size()
        # получаем ширину экрана
        width_screen = screen_size.width()
        # получаем высоту экрана
        height_screen = screen_size.height()


        self.setGeometry(
            (width_screen // 2) - (self.WIDTH_WINDOW // 2), 
            (height_screen // 2) - (self.HEIGHT_WINDOW // 2), 
            self.WIDTH_WINDOW, 
            self.HEIGHT_WINDOW
        )
        self.frame_0 = QFrame(parent= self)
        self.frame_0.setStyleSheet("background-color: pink")
        self.frame_0.setFixedSize(1024,800)
        self.horizonal_layout = QHBoxLayout()
        self.frame_0.setLayout(self.horizonal_layout)

        # self.button = QPushButton(parent=self.frame_0)
        # self.button.clicked.connect(self.get_data)

        picture_path = os.path.join(__file__,"..","..","assets", "images","image.png")
        picture_path = os.path.abspath(picture_path)
        picture_path2 = os.path.join(__file__,"..","..","assets", "images","image2.png")
        
        picture_path2 = os.path.abspath(picture_path2)
        # загружаем картинку в свойтсво self.image
        self.image_pillow = Image.open(picture_path)
        # переделіваем картинку в формат для работі с пайкт
        self.qt_image = ImageQt(self.image_pillow)
        # создаем пиксмап и в него помещаем картинку
        self.pixmap = QPixmap(QImage(self.qt_image))
        self.pixmap.scaled(200, 200)
        self.label = QLabel(parent=self.frame_0)
        # прикрепляем картинку в лейбл
        self.label.setPixmap(self.pixmap)
        self.horizonal_layout.addWidget(self.label)


        self.pixmap2 = QPixmap(picture_path2)
        self.pixmap2.scaled(200, 200)
        self.label2 = QLabel(parent=self.frame_0)
        self.label2.setPixmap(self.pixmap2)
        self.horizonal_layout.addWidget(self.label2)

    
    def get_data(self):
        # загружаем файл дотенв
        dotenv.load_dotenv()


        city_name = "Dnipro"
        # os.getenv("API_KEY") - nплучаем константу с енв
        API_key = os.getenv("API_KEY")
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
        data = response.json()

        path = os.path.abspath(os.path.join(__file__, "..", "..", "static", "data.json"))

        with open(path, "w") as file:
            json.dump(data, file, indent= 4)


main_window = MainWindow()