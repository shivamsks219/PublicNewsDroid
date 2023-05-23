function previewImage() {
    var preview = document.querySelector('img.preview');
    var file = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();
   
    reader.onloadend = function () {
      preview.src = reader.result;
      preview.style.display = 'block';
    }
   
    if (file) {
      reader.readAsDataURL(file);
    } else {
      preview.src = "";
    }
   }