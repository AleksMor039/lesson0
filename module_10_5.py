import multiprocessing
from PIL import Image  # PIL это спец библиотека для работы с изображениями
import datetime


# ф-ия которая изм.размер изобр.
def resize_image(image_path):  # принимает аргументом - путь к конкретной фотографии
    image = Image.open(image_path)
    image = image.resize((800, 600))  # методом resize изм.изобр
    image.save(image_path)


start = datetime.datetime.now()
# при помощи цикла поменяем размер фотографий с 1 до 200й
for i in range(1, 201):
    image_path = f'./images/img_{i}.jpg'  # точка и слеш означает поиск файла в текущ.директории
    resize_image(image_path)
end = datetime.datetime.now()
print(end - start)
############################################################################################


def resize_image(image_path):  # принимает аргументом - путь к конкретной фотографии
    image = Image.open(image_path)
    image = image.resize((800, 600))  # методом resize изм.изобр
    image.save(image_path)


if __name__ == '__main__':  # это проверка на то, что файл который запускается - основной(т.е. отделить от дочерних проц)
    with multiprocessing.Pool(processes=4) as pool:  # Pool принимает аргументом количество процессов
        all_images = []
        for image in range(201, 401):
            all_images.append(f'./image/img_{image}.jpg')
        start = datetime.datetime.now()
        pool.map(resize_image, all_images)  # pool приним. 1м аргум.функцию которой каждый процесс будет заниматься,
        # 2м аргум. приним список
    end = datetime.datetime.now()
    print(end - start)