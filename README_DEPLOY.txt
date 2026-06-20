Как залить на Streamlit Community Cloud:

1. Создай новый репозиторий на GitHub, например candle-traffic-streamlit.
2. Загрузи туда 3 файла:
   - streamlit_app.py
   - index.html
   - requirements.txt
3. Открой Streamlit Community Cloud.
4. Нажми Create app / New app.
5. Выбери свой GitHub-репозиторий.
6. В Main file path укажи:
   streamlit_app.py
7. Нажми Deploy.

Локальный запуск:

pip install -r requirements.txt
streamlit run streamlit_app.py

Важно:
- index.html должен лежать рядом со streamlit_app.py.
- Это одна функция: поставить свечку на 2 часа.
- Таймер хранится в localStorage браузера.
