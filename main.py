import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    # Получаем выбранный тип пива (1 – светлое, 2 – темное, 3 – пшеничное, 4 – холодного охмеления)
    try:
        beer_type = int(beer_type_var.get())
    except Exception:
        messagebox.showerror("Ошибка", "Выберите тип пива (1,2,3 или 4)")
        return

    # Функция для получения значений из набора виджетов (приводим к float)
    def get_values(entries):
        values = {}
        for key, entry in entries.items():
            try:
                values[key] = float(entry.get())
            except Exception:
                raise ValueError(f"Неверное значение для {key}")
        return values

    try:
        # Полнота вкуса (16 параметров)
        pv = get_values(entries_pv)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Полнота вкуса: {e}")
        return

    # Расчёт баллов для Полноты вкуса в зависимости от типа пива:
    if beer_type == 1:
        score_pv = (9.0 - 0.002*pv["X1"] + 0.004*pv["X2"] - 0.21*pv["X3"] +
                    0.31*pv["X4"] + 1.29*pv["X5"] - 114.7*pv["X6"] + 0.13*pv["X7"] +
                    0.05*pv["X8"] - 0.18*pv["X9"] + 1e-6*pv["X10"] - 0.07*pv["X11"] +
                    0.00024*pv["X12"] - 0.14*pv["X13"] - 0.39*pv["X14"] - 0.13*pv["X15"] +
                    1e-6*pv["X16"])
    elif beer_type == 2:
        score_pv = (2.82 - 0.024*pv["X1"] + 0.0005*pv["X2"] + 0.003*pv["X3"] -
                    0.22*pv["X4"] - 1.29*pv["X5"] + 2.12*pv["X6"] + 0.07*pv["X7"] +
                    0.98*pv["X8"] - 0.174*pv["X9"] + 1e-6*pv["X10"] - 0.012*pv["X11"] +
                    0.01*pv["X12"] + 0.18*pv["X13"] + 24*pv["X14"] + 1e-6*pv["X15"] +
                    1e-6*pv["X16"])
    elif beer_type == 3:
        score_pv = (-3.25 + 0.0187*pv["X1"] + 0.00083*pv["X2"] + 0.0109*pv["X3"] +
                    0.08*pv["X4"] + 1.12*pv["X5"] + 1.98*pv["X6"] - 0.22*pv["X7"] -
                    10.548*pv["X8"] - 0.0937*pv["X9"] + 1e-6*pv["X10"] + 0.0781*pv["X11"] +
                    0.0039*pv["X12"] - 0.312*pv["X13"] - 0.75*pv["X14"] - 0.156*pv["X15"] +
                    1e-6*pv["X16"])
    elif beer_type == 4:
        score_pv = (-2.617 + 0.0208*pv["X1"] - 4.6e-5*pv["X2"] - 0.099*pv["X3"] +
                    1.0*pv["X4"] + 10.844*pv["X5"] + 1.56*pv["X6"] + 0.0081*pv["X7"] +
                    0.0156*pv["X8"] + 0.132*pv["X9"] - 0.155*pv["X10"] - 0.0615*pv["X11"] +
                    0.0327*pv["X12"] - 0.437*pv["X13"] + 17.75*pv["X14"] + 5.5*pv["X15"] +
                    1e-6*pv["X16"])
    else:
        score_pv = 0

    # Солодовый тон (14 параметров)
    try:
        st = get_values(entries_st)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Солодовый тон: {e}")
        return

    # Если тип пива 2 – используем формулу С2, иначе (1,3,4) – С1:
    if beer_type == 2:
        score_st = (-202.88 + 1.44*st["X1"] - 0.61*st["X2"] - 0.055*st["X3"] +
                    0.52*st["X4"] + 4.19*st["X5"] - 0.077*st["X6"] - 3.43*st["X7"] -
                    0.43*st["X8"] + 0.13*st["X9"] + 0.53*st["X10"] + 0.09*st["X11"] -
                    3.03*st["X12"] - 39.19*st["X13"] + 1e-3*st["X14"])
    else:
        score_st = (-7.244 + 0.058*st["X1"] - 0.011*st["X2"] + 0.00234*st["X3"] +
                    0.313*st["X4"] + 1.424*st["X5"] - 0.0066*st["X6"] + 0.427*st["X7"] -
                    0.363*st["X8"] - 0.039*st["X9"] + 1e-6*st["X10"] - 0.0195*st["X11"] -
                    0.135*st["X12"] + 0.0029*st["X13"] + 1e-6*st["X14"])

    # Хмелевая горечь (10 параметров)
    try:
        hg = get_values(entries_hg)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Хмелевая горечь: {e}")
        return

    if beer_type == 1:
        score_hg = (1.87 + 886.3e-4*hg["X1"] + 205.9e-4*hg["X2"] - 0.99*hg["X3"] -
                    0.91*hg["X4"] - 2.84*hg["X5"] + 0.53*hg["X6"] - 0.94*hg["X7"] +
                    3.1*hg["X8"] + 46e-3*hg["X9"] + 1e-6*hg["X10"])
    elif beer_type == 2:
        score_hg = (24.5 - 0.1462*hg["X1"] + 767e-5*hg["X2"] - 414.8e-5*hg["X3"] -
                    0.4963*hg["X4"] + 0.85*hg["X5"] - 0.75*hg["X6"] - 1.5*hg["X7"] +
                    0.2*hg["X8"] - 3.1*hg["X9"] + 1e-6*hg["X10"])
    elif beer_type == 3:
        score_hg = (-2.73 - 567e-5*hg["X1"] + 463e-5*hg["X2"] + 439e-4*hg["X3"] +
                    0.234*hg["X4"] + 0.74*hg["X5"] - 0.14*hg["X6"] + 0.72*hg["X7"] +
                    781.3e-4*hg["X8"] + 273.4e-4*hg["X9"] + 1e-6*hg["X10"])
    elif beer_type == 4:
        score_hg = (5.83 + 386e-5*hg["X1"] - 235e-5*hg["X2"] - 0.2*hg["X3"] -
                    0.59*hg["X4"] + 0.99*hg["X5"] - 0.039*hg["X6"] + 0.19*hg["X7"] -
                    0.047*hg["X8"] + 0.031*hg["X9"] + 1e-6*hg["X10"])
    else:
        score_hg = 0

    # Высота пены (5 параметров)
    try:
        vp = get_values(entries_vp)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Высота пены: {e}")
        return

    score_vp = (13.8615 + 0.01299*vp["X1"] + 417.9115*vp["X2"] -
                0.07886*vp["X3"] + 0.1483*vp["X4"] + 1e-3*vp["X5"])

    # Преобразуем вычисленную высоту пены в дискретную оценку по порогам:
    if score_vp >= 40:
        score_vp_disc = 5
    elif score_vp >= 30:
        score_vp_disc = 4
    elif score_vp >= 20:
        score_vp_disc = 3
    else:
        score_vp_disc = 2

    # Пеностойкость (5 параметров)
    try:
        ps = get_values(entries_ps)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Пеностойкость: {e}")
        return

    score_ps = (-0.5012 + 0.0071*ps["X1"] + 44.5404*ps["X2"] -
                0.00323*ps["X3"] + 0.00732*ps["X4"] + 1e-3*ps["X5"])

    if score_ps >= 4:
        score_ps_disc = 5
    elif score_ps >= 3:
        score_ps_disc = 4
    elif score_ps >= 2:
        score_ps_disc = 3
    else:
        score_ps_disc = 2

    # Цвет (15 параметров)
    try:
        cv = get_values(entries_cv)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Цвет: {e}")
        return

    if beer_type == 1:
        score_cv = (-7.864 + 1.5074*cv["X1"] - 1.4956*cv["X2"] - 0.00344*cv["X3"] +
                    0.1571*cv["X4"] - 0.03603*cv["X5"] + 0.05513*cv["X6"] -
                    0.4447*cv["X7"] + 0.8355*cv["X8"] + 0.5748*cv["X9"] +
                    1.5109*cv["X10"] - 0.00846*cv["X11"] + 0.2034*cv["X12"] -
                    0.1208*cv["X13"] + 7.2118*cv["X14"] - 0.5658*cv["X15"])
    elif beer_type == 2:
        score_cv = (-87.6994 - 126.0151*cv["X1"] + 367.4559*cv["X2"] +
                    0.00032*cv["X3"] - 1.3225*cv["X4"] - 1.0913*cv["X5"] +
                    27.4562*cv["X6"] + 12.7945*cv["X7"] + 18.3104*cv["X8"] -
                    35.125*cv["X9"] + 1e-6*cv["X10"] + 0.2285*cv["X11"] +
                    11.2969*cv["X12"] - 1.1067*cv["X13"] - 23.2891*cv["X14"] +
                    1e-6*cv["X15"])
    elif beer_type == 3:
        score_cv = (-129.4085 + 14.3073*cv["X1"] - 19.8748*cv["X2"] +
                    0.1535*cv["X3"] - 4.6438*cv["X4"] - 0.1314*cv["X5"] -
                    65.3547*cv["X6"] - 4.1645*cv["X7"] + 27.066*cv["X8"] +
                    117*cv["X9"] + 1e-6*cv["X10"] + 0.05469*cv["X11"] +
                    1.2383*cv["X12"] + 0.02362*cv["X13"] + 1.209*cv["X14"] +
                    1e-6*cv["X15"])
    elif beer_type == 4:
        score_cv = (23.0629 + 1e-6*cv["X1"] + 1.6824*cv["X2"] + 0.00839*cv["X3"] -
                    0.8352*cv["X4"] - 0.05325*cv["X5"] - 0.2494*cv["X6"] -
                    0.715*cv["X7"] - 3.3336*cv["X8"] - cv["X9"] +
                    1e-6*cv["X10"] + 0.0625*cv["X11"] - 1.4922*cv["X12"] -
                    0.665*cv["X13"] - 838*cv["X14"] + 1e-6*cv["X15"])
    else:
        score_cv = 0

    # Округляем полученные баллы для первых четырёх показателей
    score_pv_int = round(score_pv)
    score_st_int = round(score_st)
    score_hg_int = round(score_hg)
    score_cv_int = round(score_cv)

    # Суммарный балл. Здесь предположим, что пенообразование рассчитывается как сумма дискретных оценок по высоте пены и пеностойкости.
    total_score = score_pv_int + score_st_int + score_hg_int + score_cv_int + score_vp_disc + score_ps_disc

    # Определяем качество пива по сумме баллов (согласно таблице)
    if 23 <= total_score <= 25:
        quality = "Пиво высокого уровня качества"
    elif 20 <= total_score <= 22:
        quality = "Пиво хорошего уровня качества"
    elif 12 <= total_score <= 19:
        quality = ("Пиво удовлетворительного качества.\n"
                   "Рекомендуется проведение дополнительных показателей готовой продукции")
    else:
        quality = ("Пиво некачественное.\n"
                   "Требуется повторное исследование партий продукции и аудит производства")

    # Формируем текст с результатами расчётов
    results_text = (
        f"Полнота вкуса: {score_pv_int}\n"
        f"Солодовый тон: {score_st_int}\n"
        f"Хмелевая горечь: {score_hg_int}\n"
        f"Цвет: {score_cv_int}\n"
        f"Высота пены (баллы): {score_vp_disc} (Вычислено: {score_vp:.2f} мм)\n"
        f"Пеностойкость (баллы): {score_ps_disc} (Вычислено: {score_ps:.2f} мин)\n"
        f"Итого баллов: {total_score}\n\n"
        f"{quality}"
    )
    results_label.config(text=results_text)

