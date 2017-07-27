# @app.route('/')
# @app.route('/<int:page>')
# def home():
#     posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, 10)
#     recent, top_tags = sidebar_data()
#     return render_template('home.html', posts=posts, recent=recent, top_tags=top_tags)

# @app.route('/post/<int:post_id>')
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     tags = post.tags
#     comments = post.comments.order_by(Comment.date.desc()).all()
#     recent, top_tags = sidebar_data()

#     return render_template('post.html', post=post, tags=tags, comments=comments, recent=recent, top_tags=top_tags)

# @app.route('/tag/<string:tag_name>')
# def tag(tag_name):
#     tag = Tag.query.filter_by(title=tag_name).first_or_404()
#     posts = tag.posts.order_by(Post.publish_date.desc()).all()
#     recent, top_tags = sidebar_data()
#     return render_template('tag.html', tag=tag, posts=posts, recent=recent, top_tags=top_tags)

# @app.route('/user/<string:username>')
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = user.posts.order_by(Post.publish_date.desc()).all()
#     recent, top_tags = sidebar_data()
#     return render_template('user.html', user=user, posts=posts, recent=recent, top_tags=top_tags)



# @app.route('/post/<int:post_id>', methods=['GET', 'POST'])
# def post(post_id):
#     form = CommentForm()
#     if form.validate_on_submit():
#         new_comment = Comment()
#     new_comment.name = form.name.data
#     new_comment.text = form.text.data
#     new_comment.post_id = post_id
#     new_comment.date = datetime.datetime().now()
#     db.session.add(new_comment)
#     db.session.commit()
#     post = Post.query.get_or_404(post_id)
#     tags = post.tags
#     comments = post.comments.order_by(Comment.date.desc()).all()
#     recent, top_tags = sidebar_data()

#     return render_template('post.html', post=post, tags=tags, comments=comments, recent=recent, top_tags=top_tags, form=form)



