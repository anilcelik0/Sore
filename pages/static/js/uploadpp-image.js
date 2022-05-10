const uploadppForm = document.getElementById('uploadpp-form')
const input = document.getElementById('id_pp')

const imageBox = document.getElementById('image-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')
const sendppBtn = document.getElementById('ppsend')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', ()=>{
    cancelBox.classList.remove('not-visible')
    sendppBtn.classList.remove('not-visible')    
    cancelBtn.addEventListener('click', ()=>{
        location.reload()
    })


    const img_data = input.files[0]
    const url = URL.createObjectURL(img_data)
    imageBox.innerHTML = '<img id="edit" src="'+url+'" width="300px" style="border-radius: 50%;">'            


    var $image = $('#edit')
    
    $image.cropper({
    aspectRatio: 3 / 4,
    viewMode: 1,
    rotatable: true,
    minContainerWidth:300,
    minContainerHeight:400,
    });
  
    var cropper =$image.data('cropper')

    sendppBtn.addEventListener('click',()=>{
        cancelBox.classList.add('not-visible')
        cropper.getCroppedCanvas().toBlob((blob)=>{
            const fd = new FormData()
            fd.append('csrfmiddlewaretoken',csrf[0].value)
            fd.append('pp', blob,'01.png')

            $.ajax({
                type: "POST",
                url: uploadppForm.action,
                enctype: 'multipart/form-data',
                data: fd,
                success: function(response) {
                    location.reload()

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
