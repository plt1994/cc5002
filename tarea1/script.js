const COMUNAS = {
    0: [],
    1: ["Arica", "Camarones", "Putre", "General Lagos"],
    2: ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"],
    13: ["Calera de Tango"],
}

function addPhotoInput(button) {
    id = button.id[button.id.length - 1]
    divPics = button.parentElement.getElementsByTagName("div")["fotos-" + id];
    currentPhotos = divPics.children;
    numberOfpics = currentPhotos.length
    if (numberOfpics < 5) {
        for (i = 0; i < currentPhotos.length; i++) {
            if (currentPhotos[i].files.length == 0) {
                return;
            }
        }
        imgInput = document.createElement("input")
        imgInput.setAttribute("type", "file");
        imgInput.setAttribute("name", "foto-avistamiento");
        imgInput.setAttribute("id", "foto-avistamiento-" + id + "-" + (numberOfpics + 1))
        imgInput.setAttribute("accept", "application/jpg");
        divPics.appendChild(imgInput);
    }
}

function goToDetail(doc) {
    id = doc.id;
    id = 1;
    window.location.href = './detail-' + id + '.html';
}

function moveTo(path) {
    window.location.href = './' + path + '.html'
}

function showImg(doc) {
    modal = document.getElementById("modal");
    img = '<img src="./img/araña-pollito-800x600.jpg" alt="imagen de araña">'
    modalimg = document.getElementById("modal-img");
    modalimg.innerHTML = img;
    modal.style.display = "block";
}

function hideModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}


function loadComunas() {
    region = document.getElementById("region").value
    tag = document.getElementById("comuna");
    tag.innerHTML = '<option value="0">Seleccione Comuna</option>'
    comunas = COMUNAS[region];
    for (let index = 0; index < comunas.length; index++) {
        tag.innerHTML += "<option value=" + (index + 1) + ">" + comunas[index] + "</option>"
    }
}

function validateEmail(mail) {
    const mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    return mailformat.test(mail)
}

function validatePhone(phone) {
    const phoneformat = /^\+[1-9]\d{10,14}$/;
    isValid = phoneformat.test(phone);
    return isValid;
}

function getIdNumber(tag) {
    return tag.id[tag.id.length - 1]
}

function validateDate(datetag) {
    id = getIdNumber(datetag);
    if (id == 0) {
        return true;
    }
    dateStr = datetag.value;
    const dateformat = /\d{4}-[01]\d-[0-3]\d [0-2]\d:[0-5]\d/;
    isValid = dateformat.test(dateStr);
    showOrHideError(isValid, datetag, "fecha-" + id);
    return isValid
}

function validateType(typetag) {
    id = getIdNumber(typetag);
    if (id == 0) {
        return true;
    }
    isValid = typetag.value != 0;
    showOrHideError(isValid, typetag, "tipo-" + id);
    return isValid;
}

function validateStatus(statustag) {
    id = getIdNumber(statustag);
    if (id == 0) {
        return true;
    }
    isValid = statustag.value != 0;
    showOrHideError(isValid, statustag, "estado-" + id);
    return isValid;
}

function showErrorMessage(tag, name) {
    tag.parentElement.querySelector("#error-" + name).style.display = "inline-block";
}

function hideErrorMessage(tag, name) {
    tag.parentElement.querySelector("#error-" + name).style.display = "none";
}

function showOrHideError(isValid, tag, name) {
    if (isValid) {
        hideErrorMessage(tag, name)
    } else {
        showErrorMessage(tag, name)
    }
}

function validatePlace() {
    region = document.getElementsByName("region")[0]
    comuna = document.getElementsByName("comuna")[0]
    sector = document.getElementsByName("sector")[0]
    hasRegion = region.value != 0;
    hasComuna = comuna.value != 0;
    validSector = sector.value.length <= 100;
    showOrHideError(hasRegion, region, "region")
    showOrHideError(hasComuna, comuna, "comuna")
    showOrHideError(validSector, sector, "sector")
    return hasComuna && hasRegion && validSector
}

function validateContact() {
    nombre = document.getElementsByName("nombre")[0]
    email = document.getElementsByName("email")[0]
    celular = document.getElementsByName("celular")[0]
    validName = nombre.value.length <= 200 && nombre.value.length > 0;
    hasEmail = email.value.length > 0;
    validEmail = validateEmail(email.value);
    validPhone = true;
    if (celular.value.length > 0) {
        validPhone = validatePhone(celular.value);
    }
    showOrHideError(validName, nombre, "nombre");
    showOrHideError(validEmail, email, "email");
    showOrHideError(validPhone, celular, "celular");
    return validName && validEmail && validPhone
}

function validateForm() {
    //validacion lugar avistamiento
    placeIsValid = validatePlace()
    //validación datos contacto
    contactIsValid = validateContact()
    //validaciones avistamientos
    fechas = document.getElementsByName("dia-hora-avistamiento")
    tipos = document.getElementsByName("tipo-avistamiento")
    estados = document.getElementsByName("estado-avistamiento")
    fotos = document.getElementsByName("foto-avistamiento")

    validDate = true
    fechas.forEach(fecha => {
        isValidDate = validateDate(fecha);
        if (isValidDate == false) {
            validDate = false;
        }
    });
    validType = true
    tipos.forEach(tipo => {
        isValidType = validateType(tipo);
        if (isValidType == false) {
            validType = false;
        }
    });
    validStatus = true;
    estados.forEach(estado => {
        isValidEstado = validateStatus(estado);
        if (isValidEstado == false) {
            validStatus = false;
        }
    });
    validFotos = true;
    fotos.forEach(foto => {
        fotoid = getIdNumber(foto);
        id = getIdNumber(foto.parentElement);
        if(fotoid == 1 && id != 0){
            isValid = foto.files.length > 0;
            showOrHideError(isValid, foto.parentElement, "foto-"+id);
            if(isValid == false){
                validFotos = false;
            }
        }
    });
    noErrors = (
        placeIsValid &&
        contactIsValid &&
        validDate &&
        validType &&
        validStatus &&
        validFotos);
    console.log(noErrors, placeIsValid, contactIsValid, validDate, validType, validStatus, validFotos)
    if (noErrors) {
        modal = document.getElementById("confirm-send-modal");
        modal.style.display = "block";
    }
}

function closeConfirmModal() {
    modal = document.getElementById("confirm-send-modal");
    modal.style.display = "none";
}

function nuevoAvistamiento() {
    divAvistamientos = document.getElementById("avistamientos")
    n = divAvistamientos.children.length
    //TODO: mejorar forma de obtener n
    nuevoDiv = document.getElementById("avistamiento-0").cloneNode(true)
    nuevoDiv.setAttribute("id", "avistamiento-" + (n - 1));
    nuevoDiv.className = "avistamiento";
    nuevoDiv.innerHTML = nuevoDiv.innerHTML.replaceAll("-0", "-" + (n - 1))
    divAvistamientos.appendChild(nuevoDiv)
}


function removerAvistamiento(avistamiento) {
    //TODO: al quitar uno, no se reordenan los otros indices
    divAvistamiento = avistamiento.parentElement.parentElement;
    divAvistamiento.parentElement.removeChild(divAvistamiento);
}


function finishReport(){
    closeConfirmModal()
    modal = document.getElementById("finish-report-modal");
    modal.style.display = "block";
}
