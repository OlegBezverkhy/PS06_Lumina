# PS06_Lumina
 Решение задания PS06

### Способ №1 - Scrapy
#### Файл с кодом: ./luminapars/puminapars/spider/luluminanewpars.py
#### Вывод результатов: ./luminapars/puminapars/spider/output.csv

Использование стандартной функциональности Scrapy - экспорт фидов, 
которая позволяет создавать фиды с извлеченными элементами, используя 
несколько форматов сериализации и механизмы хранения.

В задании требуется формат CSV:

Значение для ключа format в настройке FEEDS: csv

Используемый экспортер: CsvItemExporter

Чтобы указать столбцы для экспорта и их порядок, используйте FEED_EXPORT_FIELDS.

### Способ №2 - Selenium
#### Файл с кодом: selenium_pars.py
#### Вывод результатов: selenium_pars.csv

Испрользование Silenium: 
1. Находим всю карточки светильников на сайте, 
2. Перебираем полученнные карточки, извлекая нужную информацию при помощи XPATH
3. Сохраняем отобранную информцию в список
4. Сохраняем список в файл
