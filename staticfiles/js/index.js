
// Function to change logo based on theme
function changeLogo(isDark) {
    const logoImg = document.getElementById('logo-img');
    if (isDark) {
        logoImg.src = "/static/images/logo_dark.png"; // Dark theme logo
    } else {
        logoImg.src = "/static/images/logo.png"; // Light theme logo
    }
}

// Function to toggle the theme between light and dark mode
function toggleTheme(isDark) {
    const appDiv = document.getElementById('app');
    const nav = document.getElementById('mynavbar');
    appDiv.setAttribute('data-theme', isDark ? 'dark' : 'light');

    if (isDark) {
        nav.classList.add('navbar-dark', 'bg-dark');
        nav.classList.remove('navbar-light', 'bg-light');
    } else {
        nav.classList.add('navbar-light', 'bg-light');
        nav.classList.remove('navbar-dark', 'bg-dark');
    }
}

// Set up theme toggle switch
const themeToggle = document.getElementById('theme-toggle');
const savedPreference = localStorage.getItem('isDark');
let isDark = savedPreference !== null ? JSON.parse(savedPreference) : window.matchMedia("(prefers-color-scheme: dark)").matches;

themeToggle.checked = isDark;
toggleTheme(isDark);
changeLogo(isDark);

themeToggle.addEventListener('change', function() {
    isDark = themeToggle.checked;
	changeLogo(isDark);
    toggleTheme(isDark);
    localStorage.setItem('isDark', JSON.stringify(isDark));
});

var onResize = function () {
	var navbar = $("#mynavbar");
    var navbarHeight = navbar.outerHeight(true);
	// apply dynamic padding at the top of the body according to the fixed navbar height
	$("#content").css("padding-top", navbarHeight);
  };

  // attach the function to the window resize event
  $(window).resize(onResize);

  // call it also when the page is ready after load or reload
  $(function () {
	onResize();
  });




const sr = ScrollReveal({
    origin: 'top',
    distance: '40px',
    duration: 1000,
    delay: 100,

});

sr.reveal('.home_title, .home_img_sm, .home_img, .about_img, .home_summary',{delay: 50});
sr.reveal('.card_desc, .section_desc ,.about_career, .about_txt',{delay: 50});
sr.reveal('.home_social_icon',{ interval: 100});
sr.reveal('.skills_names, .contact_input',{interval: 0}, {delay: 0});




