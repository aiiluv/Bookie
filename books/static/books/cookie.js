const cookie = document.getElementById("cookie");
const cat = document.getElementById("angry-cat");
const logoutPage = document.getElementById("logout-page");

let moving = false;

cookie.addEventListener("click", function () {

    if (moving) return;

    moving = true;

    // Cookie mulai bergerak
    cookie.classList.add("eating");

    function checkCollision() {

        const cookieRect = cookie.getBoundingClientRect();
        const catRect = cat.getBoundingClientRect();

        const touching =
            cookieRect.left <= catRect.right &&
            cookieRect.right >= catRect.left &&
            cookieRect.top <= catRect.bottom &&
            cookieRect.bottom >= catRect.top;

        if (touching) {

            console.log("COOKIE TOUCHED CAT!");

            // Ambil URL dari HTML
            const nextUrl = logoutPage.dataset.nextUrl;

            console.log("NEXT URL:", nextUrl);

            // Pindah halaman
            window.location.assign(nextUrl);

            return;
        }

        requestAnimationFrame(checkCollision);
    }

    requestAnimationFrame(checkCollision);

});