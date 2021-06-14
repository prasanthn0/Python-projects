from flask import Flask,render_template,request,url_for,redirect


app=Flask(__name__)

posts={
    0:{
        'id': 0,
        'title': 'Hello world !',
        'content': ' This is my first post'
    }
}

@app.route('/')
def main():
    return posts[0]['title']

@app.route('/post/<int:post_id>')
def post(post_id):
    post=posts.get(post_id)

    if not post:
        return render_template('404.html', message=f'Post with id {post_id} is not found')

    return render_template('post.jinja2',post=post)

@app.route('/post/form')
def form():
    return render_template('create.jinja2')

@app.route('/post/create',methods=['POST'])
def create():

    title=request.form.get('title')  # post is hidden payload that comes with requests instead of args
    content=request.form.get('content')  #if args is used, data entered is visible to others as query string parameters
    post_id=len(posts)
    posts[post_id]={'id':post_id, 'title': title, 'content':content}

    return redirect(url_for('post', post_id=post_id))

#get requests cannot have payloads but post requests can and one benefit is can send huge amount
#of data using post requests. COs there is limit ifor number of characters in url

if __name__ == '__main__':
    app.run(debug=True)

