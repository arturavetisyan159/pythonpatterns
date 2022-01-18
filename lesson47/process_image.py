from PIL import Image, ImageFilter
import time

def filter_image(img_name):
    print(f"Работа с картинкой {img_name} началась!")
    img = Image.open(f"images/{img_name}")
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.save(f"processed_images/{img_name}")
    print(f"Работа с картинкой {img_name} завершена!")


def main():
    images = [
        "516_1.jpeg",
        "516_2.jpeg",
        "516_3.png",
        "516_4.jpg",
        "516_5.jpg",
        "516_6.jpg",
        "516_7.jpg",
        "516_8.jpg",
        "516_9.jpg"
    ]
    start_time = time.time()

    for img in images:
        filter_image(img)

    end_time = time.time()
    print(f"Время исполнения программы: {(end_time - start_time):.2f} секунд")

if __name__ == "__main__":
    main()