# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправкатипа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа

        with open("contacts.html", "r") as f:
            html_content = f.read()
        self.wfile.write(bytes(html_content, "utf-8"))

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах всети
    # принимать запросы и отправлять их на обработку специальному классу,который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящихзапросов
        webServer.serve_forever()
    except KeyboardInterrupt:
    # Корректный способ остановить сервер в консоли через сочетаниеклавиш Ctrl + C15
        pass
        # Корректная остановка веб-сервера, чтобы он освободил адрес и порт всети, которые занимал
    webServer.server_close()
    print("Server stopped.")