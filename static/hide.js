document.getElementById('add-new-workout-btn').addEventListener('click', function() {
    document.getElementById('add-workout-form').style.display = 'block';
});

document.getElementById('add-workout-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch('/add_workout', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        if (data === 'success') {
            alert('Workout added successfully!');
        } else {
            alert('Failed to add workout.');
        }
        window.location.reload();
    })
    .catch(error => console.error('Error:', error));
});
