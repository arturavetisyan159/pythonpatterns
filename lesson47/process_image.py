from PIL import Image, ImageFilter
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

def filter_image(img_name):
    print(f"{multiprocessing.current_process().name}: Работа с картинкой {img_name} началась!")
    img = Image.open(f"images/{img_name}")
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.save(f"processed_images/{img_name}")
    print(f"{multiprocessing.current_process().name}: Работа с картинкой {img_name} завершена!")


def main():
    images = [
        "516_1.jpg",
        "516_2.jpg",
        "516_3.jpg",
        "516_4.jpg",
        "516_5.jpg",
        "516_6.jpg",
        "516_7.jpg",
        "516_8.jpg",
        "516_9.jpg"
    ]
    processes = []
    start_time = time.time()

    # for img in images:
    #     filter_image(img)

    # for idx, img in enumerate(images, start=1):
    #     proc = multiprocessing.Process(target=filter_image, name=f"Процесс {idx}", args=(img,))
    #     processes.append(proc)
    #     proc.start()
    #
    # for proc in processes:
    #     proc.join()

    with ProcessPoolExecutor() as executor:
        executor.map(filter_image, images)
        

    end_time = time.time()
    print(f"Время исполнения программы: {(end_time - start_time):.2f} секунд")

if __name__ == "__main__":
    main()