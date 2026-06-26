document.getElementById("searchForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const query = document.getElementById("searchInput").value;

    fetch(`/api/images/search?q=${query}`)
        .then(res => res.json())
        .then(data => {
            const results = document.getElementById("results");
            results.innerHTML = "";

            data.images.forEach(img => {
                const image = document.createElement("img");
                image.src = img.url;
                results.appendChild(image);
            });
        });
});