import os
import shutil
from concurrent.futures import ThreadPoolExecutor


class FileSorter:
    def __init__(self):
        pass

    def process_folder(self, root, folder):
        folder_path = os.path.join(root, folder)
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1][1:]
                self.move_file(root, folder, file_extension, item, item_path)
            elif os.path.isdir(item_path):
                self.process_folder(root, os.path.join(folder, item))

    def move_file(self, root, folder, file_extension, file_name, file_path):
        destination_folder = os.path.join(root, file_extension)
        os.makedirs(destination_folder, exist_ok=True)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, destination_path)
        print(f"Moved {file_path} to {destination_path}")

    def process_directory(self):
        directory = input("Введите путь к каталогу сортировки: ")
        
        with ThreadPoolExecutor(max_workers=4) as executor: # количество потоков процессора
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    executor.submit(self.process_folder, directory, item)

    def __getstate__(self):
        # Определение состояние объекта для сериализации
        attributes = {**self.__dict__, 'file': None}
        return attributes

    def __setstate__(self, state):
        # Восстановление состояния объекта после десериализации
        self.__dict__ = state

#@3fasdfasdfasdf
file_sorter = FileSorter()
file_sorter.process_directory()
