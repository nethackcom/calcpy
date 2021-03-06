# App on Python "Calcpy"

<b><i>Предисловие</i></b>:<br>
  Идея написать этот проект у меня пришла спонтанно. На написание калькулятора у меня ушло не более 5 часов, хотя на начало написания, я не умел вообще писать приложения и мало что в этом понимал.<br>
  Приложение написано на <b>Python</b> используя модуль <b>PyQt5</b> и графический редактор <b>PyQt5 design</b>.<br>
  На протяжении всей работы над проектом, я действовал по правилу <i>"write less, do more"(пиши меньше, делай больше)</i>.<br>
  Я не только просто написал код, а и обдумал все возможные исключения, которые могут возникнуть и обработал их. Так же я старался писать как можно <b>меньше кода</b>, и <b>увеличивать производительность</b> приложения.<br>


<b><i>Цель работы</i></b>:<br>
  Проверить свои возможности в написании кода, планирования, проверки на исключения, тестирование, и научится писать программы на более новых технологиях.<br>
<b><i>Ход работы</i></b>:<br>

1. Я установил PyQt5 design и принялся за разработку графического интерфейса нашего приложения.После чего я сохранил весь графический интерфейс в файл <i>CalcDesign.ui</i><br>
2. Так как содержимое файла CalcDesign.ui было в xml формате, и при закрытии кода, не гарантируется закрытие всех модулей графического приложения, мне пришлось конвертировать xml файл CalcDesign.ui в python-файл CalcDesign.py. В этом мне помогла команда:
```
$ pyuic5 CalcDesign.ui -o CalcDesign.py
```
3. Начал писать сам код.<br>
  a. Подключил файл с графическим интерфейсом.<br>
  b. Добавил обработку события нажатия на кнопки.<br>
  c. Проработал вычисления и обработал исключения. Такие как деление на ноль и вывод ошибки, при не возможном вычислении.<br>
  d. Добавил блокировку клавиш, используя ASCII таблицу.<br>
  f. Создал функцию run и поставил в правильной последовательности вызова методов и запуска нашего объекта CalcApp.<br>
  

<b><i>Итого</b></i>:<br>
  Я освоил новую технологию для написания приложений.<br>
  Научился заранее обдумывать дальнейший код, который собираюсь написать.<br>
  В моем проекте были использованы следующие знания:<br>
    1) Использовал ООП парадигму программирования.<br>
    2) Унаследовование класса, обьекта.<br>
    3) Обработка событий нажатия на кнопку. Блокировка нажатия кнопок, с использованием библиотеки keyboard.<br>
    4) Конвертация строк.<br>
    5) Конкатенация строк.<br>
    6) Обработка исключений.<br>
    7) Работа со строками как с массивами. Индексация букв по такому же принципу как и в массивах.<br>
    8) Генератор списка. Так же выполнение действий над каждым элементом при генерации списка.<br>
    9) Работа с внутренними переменными, которые создаются при сборки проекта(__name__, __main__).<br>
    10) Знание работы обмена информации на низкоуревневом уровне архитектуры. Работа с ASCII символами.
