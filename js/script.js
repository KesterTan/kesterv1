const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    // Toggle the navlinks out
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');

        // Animate Links
        // Use index to allow for delay between each link
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index/7 + 0.4}s`;
            }
        });
        // Burger Animation
        burger.classList.toggle(`toggle`);
    });
}

// Gallery
const galleryImages = document.querySelectorAll(".gallery-img");
let getLatestOpenedImg;
const windowWidth = window.innerWidth;

// For each gallery image, open image up
if (galleryImages) {
    galleryImages.forEach((image, index) => {
        image.onclick = () => {
            // alert("working");
            // Get background image url
            const getElement = window.getComputedStyle(image);
            const FullImgUrl = getElement.getPropertyValue("background-image");
            // alert(FullImgUrl);
            const ImgUrlPos = FullImgUrl.split("/images/");
            const setNewImgUrl = ImgUrlPos[1].replace('")', '');
            // alert(setNewImgUrl);

            getLatestOpenedImg = index + 1;

            // Create div container for image being brought up
            const container = document.body;
            const newImgWindow = document.createElement("div");
            container.appendChild(newImgWindow);
            newImgWindow.setAttribute("class", "img-window");
            newImgWindow.setAttribute("onclick", "closeImg()");

            const newImg = document.createElement("img");
            newImgWindow.appendChild(newImg);
            newImg.setAttribute("src", "images/" + setNewImgUrl);
        }
    });
}

function closeImg() {
    document.querySelector(".img-window").remove();
}

navSlide();