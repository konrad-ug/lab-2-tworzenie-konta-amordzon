from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.findByPesel(dane["pesel"]) != None:
        return jsonify("Ten pesel juz istnieje"), 400
    konto = KontoOsobiste(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.addAccountToArray(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    ile = RejestrKont.accountLength()
    print("Ilość kont: "+str(ile))
    return jsonify(ile), 200


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.findByPesel(pesel)
    print(f"Request o szukanie konta z peselem: {pesel}")
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto_z_peselem(pesel):
    data = request.get_json()
    if "pesel" in data and RejestrKont.findByPesel(data["pesel"]) != None:
        return jsonify("Ten pesel juz istnieje"), 400
    konto = RejestrKont.accountUpdate(pesel, data)
    if(konto == None):
        return jsonify("Podany pesel nie istnieje!"), 200
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto_z_peselem(pesel):
    konto = RejestrKont.accountRemove(pesel)
    if(konto == None):
        return jsonify("Podany pesel nie istnieje!"), 200
    return jsonify("Delete zakonczony pomyslnie"), 200
