import streamlit as st
from streamlit_calendar import calendar


def main():
    st.title("mini_scheduler")
    # Define the calendar options
    calendar_options = {
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay"
        },
        "initialView": "timeGridWeek",
        "selectable": True,
        "editable": True
    }

    # Define the events, user should replace these with actual data
    calendar_events = [
        {
            "title": "scheduler",
            "start": "2023-04-05T09:00:00",
            "end": "2023-04-05T17:00:00"
        }
    ]

    # Render the calendar with the options and events
    result = calendar(events=calendar_events, options=calendar_options, key="calendar")

    # Handle the event of a date/time being clicked or an event being added
    if result:
        st.session_state.selected_date = result
        st.write(f"You have selected: {result}")

if __name__ == "__main__":
    main()
