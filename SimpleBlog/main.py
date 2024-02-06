from flask import Flask, render_template, url_for
from post import Post


app = Flask(__name__)

@app.route('/posts', strict_slashes=False)
@app.route('/posts/<int:blog_id>', strict_slashes=False)
def blog_posts(blog_id=None):
    posts = Post()
    data = posts.data
    if blog_id:
        blog = posts.get_blog(blog_id)
        return render_template("post.html", post=blog)
    return render_template("index.html", posts=data)

if __name__ == "__main__":
    app.run(debug=True)