# Создаём главное окно и вкладки
root = tk.Tk()
root.title("Цифровая система оценки качества пивоваренной продукции")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Вкладка для общих настроек (выбор типа пива)
tab_general = ttk.Frame(notebook)
notebook.add(tab_general, text="Общие")

beer_type_var = tk.StringVar()
tk.Label(tab_general, text="Выберите тип пива:").pack(pady=5)
beer_type_combo = ttk.Combobox(tab_general, textvariable=beer_type_var, values=["1", "2", "3", "4"], state="readonly")
beer_type_combo.pack(pady=5)
tk.Label(tab_general, text="1 – светлое, 2 – темное, 3 – пшеничное, 4 – пиво 'холодного' охмеления").pack(pady=5)

# Функция для создания рамки с полями ввода по словарю параметров
def create_entries_frame(parent, entries_dict):
    frame = ttk.Frame(parent)
    for i, (key, label_text) in enumerate(entries_dict.items()):
        tk.Label(frame, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=2)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=5, pady=2)
        entry.insert(0, "0")
        entries_dict[key] = entry  # заменяем текст метки виджетом ввода
    return frame

# Вкладка "Полнота вкуса" (16 параметров)
entries_pv_labels = {
    "X1": "Содержание β-глюкана (мг/дм3):",
    "X2": "Содержание растворимого азота (мг/дм3):",
    "X3": "Содержание меланоидинов (мг/дм3):",
    "X4": "Содержание катехинов (мг/дм3):",
    "X5": "Содержание 4-винил гваякола (мг/дм3):",
    "X6": "Содержание мирцена (мг/дм3):",
    "X7": "Содержание линалоола (мг/дм3):",
    "X8": "Содержание изоксантогумола (мг/дм3):",
    "X9": "Содержание кверцетина (мг/дм3):",
    "X10": "Содержание рутина (мг/дм3):",
    "X11": "Содержание антоцианогенов (мг/дм3):",
    "X12": "Содержание общих полифенолов (мг/дм3):",
    "X13": "Содержание изо-α-гумулона (мг/дм3):",
    "X14": "Содержание сухих веществ начального сусла (%):",
    "X15": "Суммарное содержание карбонильных соединений (мг/дм3):",
    "X16": "Суммарное содержание эфиров (мг/дм3):"
}
entries_pv = entries_pv_labels.copy()
tab_pv = ttk.Frame(notebook)
notebook.add(tab_pv, text="Полнота вкуса")
pv_frame = create_entries_frame(tab_pv, entries_pv)
pv_frame.pack(padx=10, pady=10, anchor="w")

