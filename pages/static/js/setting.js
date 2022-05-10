//settings

$(document).ready(function () {
    $('#icerik2').hide();
    $('#icerik3').hide();

})

$(document).ready(function () {
    $('#pedit').click(function () {
        $('#icerik1').fadeIn(500);
        $('#icerik2').hide();
        $('#icerik3').hide();

    })
})

$(document).ready(function () {
    $('#ppbtn').click(function () {
        $('#icerik1').hide();
        $('#icerik2').fadeIn(500);
        $('#icerik3').hide();

    })
})

$(document).ready(function () {
    $('.altMenu').hide();
    $('ul li:first').click(function () {
        $('ul li:first ul').toggle('slow')
    })
})

$(document).ready(function () {
    $('#ppassword').click(function () {
        $('#icerik1').hide();
        $('#icerik2').hide();
        $('#icerik3').fadeIn(500);

    })
})

