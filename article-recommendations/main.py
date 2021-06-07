from flask import Flask, jsonify, request

from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)


@app.route("/get-article")
def get_article():
  art = all_articles[0]
  return jsonify({
      "data": {
          "url": art[11],
          "title": art[12],
          "text": art[13],
          "lang": art[14],
          "total_events": art[15]
      },
      "status": "success"
  })


@app.route("/liked-article", methods=["POST"])
def liked_article():
  article = all_articles[0]
  liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({
      "status": "success"
  })


@app.route("/unliked-article", methods=["POST"])
def unliked_article():
  article = all_articles[0]
  not_liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({
      "status": "success"
  })


@app.route("/popular-articles")
def popular_articles():
  article_data = []
  for article in output:
    article_data.append({
        "url": article[0],
        "title": article[1],
        "text": article[2],
        "lang": article[3],
        "total_events": article[4]
    })
  return jsonify({
      "data": article_data,
      "status": "success"
  }), 200


@app.route("/recommended-articles")
def recommended_articles():
  all_recommended = []
  for liked_article in liked_articles:
    output = get_recommendations(liked_article[4])
    for data in output:
      all_recommended.append(data)
  all_recommended.sort()
  all_recommended = set(all_recommended)
  article_data = []
  for recommended in all_recommended:
    article_data.append({
        "url": recommended[0],
        "title": recommended[1],
        "text": recommended[2],
        "lang": recommended[3],
        "total_events": recommended[4]
    })
  return jsonify({
      "data": article_data,
      "status": "success"
  }), 200


if __name__ == "__main__":
  app.run()
