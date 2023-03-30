    // Función para actualizar los datos de asistencia
    function updateAttendanceInfo() {
    $.ajax({
        url: '/capture_attendance/', // Ruta de la vista capture_attendance
        success: function (data) {
            // Actualizar los datos en la página
            var attendanceInfo = data.attendance_info;
            var html = '';
            for (var i = 0; i < attendanceInfo.length; i++) {
                html += '<p>' + attendanceInfo[i].nombre + ': ' + attendanceInfo[i].status + '</p>';
            }
            $('#attendance-info').html(html);
        },
        error: function (xhr, status, error) {
            console.error(error);
        }
    });
}

    // Actualizar los datos cada 5 segundos
    setInterval(updateAttendanceInfo, 5000);