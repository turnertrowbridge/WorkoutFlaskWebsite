document.querySelectorAll('.delete-workout-btn').forEach(function(button) {
    button.addEventListener('click', function() {
        var workoutId = this.getAttribute('data-workout-id');
        var confirmDelete = confirm("Are you sure you want to delete this workout?");
        if (confirmDelete) {
            // Send a request to the server to delete the workout
            fetch('/delete_workout/' + workoutId, { method: 'DELETE' })
                .then(response => response.text())
                .then(message => {
                    console.log(message);
                    alert(message);
                    // Refresh the page
                    location.reload();
                })
                .catch(error => console.error(error));
        }
    });
});
