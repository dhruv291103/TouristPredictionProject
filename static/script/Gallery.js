   // let gallery_images = document.getElementById("gallery_images");
    // let upload = document.getElementById("upload")
    // upload.addEventListener("change",(e)=>{
    //         const files = e.target.files;
    //         for(let image of files){
    //             const picReader = new FileReader();
    //             // console.log(picReader.result)
    //             picReader.readAsDataURL(image);
    //             picReader.addEventListener("load",(e)=>{
    //                 const imageArray = sessionStorage.getItem('files');
    //                 let images = [];

    //                 if (imageArray){
    //                     images = [...JSON.parse(imageArray)]
    //                     images.push(picReader.result);
    //                 }else{
    //                     images.push(picReader.result);
    //                 }
    //                 sessionStorage.setItem("files", JSON.stringify(images));
    //             })
    //         }
    // });

    let result = document.getElementById("result")
    const images = JSON.parse(sessionStorage.getItem('data'))
    // console.log("foreach log", images)

    images.forEach((image)=>{
        result.innerHTML += `<div class="thumbnail"><img src="${image}">
        <a download target="_blank" href="${image}" class="anchor" style="display:none;"><button>download</button></a>
        </img>
        </div>`
    });


    let resultImgSection = document.getElementById("result");
    let largeImage = document.getElementById("largeImage");
    let cross = document.getElementById("cross");
    let download = document.getElementById("download")
    resultImgSection.addEventListener("dblclick",(e)=>{
        result.style.display = "none";
        const largeImageDiv = document.createElement("div");
        largeImageDiv.setAttribute("id","largeImageDiv");
        largeImageDiv.innerHTML = `<img src="${e.target.src}">`;
        largeImage.classList.add("imgIncOnClick");
        largeImage.appendChild(largeImageDiv);
        largeImage.style.display = "flex";
    });

    cross.addEventListener("click",()=>{
        let largeImageDiv = document.getElementById("largeImageDiv");
        largeImageDiv.remove();
        largeImage.style.display = "none"
        result.style.display = "";
    });

    // const watermark_security = document.getElementsByClassName("watermark_security");
    // const arr = Array.from(watermark_security)
    // arr.map((data)=>{
    //     data.style.position = "relative";
    //     data.style.top = "-9rem";
    //     data.style.left = "2rem";
    //     data.style.zIndex = "99";
    //     data.style.color = "white";
    //     data.style.opacity = ".4"
    //     data.style.transform = "rotate(-50deg)"
    // })


    
    