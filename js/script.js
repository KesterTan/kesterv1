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
            newImg.setAttribute("id", "current-img");
            
            // Check if img loaded
            newImg.onload = () => {
                //alert('loaded');
                // Width of object
                let imgWidth = newImg.width;
                //alert(imgWidth);
                let calcImgToEdge = ((windowWidth - imgWidth) / 2) - 50;
                if (calcImgToEdge < 0) {
                    calcImgToEdge = 0;
                }
                //alert(calcImgToEdge);


                // Next btn
                const newNextBtn = document.createElement("a");
                const btnNextText = document.createTextNode("Next");
                newNextBtn.appendChild(btnNextText);
                container.appendChild(newNextBtn);
                newNextBtn.setAttribute("class", "img-btn-next");
                newNextBtn.setAttribute("onclick", "changeImg(1)");
                newNextBtn.style.cssText = `right: ${calcImgToEdge}px;`;

                // Prev btn
                const newPrevBtn = document.createElement("a");
                const btnPrevText = document.createTextNode("Prev");
                newPrevBtn.appendChild(btnPrevText);
                container.appendChild(newPrevBtn);
                newPrevBtn.setAttribute("class", "img-btn-prev");
                newPrevBtn.setAttribute("onclick", "changeImg(0)");
                newPrevBtn.style.cssText = `left: ${calcImgToEdge}px;`;
            }

        }
    });
}

function closeImg() {
    document.querySelector(".img-window").remove();
    document.querySelector(".img-btn-next").remove();
    document.querySelector(".img-btn-prev").remove();
}

function changeImg(changeDir) {
    document.querySelector("#current-img").remove();

    const getImgWindow = document.querySelector(".img-window");
    const newImg = document.createElement("img");
    getImgWindow.appendChild(newImg);

    let calcNewImg;
    if(changeDir === 1) {
        calcNewImg = getLatestOpenedImg + 1;
        if (calcNewImg > galleryImages.length) {
            calcNewImg = 1;
        }
    }
    else if(changeDir === 0) {
        calcNewImg = getLatestOpenedImg - 1;
        if (calcNewImg < 1) {
            calcNewImg = galleryImages.length;
        }
    }

    newImg.setAttribute("src", "images/Pic" + calcNewImg + ".jpg");
    //alert(calcNewImg);

    // Updating images variables
    newImg.setAttribute("id", "current-img");
    getLatestOpenedImg = calcNewImg;

    newImg.onload = () => {
        let imgWidth = newImg.width();
        let calcImgToEdge = ((windowWidth - imgWidth) / 2) - 50;
            if (calcImgToEdge < 0) {
                calcImgToEdge = 0;
            }
        
        const nextBtn = document.querySelector(".img-btn-next");
        nextBtn.style.cssText = `right: ${calcImgToEdge}px;`;

        const prevBtn = document.querySelector(".img-btn-prev");
        prevBtn.style.cssText = `left: ${calcImgToEdge}px;`;
    }
}

navSlide();

