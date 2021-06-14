from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

posts = {
    0: {
        'id': 0,
        'title': 'Hello world !',
        'content': ' This is my first post'
    }
}


@app.route('/')
def main():
    return render_template('home.jinja2' , posts=posts)

#ul is bullet point list
# a is anchor tag i.e. a link  and href is the url that a tag redirects to


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)

    if not post:
        return render_template('404.html', message=f'Post with id {post_id} is not found')

    return render_template('post.jinja2', post=post)





@app.route('/post/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')  # post is hidden payload that comes with requests instead of args
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))

    return render_template('create.jinja2')

#This can do both the task of creating a form page if its not POST request. So form method is not needed annymore.


if __name__ == '__main__':
    app.run(debug=True)

