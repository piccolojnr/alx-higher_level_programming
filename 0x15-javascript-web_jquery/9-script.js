$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data, textStatus, jqXHR) {
      $('#hello').text(data.hello);
    }
  );
});