# Вкладка "Солодовый тон" (14 параметров)
entries_st_labels = {
    "X1": "Содержание зернопродуктов (кг):",
    "X2": "Содержание β-глюкана (мг/дм3):",
    "X3": "Содержание растворимого азота (мг/дм3):",
    "X4": "Содержание изогумулона (мг/дм3):",
    "X5": "Содержание изоксантогумола (мг/дм3):",
    "X6": "Содержание катехинов (мг/дм3):",
    "X7": "Содержание кверцетина (мг/дм3):",
    "X8": "Содержание рутина (мг/дм3):",
    "X9": "Содержание меланоидинов (мг/дм3):",
    "X10": "Содержание катионов Са (мг/дм3):",
    "X11": "Содержание катионов Mg (мг/дм3):",
    "X12": "Содержание катионов Mn (мг/дм3):",
    "X13": "Содержание катионов Со (мг/дм3):",
    "X14": "Содержание катионов Na (мг/дм3):"
}
entries_st = entries_st_labels.copy()
tab_st = ttk.Frame(notebook)
notebook.add(tab_st, text="Солодовый тон")
st_frame = create_entries_frame(tab_st, entries_st)
st_frame.pack(padx=10, pady=10, anchor="w")

# Вкладка "Хмелевая горечь" (10 параметров)
entries_hg_labels = {
    "X1": "Содержание β-глюкана (мг/дм3):",
    "X2": "Содержание растворимого азота (мг/дм3):",
    "X3": "Содержание меланоидинов (мг/дм3):",
    "X4": "Содержание катехинов (мг/дм3):",
    "X5": "Содержание изоксантогумола (мг/дм3):",
    "X6": "Содержание кверцетина (мг/дм3):",
    "X7": "Содержание рутина (мг/дм3):",
    "X8": "Содержание антоцианогенов (мг/дм3):",
    "X9": "Содержание общих полифенолов (мг/дм3):",
    "X10": "Содержание изо-α-гумулона (мг/дм3):"
}
entries_hg = entries_hg_labels.copy()
tab_hg = ttk.Frame(notebook)
notebook.add(tab_hg, text="Хмелевая горечь")
hg_frame = create_entries_frame(tab_hg, entries_hg)
hg_frame.pack(padx=10, pady=10, anchor="w")

