let title = document.querySelector("title")
let counter = 450;
let chain = document.getElementById("chain");
let otherchain = document.getElementById("otherchain");
 otherchain.style.top = '-' + otherchain.scrollHeight + 'px'

document.addEventListener("DOMContentLoaded", function () {


    // click to start
    Pd.startOnClick(document.body, function () {

        document.querySelector('#start').style.display = 'none'

        // animation title

        let forward = true

        function changeTitle() {
            if (title.textContent.length <= 2) {
                forward = true
            } else if (title.textContent.length >= 10) {
                forward = false
            }

            if (forward == true) {
                title.textContent += "🫒";
            } else {
                title.textContent = title.textContent.substring(0, title.textContent.length - 2);;
            }

        }

        setInterval(changeTitle, 300);



  


        // animation left

        let checkPos = chain.scrollHeight
        checkPos = -checkPos
        function down() {

            Pd.send('stopvelox', [1]);

            if (counter <= checkPos) {
                chain.style.top = "0";
                counter = 900;
                Pd.send('fastdue', [2]);
            }

            chain.style.top = `${counter}px`;
            counter = counter - 250;
            Pd.send('startvelox', [.1]);
        }

        setInterval(down, 5000);

        // animation right

        let toBottom = true;
        const chainHeight = otherchain.scrollHeight;

        otherchain.style.top = `-${chainHeight}px`;

        otherchain.addEventListener('transitionend', function (e) {
            if (toBottom) {
                otherchain.style.top = `${chainHeight}px`;
                otherchain.style.transition = 'top 1000s linear'; 

                toBottom = false;
            } else {
                otherchain.style.top = `-${chainHeight}px`;
                otherchain.style.transition = 'top 1s linear';
                Pd.send('fastuno', [2]);
                toBottom = true;
            }
        });

        setTimeout(() => {
            otherchain.style.top = `${chainHeight}px`;
            toBottom = false;
        }, 10);



    })
});