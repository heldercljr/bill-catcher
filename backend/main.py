import fitz
import re
from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import os.path

from pathlib import Path
from typing import List

from src.billtypes import DAES, DASN
from src.utils.util import pix_qrcode_decoder, email_catcher

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'



class PdfCatcher(Resource):
  	def get(self):
				email_catcher()
				DOCUMENT_TYPES = ("DASN", "DAES")			

				for filepath in Path("pdfs").glob("*.pdf"):
						if filepath.stem.upper().startswith(DOCUMENT_TYPES):
								DOC = globals()[filepath.stem[:4].upper()]
								filename = filepath.absolute()

								with fitz.open(filename) as bill:

										plain_text: str = bill[0].get_text()

										splitted_text: List[str] = plain_text.split("\n")
						
										splitted_text.append(pix_qrcode_decoder(bill))

										DOC(splitted_text).to_json()
				debits = []
				path = 'jsons'
				for filenames in os.walk(path):
					debits.append(filenames)
				data_list = []
				#print(len(filenames[2]))
				for i in range(len(filenames[2])):
					try:
						data = json.load(open('jsons/' + filenames[2][i], encoding='utf-8'))
						#print(filenames[2][i])
						data_final = dict((k, data[k]) for k in ('cpfcnpj', 'value', 'due_date', 'bar_code', 'pix_string', 'doc_type'))
						
						#print(data_final)

						data_list.append(data_final)
						#print(data_final)
					except Exception:
						pass
				out_file = open("C:/Users/matth/BillCrawler/bill-catcher/frontend/load-json-file/src/Data/debits.json", "w")
				json.dump(data_list, out_file, indent=2)
				out_file.close()
						

				return make_response(jsonify({"message":"Processamento realizado com sucesso!"}), 200) 

api.add_resource(PdfCatcher, '/') 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
