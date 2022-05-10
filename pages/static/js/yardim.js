$(document).ready(function(){
			
    $('#input').keyup(function(){
            var charMap = {Ç:'C',Ö:'O',Ş:'S',İ:'I',I:'i',Ü:'U',Ğ:'G',ç:'c',ö:'o',ş:'s',ı:'i',ü:'u',ğ:'g'};

            var str = $('#input').val();
            str_array = str.split('');

            for(var i=0, len = str_array.length; i < len; i++) {
                str_array[i] = charMap[ str_array[i] ] || str_array[i];
            }

            str = str_array.join('');

            var clearStr = str.replace(" ","").replace("-","").replace(/[^a-z0-9-.çöşüğı]/gi,"");

            
            $('#input').val(clearStr);
            var print = clearStr;
    
    });
});