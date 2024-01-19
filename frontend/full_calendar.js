document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'dayGrid', 'timeGrid' ], // Need to define plugins to use
    initialView: 'timeGridWeek',  // Sets the initial view to a weekly view
    // Add other FullCalendar configurations here
  });

  calendar.render();
});
