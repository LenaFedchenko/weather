from PyQt6.QtWidgets import QLabel, QMainWindow,QFrame ,QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from modules.app import app 
import requests, os, json
import dotenv


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

        self.button = QPushButton(parent=self.frame_0)
        self.button.clicked.connect(self.get_data)
    
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