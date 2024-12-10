import datetime
import marksfuncs
from PIL import Image
from application.salary import calculate_salary
from application.db.people import get_employees



def create_graph_image(im_buf):
    img = Image.open(im_buf)
    img.show(title="Grafic Image")


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_day = datetime.datetime.today()
    print(current_day.strftime('текущая дата: %d.%m.%Y'))

    while True:
        t = input('Введите 1 или 2 для создания картинки графика: 1 - линейной функции, 2 - экспоненциальной функции: ')

        if t == '1':
            img_buffer = marksfuncs.Linear(m=3, b=5, x_values_list=[-5, 5, 100]).image()
        elif t == '2':
            img_buffer = marksfuncs.Exponential(a=3, b=3, x_values_list=[-1, 5, 100]).image()
        else:
            print('Вы не ввели 1 или 2')
            break

        create_graph_image(img_buffer)
