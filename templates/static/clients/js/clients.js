function addCar(){
    container = document.getElementById("form-car")

    html = '<br><div class="row"> <div class="col-md"> <input type="text" placeholder="car" class="form-control" name=""></div> <div class="col-md"><input type="text" placeholder="reg-car" class="form-control"> </div> <div class="col-md"> <input type="number" placeholder="year" class="form-control" name="ano">'

    container.innerHTML += html
}