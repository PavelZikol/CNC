
ncn = {
"Позиционирование": "Функция G00 используется для выполнения ускоренного перемещения режущего инструмента к позиции обработки или к безопасной позиции. Ускоренное перемещение никогда не используется для выполнения обработки, так как скорость движения исполнительного органа станка очень высока. Код G00 отменяется кодами: G01, G02, G03.",

"Линейная интерполяция": "Функция G01 используется для выполнения прямолинейных перемещений с заданной скоростью (F). При программировании задаются координаты конечной точки в абсолютных значениях (G90) или приращениях (G91) с соответственными адресами перемещений (например X, Y, Z). Код G01 отменяется кодами: G00, G02, G03.",

"Круговая интерполяция по часовой стрелке": "Функция G02 предназначена для выполнения перемещения инструмента по дуге (окружности) в направлении часовой стрелки с заданной скоростью (F). При программировании задаются координаты конечной точки в абсолютных значениях (G90) или приращениях (G91) с соответственными адресами перемещений (например X, Y, Z). Параметры интерполяции I, J, K, которые определяют координаты центра дуги окружности в выбранной плоскости, программируются в приращениях от начальной точки к центру окружности, в направлениях, параллельных осям X, Y, Z соответственно. Код G02 отменяется кодами: G00, G01, G03.",

"Круговая интерполяция против часовой стрелки":" Функция G03 предназначена для выполнения перемещения инструмента по дуге (окружности) в направлении против часовой стрелки с заданной скоростью (F). При программировании задаются координаты конечной точки в абсолютных значениях (G90) или приращениях (G91) с соответственными адресами перемещений (например X, Y, Z). Параметры интерполяции I, J, K, которые определяют координаты центра дуги окружности в выбранной плоскости, программируются в приращениях от начальной точки к центру окружности, в направлениях, параллельных осям X, Y, Z соответственно. Код G03 отменяется кодами: G00, G01, G02.",

"Пауза": "Функция G04 : команда на выполнение выдержки с заданным временем. Этот код программируется вместе с X или Р адресом, который указывает длительность времени выдержки. Обычно, это время составляет от 0.001 до 99999.999 секунд. Например G04 X2.5 : пауза 2.5 секунды, G04 Р1000 : пауза 1 секунда.",

"Выбор плоскости XY": "Код G17 предназначен для выбора плоскости XY в качестве рабочей. Плоскость XY становится определяющей при использовании круговой интерполяции, вращении системы координат и постоянных циклов сверления.",

"Выбор плоскости XZ": "Код G18 предназначен для выбора плоскости XZ в качестве рабочей. Плоскость XZ становится определяющей при использовании круговой интерполяции, вращении системы координат и постоянных циклов сверления.",

"Выбор плоскости YZ": "Код G19 предназначен для выбора плоскости YZ в качестве рабочей. Плоскость YZ становится определяющей при использовании круговой интерполяции, вращении системы координат и постоянных циклов сверления.",

"Отмена коррекции на радиус инструмента": "Функция G40 отменяет действие автоматической коррекции на радиус инструмента G41 и G42.",

"Левая коррекция на радиус инструмента": "Функция G41 применяется для включения автоматической коррекции на радиус инструмента находящегося слева от обрабатываемой поверхности (если смотреть от инструмента в направлении его движения относительно заготовки). Программируется вместе с функцией инструмента (D).",

"Правая коррекция на радиус инструмента": "Функция G42 применяется для включения автоматической коррекции на радиус инструмента находящегося справа от обрабатываемой поверхности (если смотреть от инструмента в направлении его движения относительно заготовки). Программируется вместе с функцией инструмента (D).",

"Коррекция на положение инструмента": "Функция G43 применяется для компенсации длинны инструмента. Программируется вместе с функцией инструмента (H).",

"Заданное смещение": "G54 : G59 Смещение рабочей системы координат детали относительно системы координат станка.",

"Ввод дюймовых данных": "Функция G70 активизирует режим работы с дюймовыми данными.",

"Ввод метрических данных": "Функция G71 активизирует режим работы с метрическими данными.",

"Отмена постоянного цикла": "G80 Функция, которая отменяет любой постоянный цикл.",

"Cтандартный цикл сверления": "Цикл G81 предназначен для зацентровки и сверления отверстий. Движение в процессе обработки происходит на рабочей подаче. Движение в исходное положение после обработки идет на ускоренной подаче.",

"Cверление с выдержкой":" Цикл G82 предназначен для сверления и зенкования отверстий. Движение в процессе обработки происходит на рабочей подаче с паузой в конце. Движение в исходное положение после обработки идет на ускоренной подаче.",

"Цикл прерывистого сверления": "Цикл G83 предназначен для глубокого сверления отверстий. Движение в процессе обработки происходит на рабочей подаче с периодическим выводом инструмента в плоскость отвода. Движение в исходное положение после обработки идет на ускоренной подаче.",

"Цикл нарезания резьбы": "Цикл G84 предназначен для нарезания резьбы метчиком. Движение в процессе обработки происходит на рабочей подаче, шпиндель вращается в заданном направлении. Движение в исходное положение после обработки идет на рабочей подаче с обратным вращением шпинделя.",

"Стандартный цикл растачивания":" Цикл G85 предназначен для развертывания и растачивания отверстий. Движение в процессе обработки происходит на рабочей подаче. Движение в исходное положение после обработки идет на рабочей подаче.",

"Цикл растачивания с остановкой вращения шпинделя": "Цикл G86 предназначен для растачивания отверстий. Движение в процессе обработки происходит на рабочей подаче. В конце обработки происходит остановка шпинделя. Движение в исходное положение после обработки идет на ускоренной подаче.",

"Цикл растачивания с отводом вручную":" Цикл G87 предназначен для растачивания отверстий. Движение в процессе обработки происходит на рабочей подаче. В конце обработки происходит остановка шпинделя. Движение в исходное положение после обработки идет вручную.",

"Режим абсолютного позиционирования":" В режиме абсолютного позиционирования G90 перемещения исполнительных органов производятся относительно нулевой точки рабочей системы координат G54:G59 (программируется, куда должен двигаться инструмент). Код G90 отменяется при помощи кода относительного позиционирования G91.",

"Режим относительного позиционирования": "В режиме относительного (инкрементального) позиционирования G91 за нулевое положение каждый раз принимается положение исполнительного органа, которое он занимал перед началом перемещения к следующей опорной точке (программируется, на сколько должен переместиться инструмент). Код G91 отменяется при помощи кода абсолютного позиционирования G90.",

"Скорость подачи в дюймах/миллиметрах в минуту":" При помощи функции G94 указанная скорость подачи устанавливается в дюймах или в миллиметрах за 1 минуту. Программируется вместе с функцией подачи (F). Код G94 отменяется кодом G95.",

"Скорость подачи в дюймах/миллиметрах на оборот":" При помощи функции G95 указанная скорость подачи устанавливается в дюймах или в миллиметрах на 1 оборот шпинделя. Т.е. скорость подачи F синхронизируется со скоростью вращения шпинделя S. Код G95 отменяется кодом G94.",

"Программируемый останов":" Когда СЧПУ исполняет команду М00, то происходит останов. Все осевые перемещения останавливаются, при этом шпиндель (у большинства станков) продолжает вращаться. Работа по программе возобновляется со следующего кадра после нажатия кнопки Старт.",

"Останов с подтверждением":" Код М01 действует аналогично М00, но выполняется только после подтверждения с пульта управления станка. Если клавиша подтверждения нажата, то при чтении кадра с М01 происходит останов. Если же клавиша не нажата, то кадр М01 пропускается и выполнение УП не прерывается.",

"Завершение программы": "Код М02 указывает на завершение программы и приводит к останову шпинделя, подачи и выключению охлаждения.",

"Вращение шпинделя по часовой стрелке":" При помощи кода М0З включается прямое вращение шпинделя с запрограммированным числом оборотов (S). Код М0З действует до тех пор, пока он не будет отменен с помощью М04 или М05.",

"Вращение шпинделя против часовой стрелки":" При помощи кода М04 включается обратное вращение шпинделя с запрограммированным числом оборотов (S). Код М04 действует до тех пор, пока он не будет отменен с помощью М03 или М05.",

"Останов шпинделя": " Код М05 останавливает вращение шпинделя, но не останавливает осевые перемещения.",

"Смена инструмента": " При помощи кода М06 инструмент, закрепленный в шпинделе, меняется на инструмент, находящийся в положении готовности в магазине инструментов.",

"Включение охлаждение №2": "Код М07 включает подачу СОЖ в зону обработки в распыленном виде, если станок обладает такой возможностью.",

"Включение охлаждения №1": " Код М08 включает подачу СОЖ в зону обработки в виде струи.",

"Отключение охлаждения": " Код М09 выключает подачу СОЖ и отменяет команды М07 и М08.",

"Зажим": "Код М10 относиться к работе с зажимным приспособлением подвижных органов станка.",

"Разжим": " Код М11 относиться к работе с зажимным приспособлением подвижных органов станка.",

"Конец информации":" Код МЗ0 информирует СЧПУ о завершении программы, приводит к останову шпинделя, подачи и выключению охлаждения.",

"Команды осевого перемещения": " X, Y, Z",

"Команды кругового перемещения": " А, В, С  вокруг осей X, Y, Z соответственно:",

"Параметры круговой интерполяции": " I, J, К параллельные осям X, Y, Z соответственно.",

"Радиус": " При круговой интерполяции G02 или G03, R определяет радиус, который соединяет начальную и конечную точки дуги. В постоянных циклах R определяет положение плоскости отвода. При работе с командой вращения R определяет угол поворота координатной системы.",

"Значение коррекции на радиус инструмента": " D",

"Значение компенсации длины инструмента": " H",

"Функция подачи": " F",

"Функция главного движения": " S",

"Значение определяющее номер инструмента, который необходимо переместить в позицию смены, путем поворота инструментального магазина": " T",

"Нумерация кадров УП":" N",

"Пропуск кадра":" /",

"Комментарии в УП": " (...)"
}


