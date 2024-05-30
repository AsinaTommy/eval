var table  = document.querySelector('.mypagination')
var tbody = table.querySelector('tbody')
var thead = table.querySelector('thead')
var url = table.getAttribute('url')
var nbelement = table.getAttribute("nb")

var tr = tbody.querySelector('tr')
var td_list = tr.querySelectorAll('td')

var page = 1
var size = 7
var lengthPage = parseInt(nbelement/size) + 1

var next = document.querySelector('.next')
var previous = document.querySelector('.previous')
var go = document.querySelector('.go')
var goinput = document.querySelector('.goinput')

goinput.value = page

console.log(next)


function paginer(page, size, tri){
    formData = new FormData()
    formData.append('size',size)
    formData.append('page',page)
    formData.append('tri',tri)

    getApi(url,formData,'POST')
    .then(function(response) {
        afficherData(response.data)
    })
    .catch(function(error) {
        console.error('Erreur:', error);
    });
}

function afficherData(data){
    tbody.innerHTML = ""
    for(let i = 0; i<data.length; i++){
        tr_new  = tr.cloneNode(true)
        tr_new.style.backgroundColor = "#00ff00";
        Array.from(tr_new.children).forEach(function(td_new) {
            if(contientElements(td_new)){
                td_new.innerHTML = td_new.innerHTML.replaceAll("{"+td_new.getAttribute("value")+"}", data[i][td_new.getAttribute("value")])
            }else{
                td_new.textContent = data[i][td_new.getAttribute("name")]
            }
        });
        tbody.appendChild(tr_new)
    }
}

function contientElements(element) {
    return element.children.length > 0;
}



function maty(){
        if (page<lengthPage){
        page = page + 1
        goinput.value = page
        paginer(page,size,tri)
    }
}

function moty(){
    if (page>1){
        page = page - 1
        goinput.value = page
        paginer(page,size,tri)
    }
}


function mety(){
    if(goinput.value<=lengthPage && goinput.value>=1){
        page = parseInt(goinput.value)
        paginer(page,size,tri)
    }
}



paginer(page,size,tri)

//end of pagination


// choix de colonnes
checkboxs= document.querySelector('.choix').querySelectorAll('input')
console.log(checkboxs)
checkboxs.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        console.log("salut")
        terminer(checkbox)
    });
});

disp = {
    '':'none',
    'none':'',
}




function terminer(check){
    n = check.getAttribute("name")
    element_head = thead.querySelector('th[name="'+n+'"]');
    elements = table.querySelectorAll('td[name="'+n+'"]');
    element_head.style.display = disp[element_head.style.display]
    princ_td = getTrByName(n);
    princ_td.style.display = element_head.style.display
    elements.forEach(function(el){
        el.style.display = disp[el.style.display]
    });
}


function getTrByName(nom){
    for(let i =0; i<td_list.length; i++){
        if (td_list[i].getAttribute('name')==nom){
            return td_list[i];
        }
    }
    return null;
}

// end of choix des colonnes


// tri par colonne
var tri = null

radios= document.querySelector('.tri').querySelectorAll('input')
radios.forEach(function(radio) {
    radio.addEventListener('change', function() {
        colonne = radio.getAttribute("id");
        tri = colonne;
        paginer(page,size,tri)
    });
});