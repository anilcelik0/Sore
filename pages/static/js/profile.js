//icerik degis
$(document).ready(function(){
    $('#ciftphotos').hide()
    $('#tek').css('border-bottom','1px solid black')

    $('#tek').click(function(){
        $('#ciftphotos').hide()
        $('#tekphotos').show()
        $('#cift').css('border-bottom','none')
        $('#tek').css('border-bottom','1px solid black')
        return false;
    })

    $('#cift').click(function(){
        $('#tekphotos').hide()
        $('#ciftphotos').show()
        $('#tek').css('border-bottom','none')
        $('#cift').css('border-bottom','1px solid black')
        $( "#cift").off("click");
        return false;
    })
})

$(document).ready(function(){
    $('#ciftupload').hide()
    $('#tekupload').hide()

    $('#form1').click(function(){
        $('#ciftupload').hide()
        $('#tekupload').show()
        return false;
    })

    $('#form2').click(function(){
        $('#tekupload').hide()
        $('#ciftupload').show()
        return false;
    })
})


$(document).ready(function(){
    $('#btntakip').click(function(){
        $('#takip').show()
        $('#takipci').hide()
    })
    $('#btntakipci').click(function(){
        $('#takipci').show()
        $('#takip').hide()
    })
})

$(document).ready(function(){
    $( ".edit" ).hide();
    $("#editbtn").click(function(){
        $( ".edit" ).toggle();
    })
})