
const uploadForm = document.getElementById('upload-form')
const input = document.getElementById('id_photo_name')

const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')
const confirmBtn = document.getElementById('confirm')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', ()=>{
    input.classList.add('not-visible')
    cancelBox.classList.remove('not-visible')
    cancelBtn.addEventListener('click', ()=>{
        location.reload()
    })

    const img_data = input.files[0]
    const url = URL.createObjectURL(img_data)
    imageBox.innerHTML = '<img id="edit" src="'+url+'" style="width:250px;">'
    confirmBtn.classList.remove('not-visible')
    
    var $image = $('#edit')
    
    $image.cropper({
    aspectRatio: 3 / 4,
    viewMode: 1,
    rotatable: true,
    minContainerWidth:300,
    minContainerHeight:400,
    });
  
    var cropper =$image.data('cropper')

    confirmBtn.addEventListener('click',()=>{
        cancelBox.classList.add('not-visible')
        cropper.getCroppedCanvas().toBlob((blob)=>{
            const fd = new FormData()
            fd.append('csrfmiddlewaretoken',csrf[0].value)
            fd.append('photo_name', blob,'01.jpg')

            $.ajax({
                type: "POST",
                url: uploadForm.action,
                enctype: 'multipart/form-data',
                data: fd,
                success: function(response) {
                    window.location = 'http://127.0.0.1:8000/user/profile/' 

                },

                error: function(error) {
                    alert("Hata oluştu tekrar deneyiniz")
                    location.reload()

                },
        
                cache: false,
                contentType: false,
                processData: false
            });
        })
    })
})
