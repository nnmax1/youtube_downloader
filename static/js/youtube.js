function downloadedFiles(){
    fetch('/downloadedfiles').then(response => response.json())
    .then(data => { 
        if (data.data.length > 0){
            var msg = document.getElementById("fileMsg")
            msg.setAttribute("style", "opacity: 100;")
            msg.innerHTML= "Files Downloaded:"
            var list= document.getElementById("fileList")
            listHTML =""
            list.innerHTML = ""
            for (i =0;i< data.data.length; i++){
                listHTML =listHTML + "<li>"+data.data[i]+"</li>"
            }
            list.innerHTML = listHTML 
        }
    });
}
var download= setInterval(downloadedFiles, 10000);

function setText() {
    document.getElementById("downloadingMsg").innerHTML = "Downloading..."
}
function deleteFiles() {
    fetch('/deleteData').then(response => response.json())
    .then(data => {
        console.log(data.status)
        document.getElementById("downloadingMsg").innerHTML = "Files deleted"
    });
    var msg = document.getElementById("fileMsg").setAttribute("style", "opacity: 0;")
    var filelist= document.getElementById("fileList").setAttribute("style", "opacity: 0;")
}