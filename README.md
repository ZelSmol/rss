#RSS reader

## Использование
__Запустить файл main.py (bold)__
В запустившемся окне, можно пользоваться реализованным функционалом.
![Alt-текст](https://vk.com/im?sel=169941761&z=photo169941761_457248733%2Fmail493856 "main window")
Чтобы получить список новостей из имеющегося RSS-источника, необходимо вставить ссылку в input и нажать на кнопку `Get news` 

## Функционал
- Выдача базовой подборки новостей из уже имющихся источников
- Сортировка новостей по релевантности, с помощью очереди с приоритетами
- Сохранение данных о предпочтении пользоваетеля в JSON-файл.

## Необходимые библиотеки
- sklearn
- eel
- requests
```
pip install eel sklearn requests
```
## Приложения
Код блока новостей в коде HTML
```html
<div class="px-5">
    <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static">
            <span class="badge rounded-pill bg-{color}" style="width: 25%;">{category}</span>
            <h3 class="mb-0">{title}</h3>
            <div class="mb-1 text-muted">{pub_date}</div>
            <p class="mb-auto">{description}</p>
            <p class="mb-auto"><i>{author}</i></p>
            <a href="{guid}" target="_blank" onclick="update_user_profile('{category}', '{url}')" class="btn btn-primary" id="guid-link" style="width: 25%;">Continue reading</a>
        </div>
        <div class="col-auto d-none d-lg-block ">
            <img src={img_link} width=151px height=151px class="rounded-circle mt-5">
        </div>
    </div>
</div>
```
Блок-схема работы алгоритма
![Alt-текст]([https://vk.com/im?sel=169941761&z=photo169941761_457248733%2Fmail493856](https://vk.com/im?sel=169941761&z=photo169941761_457248734%2Fmail493897) "diagram")
