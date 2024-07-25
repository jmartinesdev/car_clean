function addCar(){
    container = document.getElementById("form-car")

    html = '<br><div class="row"> <div class="col-md"> <input type="text" placeholder="car" class="form-control" name="car"></div> <div class="col-md"> <input type="text" placeholder="reg-car" class="form-control" name="reg-car"> </div> <div class="col-md"> <input type="number" placeholder="year" class="form-control" name="year">'

    container.innerHTML += html
}

function display_form(type){

    add_clients = document.getElementById('add-clients')
    upd_clients = document.getElementById('upd-clients')

    if(type == "1"){
        upd_clients.style.display = "none"
        add_clients.style.display = "block"

    }else if(type == "2"){
        add_clients.style.display = "none";
        upd_clients.style.display = "block"
    }

}

