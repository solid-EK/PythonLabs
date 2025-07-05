from tkinter import *
from tkinter import ttk


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = []

    def describe_restaurant(self):
        av_rate = self.calculate_average_rating()
        print('Название:', self.restaurant_name, '\nВид кухни:', self.cuisine_type, '\nРейтинг:', av_rate)

    def open_restaurant(self):
        print('Ресторан открыт')

    def renew_rating(self, new_rating):
        self.rating.append(new_rating)

    def calculate_average_rating(self):
        if not self.rating:
            return 0
        return sum(self.rating) / len(self.rating)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, schedule, output_label):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.schedule = schedule
        self.types_ice = {"На палочке": ["Эскимо", "Банановое"], "В вафельном стаканчике": ["Шоколадное", "Ваниль"]}
        self.output_label = output_label

    def describe_restaurant(self):
        super().describe_restaurant()
        print('Место:', self.location, '\nРасписание:', self.schedule)
        self.output_label["text"] = f'Название: {self.restaurant_name}\nВид кухни: {self.cuisine_type}\nРейтинг: {self.calculate_average_rating()}\nМесто: {self.location}\nРасписание:{self.schedule}'

    def display_flavors(self):
        print('Вкусы мороженого:', ','.join(self.flavors))
        self.output_label["text"] = f'Вкусы мороженого: {", ".join(self.flavors)}'

    def add_flavor(self, new_flavor):
        if new_flavor.isalpha():
            self.flavors.append(new_flavor)

    def delete_flavor(self, del_flavor):
        if del_flavor.isalpha():
            self.flavors.remove(del_flavor)

    def check(self, srch_flav):
        if srch_flav in self.flavors:
            print(srch_flav, 'есть в наличии!')
        else:
            print('Этот вкус отсутствует (')

    def check_types(self, flv_chk):
        for k, v in self.types_ice.items():
            if flv_chk in v:
                print(f"{flv_chk} относится к типу '{k.lower()}'")
                # print(", ".join(self.types_ice[flv_chk]))



if __name__ == '__main__':
  root = Tk()
  root.title('МРЖН')
  root.geometry("500x500")
  output = ttk.Label(root, text="")
  output.pack(side=TOP)
  morz = IceCreamStand('Петрохолод', 'Десерты', ['Ваниль', 'Эскимо', 'Банановое'], 'Овсянический парк', '10:00-18:00', output)
  btn = ttk.Button(root, text='Информация о ресторане', command=morz.describe_restaurant)
  btn.pack(anchor=NW)
  btn2 = ttk.Button(root, text="Информация о вкусах", command=morz.display_flavors)
  btn2.pack(anchor=W)
  entry = ttk.Entry()
  entry.pack(anchor=SW)
  btn3 = ttk.Button(root, text="Добавить вкус", command=lambda: morz.add_flavor(entry.get()))
  btn3.pack(anchor=S)
  btn4 = ttk.Button(root, text="Обновить рейтинг", command=lambda: morz.renew_rating(int(entry.get())))
  btn4.pack(anchor=E)
  btn5 = ttk.Button(root, text="Удалить вкус", command=lambda: morz.delete_flavor(entry.get()))
  btn5.pack(anchor=S)
  root.mainloop()

