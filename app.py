from flask import Flask, render_template, request
from routes.image_routes import image_bp

app = Flask(__name__)

# ✅ API routes (upload, Azure plus tard)
app.register_blueprint(image_bp, url_prefix="/api/images")


# ✅ PAGE ACCUEIL
@app.route("/")
def home():
    return render_template("index.html")


# ✅ PAGE RECHERCHE
@app.route("/search")
def search_page():
    # ✅ récupérer la recherche texte
    query = request.args.get("q", "").lower()
    keywords = query.split()

    # ✅ récupérer les filtres
    human_filter = request.args.get("human")
    environment_filter = request.args.get("environment")

    # ✅ FAKE DATABASE
    all_images = [
        {
            "url": "https://picsum.photos/300?random=1",
            "tags": ["canard", "food", "dish"],
            "product": "volaille",
            "human": False,
            "environment": "cuisine"
        },
        {
            "url": "https://picsum.photos/300?random=2",
            "tags": ["chef", "cooking", "human"],
            "product": "cuisine",
            "human": True,
            "environment": "cuisine"
        },
        {
            "url": "https://picsum.photos/300?random=3",
            "tags": ["viande", "grill"],
            "product": "viande",
            "human": False,
            "environment": "extérieur"
        },
        {
            "url": "https://picsum.photos/300?random=4",
            "tags": ["dessert", "gâteau", "sucré"],
            "product": "dessert",
            "human": False,
            "environment": "cuisine"
        }
    ]

    # ✅ FILTRAGE INTELLIGENT + FILTRES AVANCES
    results = []

    for img in all_images:
        matched = 0

        # 🔎 multi-keywords
        for word in keywords:
            if (
                word in img["tags"]
                or word in img["product"]
                or word in img["environment"]
                or (word == "human" and img["human"])
            ):
                matched += 1

        # ✅ condition : tous les mots doivent matcher
        if keywords and matched != len(keywords):
            continue

        # ✅ filtre humain
        if human_filter == "yes" and not img["human"]:
            continue

        if human_filter == "no" and img["human"]:
            continue

        # ✅ filtre environnement
        if environment_filter:
            if environment_filter.lower() not in img["environment"]:
                continue

        results.append(img)

    return render_template(
        "results.html",
        images=results,
        query=query
    )


# ✅ RUN
if __name__ == "__main__":
    app.run(debug=True)