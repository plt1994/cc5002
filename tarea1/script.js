function addPhotoInput(){
    currentPhotos = document.getElementsByName("foto-avistamiento");
    numberOfpics = currentPhotos.length
    if (numberOfpics < 5) {
        imgInput = '<input type="file" name="foto-avistamiento" id="foto-avistamiento-'+(numberOfpics+1)+'" accept="application/jpg">'
        divPics = document.getElementById("fotos");
        divPics.innerHTML = divPics.innerHTML + imgInput
    }
}