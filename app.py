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
        words = []
        if request.method=='POST':
            mname = request.form.get('mname')
            if mname=='':
                words = ''
                return render_template('home.html',words=words)  
    
            for word in mname.split(' '):
                all_sggestions = []
                print(word)
                if word != '':
                    for i in replacer:
                        word = word.replace(i,"")
                    all_sggestions = (checker.check(word.lower()))
                    print(all_sggestions)
                if "spelled" in all_sggestions:
                    words.append((word,all_sggestions))
                elif "not found" in all_sggestions:
                    words.append((word,all_sggestions))
                else:
                    words.append((word,all_sggestions[:5]))
        print(words)
        return render_template('home.html',words=words)
    return app

create_app()
# if __name__=="__main__":
#     app.run()
