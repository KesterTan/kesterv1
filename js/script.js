const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    const navBar = document.querySelector('.navBar')

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

// function autoSlider() {
//     var counter = 1;

//     setInterval(function() {
//         document.getElementById('radio' + counter).checked = true;
//         counter ++;
//         if (counter > 2){
//             counter = 1;
//         };
//     }, 5000);

// }
// autoSlider();

function slider(){
    const slides = document.querySelectorAll(".slide");
    const btns = document.querySelectorAll(".nav-btn");
    var currentSlide = 1;

    // manual nav
    const manualNav = function(manual){
        slides.forEach((slide) => {
            slide.classList.remove("active");

            btns.forEach((btn) => {
                btn.classList.remove("active");
            })
        })

        slides[manual].classList.add("active");
        btns[manual].classList.add("active");
    }

    btns.forEach((btn, i) => {
        btn.addEventListener("click", () => {
            manualNav(i);
            currentSlide = i;
        })
    })

    var repeat = function(activeClass){
        let active = document.getElementsByClassName('active');
        let i = 1;

        var repeater = () => {
            setTimeout(function(){
                [...active].forEach((activeSlide) => {
                    activeSlide.classList.remove("active");
                });

                slides[i].classList.add('active');
                btns[i].classList.add('active');
                i++;
                
                if(slides.length ==i){
                    i = 0;
                }

                if(i >= slides.length){
                    return;
                }

                repeater();

            }, 10000);
        }

        repeater();
    }
    repeat();
}



slider();
navSlide();