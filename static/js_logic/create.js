// CREATING FULL URL API
function CreateForm(event, url, csrf) {
    const myForm = event.target
    const myFormData = new FormData(myForm)
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.open("POST", ""+url+"");
    xhr.setRequestHeader("X-CSRFToken", csrf);

    xhr.send(myFormData);  
}
// END CREATING FULL URL API


function CreateFormTwo(url, csrf, field, value) {
    var data = new FormData();
    data.append(field, value)

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.open("POST", url);
    xhr.setRequestHeader("X-CSRFToken", csrf);

    xhr.send(data);
}