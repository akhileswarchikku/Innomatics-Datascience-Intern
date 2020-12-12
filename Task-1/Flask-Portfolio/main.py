from flask import Flask,render_template
import os
t = os.getcwd() + '\\static'
t = t.split('\\')
t = '//'.join(t)
static_folder = t
print(static_folder)

app=Flask(__name__,static_folder=static_folder)

@app.route('/')
def View1():
    return render_template('SelectScreen.html')


if __name__=='__main__':
    app.run(debug=True,port=2020)