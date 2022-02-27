from flask import Flask, render_template, Response, request, session, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from core.removebg import rmbg
from core.background import bg, color
import os

application = Flask(__name__) # initializing a flask app

app=application
app.secret_key = 'paspoto'
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

warna = [x for x in color.warna.keys()]

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", warna=warna)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    
    
    try:
        if request.method == 'POST':
            c = request.form['warna']   
            f = request.files['file']
            
            # print (f.filename)
            
            filename = secure_filename(f.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(filepath)
            try:
                rmbg.predict(filepath)
                if c != 'Hanya Hapus Background':
                    bg.fillbg("static/results/output.png", c)            
                else:
                    pass
            except:
                flash('Telah terjadi kesalahan di Paspoto anda')
                return redirect(url_for('index'))

            return render_template("uploaded.html", warna=warna)

    except:
        flash('Mohon Uppload Paspoto terlebih dahulu')
        return redirect(url_for('index'))


@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run(debug=True)
