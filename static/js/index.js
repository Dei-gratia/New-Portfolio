
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
const preference = window.matchMedia("(prefers-color-scheme: dark)").matches;
let isDark = JSON.parse(localStorage.getItem('isDark')) || preference;
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
    distance: '60px',
    duration: 2000,
    delay: 200,

});

sr.reveal('.home_data, .about_img, .skills_category, .project_title, .projects_img, .skills_txt',{}); 
sr.reveal('.home_img, .about_subtitle , .about_career, .about_txt, .skills_img',{delay: 400}); 
sr.reveal('.home_social_icon',{ interval: 200}); 
sr.reveal('.skills_data, .contact_input',{interval: 200});




