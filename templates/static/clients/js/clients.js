function addCar(){
    container = document.getElementById("form-car")

    html = '<br><div class="row"> <div class="col-md"> <input type="text" placeholder="car" class="form-control" name="car"></div> <div class="col-md"> <input type="text" placeholder="reg-car" class="form-control" name="reg-car"> </div> <div class="col-md"> <input type="number" placeholder="year" class="form-control" name="year">'

    container.innerHTML += html
}