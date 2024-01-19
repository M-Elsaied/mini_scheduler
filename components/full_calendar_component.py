import os
import streamlit.components.v1 as components

_FULL_CALENDAR_HTML = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend/index.html')

def full_calendar():
    with open(_FULL_CALENDAR_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()
        components.html(html_content, height=800)

if __name__ == "__main__":
    full_calendar()
