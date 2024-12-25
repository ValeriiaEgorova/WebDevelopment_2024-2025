import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import time

class WebPageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Page Viewer")

        # Интерфейс для ввода списка URL
        self.label = tk.Label(root, text="Enter URLs (one per line):")
        self.label.pack()

        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack()

        # Интерфейс для задания интервала
        self.interval_label = tk.Label(root, text="Enter interval (seconds):")
        self.interval_label.pack()

        self.interval_entry = tk.Entry(root)
        self.interval_entry.pack()

        # Кнопки управления
        self.start_button = tk.Button(root, text="Start", command=self.start_viewing)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_viewing, state=tk.DISABLED)
        self.stop_button.pack()

        # Флаг для управления потоком
        self.running = False

    def start_viewing(self):
        try:
            # Получаем список URL и интервал
            urls = self.text_area.get("1.0", tk.END).strip().split("\n")
            self.urls = [url.strip() for url in urls if url.strip()]
            if not self.urls:
                raise ValueError("No URLs provided.")

            self.interval = float(self.interval_entry.get())
            if self.interval <= 0:
                raise ValueError("Interval must be positive.")

            # Блокируем элементы интерфейса во время выполнения
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.running = True

            # Запуск отдельного потока для выполнения задачи
            threading.Thread(target=self.view_pages).start()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def stop_viewing(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def view_pages(self):
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s""  # Укажите путь к Google Chrome
        browser = webbrowser.get(chrome_path)

        for url in self.urls:
            if not self.running:
                break
            browser.open(url)
            time.sleep(self.interval)

        # Разблокируем интерфейс после завершения
        self.stop_viewing()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebPageViewer(root)
    root.mainloop()
