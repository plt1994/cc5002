function addPhotoInput(){
    currentPhotos = document.getElementsByName("foto-avistamiento");
    numberOfpics = currentPhotos.length
    if (numberOfpics < 5) {
        imgInput = '<input type="file" name="foto-avistamiento" id="foto-avistamiento-'+(numberOfpics+1)+'" accept="application/jpg">'
        divPics = document.getElementById("fotos");
        divPics.innerHTML = divPics.innerHTML + imgInput
    }
}

function goToDetail(doc){
    id = doc.id;
    id = 1;
    window.location.href='./detail-'+id+'.html';
}

function moveTo(path){
    window.location.href='./'+path+'.html'
}

function showImg(doc){
    modal = document.getElementById("modal");
    img = '<img src="./img/araña-pollito-800x600.jpg" alt="imagen de araña">'
    modalimg = document.getElementById("modal-img");
    modalimg.innerHTML = img;
    modal.style.display = "block";
}

function hideModal(){
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}
