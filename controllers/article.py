from flask import render_template, request,redirect,url_for
from models.database import ArticleMapper

class Article():
    def __init__(self,session):
        self.session = session

    def index(self):
        _articles = self.session.query(ArticleMapper).all()
        return render_template('blog.index.html', articles=_articles)

    def show(self,_id):
        _article = self.session.query(ArticleMapper).filter_by(id=_id).one()
        return render_template('blog.show.html', article=_article)

    def create(self,method):
        if method=='POST':
            if 'titre' in request.form:
                article = ArticleMapper(title=request.form.get('titre'),description=request.form.get('description'))
                self.session.add(article)
                self.session.commit()
            return redirect(url_for('Index'),302)
        else:
            return render_template('blog.create.html')
            
    def edit(self,_id):
        _article = self.session.query(ArticleMapper).filter_by(id=_id).one()
        if _article:
            return render_template('blog.edit.html',article=_article)
        else:
            #flash bag article dont exists
            return redirect(url_for('Index'),302)
            
    def update(self,method):
        if method=='POST':
            if 'id' in request.form:
                if 'titre' in request.form:
                    article = self.session.query(ArticleMapper).filter_by(id=request.form.get('id')).one()
                    article.title = request.form.get('titre');
                    article.description = request.form.get('description');
                    article.status = request.form.get('status');
                    self.session.add(article)
                    self.session.commit()
                #Missing Title
                return redirect(url_for('Index'),302)
            else:
                #No valide article
                return redirect(url_for('Index'),302)
        else:
            #flash bag bad request
            return redirect(url_for('Index'),302)
