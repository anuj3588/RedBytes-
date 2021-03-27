// Delete
function deleteFunctionNow(url, csrf) {
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", url);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", csrf);
    xhr.send();
    $("#table").find("tr:gt(0)").remove();
    setTimeout(()=>{
        list()
    },100)
}

function deleteNow(urls,csrf,slug) {
    swal({
        title: "Are you sure?",
        text: "You want to delete!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            swal("Deleted ", "", "successfully", {
                icon: "success",
            });
            const url = '/secret/api/v1/router/'+ urls +'/' + slug + '/'
            deleteFunctionNow(url,csrf)
            $("#table").find("tr:gt(0)").remove();
        } else {
            swal("Request cancel!");
        }
    });
}
// End Delete

// delete with all url
function deleteFullUrls(urls,csrf,slug) {
    swal({
        title: "Are you sure?",
        text: "You want to delete!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            swal("Deleted ", "", "successfully", {
                icon: "success",
            });
            const url = ''+ urls +''+ slug + '/'
            deleteFunctionNow(url,csrf)
            $("#table").find("tr:gt(0)").remove();
        } else {
            swal("Request cancel!");
        }
    });
}


// Delete function for redirect
function deleteFullUrlsRedirect(urls,csrf,slug) {
    swal({
        title: "Are you sure?",
        text: "You want to delete!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            swal("Deleted ", "", "successfully", {
                icon: "success",
            });
            const url = ''+ urls +''+ slug + '/'
            deleteFunctionNow(url,csrf)
            $("#table").find("tr:gt(0)").remove();
            
        } else {
            swal("Request cancel!");
        }
    });
}