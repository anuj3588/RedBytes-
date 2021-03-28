// LIST ROUTER API
function listRouterForm(url) {
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.open("GET", "/secret/api/v1/router/"+url+"/",true);
    xhr.onload = function() {
        const response = xhr.response
        $("#table").find("tr:gt(0)").remove();
        getData(response)
    }
    xhr.send();
}
// END LIST ROUTER API


// LIST without ROUTER API
function listForm(url,slug) {
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    
    xhr.open("GET", "/secret/api/v1/"+url+"/"+slug+"/",true);
    xhr.onload = function() {
        const response = xhr.response
        $("#table").find("tr:gt(0)").remove();
        getDataTwo(response)
    }
    xhr.send();
}
// END LIST without ROUTER API


// LIST NOT ROUTER API
function listNotRouterFunction(url) {
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    
    xhr.open("GET", "/secret/api/v1/"+url+"/",true);
    xhr.onload = function() {
        const response = xhr.response
        getData(response)
    }
    xhr.send();
}
// END LIST NOT ROUTER API


// LIST ROUTER API
function listRouterWithCustomFunction(url,function_name) {
    var f_name = function_name
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    
    xhr.open("GET", url,true);
    xhr.onload = function() {
        const response = xhr.response
        f_name(response)
    }
    xhr.send();
}
// END LIST ROUTER API


// LIST
function listFunction(url) {
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    
    xhr.open("GET", ""+url+"",true);
    xhr.onload = function() {
        const response = xhr.response
        getData(response)
    }
    xhr.send();
}
// END LIST


// list 
function listFullUrlFunction(url,function_name) { 
    const f_name = function_name 
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    
    xhr.open("GET", ""+url+"",true);

    xhr.onload = function() {
        const response = xhr.response
        f_name(response, status=xhr.status)
    }
    xhr.send();
}
// END list 
