$(document).ready(function() {
    // Function to load JSON data and update the table
    function loadModuleData(moduleName) {
        $.ajax({
            url: `assets/json/${moduleName}.json`, // Construct the URL using the module name
            dataType: 'json',
            success: function(data) {
                // Clear the table body
                $('#moduleTable tbody').empty();
                // Iterate through the JSON data and insert into the table
                $.each(data, function(index, item) {
                    $('#moduleTable tbody').append('<tr><td>' + item.date + '</td><td>' + item.time + '</td><td>' + item.callsign + '</td></tr>');
                });
            },
            error: function(xhr, status, error) {
                console.error('Error loading JSON:', status, error);
            }
        });
    }

    // Function to initialize the module
    function initializeModule() {
        // Get the module name from the data-module attribute
        const moduleName = $('#moduleTable').data('module');
        if (moduleName) {
            // Load JSON initially
            loadModuleData(moduleName);
            // Refresh JSON every 15 seconds
            setInterval(function() {
                loadModuleData(moduleName);
            }, 15000);
        } else {
            console.error('No module name specified in data-module attribute');
        }
    }

    // Initialize the module
    initializeModule();
});
