from flask import Flask, request
from flask.templating import render_template
from classes.disc import Disc
from flask_mail import Mail, Message

import random
import string
import constants.mail_body as mail_body
import constants.mail_server as mail_config
import functions.database as db_operations

app = Flask(__name__)

app.config['MAIL_SERVER'] = mail_config.SERVER
app.config['MAIL_PORT'] = mail_config.PORT
app.config['MAIL_USE_TLS'] = mail_config.USE_TLS
app.config['MAIL_USERNAME'] = mail_config.USERNAME
app.config['MAIL_PASSWORD'] = mail_config.PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = mail_config.DEFAULT_SENDER
mail = Mail(app)


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/discs-list")
def discs_list():
    lst = db_operations.get_validated_disks()

    return render_template("discs-list.html", var_list=lst)


@app.route("/add-disc")
def add_disc():
    return render_template("add-disc.html", action="new-disc")


@app.route("/confirm-delete")
def confirm_delete():
    id_disc = request.args.get("id")
    disc = db_operations.get_disc_by_id(id_disc)
    
    return render_template("/confirm-delete.html", id=id_disc, title=disc.title,
                           performer=disc.performer, musicStyle=disc.music_style,
                           tracks=disc.tracks, price=disc.price, email=disc.email)

@app.route("/delete-disc")
def delete_disc():
    disc_id = request.args.get("id")
    db_operations.delete_disc(disc_id)
    return render_template("/delete-ok.html")

@app.route("/edit-disc")
def edit_disc():
    id_disc = request.args.get("id")
    disc = db_operations.get_disc_by_id(id_disc)
    return "Se va a editar el disco " + disc.to_string()


@app.route("/new-disc")
def new_disc():
    disc = Disc()
    disc.title = request.args.get("title")
    disc.performer = request.args.get("performer")
    disc.music_style = request.args.get("musicStyle")
    disc.tracks = int(request.args.get("tracks"))
    disc.price = float(request.args.get("price"))
    disc.email = request.args.get("email")

    disc = db_operations.insert_disc(disc)

    validation_code = "".join(random.choices(
        string.ascii_letters + string.digits, k=100))
    db_operations.insert_validation_code(disc.id_disc, validation_code)

    msg = Message("Gracias por registrar tu anuncio", recipients=[disc.email])
    msg.html = (mail_body.MAIL_BODY).format(disc.id_disc, validation_code)
    mail.send(msg)

    return render_template("save-ok.html", var_disc=disc)


@app.route("/validate-disc")
def validate_disc():
    disc_id = int(request.args.get("id"))
    validation_code = request.args.get("code")

    valid = db_operations.check_validation_code(disc_id, validation_code)

    if valid:
        db_operations.validate_disc(disc_id)
        db_operations.delete_validation_code(disc_id)
        return render_template("validation-ok.html")
    else:
        return render_template("validation-nook.html")


app.run(debug=True)