# Вкладка "Высота пены" (5 параметров)
entries_vp_labels = {
    "X1": "Содержание β-глюкана (мг/дм3):",
    "X2": "Соотношение растворимого азота/азота с тиоловыми группами:",
    "X3": "Содержание катехинов (мг/дм3):",
    "X4": "Содержание катионов Са (мг/дм3):",
    "X5": "Содержание катионов Mg (мг/дм3):"
}
entries_vp = entries_vp_labels.copy()
tab_vp = ttk.Frame(notebook)
notebook.add(tab_vp, text="Высота пены")
vp_frame = create_entries_frame(tab_vp, entries_vp)
vp_frame.pack(padx=10, pady=10, anchor="w")

# Вкладка "Пеностойкость" (5 параметров)
entries_ps_labels = {
    "X1": "Содержание β-глюкана (мг/дм3):",
    "X2": "Соотношение растворимого азота/азота с тиоловыми группами:",
    "X3": "Содержание катехинов (мг/дм3):",
    "X4": "Содержание катионов Са (мг/дм3):",
    "X5": "Содержание катионов Mn (мг/дм3):"
}
entries_ps = entries_ps_labels.copy()
tab_ps = ttk.Frame(notebook)
notebook.add(tab_ps, text="Пеностойкость")
ps_frame = create_entries_frame(tab_ps, entries_ps)
ps_frame.pack(padx=10, pady=10, anchor="w")

