from flask import Flask,render_template,request
import numpy as np
from errors.handlers import errors
from checker import SpellChecker

checker = SpellChecker("book.txt")
replacer = [",",".",'"',"?","!","@","1","2","3","4","5","6","7","8","9","0","$","%","/","*","+","-","_","&","|","(",")","[","]","{","}"]
def create_app():
    app = Flask(__name__)
    app.register_blueprint(errors)
    @app.route("/")
    def main():
        return render_template('home.html')

    @app.route("/",methods=['POST','GET'])
    def home():
        if request.method=='POST':
            mname = request.form.get('mname')
            if mname=='':
                words = ''
                return render_template('home.html',words=words)
            words = []
            for word in mname.split(' '):
                print(word)
                if word != '':
                    for i in replacer:
                        word = word.replace(i,"")
                    words.append((word,checker.check(word.lower())))
                print(words)
        return render_template('home.html',words=words)
    return app

# create_app()
# if __name__=="__main__":
#     app.run()
