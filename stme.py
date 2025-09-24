import time
class STme:

    def __init__(self, process_name):
        self.process_name = process_name
        self.diff = 0
        self.start_time = time.time()

    def stop(self):
        self.diff = time.time() - self.start_time
        print(f"Процесс \"{self.process_name}\" остановлен: {self.diff:0.4f} сек.")
        return self.diff