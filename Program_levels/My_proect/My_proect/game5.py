from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title("Pythonicway PyPaint")  # РЈСЃС‚Р°РЅР°РІР»РёРІР°РµРј РЅР°Р·РІР°РЅРёРµ РѕРєРЅР°
        self.pack(fill=BOTH, expand=1)  # Р Р°Р·РјРµС‰Р°РµРј Р°РєС‚РёРІРЅС‹Рµ СЌР»РµРјРµРЅС‚С‹ РЅР° СЂРѕРґРёС‚РµР»СЊСЃРєРѕРј РѕРєРЅРµ

        self.columnconfigure(6, weight=1) # Р”Р°РµРј СЃРµРґСЊРјРѕРјСѓ СЃС‚РѕР»Р±С†Сѓ РІРѕР·РјРѕР¶РЅРѕСЃС‚СЊ СЂР°СЃС‚СЏРіРёРІР°С‚СЊСЃСЏ, Р±Р»Р°РіРѕРґР°СЂСЏ С‡РµРјСѓ РєРЅРѕРїРєРё РЅРµ Р±СѓРґСѓС‚ СЂР°Р·СЉРµР·Р¶Р°С‚СЊСЃСЏ РїСЂРё СЂРµСЃР°Р№Р·Рµ
        self.rowconfigure(2, weight=1) # РўРѕ Р¶Рµ СЃР°РјРѕРµ РґР»СЏ С‚СЂРµС‚СЊРµРіРѕ СЂСЏРґР°

        self.canv = Canvas(self, bg="white")  # РЎРѕР·РґР°РµРј РїРѕР»Рµ РґР»СЏ СЂРёСЃРѕРІР°РЅРёСЏ, СѓСЃС‚Р°РЅР°РІР»РёРІР°РµРј Р±РµР»С‹Р№ С„РѕРЅ
        self.canv.grid(row=2, column=0, columnspan=7,
                      padx=5, pady=5, sticky=E+W+S+N)  # РџСЂРёРєСЂРµРїР»СЏРµРј РєР°РЅРІР°СЃ РјРµС‚РѕРґРѕРј grid. РћРЅ Р±СѓРґРµС‚ РЅР°С…РѕРґРёС‚СЃСЏ РІ 3Рј СЂСЏРґСѓ, РїРµСЂРІРѕР№ РєРѕР»РѕРЅРєРµ, Рё Р±СѓРґРµС‚ Р·Р°РЅРёРјР°С‚СЊ 7 РєРѕР»РѕРЅРѕРє, Р·Р°РґР°РµРј РѕС‚СЃС‚СѓРїС‹ РїРѕ X Рё Y РІ 5 РїРёРєСЃРµР»РµР№, Рё Р·Р°СЃС‚Р°РІР»СЏРµРј СЂР°СЃС‚СЏРіРёРІР°С‚СЊСЃСЏ РїСЂРё СЂР°СЃС‚СЏРіРёРІР°РЅРёРё РІСЃРµРіРѕ РѕРєРЅР°
        self.canv.bind("<B1-Motion>", self.draw) # РџСЂРёРІСЏР·С‹РІР°РµРј РѕР±СЂР°Р±РѕС‚С‡РёРє Рє РєР°РЅРІР°СЃСѓ. <B1-Motion> РѕР·РЅР°С‡Р°РµС‚ "РїСЂРё РґРІРёР¶РµРЅРёРё Р·Р°Р¶Р°С‚РѕР№ Р»РµРІРѕР№ РєРЅРѕРїРєРё РјС‹С€Рё" РІС‹Р·С‹РІР°С‚СЊ С„СѓРЅРєС†РёСЋ draw

        color_lab = Label(self, text="Color: ") # РЎРѕР·РґР°РµРј РјРµС‚РєСѓ РґР»СЏ РєРЅРѕРїРѕРє РёР·РјРµРЅРµРЅРёСЏ С†РІРµС‚Р° РєРёСЃС‚Рё
        color_lab.grid(row=0, column=0, padx=6) # РЈСЃС‚Р°РЅР°РІР»РёРІР°РµРј СЃРѕР·РґР°РЅРЅСѓСЋ РјРµС‚РєСѓ РІ РїРµСЂРІС‹Р№ СЂСЏРґ Рё РїРµСЂРІСѓСЋ РєРѕР»РѕРЅРєСѓ, Р·Р°РґР°РµРј РіРѕСЂРёР·РѕРЅС‚Р°Р»СЊРЅС‹Р№ РѕС‚СЃС‚СѓРї РІ 6 РїРёРєСЃРµР»РµР№

        red_btn = Button(self, text="Red", width=10,
                         command=lambda: self.set_color("red")) # РЎРѕР·РґР°РЅРёРµ РєРЅРѕРїРєРё:  РЈСЃС‚Р°РЅРѕРІРєР° С‚РµРєСЃС‚Р° РєРЅРѕРїРєРё, Р·Р°РґР°РЅРёРµ С€РёСЂРёРЅС‹ РєРЅРѕРїРєРё (10 СЃРёРјРІРѕР»РѕРІ), С„СѓРЅРєС†РёСЏ РІС‹Р·С‹РІР°РµРјР°СЏ РїСЂРё РЅР°Р¶Р°С‚РёРё РєРЅРѕРїРєРё.
        red_btn.grid(row=0, column=1) # РЈСЃС‚Р°РЅР°РІР»РёРІР°РµРј РєРЅРѕРїРєСѓ

        # РЎРѕР·РґР°РЅРёРµ РѕСЃС‚Р°Р»СЊРЅС‹С… РєРЅРѕРїРѕРє РїРѕРІС‚РѕСЂСЏРµС‚ С‚Сѓ Р¶Рµ Р»РѕРіРёРєСѓ, С‡С‚Рѕ Рё СЃРѕР·РґР°РЅРёРµ
        # РєРЅРѕРїРєРё СѓСЃС‚Р°РЅРѕРІРєРё РєСЂР°СЃРЅРѕРіРѕ С†РІРµС‚Р°, РѕС‚Р»РёС‡Р°СЋС‚СЃСЏ Р»РёС€СЊ Р°СЂРіСѓРјРµРЅС‚С‹.

        green_btn = Button(self, text="Green", width=10,
                           command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=10,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=10,
                           command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="White", width=10,
                           command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10,
                          command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10,
                           command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="Twenty", width=10,
                         command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="Fifty", width=10,
                            command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)


def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()