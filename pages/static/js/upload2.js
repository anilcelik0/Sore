$(document).ready(function () {
    $('#upload2-form').hide()

    $('#form1').click(function () {
        $('#upload-form').show()
        $('#upload2-form').hide()
    })
    $('#form2').click(function () {
        $('#upload-form').hide()
        $('#upload2-form').show()
    })
    
})

document.getElementById('id_hide').classList.add('form-select')

const uploadForm2 = document.getElementById('upload2-form')
const input1 = document.getElementById('id_photo_name1')

const alertBox1 = document.getElementById('alert-box1')
const imageBox1 = document.getElementById('image-box1')
const cancelBox1 = document.getElementById('cancel-box1')
const cancelBtn1 = document.getElementById('cancel-btn1')
const confirmBtn1 = document.getElementById('confirm1')

const input2 = document.getElementById('id_photo_name2')
input2.classList.add('not-visible')

const imageBox2 = document.getElementById('image-box2')
const sendBtn2 = document.getElementById('send2')

const csrf2 = document.getElementsByName('csrfmiddlewaretoken')

   
input1.addEventListener('change', () => {
    cancelBox1.classList.remove('not-visible')
    input1.classList.add('not-visible')

    const img_data1 = input1.files[0]
    const url1 = URL.createObjectURL(img_data1)
    imageBox1.innerHTML = '<img id="edit1" src="' + url1 + '" width="200px">'

    var $image = $('#edit1')

    $image.cropper({
        aspectRatio: 3 / 4,
        viewMode: 1,
        rotatable: true,
        minContainerWidth: 300,
        minContainerHeight: 400,
    });

    var cropper = $image.data('cropper')
    cancelBox1.classList.add('not-visible')
    confirmBtn1.classList.remove('not-visible')

    confirmBtn1.addEventListener('click', () => {
        input2.classList.remove('not-visible')
        confirmBtn1.classList.add('not-visible')
        cropper.getCroppedCanvas().toBlob((blob2) => {
            input2.addEventListener('change', () => {
                sendBtn2.classList.remove('not-visible')
                input2.classList.add('not-visible')

                const img_data2 = input2.files[0]
                const url2 = URL.createObjectURL(img_data2)
                imageBox2.innerHTML = '<img id="edit2" src="' + url2 + '" width="200px">'

                var $image2 = $('#edit2')

                $image2.cropper({
                    aspectRatio: 3 / 4,
                    viewMode: 1,
                    rotatable: true,
                    minContainerWidth: 300,
                    minContainerHeight: 400,
                });

                var cropper2 = $image2.data('cropper')

                sendBtn2.addEventListener('click', () => {
                    
                    var option2 = document.getElementById("id_hide").value

                    cropper2.getCroppedCanvas().toBlob((blob) => {
                        const fd2 = new FormData()
                        fd2.append('photo_name2', blob, '2.png')
                        fd2.append('csrfmiddlewaretoken', csrf[0].value)
                        fd2.append('photo_name1', blob2, '1.png')
                        fd2.append('hide',option2)


                        $.ajax({
                            type: "POST",
                            url: uploadForm2.action,
                            enctype: 'multipart/form-data',
                            data: fd2,
                            success: function (response) {
                                window.location = 'http://127.0.0.1:8000/user/profile/' 
                            },

                            error: function (error) {
                                alert("Hata oluştu tekrar deneyiniz")
                                location.reload()

                            },

                            cache: false,
                            contentType: false,
                            processData: false
                        });
                    });
                });
            })
        });
    })
});

