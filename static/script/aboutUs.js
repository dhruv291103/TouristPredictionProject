// adding review function(circle button)
// let circle = document.querySelectorAll(".circle")
let review = document.querySelectorAll(".review")
let read_less = document.getElementById("read_less")
let read_more = document.getElementById("read_more")
let details = document.getElementById("details")
// console.log(circle)
// console.log(review);
// let arr = Array.from(review);
// let value = 1
// const arr = Array.from(circle)
// arr.map((curElem)=>{
//     curElem.addEventListener("click",()=>{
//         if(value == 1){
//             curElem.style.backgroundColor = "green";
//             value = 0;
//         }else{
//             curElem.style.backgroundColor = "white";
//             value = 1;
//         }
//     })
// });

// for(let i =0;i<circle.length; i++){
//     circle[i].starValue = (i+1);
//     circle[i].addEventListener("mouseover", showRating)
// }
// function showRating(e){
//     console.log("hello");
//     let starValue = this.starValue;
    
//     // console.log("clicked on", starValue);
//     circle.forEach(function(elem, ind){
//         if(ind < starValue){
//             elem.classList.add("green");
//         }else{
//             elem.classList.remove("green");
//         }
//     })
// }



// read more button functionality
details.style.display = "none";
read_less.style.display = "none";
read_more.addEventListener("click",()=>{
    read_less.style.display = "inline";
    read_more.style.display = "none";
    details.style.display ="inline";
})
read_less.addEventListener("click",()=>{
    read_more.style.display ="inline";
    read_less.style.display = "none";
    details.style.display ="none";
})