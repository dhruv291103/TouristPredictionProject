const LoginDetails = document.getElementById("LoginDetails")
  const loginDiv = document.getElementById("loginDiv")
  const loginmenu = document.getElementById("loginmenu")
  const Info_div = document.getElementById("info")
  const ul_info = document.getElementById("ulinfo")
  const liname = document.getElementById("liname")
  const liemail = document.getElementById("liemail")
  const btnlogout = document.getElementById("btnlogout")
  if('{{session.email}}')
  {
    console.log('{{session.email}}');
    LoginDetails.style.display = "flex";
    loginDiv.style.display = "flex";
    loginmenu.style.display= "none";

    loginDiv.addEventListener("click",()=>{
      console.log("helo")
      Info_div.style.display = "flex";
      Info_div.classList.add("info")
   
      liemail.innerText = '{{session.email}}'.replace('&#39','')
      ul_info.append(liemail)
      const a = document.createElement("a")
      a.innerHTML = '<a href="{{ url_for(`${{login}}`)}}" class="btn btn-light" id="logoutBtn">Logout</a>'
      // btnlogout.innerHTML = '<a class="btn btn-light" id="logoutBtn">Logout</a>'
      ul_info.append(a)
    })
  }