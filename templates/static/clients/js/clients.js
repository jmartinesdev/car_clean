function addCar(){
    container = document.getElementById("form-car")

    html = '<br><div class="row"> <div class="col-md"> <input type="text" placeholder="car" class="form-control" name="car"></div> <div class="col-md"> <input type="text" placeholder="reg-car" class="form-control" name="reg-car"> </div> <div class="col-md"> <input type="number" placeholder="year" class="form-control" name="year">'

    container.innerHTML += html
}

function display_form(type){

    add_client = document.getElementById('add-clients')
    upd_client = document.getElementById('upd_client')

    if(type == '1'){
        upd_client.style.display = "none"
        add_client.style.display = "block"
    }else if(type == "2"){
        upd_client.style.display = "block"
        add_client.style.display = "none"
    }
}