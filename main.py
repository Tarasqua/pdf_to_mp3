import pdfplumber
from art import tprint
from gtts import gTTS
from pathlib import Path


def pdf_to_mp3(file_path, file_language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        # Информация во время обработки
        print(f'\n[+] Original file "{Path(file_path).name}"')  # Изначальное имя pdf файла
        print('[+] Processing...')  # Изначальное имя pdf файла

        # Открываем файл в двоично режиме
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf_file:
            # Пробегаемся по страницам и извлекаем из них текст
            pages = [page.extract_text() for page in pdf_file.pages]

        # Склеиваем текст и избавляемся от переносов строк, чтобы не было паузы в аудио
        text = ''.join(pages).replace('\n', '')

        # Формируем аудио-файл
        audio_file = gTTS(text=text, lang=file_language)
        file_name = Path(file_path).stem  # Имя файла без суффикса (.pdf)
        audio_file.save(f'{file_name}.mp3')

        return f'\n[+] {file_name}.mp3 saved successfully!'
    else:
        return 'File not exists!'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input('\n[+] Please, enter the path to file: ')
    file_language = input('[+] Choose language (en, ru, etc.): ')
    print(pdf_to_mp3(file_path=file_path, file_language=file_language))


if __name__ == '__main__':
    main()