$(document).ready(function () {
    $("#language_code").keypress(function (e) {
        if (e.key == "Enter") {
            const lang = $("#language_code").val()
            $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
                function (data, textStatus, jqXHR) {
                    $("#hello").html(data.hello)
                }
            );
        }
    });
    $("#btn_translate").click(function () {
        const lang = $("#language_code").val()
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
            function (data, textStatus, jqXHR) {
                $("#hello").html(data.hello)
            }
        );
    });
}); 