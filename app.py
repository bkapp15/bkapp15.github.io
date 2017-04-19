
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/ModelPages/songs")
def songs():
    return render_template('ModelPages/songs.html')

@app.route("/ModelPages/songs_2")
def songs_2():
    return render_template('ModelPages/songs_2.html')

@app.route("/ModelPages/songs_3")
def songs_3():
    return render_template('ModelPages/songs_3.html')

@app.route("/ModelPages/labels")
def labels():
    return render_template('ModelPages/labels.html')

@app.route("/ModelPages/labels_2")
def labels_2():
    return render_template('ModelPages/labels_2.html')

@app.route("/ModelPages/labels_3")
def labels_3():
    return render_template('ModelPages/labels_3.html')

@app.route("/ModelPages/artists")
def artists():
    return render_template('ModelPages/artists.html')

@app.route("/ModelPages/artists_2")
def artists_2():
    return render_template('ModelPages/artists_2.html')

@app.route("/ArtistPages/beyonce.html")
def beyonce():
    return render_template('ArtistPages/beyonce.html')

@app.route("/ArtistPages/twentyonepilots.html")
def twentyonepilots():
    return render_template('ArtistPages/21pilots.html')

@app.route("/ArtistPages/rihanna.html")
def rihanna():
    return render_template('ArtistPages/rihanna.html')

@app.route("/ArtistPages/thechainsmokers.html")
def thechainsmokers():
    return render_template('ArtistPages/thechainsmokers.html')

@app.route("/ArtistPages/edsheeran.html")
def edsheeran():
    return render_template('ArtistPages/edsheeran.html')

@app.route("/ArtistPages/brunomars.html")
def brunomars():
    return render_template('ArtistPages/brunomars.html')

@app.route("/ArtistPages/arianagrande.html")
def arianagrande():
    return render_template('ArtistPages/arianagrande.html')

@app.route("/ArtistPages/sia.html")
def sia():
    return render_template('ArtistPages/sia.html')

@app.route("/ArtistPages/adele.html")
def adele():
    return render_template('ArtistPages/adele.html')

@app.route("/ArtistPages/fifthharmony.html")
def fifthharmony():
    return render_template('ArtistPages/fifthharmony.html')

@app.route("/ArtistPages/hozier.html")
def hozier():
    return render_template('ArtistPages/hozier.html')

@app.route("/ArtistPages/taylorswift.html")
def taylorswift():
    return render_template('ArtistPages/taylorswift.html')

@app.route("/SongPages/sorry_beyonce.html")
def sorry_beyonce():
    return render_template('SongPages/sorry_beyonce.html')

@app.route("/SongPages/StressedOut_21Pilots.html")
def StressedOut_21Pilots():
    return render_template('SongPages/StressedOut_21Pilots.html')

@app.route("/SongPages/work_rihanna.html")
def work_rihanna():
    return render_template('SongPages/work_rihanna.html')

@app.route("/SongPages/closer_chainsmokers.html")
def closer_chainsmokers():
    return render_template('SongPages/closer_chainsmokers.html')

@app.route("/SongPages/shapeofyou_edsheeran.html")
def shapeofyou_edsheeran():
    return render_template('SongPages/shapeofyou_edsheeran.html')

@app.route("/SongPages/24kmagic_brunomars.html")
def magic_brunomars():
    return render_template('SongPages/24kmagic_brunomars.html')

@app.route("/SongPages/sidetoside_arianagrande.html")
def sidetoside_arianagrande():
    return render_template('SongPages/sidetoside_arianagrande.html')

@app.route("/SongPages/cheapthrills_sia.html")
def cheapthrills_sia():
    return render_template('SongPages/cheapthrills_sia.html')

@app.route("/SongPages/heathens_21pilots.html")
def heathens_21pilots():
    return render_template('SongPages/heathens_21pilots.html')

@app.route("/SongPages/hello_adele.html")
def hello_adele():
    return render_template('SongPages/hello_adele.html')

@app.route("/SongPages/workfromhome_fifthharmony.html")
def workfromhome_fifthharmony():
    return render_template('SongPages/workfromhome_fifthharmony.html')

@app.route("/SongPages/stay_rihanna.html")
def stay_rihanna():
    return render_template('SongPages/stay_rihanna.html')

@app.route("/SongPages/takemetochurch_hozier.html")
def takemetochurch_hozier():
    return render_template('SongPages/takemetochurch_hozier.html')

@app.route("/SongPages/badblood_taylorswift.html")
def badblood_taylorswift():
    return render_template('SongPages/badblood_taylorswift.html')

@app.route("/SongPages/xo_beyonce.html")
def xo_beyonce():
    return render_template('SongPages/xo_beyonce.html')

@app.route("/LabelPages/columbia.html")
def columbia():
    return render_template('LabelPages/columbia.html')

@app.route("/LabelPages/ramen.html")
def ramen():
    return render_template('LabelPages/ramen.html')

@app.route("/LabelPages/roc_nation.html")
def roc_nation():
    return render_template('LabelPages/roc_nation.html')

@app.route("/LabelPages/atlantic.html")
def atlantic():
    return render_template('LabelPages/atlantic.html')

@app.route("/LabelPages/republic.html")
def republic():
    return render_template('LabelPages/republic.html')

@app.route("/LabelPages/rca.html")
def rca():
    return render_template('LabelPages/rca.html')

@app.route("/LabelPages/warner_bros.html")
def warner_bros():
    return render_template('LabelPages/warner_bros.html')

@app.route("/LabelPages/xl.html")
def xl():
    return render_template('LabelPages/xl.html')

@app.route("/LabelPages/epic.html")
def epic():
    return render_template('LabelPages/epic.html')

@app.route("/LabelPages/def_jam.html")
def def_jam():
    return render_template('LabelPages/def_jam.html')

@app.route("/LabelPages/island.html")
def island():
    return render_template('LabelPages/island.html')

@app.route("/LabelPages/bigmachine.html")
def bigmachine():
    return render_template('LabelPages/bigmachine.html')

if __name__ == "__main__":
    app.run('104.131.67.71','80')
