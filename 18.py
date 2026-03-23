class Logger:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, "a")
        print(f"Logger started, writing to {self.file_path}")

    def log(self, message, level="INFO"):
        log_entry = f"[{level}] {message}\n"
        self.file.write(log_entry)
        print(log_entry.strip())

    def info(self, message):
        self.log(message, "INFO")

    def warning(self, message):
        self.log(message, "WARNING")

    def error(self, message):
        self.log(message, "ERROR")

    def __del__(self):
        if self.file:
            self.file.close()
            print("Logger closed.")

logger = Logger("app.log")
logger.info("Application started")
logger.warning("Low disk space")
logger.error("File not found")
del logger