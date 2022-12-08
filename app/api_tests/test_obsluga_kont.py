import unittest
import requests

class TestObsługaKont(unittest.TestCase):
    body = {
        "imie": "james",
        "nazwisko":"hetfield",
        "pesel":"89092909825"
    }

    url="http://127.0.0.1:5000/"

    new_data={
        "imie": "James",
        "nazwisko": "hetfield"
    }

    def test_1_tworzenie_kont_poprawne(self):
        create_resp=requests.post(self.url+"/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 201)
    
    def test_2_get_po_peselu(self):
        get_resp=requests.get(self.url+f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body=get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)
    
    def test_3_update_po_peselu_ok(self):
        get_resp = requests.put(
            self.url+f"/konta/konto/{self.body['pesel']}", json=self.new_data)
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.new_data["nazwisko"])
        self.assertEqual(resp_body["imie"], self.new_data["imie"])
        self.assertEqual(resp_body["pesel"], self.body["pesel"])
        self.assertEqual(resp_body["saldo"], 0)
    
    def test_4_update_po_peselu_zle(self):
        get_resp = requests.put(
            self.url+f"/konta/konto/89092909821", json=self.new_data)
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body, "Podany pesel nie istnieje!")
    
    def test_5_delete_po_peselu(self):
        ile_kont = int(requests.get(self.url + f"/konta/ile_kont").json())
        get_resp = requests.delete(
            self.url+f"/konta/konto/{self.body['pesel']}", json=self.new_data)
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body, "Delete zakonczony pomyslnie")
        ile_kont_po = int(requests.get(self.url + f"/konta/ile_kont").json())
        self.assertEqual(ile_kont, ile_kont_po+1)
    
    def test_6_delete_po_peselu_zle(self):
        ile_kont = int(requests.get(self.url + f"/konta/ile_kont").json())
        get_resp = requests.delete(
            self.url+f"/konta/konto/89092909821", json=self.new_data)
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body, "Podany pesel nie istnieje!")
        ile_kont_po = int(requests.get(self.url + f"/konta/ile_kont").json())
        self.assertEqual(ile_kont, ile_kont_po)
