let display_btn = document.getElementById("display")

  

window.addEventListener('load',function(e){
    e.preventDefault()
    axios.get("/display/").then(function(resp){

        document.getElementById("details").innerHTML+= resp.data
    }).catch((err) => {
        console.log(err);
    });
})

