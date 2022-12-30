let degree = document.getElementById('degree')
let subject = document.getElementById('subject')
// let test_temp = document.getElementById('temp_id')
window.addEventListener('load',function(e){
    e.preventDefault()
    axios.get("/get_degrees/").then(function(resp){
        degree.innerHTML += resp.data
    }).catch(function(err){
        console.log(err);
    })
})

// window.addEventListener('load',function(e){
//     e.preventDefault()
//     axios.get("/get_subjects/").then(function(resp) {
//         subject.innerHTML += resp.data;
//     }).catch((err) => {
//         console.log(err);
//     });
// })

degree.addEventListener('change',function(){
    let selected_degree = document.getElementById('degree').value
    selected_degree = parseInt(selected_degree)
    console.log(selected_degree);
    let url = "/get_subjects/" +selected_degree
    axios.get(url).then(function(resp){
        subject.innerHTML = resp.data
        ;
    }).catch(function(err){
        console.log(err);
    })
})

let form = document.getElementById('info')

form.addEventListener('submit',function(e){
    e.preventDefault()

    let fd = new FormData()

    fd.append("name",document.getElementById('name').value)

    fd.append("dob",document.getElementById('dob').value)
    fd.append("degree",document.getElementById('degree').value)
    fd.append("subject",document.getElementById('subject').value)
    fd.append("csrfmiddlewaretoken",'{csrf_token}')

    axios.post("/add/",fd).then(function(resp)  {
        form.reset()
        console.log(resp.data.status);
    }).catch((err) => {
        console.log(err);
    });
})

let form_2 = document.getElementById('test')

form_2.addEventListener('submit',function(e){
    e.preventDefault();
    let form_2_data = new FormData(form_2)
    // let url_var = form_2_data.append("temp_id",document.getElementById('temp_id').value)
    let url_var =document.getElementById("temp_id").value
    console.log(url_var);
    url_var = parseInt(url_var)
    let new_url = "/test/"+url_var

    axios.get(new_url).then(function(res){
        console.log(res.data); 
        form_2.reset()      
    }).catch((err) => {
        
    });
})
