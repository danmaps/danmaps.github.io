from flask import render_template

@app.route('/posts')
def all_posts():
    posts = get_all_posts()  # Your function to get all posts
    return render_template('post.html', posts=posts) 