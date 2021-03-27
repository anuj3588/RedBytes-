    function editformDidSubmit(event,url,slug,csrf) {
        event.preventDefault
        const myForm = event.target
        const myFormData = new FormData(myForm)
        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        
        xhr.open("PATCH", "/secret/api/"+ url +"/"+ slug +"/");
        xhr.setRequestHeader("X-CSRFToken", csrf);
        xhr.onload = function() {
            if(xhr.status == 400 || xhr.status == 403){
                toastr.warning('Something went worng', 'warning',xhr.status)
            }
    
            if(xhr.status == 500){
                toastr.warning('Server error', 'danger',xhr.status)
            }
    
            if(xhr.status == 201){
                toastr.success('Created successfully.', 'Success',xhr.status)
            }
        }
        $("#table").find("tr:gt(0)").remove();
        try{
            setTimeout(()=>{
                list()
            },100)
        }catch(e){
            pass
        }
        xhr.send(myFormData);
    }


    function editformRouterSubmit(event,url,slug,csrf) {
        event.preventDefault
        const myForm = event.target
        const myFormData = new FormData(myForm)
        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function() {
            if(this.readyState === 4) {
                console.log(this.responseText);
            }
        });

        xhr.open("PATCH", "/secret/api/v1/router/"+ url +"/"+ slug +"/");
        xhr.setRequestHeader("X-CSRFToken", csrf);

        xhr.onload = function() {
            if(xhr.status == 400 || xhr.status == 403){
                toastr.warning('Something went worng', 'warning',xhr.status)
            }

            if(xhr.status == 500){
                toastr.warning('Server error', 'danger',xhr.status)
            }

            if(xhr.status == 201 || xhr.status == 200){
                toastr.success('Update successfully.', 'Success',xhr.status)
            }
        }
        $("#table").find("tr:gt(0)").remove();
        try{
            setTimeout(()=>{
                list()
            },100)
        }catch(e){
            pass
        }
        xhr.send(myFormData);
    }


    function editFullUrlSubmit(event,url,slug,csrf) {
        event.preventDefault
        const myForm = event.target
        const myFormData = new FormData(myForm)
        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.open("PATCH", ""+ url +""+ slug +"/");
        xhr.setRequestHeader("X-CSRFToken", csrf);

        xhr.onload = function() {
            if(xhr.status == 400 || xhr.status == 403){
                toastr.warning('Something went worng', 'warning',xhr.status)
            }

            if(xhr.status == 500){
                toastr.warning('Server error', 'danger',xhr.status)
            }

            if(xhr.status == 201 || xhr.status == 200){
                toastr.success('Update successfully.', 'Success',xhr.status)
            }
        }
        
        $("#table").find("tr:gt(0)").remove();
        try{
            setTimeout(()=>{
                list()
            },100)
        }catch(e){
            pass
        }
        xhr.send(myFormData);
    }
   
    function editImageSubmit(data,url,csrf) {
        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;
        
        
        xhr.open("PATCH", ""+ url +"/");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("X-CSRFToken", csrf);
        

        xhr.onload = function() {
            if(xhr.status == 400 || xhr.status == 403){
                toastr.warning('Something went worng', 'warning',xhr.status)
            }

            if(xhr.status == 500){
                toastr.warning('Server error', 'danger',xhr.status)
            }

            if(xhr.status == 201 || xhr.status == 200){
                toastr.success('Update successfully.', 'Success',xhr.status)
            }
        }

        xhr.send(data);
    }


    function patchFullUrlSubmit(url, slug, csrf, field, value) {
        var data = new FormData();
        data.append(field, value)

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.open("PATCH", ""+ url +""+ slug +"/");
        xhr.setRequestHeader("X-CSRFToken", csrf);

        xhr.onload = function() {
            if(xhr.status == 400 || xhr.status == 403){
                toastr.warning('Something went worng', 'warning',xhr.status)
            }

            if(xhr.status == 500){
                toastr.warning('Server error', 'danger',xhr.status)
            }

            if(xhr.status == 201 || xhr.status == 200){
                toastr.success('Update successfully.', 'Success',xhr.status)
            }
        }
        
        $("#table").find("tr:gt(0)").remove();
        try{
            setTimeout(()=>{
                list()
            },100)
        }catch(e){
            pass
        }
        xhr.send(data);
    }

    function patchFullUrlNoSlugSubmit(url, csrf) {
        alert('url', url, csrf)
        var data = new FormData();
        data.append(field, value)

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.open("PATCH", ""+ url +"");
        xhr.setRequestHeader("X-CSRFToken", csrf);

        xhr.onload = function() {
            if(xhr.status == 400 || xhr.status == 403){
                toastr.warning('Something went worng', 'warning',xhr.status)
            }

            if(xhr.status == 500){
                toastr.warning('Server error', 'danger',xhr.status)
            }

            if(xhr.status == 201 || xhr.status == 200){
                toastr.success('Update successfully.', 'Success',xhr.status)
            }
        }
        
        $("#table").find("tr:gt(0)").remove();
        try{
            setTimeout(()=>{
                list()
            },100)
        }catch(e){
            pass
        }
        xhr.send(data);
    }