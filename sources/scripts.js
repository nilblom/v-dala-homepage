/* Keep lunr variables as global for easier debugging. */
var lunr_results, lunr_idx;

document.addEventListener("DOMContentLoaded", function() {
    enable_translate();

    if (localStorage.getItem("language") == "en")
    	translate();

    enable_contact_helper();
    enable_search();
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

function enable_contact_helper() {
	var helper = document.getElementById("contact-helper-select");
	var display = document.getElementById("contact-helper-display");
	if (helper == null)
		return;
	helper.onchange = function() {
		display.value = helper.value;
	}
	// Initialize the helper.
	display.value = helper.value;
}

function enable_search() {
	var search_results = document.getElementById("search-results");

	lunr_idx = lunr(function () {
  		this.ref('filename')
  		this.field('text')
  		this.field("title")

  	lunr_documents.forEach(function (doc) {
    	this.add(doc)
  	}, this);
})

	var input = document.getElementById("search-input");
	var go = document.getElementById("search-go-button");
	var search_results_list;
	go.onclick = function() {
		lunr_results = lunr_idx.search(input.value);
		search_results.innerHTML = "";

		if (lunr_results.length == 0)
			search_results.innerText = "Inga sidor matchade.";
		else {
			search_results_list = document.createElement("ul");
			search_results.appendChild(search_results_list);
		}

		for (var i = 0; i < lunr_results.length; i++) {
			var result = document.createElement("li");
			result.setAttribute("class", "search-result");
			var result_link = document.createElement("a");

			result_link.setAttribute("class", "search-result-link");
			result_link.innerText = lunr_documents_id_map[lunr_results[i].ref];
			result_link.setAttribute("href", lunr_results[i].ref);
			result.appendChild(result_link);

			search_results_list.appendChild(result);
		}
	}
}