# Вкладка "Цвет" (15 параметров)
entries_cv_labels = {
    "X1": "Содержание сухих веществ начального сусла (%):",
    "X2": "Содержание алкоголя (мас%):",
    "X3": "Содержание растворимого азота (мг/дм3):",
    "X4": "Содержание азота с тиоловыми группами (мг/дм3):",
    "X5": "Содержание β-глюкана (мг/дм3):",
    "X6": "Содержание кверцетина (мг/дм3):",
    "X7": "Содержание рутина (мг/дм3):",
    "X8": "Содержание катехинов (мг/дм3):",
    "X9": "Содержание рибофлавина (мг/дм3):",
    "X10": "Содержание карамелей (HI):",
    "X11": "Содержание меланоидинов (мг/дм3):",
    "X12": "Содержание катионов Са (мг/дм3):",
    "X13": "Содержание катионов Mg (мг/дм3):",
    "X14": "Содержание катионов Mn (мг/дм3):",
    "X15": "Содержание катионов Со (мг/дм3):"
}
entries_cv = entries_cv_labels.copy()
tab_cv = ttk.Frame(notebook)
notebook.add(tab_cv, text="Цвет")
cv_frame = create_entries_frame(tab_cv, entries_cv)
cv_frame.pack(padx=10, pady=10, anchor="w")

# Вкладка с результатами
tab_results = ttk.Frame(notebook)
notebook.add(tab_results, text="Результаты")
results_label = tk.Label(tab_results, text="", justify="left", font=("Arial", 11))
results_label.pack(padx=10, pady=10)

# Кнопка расчёта размещается в нижней части основного окна
calc_button = tk.Button(root, text="Рассчитать", command=calculate, font=("Arial", 12))
calc_button.pack(pady=10)

root.mainloop()