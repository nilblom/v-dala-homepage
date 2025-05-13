document.addEventListener("DOMContentLoaded", function() {

    if (localStorage.getItem("mobile") == "false")
    	window.location.href = "./index.html";

    if (window.location.href.includes("/mobile/"))
    	localStorage.setItem("mobile", "true");
    else
    	localStorage.setItem("mobile", "false")

    enable_translate();

    if (localStorage.getItem("language") == "en")
        translate();
});

/* Functions to enable translation to English. */

function enable_translate() {
    document.getElementById("switch-language").addEventListener("click", function(e) {
        translate();
        if (localStorage.getItem("language") == "sv")
            localStorage.setItem("language", "en");
        else
            localStorage.setItem("language", "sv");
    });
}

function translate() {
    document.querySelectorAll("[t]").forEach(node => {
        var original_text = node.innerText;
        node.innerText = node.getAttribute("t");
        node.setAttribute("t", original_text);
    });
}
