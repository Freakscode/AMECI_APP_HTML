$.getJSON('usuariosactivos', function(data) {
  var table = $('#Users_table').DataTable();
  data = JSON.parse(data);
  data.forEach(function(usuario) {
    var row = $('<tr>');
    row.append($('<td>').text(usuario.fields.nombre));
    row.append($('<td>').text(usuario.fields.cedula));
    row.append($('<td>').text(usuario.fields.celular));
    row.append($('<td>').text(usuario.fields.tarifa));
    row.append($('<td>').text(usuario.fields.fechainicio));
    row.append($('<td>').text(usuario.fields.fechavencimiento));
    var id = usuario.pk;
    row.append($('<td>').text(id));
    table.row.add(row);
  });
  table.draw();
});