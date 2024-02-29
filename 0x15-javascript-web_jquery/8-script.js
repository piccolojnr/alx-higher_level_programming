$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json",
        function (data, textStatus, jqXHR) {
            htmlList = $("#list_movies")
            for (const item of data.results) {
                htmlList.append(`<li>${item.title}</li>`);
            }
        }
    );
});