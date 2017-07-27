import datetime
from os import path
from sqlalchemy import func
from flask import render_template, Blueprint, redirect

from webapp.models import db, Post, Tag, Comment, User, tags
from webapp.forms import CommentForm, PostForm


blog_blueprint = Blueprint('blog', __name__, template_folder=path.join(path.pardir, 'templates', 'blog'), url_prefix="/blog")


def sidebar_data():
    recent = Post.query.order_by(Post.publish_date.desc()).limit(5).all
    top_tags = db.session.query(Tag, func.count(tags.c.post_id).label('total')).join(tags).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags


@blog_blueprint.route('/new', methods=['POST', 'GET'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(form.title.data)
        new_post.text = form.text.data
        new_post.publish_date = datetime.datetime.now()

        db.session.add(new_post)
        db.session.commit()
    return render_template('new.html', form=form)


@blog_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post():
    post = Post.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.publish_date = datetime.datetime.now()

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('.post', post_id=post.id))
    
    form.text.data = post.text

    return render_template('edit.html', form=form, post=post)
    