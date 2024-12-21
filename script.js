
document.addEventListener("DOMContentLoaded", function () {
    let title =  document.querySelector("title")
    let counter = 450;
    let chain = document.getElementById("chain");
    let otherchain = document.getElementById("otherchain");
    

    // animation title

    let forward = true 

    function changeTitle() {
        if (title.textContent.length<=2){
            forward = true
        } else if(title.textContent.length>=10){
            forward = false
        }

        if(forward == true){
            title.textContent += "🫒";
        } else {
            title.textContent = title.textContent.substring(0, title.textContent.length - 2);; 
        }

    }

    setInterval(changeTitle, 300);

    // animation one

    function down() {
        if (counter <= Number(-134185)) {
            setTimeout(() => {
                window.location.reload()
            }, 400);
        }
        chain.style.bottom = `${counter}px`;
        counter = counter - 250;
        console.log(counter);
    }

    setInterval(down, 3000);

    // animation two

    otherchain.style.top = '-'+otherchain.scrollHeight+'px'

    otherchain.scrollTo({ top: 0, left: 0, behavior: "smooth" });

    // toggle theme

    document.getElementById('theme').addEventListener("click", ()=>{
        document.body.classList.toggle('light');
    })

});