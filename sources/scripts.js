document.addEventListener("DOMContentLoaded", function() {
    // Your code here
    enable_translate();

    if (localStorage.getItem("language") == "en")
    	translate();
});

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