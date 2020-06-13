"""B3 module."""
import collections
import datetime
import sys
from typing import List


RatePeriod = collections.namedtuple("RatePeriod", ["start_date", "end_date", "rate"])

EMOLUMENTOS_PERIODS = [
    RatePeriod(
        datetime.datetime(2019, 1, 3), datetime.datetime(2019, 2, 1), 0.00004476
    ),
    RatePeriod(
        datetime.datetime(2019, 2, 4), datetime.datetime(2019, 3, 1), 0.00004032
    ),
    RatePeriod(
        datetime.datetime(2019, 3, 6), datetime.datetime(2019, 4, 1), 0.00004157
    ),
    RatePeriod(datetime.datetime(2019, 4, 2), datetime.datetime(2019, 5, 2), 0.0000408),
    RatePeriod(
        datetime.datetime(2019, 5, 3), datetime.datetime(2019, 6, 3), 0.00004408
    ),
    RatePeriod(
        datetime.datetime(2019, 6, 4), datetime.datetime(2019, 7, 1), 0.00004245
    ),
    RatePeriod(
        datetime.datetime(2019, 7, 2), datetime.datetime(2019, 8, 1), 0.00004189
    ),
    RatePeriod(
        datetime.datetime(2019, 8, 2), datetime.datetime(2019, 9, 2), 0.00004115
    ),
    RatePeriod(
        datetime.datetime(2019, 9, 3), datetime.datetime(2019, 10, 1), 0.00003756
    ),
    RatePeriod(
        datetime.datetime(2019, 10, 2), datetime.datetime(2019, 11, 1), 0.00004105
    ),
    RatePeriod(
        datetime.datetime(2019, 11, 4), datetime.datetime(2019, 12, 2), 0.0000411
    ),
    RatePeriod(
        datetime.datetime(2019, 12, 3), datetime.datetime(2020, 1, 2), 0.00003802
    ),
]
EMOLUMENTOS_AUCTION_RATE = 0.00007
LIQUIDACAO_RATE = 0.000275

STOCKS = {
    "AALR3": {"empresa": "CENTRO DE IMAGEM DIAGNOSTICOS", "cnpj": "42.771.949/0001-35"},
    "ABCB4": {"empresa": "BANCO ABC BRASIL", "cnpj": "28.195.667/0001-06"},
    "ABEV3": {"empresa": "AMBEV", "cnpj": "07.526.557/0001-00"},
    "ADHM3": {
        "empresa": "ADVANCED DIGITAL HEALTH MEDICINA PREVENTIVA",
        "cnpj": "10.345.009/0001-98",
    },
    "AGRO3": {"empresa": "BRASILAGRO", "cnpj": "07.628.528/0001-59"},
    "ALPA3": {"empresa": "ALPARGATAS", "cnpj": "61.079.117/0001-05"},
    "ALPA4": {"empresa": "ALPARGATAS", "cnpj": "61.079.117/0001-05"},
    "ALSC3": {"empresa": "ALIANSCE SHOPPING CENTERS", "cnpj": "06.082.980/0001-03"},
    "ALUP11": {"empresa": "ALUPAR INVESTIMENTO", "cnpj": "08.364.948/0001-38"},
    "ALUP3": {"empresa": "ALUPAR INVESTIMENTO", "cnpj": "08.364.948/0001-38"},
    "ALUP4": {"empresa": "ALUPAR INVESTIMENTO", "cnpj": "08.364.948/0001-38"},
    "AMAR3": {"empresa": "LOJAS MARISA", "cnpj": "61.189.288/0001-89"},
    "ANIM3": {"empresa": "ANIMA HOLDING", "cnpj": "09.288.252/0001-32"},
    "ARZZ3": {"empresa": "AREZZO INDÚSTRIA E COMÉRCIO", "cnpj": "16.590.234/0001-76"},
    "ATOM3": {"empresa": "ATOM", "cnpj": "00.359.742/0001-08"},
    "AZUL4": {"empresa": "AZUL", "cnpj": "09.305.994/0001-29"},
    "B3SA3": {"empresa": "B3 – BRASIL – BOLSA – BALCÃO", "cnpj": "09.346.601/0001-25"},
    "BAUH3": {"empresa": "EXCELSIOR ALIMENTOS", "cnpj": "95.426.862/0001-97"},
    "BAUH4": {"empresa": "EXCELSIOR ALIMENTOS", "cnpj": "95.426.862/0001-97"},
    "BBAS3": {"empresa": "BANCO DO BRASIL", "cnpj": "00.000.000/0001-91"},
    "BBDC3": {"empresa": "BANCO BRADESCO", "cnpj": "60.746.948/0001-12"},
    "BBDC4": {"empresa": "BANCO BRADESCO", "cnpj": "60.746.948/0001-12"},
    "BBRK3": {"empresa": "BRASIL BROKERS", "cnpj": "08.613.550/0001-98"},
    "BBSE3": {"empresa": "BB SEGURIDADE", "cnpj": "17.344.597/0001-94"},
    "BEEF3": {"empresa": "MINERVA", "cnpj": "67.620.377/0001-14"},
    "BIDI4": {"empresa": "BANCO INTER", "cnpj": "18.945.670/0001-46"},
    "BIDI11": {"empresa": "BANCO INTER", "cnpj": "18.945.670/0001-46"},
    "BOBR3": {"empresa": "BOMBRIL", "cnpj": "50.564.053/0001-03"},
    "BOBR4": {"empresa": "BOMBRIL", "cnpj": "50.564.053/0001-03"},
    "BPAC11": {"empresa": "BANCO BTG PACTUAL", "cnpj": "30.306.294/0001-45"},
    "BPAC3": {"empresa": "BANCO BTG PACTUAL", "cnpj": "30.306.294/0001-45"},
    "BPAC5": {"empresa": "BANCO BTG PACTUAL", "cnpj": "30.306.294/0001-45"},
    "BPAN4": {"empresa": "BANCO PAN", "cnpj": "59.285.411/0001-13"},
    "BPHA3": {"empresa": "BRASIL PHARMA", "cnpj": "11.395.624/0001-71"},
    "BRAP3": {"empresa": "BRADESPAR", "cnpj": "03.847.461/0001-92"},
    "BRAP4": {"empresa": "BRADESPAR", "cnpj": "03.847.461/0001-92"},
    "BRDT3": {"empresa": "PETROBRAS DISTRIBUIDORA", "cnpj": "34.274.233/0001-02"},
    "BRFS3": {"empresa": "BRF", "cnpj": "01.838.723/0001-27"},
    "BRIN3": {
        "empresa": "BR INSURANCE CORRETORA DE SEGUROS",
        "cnpj": "11.721.921/0001-60",
    },
    "BRKM3": {"empresa": "BRASKEM", "cnpj": "42.150.391/0001-70"},
    "BRKM5": {"empresa": "BRASKEM", "cnpj": "42.150.391/0001-70"},
    "BRKM6": {"empresa": "BRASKEM", "cnpj": "42.150.391/0001-70"},
    "BRML3": {"empresa": "BR MALLS PARTICIPACOES", "cnpj": "06.977.745/0001-91"},
    "BRPR3": {"empresa": "BR PROPERTIES", "cnpj": "06.977.751/0001-49"},
    "BMGB4": {"empresa": "BANCO BMG", "cnpj": "61.186.680/0001-74"},
    "BRSR3": {"empresa": "BANRISUL", "cnpj": "92.702.067/0001-96"},
    "BRSR5": {"empresa": "BANRISUL", "cnpj": "92.702.067/0001-96"},
    "BRSR6 ": {"empresa": "BANRISUL", "cnpj": "92.702.067/0001-96"},
    "BSEV3": {"empresa": "BIOSEV", "cnpj": "15.527.906/0001-36"},
    "BTOW3": {"empresa": "B2W – COMPANHIA DIGITAL", "cnpj": "00.776.574/0001-56"},
    "CAML3": {"empresa": "CAMIL ALIMENTOS", "cnpj": "64.904.295/0001-03"},
    "CARD3": {"empresa": "CSU CARDSYSTEM", "cnpj": "01.896.779/0001-38"},
    "CCRO3": {"empresa": "CCR", "cnpj": "02.846.056/0001-97"},
    "CCXC3": {"empresa": "CCX CARVÃO DA COLÔMBIA", "cnpj": "07.950.674/0001-04"},
    "CEPE3": {
        "empresa": "CIA ENERGETICA DE PERNAMBUCO – CELPE",
        "cnpj": "10.835.932/0001-08",
    },
    "CEPE5": {
        "empresa": "CIA ENERGETICA DE PERNAMBUCO – CELPE",
        "cnpj": "10.835.932/0001-08",
    },
    "CEPE6": {
        "empresa": "CIA ENERGETICA DE PERNAMBUCO – CELPE",
        "cnpj": "10.835.932/0001-08",
    },
    "CESP3": {
        "empresa": "CIA ENERGETICA DE SAO PAULO – CESP",
        "cnpj": "60.933.603/0001-78",
    },
    "CESP5": {
        "empresa": "CIA ENERGETICA DE SAO PAULO – CESP",
        "cnpj": "60.933.603/0001-78",
    },
    "CESP6": {
        "empresa": "CIA ENERGETICA DE SAO PAULO – CESP",
        "cnpj": "60.933.603/0001-78",
    },
    "CGAS3": {"empresa": "CIA GAS DE SAO PAULO – COMGAS", "cnpj": "61.856.571/0001-17"},
    "CGAS5": {"empresa": "CIA GAS DE SAO PAULO – COMGAS", "cnpj": "61.856.571/0001-17"},
    "CGRA3": {"empresa": "GRAZZIOTIN", "cnpj": "92.012.467/0001-70"},
    "CGRA4": {"empresa": "GRAZZIOTIN", "cnpj": "92.012.467/0001-70"},
    "CIEL3": {"empresa": "CIELO", "cnpj": "01.027.058/0001-91"},
    "CMIG3": {
        "empresa": "CIA ENERGETICA DE MINAS GERAIS – CEMIG",
        "cnpj": "17.155.730/0001-64",
    },
    "CMIG4": {
        "empresa": "CIA ENERGETICA DE MINAS GERAIS – CEMIG",
        "cnpj": "17.155.730/0001-64",
    },
    "CNTO3": {"empresa": "CENTAURO", "cnpj": "13.217.485/0001-11"},
    "COCE3": {
        "empresa": "CIA ENERGETICA DO CEARA – COELCE",
        "cnpj": "07.047.251/0001-70",
    },
    "COCE5": {
        "empresa": "CIA ENERGETICA DO CEARA – COELCE",
        "cnpj": "07.047.251/0001-70",
    },
    "COCE6": {
        "empresa": "CIA ENERGETICA DO CEARA – COELCE",
        "cnpj": "07.047.251/0001-70",
    },
    "CPFE3": {"empresa": "CPFL ENERGIA", "cnpj": "02.429.144/0001-93"},
    "CREM3": {"empresa": "CREMER", "cnpj": "82.641.325/0001-18"},
    "CRFB3": {"empresa": "ATACADÃO", "cnpj": "75.315.333/0001-09"},
    "CSAN3": {"empresa": "COSAN", "cnpj": "50.746.577/0001-15"},
    "CSMG3": {
        "empresa": "CIA SANEAMENTO DE MINAS GERAIS – COPASA",
        "cnpj": "17.281.106/0001-03",
    },
    "CSNA3": {"empresa": "CIA SIDERURGICA NACIONAL", "cnpj": "33.042.730/0001-04"},
    "CEAB3": {"empresa": "C&A MODAS", "cnpj": "45.242.914/0001-05"},
    "CTKA3": {"empresa": "KARSTEN", "cnpj": "82.640.558/0001-04"},
    "CTKA4": {"empresa": "KARSTEN", "cnpj": "82.640.558/0001-04"},
    "CTNM3": {
        "empresa": "CIA TECIDOS NORTE DE MINAS COTEMINAS",
        "cnpj": "22.677.520/0001-76",
    },
    "CTNM4": {
        "empresa": "CIA TECIDOS NORTE DE MINAS COTEMINAS",
        "cnpj": "22.677.520/0001-76",
    },
    "CVCB3": {
        "empresa": "CVC BRASIL OPERADORA E AGÊNCIA DE VIAGENS",
        "cnpj": "10.760.260/0001-19",
    },
    "CYRE3": {
        "empresa": "CYRELA BRAZIL REALTYEMPREEND E PART",
        "cnpj": "73.178.600/0001-18",
    },
    "DAGB33": {"empresa": "DUFRY A.G.", "cnpj": "11.423.623/0001-93"},
    "DIRR3": {"empresa": "DIRECIONAL ENGENHARIA", "cnpj": "16.614.075/0001-00"},
    "DMMO3": {"empresa": "DOMMO", "cnpj": "08.926.302/0001-05"},
    "DTEX3": {"empresa": "DURATEX", "cnpj": "97.837.181/0001-47"},
    "ECOR3": {
        "empresa": "ECORODOVIAS INFRAESTRUTURA E LOGÍSTICA",
        "cnpj": "04.149.454/0001-80",
    },
    "EGIE3": {"empresa": "ENGIE BRASIL ENERGIA", "cnpj": "02.474.103/0001-19"},
    "ELEK3": {"empresa": "ELEKEIROZ", "cnpj": "13.788.120/0001-47"},
    "ELEK4": {"empresa": "ELEKEIROZ", "cnpj": "13.788.120/0001-47"},
    "ELPL3": {"empresa": "ELETROPAULO", "cnpj": "61.695.227/0001-93"},
    "ELET3": {"empresa": "ELETROBRAS", "cnpj": "00.001.180/0001-26"},
    "ELET6": {"empresa": "ELETROBRAS", "cnpj": "00.001.180/0001-26"},
    "EMBR3": {"empresa": "EMBRAER", "cnpj": "07.689.002/0001-89"},
    "ENBR3": {"empresa": "EDP – ENERGIAS DO BRASIL", "cnpj": "03.983.431/0001-03"},
    "ENEV3": {"empresa": "ENEVA", "cnpj": "04.423.567/0001-21"},
    "ENGI11": {"empresa": "ENERGISA", "cnpj": "00.864.214/0001-06"},
    "ENGI3": {"empresa": "ENERGISA", "cnpj": "00.864.214/0001-06"},
    "ENGI4": {"empresa": "ENERGISA", "cnpj": "00.864.214/0001-06"},
    "EQTL3": {"empresa": "EQUATORIAL ENERGIA", "cnpj": "03.220.438/0001-73"},
    "YDUQ3": {"empresa": "YDUQS", "cnpj": "08.807.432/0001-10"},
    "ESTR3": {
        "empresa": "MANUFATURA DE BRINQUEDOS ESTRELA",
        "cnpj": "61.082.004/0001-50",
    },
    "ESTR4": {
        "empresa": "MANUFATURA DE BRINQUEDOS ESTRELA",
        "cnpj": "61.082.004/0001-50",
    },
    "ETER3": {"empresa": "ETERNIT", "cnpj": "61.092.037/0001-81"},
    "EUCA3": {"empresa": "EUCATEX", "cnpj": "56.643.018/0001-66"},
    "EUCA4": {"empresa": "EUCATEX", "cnpj": "56.643.018/0001-66"},
    "EVEN3": {
        "empresa": "EVEN CONSTRUTORA E INCORPORADORA",
        "cnpj": "43.470.988/0001-65",
    },
    "EZTC3": {"empresa": "EZ TEC", "cnpj": "08.312.229/0001-73"},
    "FESA3": {
        "empresa": "CIA FERRO LIGAS DA BAHIA – FERBASA",
        "cnpj": "15.141.799/0001-03",
    },
    "FESA4": {
        "empresa": "CIA FERRO LIGAS DA BAHIA – FERBASA",
        "cnpj": "15.141.799/0001-03",
    },
    "FHER3": {"empresa": "FERTILIZANTES HERINGER", "cnpj": "22.266.175/0001-88"},
    "TASA3": {"empresa": "TAURUS ARMAS", "cnpj": "92.781.335/0001-02"},
    "TASA4": {"empresa": "TAURUS ARMAS", "cnpj": "92.781.335/0001-02"},
    "FJTA3": {"empresa": "TAURUS ARMAS", "cnpj": "92.781.335/0001-02"},
    "FJTA4": {"empresa": "TAURUS ARMAS", "cnpj": "92.781.335/0001-02"},
    "FLRY3": {"empresa": "FLEURY", "cnpj": "60.840.055/0001-31"},
    "FRAS3": {"empresa": "FRAS-LE", "cnpj": "88.610.126/0001-29"},
    "GNDI3": {"empresa": "NOTRE DAME INTERMÉDICA", "cnpj": "19.853.511/0001-84"},
    "HAPV3": {"empresa": "HAPVIDA", "cnpj": "63.554.067/0001-98"},
    "FRIO3": {"empresa": "METALFRIO SOLUTIONS", "cnpj": "04.821.041/0001-08"},
    "GEPA3": {"empresa": "RIO PARANAPANEMA ENERGIA", "cnpj": "02.998.301/0001-81"},
    "GEPA4": {"empresa": "RIO PARANAPANEMA ENERGIA", "cnpj": "02.998.301/0001-81"},
    "GFSA3": {"empresa": "GAFISA", "cnpj": "01.545.826/0001-07"},
    "GGBR3": {"empresa": "GERDAU", "cnpj": "33.611.500/0001-19"},
    "GGBR4": {"empresa": "GERDAU", "cnpj": "33.611.500/0001-19"},
    "GOAU3": {"empresa": "METALURGICA GERDAU", "cnpj": "92.690.783/0001-09"},
    "GOAU4": {"empresa": "METALURGICA GERDAU", "cnpj": "92.690.783/0001-09"},
    "GOLL4": {
        "empresa": "GOL LINHAS AEREAS INTELIGENTES",
        "cnpj": "06.164.253/0001-87",
    },
    "GRND3": {"empresa": "GRENDENE", "cnpj": "89.850.341/0001-60"},
    "GSHP3": {"empresa": "GENERAL SHOPPING BRASIL", "cnpj": "08.764.621/0001-53"},
    "GUAR3": {"empresa": "GUARARAPES CONFECCOES", "cnpj": "08.402.943/0001-52"},
    "GUAR4": {"empresa": "GUARARAPES CONFECCOES", "cnpj": "08.402.943/0001-52"},
    "HBOR3": {"empresa": "HELBOR EMPREENDIMENTOS", "cnpj": "49.263.189/0001-02"},
    "HGTX3": {"empresa": "HERING", "cnpj": "78.876.950/0001-71"},
    "HYPE3": {"empresa": "HYPERMARCAS", "cnpj": "02.932.074/0001-91"},
    "HOOT3": {"empresa": "HOTEIS OTHON", "cnpj": "33.200.049/0001-47"},
    "HOOT4": {"empresa": "HOTEIS OTHON", "cnpj": "33.200.049/0001-47"},
    "IDNT3": {"empresa": "IDEIASNET", "cnpj": "02.365.069/0001-44"},
    "IGTA3": {
        "empresa": "IGUATEMI EMPRESA DE SHOPPING CENTERS",
        "cnpj": "51.218.147/0001-93",
    },
    "IRBR3": {"empresa": "IRB – BRASIL RESSEGUROS", "cnpj": "33.376.989/0001-91"},
    "ITSA3": {"empresa": "ITAUSA INVESTIMENTOS", "cnpj": "61.532.644/0001-15"},
    "ITSA4": {"empresa": "ITAUSA INVESTIMENTOS", "cnpj": "61.532.644/0001-15"},
    "ITUB3": {"empresa": "ITAU UNIBANCO HOLDING", "cnpj": "60.872.504/0001-23"},
    "ITUB4": {"empresa": "ITAU UNIBANCO HOLDING", "cnpj": "60.872.504/0001-23"},
    "JBSS3": {"empresa": "JBS", "cnpj": "02.916.265/0001-60"},
    "JHSF3": {"empresa": "JHSF PARTICIPACOES", "cnpj": "08.294.224/0001-65"},
    "JSLG3": {"empresa": "JSL", "cnpj": "52.548.435/0001-79"},
    "KEPL3": {"empresa": "KEPLER WEBER", "cnpj": "91.983.056/0001-69"},
    "KLBN11": {"empresa": "KLABIN", "cnpj": "89.637.490/0001-45"},
    "KLBN3": {"empresa": "KLABIN", "cnpj": "89.637.490/0001-45"},
    "KLBN4": {"empresa": "KLABIN", "cnpj": "89.637.490/0001-45"},
    "COGN3": {"empresa": "KROTON EDUCACIONAL S.A.", "cnpj": "02.800.026/0001-40"},
    "KROT3": {"empresa": "KROTON EDUCACIONAL S.A.", "cnpj": "02.800.026/0001-40"},
    "LAME3": {"empresa": "LOJAS AMERICANAS", "cnpj": "33.014.556/0001-96"},
    "LAME4": {"empresa": "LOJAS AMERICANAS", "cnpj": "33.014.556/0001-96"},
    "LCAM3": {"empresa": "CIA LOCAÇÃO DAS AMÉRICAS", "cnpj": "10.215.988/0001-60"},
    "LEVE3": {"empresa": "MAHLE-METAL LEVE", "cnpj": "60.476.884/0001-87"},
    "LIGT3": {"empresa": "LIGHT", "cnpj": "03.378.521/0001-75"},
    "LINX3": {"empresa": "LINX", "cnpj": "06.948.969/0001-75"},
    "LLIS3": {
        "empresa": "RESTOQUE COMÉRCIO E CONFECÇÕES DE ROUPAS",
        "cnpj": "49.669.856/0001-43",
    },
    "LIQO3": {"empresa": "LIQ PARTICIPAÇÕES", "cnpj": "04.032.433/0001-80"},
    "LOGG3": {"empresa": "LOG COMMERCIAL PROPERTIES", "cnpj": "09.041.168/0001-10"},
    "LOGN3": {"empresa": "LOG-IN LOGISTICA INTERMODAL", "cnpj": "42.278.291/0001-24"},
    "LPSB3": {
        "empresa": "LPS BRASIL – CONSULTORIA DE IMOVEIS",
        "cnpj": "08.078.847/0001-09",
    },
    "LREN3": {"empresa": "LOJAS RENNER", "cnpj": "92.754.738/0001-62"},
    "LUPA3": {"empresa": "LUPATECH", "cnpj": "89.463.822/0001-12"},
    "MAGG3": {"empresa": "MAGNESITA REFRATARIOS", "cnpj": "08.684.547/0001-65"},
    "MDIA3": {
        "empresa": "M.DIAS BRANCO IND COM DE ALIMENTOS",
        "cnpj": "07.206.816/0001-15",
    },
    "MGLU3": {"empresa": "MAGAZINE LUIZA", "cnpj": "47.960.950/0001-21"},
    "MILS3": {
        "empresa": "MILLS ESTRUTURAS E SERVIÇOS DE ENGENHARIA",
        "cnpj": "27.093.558/0001-15",
    },
    "MMXM3": {"empresa": "MMX MINERACAO E METALICOS", "cnpj": "02.762.115/0001-49"},
    "MNDL3": {"empresa": "MUNDIAL – PRODUTOS DE CONSUMO", "cnpj": "88.610.191/0001-54"},
    "MOVI3": {"empresa": "MOVIDA", "cnpj": "21.314.559/0001-66"},
    "MPLU3": {"empresa": "MULTIPLUS", "cnpj": "11.094.546/0001-75"},
    "MRFG3": {"empresa": "MARFRIG GLOBAL FOODS", "cnpj": "03.853.896/0001-40"},
    "MRVE3": {"empresa": "MRV ENGENHARIA", "cnpj": "08.343.492/0001-20"},
    "MULT3": {"empresa": "MULTIPLAN", "cnpj": "07.816.890/0001-53"},
    "MYPK3": {"empresa": "IOCHPE MAXION", "cnpj": "61.156.113/0001-75"},
    "NAFG3": {"empresa": "NADIR FIGUEIREDO", "cnpj": "61.067.161/0001-97"},
    "NAFG4": {"empresa": "NADIR FIGUEIREDO", "cnpj": "61.067.161/0001-97"},
    "NATU3": {"empresa": "NATURA COSMETICOS", "cnpj": "71.673.990/0001-77"},
    "ODPV3": {"empresa": "ODONTOPREV", "cnpj": "58.119.199/0001-51"},
    "OFSA3": {"empresa": "OURO FINO SAUDE ANIMAL", "cnpj": "20.258.278/0001-70"},
    "OIBR3": {"empresa": "OI", "cnpj": "76.535.764/0001-43"},
    "OIBR4": {"empresa": "OI", "cnpj": "76.535.764/0001-43"},
    "OSXB3": {"empresa": "OSX BRASIL", "cnpj": "09.112.685/0001-32"},
    "PARD3": {"empresa": "INSTITUTO HERMES PARDINI", "cnpj": "19.378.769/0001-76"},
    "PCAR3": {
        "empresa": "CIA BRASILEIRA DE DISTRIBUICAO",
        "cnpj": "47.508.411/0001-56",
    },
    "PCAR4": {
        "empresa": "CIA BRASILEIRA DE DISTRIBUICAO",
        "cnpj": "47.508.411/0001-56",
    },
    "PDGR3": {"empresa": "PDG REALTY", "cnpj": "02.950.811/0001-89"},
    "PETR3": {"empresa": "PETROLEO BRASILEIRO PETROBRAS", "cnpj": "33.000.167/0001-01"},
    "PETR4": {"empresa": "PETROLEO BRASILEIRO PETROBRAS", "cnpj": "33.000.167/0001-01"},
    "PFRM3": {
        "empresa": "PROFARMA DISTRIB PROD FARMACEUTICOS",
        "cnpj": "45.453.214/0001-51",
    },
    "PINE3": {"empresa": "BANCO PINE", "cnpj": "62.144.175/0001-20"},
    "PINE4": {"empresa": "BANCO PINE", "cnpj": "62.144.175/0001-20"},
    "PMAM3": {"empresa": "PARANAPANEMA", "cnpj": "60.398.369/0004-79"},
    "POMO3": {"empresa": "MARCOPOLO", "cnpj": "88.611.835/0001-29"},
    "POMO4": {"empresa": "MARCOPOLO", "cnpj": "88.611.835/0001-29"},
    "POSI3": {"empresa": "POSITIVO TECNOLOGIA", "cnpj": "81.243.735/0001-48"},
    "PRIO3": {"empresa": "PETRO RIO", "cnpj": "10.629.105/0001-68"},
    "PRML3": {"empresa": "PRUMO LOGÍSTICA", "cnpj": "08.741.499/0001-08"},
    "PSSA3": {"empresa": "PORTO SEGURO", "cnpj": "02.149.205/0001-69"},
    "QGEP3": {"empresa": "QGEP", "cnpj": "11.669.021/0001-10"},
    "QUAL3": {"empresa": "QUALICORP", "cnpj": "11.992.680/0001-93"},
    "RADL3": {"empresa": "RAIA DROGASIL", "cnpj": "61.585.865/0001-51"},
    "RAIL3": {"empresa": "RUMO", "cnpj": "02.387.241/0001-60"},
    "RAPT3": {"empresa": "RANDON IMPLEMENTOS", "cnpj": "89.086.144/0001-16"},
    "RAPT4": {"empresa": "RANDON IMPLEMENTOS", "cnpj": "89.086.144/0001-16"},
    "RCSL3": {"empresa": "RECRUSUL", "cnpj": "91.333.666/0001-17"},
    "RCSL4": {"empresa": "RECRUSUL", "cnpj": "91.333.666/0001-17"},
    "REDE3": {"empresa": "REDE ENERGIA", "cnpj": "61.584.140/0001-49"},
    "RENT3": {"empresa": "LOCALIZA RENT A CAR", "cnpj": "16.670.085/0001-55"},
    "RNEW11": {"empresa": "RENOVA ENERGIA", "cnpj": "08.534.605/0001-74"},
    "RNEW3": {"empresa": "RENOVA ENERGIA", "cnpj": "08.534.605/0001-74"},
    "RNEW4": {"empresa": "RENOVA ENERGIA", "cnpj": "08.534.605/0001-74"},
    "ROMI3": {"empresa": "INDUSTRIAS ROMI", "cnpj": "56.720.428/0001-63"},
    "RPMG3": {
        "empresa": "REFINARIA DE PETROLEOS MANGUINHOS",
        "cnpj": "33.412.081/0001-96",
    },
    "RSID3": {"empresa": "ROSSI RESIDENCIAL", "cnpj": "61.065.751/0001-80"},
    "SANB11": {"empresa": "BANCO SANTANDER", "cnpj": "90.400.888/0001-42"},
    "SANB3": {"empresa": "BANCO SANTANDER", "cnpj": "90.400.888/0001-42"},
    "SANB4": {"empresa": "BANCO SANTANDER", "cnpj": "90.400.888/0001-42"},
    "SAPR11": {
        "empresa": "CIA SANEAMENTO DO PARANA – SANEPAR",
        "cnpj": "76.484.013/0001-45",
    },
    "SAPR3": {
        "empresa": "CIA SANEAMENTO DO PARANA – SANEPAR",
        "cnpj": "76.484.013/0001-45",
    },
    "SAPR4": {
        "empresa": "CIA SANEAMENTO DO PARANA – SANEPAR",
        "cnpj": "76.484.013/0001-45",
    },
    "SBSP3": {
        "empresa": "CIA SANEAMENTO BASICO SAO PAULO – SABESP",
        "cnpj": "43.776.517/0001-80",
    },
    "SCAR3": {"empresa": "SAO CARLOS", "cnpj": "29.780.061/0001-09"},
    "SEDU3": {"empresa": "SOMOS EDUCAÇÃO", "cnpj": "02.541.982/0001-54"},
    "SEER3": {"empresa": "SER EDUCACIONAL", "cnpj": "04.986.320/0001-13"},
    "SGPS3": {"empresa": "SPRINGS GLOBAL", "cnpj": "07.718.269/0001-57"},
    "SHOW3": {"empresa": "T4F ENTRETENIMENTO", "cnpj": "02.860.694/0001-62"},
    "SHUL3": {"empresa": "SCHULZ", "cnpj": "84.693.183/0001-68"},
    "SHUL4": {"empresa": "SCHULZ", "cnpj": "84.693.183/0001-68"},
    "SLCE3": {"empresa": "SLC AGRICOLA", "cnpj": "89.096.457/0001-55"},
    "SLED3": {"empresa": "SARAIVA LIVREIROS EDITORES", "cnpj": "60.500.139/0001-26"},
    "SLED4": {"empresa": "SARAIVA LIVREIROS EDITORES", "cnpj": "60.500.139/0001-26"},
    "SMLS3": {"empresa": "SMILES FIDELIDADE", "cnpj": "05.730.375/0001-20"},
    "SMTO3": {"empresa": "SAO MARTINHO", "cnpj": "51.466.860/0001-56"},
    "SQIA3": {"empresa": "SINQIA S.A.", "cnpj": "04.065.791/0001-99"},
    "SNSL3": {"empresa": "SINQIA S.A.", "cnpj": "04.065.791/0001-99"},
    "SSBR3": {"empresa": "SONAE SIERRA BRASIL", "cnpj": "05.878.397/0001-32"},
    "STBP3": {"empresa": "SANTOS BRASIL", "cnpj": "02.762.121/0001-04"},
    "SULA11": {"empresa": "SUL AMERICA", "cnpj": "29.978.814/0001-87"},
    "SULA3": {"empresa": "SUL AMERICA", "cnpj": "29.978.814/0001-87"},
    "SULA4": {"empresa": "SUL AMERICA", "cnpj": "29.978.814/0001-87"},
    "SUZB3": {"empresa": "SUZANO PAPEL E CELULOSE", "cnpj": "16.404.287/0001-55"},
    "TAEE11": {
        "empresa": "TRANSMISSORA ALIANÇA DE ENERGIA ELÉTRICA",
        "cnpj": "07.859.971/0001-30",
    },
    "TAEE3": {
        "empresa": "TRANSMISSORA ALIANÇA DE ENERGIA ELÉTRICA",
        "cnpj": "07.859.971/0001-30",
    },
    "TAEE4": {
        "empresa": "TRANSMISSORA ALIANÇA DE ENERGIA ELÉTRICA",
        "cnpj": "07.859.971/0001-30",
    },
    "TCNO3": {"empresa": "TECNOSOLO ENGENHARIA", "cnpj": "33.111.246/0001-90"},
    "TCNO4": {"empresa": "TECNOSOLO ENGENHARIA", "cnpj": "33.111.246/0001-90"},
    "TCSA3": {"empresa": "TECNISA", "cnpj": "08.065.557/0001-12"},
    "TECN3": {"empresa": "TECHNOS", "cnpj": "09.295.063/0001-97"},
    "TEKA3": {"empresa": "TEKA-TECELAGEM KUEHNRICH", "cnpj": "82.636.986/0001-55"},
    "TEKA4": {"empresa": "TEKA-TECELAGEM KUEHNRICH", "cnpj": "82.636.986/0001-55"},
    "TEND3": {"empresa": "CONSTRUTORA TENDA", "cnpj": "71.476.527/0001-35"},
    "TGMA3": {"empresa": "TEGMA GESTAO LOGISTICA", "cnpj": "02.351.144/0001-18"},
    "TIET11": {"empresa": "AES TIETE ENERGIA", "cnpj": "04.128.563/0001-10"},
    "TIET3": {"empresa": "AES TIETE ENERGIA", "cnpj": "04.128.563/0001-10"},
    "TIET4": {"empresa": "AES TIETE ENERGIA", "cnpj": "04.128.563/0001-10"},
    "TIMP3": {"empresa": "TIM", "cnpj": "02.558.115/0001-21"},
    "TOTS3": {"empresa": "TOTVS", "cnpj": "53.113.791/0001-22"},
    "TOYB3": {"empresa": "TEC TOY", "cnpj": "22.770.366/0001-82"},
    "TOYB4": {"empresa": "TEC TOY", "cnpj": "22.770.366/0001-82"},
    "TPIS3": {"empresa": "TRIUNFO PART", "cnpj": "03.014.553/0001-91"},
    "TRIS3": {"empresa": "TRISUL", "cnpj": "08.811.643/0001-27"},
    "TRPL3": {
        "empresa": "CIA TRANSMISSÃO ENERGIA ELÉTRICA PAULISTA – CTEEP",
        "cnpj": "02.998.611/0001-04",
    },
    "TRPL4": {
        "empresa": "CIA TRANSMISSÃO ENERGIA ELÉTRICA PAULISTA – CTEEP",
        "cnpj": "02.998.611/0001-04",
    },
    "TRPN3": {"empresa": "TARPON INVESTIMENTOS", "cnpj": "05.341.549/0001-63"},
    "TUPY3": {"empresa": "TUPY", "cnpj": "84.683.374/0001-49"},
    "UCAS3": {"empresa": "UNICASA INDÚSTRIA DE MoVEIS", "cnpj": "90.441.460/0001-48"},
    "UGPA3": {"empresa": "ULTRAPAR PARTICIPACOES", "cnpj": "33.256.439/0001-39"},
    "UNIP6": {"empresa": "UNIPAR CARBOCLORO S.A.", "cnpj": "33.958.695/0001-78"},
    "USIM3": {
        "empresa": "USINAS SIDERÚRGICAS DE MINAS GERAIS – USIMINAS",
        "cnpj": "60.894.730/0001-05",
    },
    "USIM5": {
        "empresa": "USINAS SIDERÚRGICAS DE MINAS GERAIS – USIMINAS",
        "cnpj": "60.894.730/0001-05",
    },
    "USIM6": {
        "empresa": "USINAS SIDERÚRGICAS DE MINAS GERAIS – USIMINAS",
        "cnpj": "60.894.730/0001-05",
    },
    "VALE3": {"empresa": "VALE", "cnpj": "33.592.510/0001-54"},
    "VIVA3": {"empresa": "VIVARA", "cnpj": "84.453.844/0342-44"},
    "VIVR3": {
        "empresa": "VIVER INCORPORADORA E CONSTRUTORA",
        "cnpj": "67.571.414/0001-41",
    },
    "VIVT3": {"empresa": "TELEFÔNICA BRASIL", "cnpj": "02.558.157/0001-62"},
    "VIVT4": {"empresa": "TELEFÔNICA BRASIL", "cnpj": "02.558.157/0001-62"},
    "VLID3": {"empresa": "VALID SOLUÇÕES", "cnpj": "33.113.309/0001-47"},
    "VULC3": {"empresa": "VULCABRAS/AZALEIA", "cnpj": "50.926.955/0001-42"},
    "VVAR11": {"empresa": "VIA VAREJO", "cnpj": "33.041.260/0652-90"},
    "VVAR3": {"empresa": "VIA VAREJO", "cnpj": "33.041.260/0652-90"},
    "VVAR4": {"empresa": "VIA VAREJO", "cnpj": "33.041.260/0652-90"},
    "WEGE3": {"empresa": "WEG S.A.", "cnpj": "84.429.695/0001-11"},
    "WHRL3": {"empresa": "WHIRLPOOL", "cnpj": "59.105.999/0001-86"},
    "WHRL4": {"empresa": "WHIRLPOOL", "cnpj": "59.105.999/0001-86"},
    "WIZS3": {
        "empresa": "WIZ SOLUÇÕES E CORRETAGEM DE SEGUROS",
        "cnpj": "42.278.473/0001-03",
    },
    "WSON33": {"empresa": "WILSON SONS", "cnpj": "05.721.735/0001-28"},
    "NEOE3": {"empresa": "NEOENERGIA S.A.", "cnpj": "01.083.200/0001-18"},
    "TELB3": {
        "empresa": "TELEC BRASILEIRAS S.A. TELEBRAS",
        "cnpj": "00.336.701/0001-04",
    },
    "TELB4": {
        "empresa": "TELEC BRASILEIRAS S.A. TELEBRAS",
        "cnpj": "00.336.701/0001-04",
    },
    "BEES3": {
        "empresa": "BANESTES S.A. - BCO EST ESPIRITO SANTO",
        "cnpj": "28.127.603/0001-78",
    },
    "BEES4": {
        "empresa": "BANESTES S.A. - BCO EST ESPIRITO SANTO",
        "cnpj": "28.127.603/0001-78",
    },
    "EALT4": {"empresa": "ELECTRO ACO ALTONA S.A.", "cnpj": "82.643.537/0001-34"},
    "MEAL3": {
        "empresa": "INTERNATIONAL MEAL COMPANY ALIMENTACAO S.A.",
        "cnpj": "17.314.329/0001-20",
    },
    "PTNT4": {
        "empresa": "PETTENATI S.A. INDUSTRIA TEXTIL",
        "cnpj": "88.613.658/0001-10",
    },
    "JPSA3": {"empresa": "JEREISSATI PARTICIPACOES S.A.", "cnpj": "60.543.816/0001-93"},
    "ENAT3": {"empresa": "ENAUTA PARTICIPACOES S.A.", "cnpj": "11.669.021/0001-10"},
    "CRPG5": {
        "empresa": "TRONOX PIGMENTOS DO BRASIL S.A.",
        "cnpj": "15.115.504/0001-24",
    },
    "BKBR3": {
        "empresa": "BK BRASIL OPERAÇÃO E ASSESSORIA A RESTAURANTES SA",
        "cnpj": "13.574.594/0001-96",
    },
    "GBIO33": {"empresa": "BIOTOSCANA INVESTMENTS S.A.", "cnpj": "19.688.956/0001-56"},
    "PTBL3": {"empresa": "PBG S/A", "cnpj": "83.475.913/0001-91"},
    "ALSO3": {
        "empresa": "ALIANSCE SONAE SHOPPING CENTERS S.A.",
        "cnpj": "05.878.397/0001-32",
    },
    "BMEB4": {"empresa": "BCO MERCANTIL DO BRASIL S.A.", "cnpj": "17.184.037/0001-10"},
    "BTTL3": {
        "empresa": "BATTISTELLA ADM PARTICIPACOES S.A.",
        "cnpj": "42.331.462/0001-31",
    },
    "FRTA3": {"empresa": "POMIFRUTAS S/A", "cnpj": "86.550.951/0001-50"},
    "TESA3": {"empresa": "TERRA SANTA AGRO S.A.", "cnpj": "05.799.312/0001-20"},
    "MNPR3": {"empresa": "MINUPAR PARTICIPACOES S.A.", "cnpj": "90.076.886/0001-40"},
    "AZEV4": {"empresa": "AZEVEDO E TRAVASSOS S.A.", "cnpj": "61.351.532/0001-68"},
    "NTCO3": {"empresa": "NATURA &CO HOLDING S.A.", "cnpj": "32.785.497/0001-97"},
}

ETFS = {
    "BBSD": {
        "RazaoSocial": "BB ETF S&P DIVIDENDOS BRASIL FUNDO DE INDICE",
        "Fundo": "BB ETF SP DV",
        "Cnpj": "17.817.528/0001-50",
    },
    "XBOV": {
        "RazaoSocial": "CAIXA ETF IBOVESPA FUNDO DE INDICE",
        "Fundo": "CAIXAETFXBOV",
        "Cnpj": "14.120.533/0001-11",
    },
    "BOVB": {
        "RazaoSocial": "ETF BRADESCO IBOVESPA FDO DE INDICE",
        "Fundo": "ETF BRAD BOV",
        "Cnpj": "32.203.211/0001-18",
    },
    "IVVB": {
        "RazaoSocial": "ISHARES S&P 500 FDO INV COTAS FDO INDICE",
        "Fundo": "ISHARE SP500",
        "Cnpj": "19.909.560/0001-91",
    },
    "BOVA": {
        "RazaoSocial": "ISHARES IBOVESPA FUNDO DE INDICE",
        "Fundo": "ISHARES BOVA",
        "Cnpj": "10.406.511/0001-61",
    },
    "BRAX": {
        "RazaoSocial": "ISHARES IBRX - INDICE BRASIL (IBRX-100) FDO INDICE",
        "Fundo": "ISHARES BRAX",
        "Cnpj": "11.455.378/0001-04",
    },
    "ECOO": {
        "RazaoSocial": "ISHARES INDICE CARBONO EFIC. (ICO2) BRASIL-FDO IND",
        "Fundo": "ISHARES ECOO",
        "Cnpj": "15.562.377/0001-01",
    },
    "SMAL": {
        "RazaoSocial": "ISHARES BMFBOVESPA SMALL CAP FUNDO DE INDICE",
        "Fundo": "ISHARES SMAL",
        "Cnpj": "10.406.600/0001-08",
    },
    "BOVV": {
        "RazaoSocial": "IT NOW IBOVESPA FUNDO DE INDICE",
        "Fundo": "IT NOW IBOV",
        "Cnpj": "21.407.758/0001-19",
    },
    "DIVO": {
        "RazaoSocial": "IT NOW IDIV FUNDO DE INDICE",
        "Fundo": "IT NOW IDIV",
        "Cnpj": "13.416.245/0001-46",
    },
    "FIND": {
        "RazaoSocial": "IT NOW IFNC FUNDO DE INDICE",
        "Fundo": "IT NOW IFNC",
        "Cnpj": "11.961.094/0001-81",
    },
    "GOVE": {
        "RazaoSocial": "IT NOW IGCT FUNDO DE INDICE",
        "Fundo": "IT NOW IGCT",
        "Cnpj": "11.184.136/0001-15",
    },
    "MATB": {
        "RazaoSocial": "IT NOW IMAT FUNDO DE INDICE",
        "Fundo": "IT NOW IMAT",
        "Cnpj": "13.416.228/0001-09",
    },
    "ISUS": {
        "RazaoSocial": "IT NOW ISE FUNDO DE INDICE",
        "Fundo": "IT NOW ISE",
        "Cnpj": "12.984.444/0001-98",
    },
    "PIBB": {
        "RazaoSocial": "IT NOW PIBB IBRX-50 - FUNDO DE INDICE",
        "Fundo": "IT NOW PIBB",
        "Cnpj": "06.323.688/0001-27",
    },
    "SMAC": {
        "RazaoSocial": "IT NOW SMALL FDO INDICE",
        "Fundo": "IT NOW SMALL",
        "Cnpj": "34.803.814/0001-86",
    },
    "SPXI": {
        "RazaoSocial": "IT NOW S&P500 TRN FUNDO DE INDICE",
        "Fundo": "IT NOW SPXI",
        "Cnpj": "17.036.289/0001-00",
    },
}

FIIS = {
    "ALZR": {
        "nome": "ALIANZA TRUST RENDA IMOBILIÁRIA",
        "cnpj": "28.737.771/0001-85",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "AQLL": {
        "nome": "ÁQUILLA",
        "cnpj": "13.555.918/0001-49",
        "nome_adm": "FOCO DTVM LTDA.",
        "cnpj_adm": "00.329.598/0001-67",
    },
    "BCRI": {
        "nome": "BANESTES RECEBÍVEIS IMOBILIÁRIOS",
        "cnpj": "22.219.335/0001-38",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "BNFS": {
        "nome": "BANRISUL NOVAS FRONTEIRAS",
        "cnpj": "15.570.431/0001-60",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "BBPO": {
        "nome": "BB PROGRESSIVO II",
        "cnpj": "14.410.722/0001-29",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "BBIM": {
        "nome": "BB RECEBÍVEIS IMOBILIÁRIOS",
        "cnpj": "20.716.161/0001-93",
        "nome_adm": "BB GESTAO DE RECURSOS DTVM S.A",
        "cnpj_adm": "30.822.936/0001-69",
    },
    "BBRC": {
        "nome": "BB RENDA CORPORATIVA",
        "cnpj": "12.681.340/0001-04",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "RDPD": {
        "nome": "BB RENDA DE PAPEIS IMOBILIÁRIOS II",
        "cnpj": "23.120.027/0001-13",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "RNDP": {
        "nome": "BB RENDA DE PAPÉIS IMOBILIÁRIOS",
        "cnpj": "15.394.563/0001-89",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "BCIA": {
        "nome": "BRADESCO CARTEIRA IMOBILIÁRIA ATIVA",
        "cnpj": "20.216.935/0001-17",
        "nome_adm": "BANCO BRADESCO S.A.",
        "cnpj_adm": "60.746.948/0001-12",
    },
    "BZLI": {
        "nome": "BRAZIL REALTY",
        "cnpj": "14.074.706/0001-02",
        "nome_adm": "FOCO DTVM LTDA.",
        "cnpj_adm": "00.329.598/0001-67",
    },
    "CARE": {
        "nome": "BRAZILIAN GRAVEYARD AND DEATH CARE",
        "cnpj": "13.584.584/0001-31",
        "nome_adm": (
            "PLANNER TRUSTEE DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "67.030.395/0001-46",
    },
    "BRCO": {
        "nome": "FII BRESCO",
        "cnpj": "20.748.515/0001-81",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "BTLG": {
        "nome": "FII BTLG",
        "cnpj": "11.839.593/0001-09",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "CRFF": {
        "nome": "FII CX RBRA2",
        "cnpj": "31.887.401/0001-39",
        "nome_adm": "CAIXA ECONOMICA FEDERAL",
        "cnpj_adm": "00.360.305/0001-04",
    },
    "CXRI": {
        "nome": "CAIXA RIO BRAVO",
        "cnpj": "17.098.794/0001-70",
        "nome_adm": "CAIXA ECONOMICA FEDERAL",
        "cnpj_adm": "00.360.305/0001-04",
    },
    "CPFF": {
        "nome": "FII CAP REIT",
        "cnpj": "34.081.611/0001-23",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "CBOP": {
        "nome": "CASTELLO BRANCO OFFICE PARK",
        "cnpj": "17.144.039/0001-85",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "GRLV": {
        "nome": "CSHG GR LOUVEIRA",
        "cnpj": "17.143.998/0001-86",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "HGFF": {
        "nome": "FII CSHG FOF",
        "cnpj": "32.784.898/0001-22",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "HGLG": {
        "nome": "CGHG LOGÍSTICA",
        "cnpj": "11.728.688/0001-47",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "HGPO": {
        "nome": "FII CSHGPRIM",
        "cnpj": "11.260.134/0001-68",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "HGRE": {
        "nome": "CSHG REAL ESTATE",
        "cnpj": "09.072.017/0001-29",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "HGCR": {
        "nome": "CGHG RECEBÍVEIS IMOBILIÁRIOS",
        "cnpj": "11.160.521/0001-22",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "HGRU": {
        "nome": "CSHG RENDA URBANA",
        "cnpj": "29.641.226/0001-53",
        "nome_adm": "CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.",
        "cnpj_adm": "61.809.182/0001-30",
    },
    "ERPA": {
        "nome": "FII EUROPA",
        "cnpj": "31.469.385/0001-64",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "KINP": {
        "nome": "EVEN PERMUTA KINEA",
        "cnpj": "24.070.076/0001-51",
        "nome_adm": "INTRAG DTVM LTDA.",
        "cnpj_adm": "62.418.140/0001-31",
    },
    "VRTA": {
        "nome": "FATOR VERITA",
        "cnpj": "11.664.201/0001-00",
        "nome_adm": "BANCO FATOR S/A",
        "cnpj_adm": "33.644.196/0001-06",
    },
    "BMII": {
        "nome": "BRASILIO MACHADO",
        "cnpj": "02.027.437/0001-44",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "BTCR": {
        "nome": "BTG PACTUAL CRÉDITO IMOBILIÁRIO",
        "cnpj": "29.787.928/0001-40",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "FAED": {
        "nome": "ANHANGUERA EDUCACIONAL",
        "cnpj": "11.179.118/0001-45",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "BPRP": {
        "nome": "FII BRLPROP",
        "cnpj": "29.800.650/0001-01",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "BRCR": {
        "nome": "BTG PACTUAL CORPORATE OFFICE",
        "cnpj": "08.924.783/0001-01",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "FEXC": {
        "nome": "BTG PACTUAL FUNDO DE CRI",
        "cnpj": "09.552.812/0001-14",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "BCFF": {
        "nome": "BTG FUNDO DE FUNDOS",
        "cnpj": "11.026.627/0001-38",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "FCFL": {
        "nome": "CAMPUS FARIA LIMA",
        "cnpj": "11.602.654/0001-01",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "CNES": {
        "nome": "CENESP",
        "cnpj": "13.551.286/0001-45",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "CEOC": {
        "nome": "CYRELA COMMERCIAL PROPERTIES",
        "cnpj": "15.799.397/0001-09",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "THRA": {
        "nome": "CYRELA THERA CORPORATE",
        "cnpj": "13.966.653/0001-71",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "EDGA": {
        "nome": "EDIFÍCIO GALERIA",
        "cnpj": "15.333.306/0001-37",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "FLRP": {
        "nome": "FLORIPA SHOPPING",
        "cnpj": "10.375.382/0001-91",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "HCRI": {
        "nome": "HOSPITAL DA CRIANÇA",
        "cnpj": "04.066.582/0001-60",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "NSLU": {
        "nome": "HOSPITAL NOSSA SRA LOURDES",
        "cnpj": "08.014.513/0001-63",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "HTMX": {
        "nome": "HOTEL MAXINVEST",
        "cnpj": "08.706.065/0001-69",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "MAXR": {
        "nome": "MAX RETAIL",
        "cnpj": "11.274.415/0001-70",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "NCHB": {
        "nome": "NCH BRASIL RECEBÍVEIS IMOBILIÁRIOS",
        "cnpj": "18.085.673/0001-57",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "NVHO": {
        "nome": "NOVO HORIZONTE",
        "cnpj": "17.025.970/0001-44",
        "nome_adm": "PLURAL S.A. BANCO MÚLTIPLO",
        "cnpj_adm": "45.246.410/0001-55",
    },
    "PQDP": {
        "nome": "PARQUE DOM PEDRO SHOPPING CENTER",
        "cnpj": "10.869.155/0001-12",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "PRSV": {
        "nome": "PRESIDENTE VARGAS",
        "cnpj": "11.281.322/0001-72",
        "nome_adm": "BEM - DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "00.066.670/0001-00",
    },
    "RBRM": {
        "nome": "FII RBR DES",
        "cnpj": "26.314.437/0001-93",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "RBRR": {
        "nome": "RBR RENDIMENTO HIGH GRADE",
        "cnpj": "29.467.977/0001-03",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "JRDM": {
        "nome": "SHOPPING JARDIM SUL ",
        "cnpj": "14.879.856/0001-93",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "TBOF": {
        "nome": "TB OFFICE",
        "cnpj": "17.365.105/0001-47",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "ALMI": {
        "nome": "TORRE ALMIRANTE",
        "cnpj": "07.122.725/0001-00",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "TRNT": {
        "nome": "TORRE NORTE",
        "cnpj": "04.722.883/0001-02",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "RECT": {
        "nome": "FII UBSOFFIC",
        "cnpj": "32.274.163/0001-59",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "UBSR": {
        "nome": "UBS BR RECEBÍVEIS IMOBILIÁRIOS",
        "cnpj": "28.152.272/0001-26",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "VLOL": {
        "nome": "VILA OLÍMPIA CORPORATE",
        "cnpj": "15.296.696/0001-12",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "OUFF": {
        "nome": "FII OURI FOF",
        "cnpj": "30.791.386/0001-68",
        "nome_adm": "BANCO OURINVEST S.A.",
        "cnpj_adm": "78.632.767/0001-20",
    },
    "VVPR": {
        "nome": "FII V2 PROP",
        "cnpj": "33.045.581/0001-37",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "LVBI": {
        "nome": "FII VBI LOG",
        "cnpj": "30.629.603/0001-18",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "BARI": {
        "nome": "FII BARIGUI",
        "cnpj": "29.267.567/0001-00",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "BBVJ": {
        "nome": "BB VOTORANTIM CIDADE JARDIM CONTINENTAL TOWER",
        "cnpj": "10.347.985/0001-80",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "BPFF": {
        "nome": "BRASIL PLURAL ABSOLUTO FUNDO DE FUNDOS",
        "cnpj": "17.324.357/0001-28",
        "nome_adm": "GENIAL INVESTIMENTOS CORRETORA DE VALORES MOBILIÁRIOS S.A.",
        "cnpj_adm": "27.652.684/0001-62",
    },
    "BVAR": {
        "nome": "BRASIL VAREJO",
        "cnpj": "21.126.204/0001-43",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "BPML": {
        "nome": "FII BTG SHOP",
        "cnpj": "33.046.142/0001-49",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "CXTL": {
        "nome": "CAIXA TRX LOGÍSTICA RENDA",
        "cnpj": "12.887.506/0001-43",
        "nome_adm": "CAIXA ECONOMICA FEDERAL",
        "cnpj_adm": "00.360.305/0001-04",
    },
    "CTXT": {
        "nome": "CENTRO TÊXTIL INTERNACIONAL",
        "cnpj": "00.762.723/0001-28",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "FLMA": {
        "nome": "CONTINENTAL SQUARE FARIA LIMA",
        "cnpj": "04.141.645/0001-03",
        "nome_adm": "BR-CAPITAL DTVM S.A.",
        "cnpj_adm": "44.077.014/0001-89",
    },
    "EURO": {
        "nome": "EUROPAR",
        "cnpj": "05.437.916/0001-27",
        "nome_adm": "COINVALORES CCVM LTDA",
        "cnpj_adm": "00.336.036/0001-40",
    },
    "FIGS": {
        "nome": "GENERAL SHOPPING ATIVO E RENDA",
        "cnpj": "17.590.518/0001-25",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "ABCP": {
        "nome": "GRAND PLAZA SHOPPING",
        "cnpj": "01.201.140/0001-90",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "GTWR": {
        "nome": "FII G TOWERS",
        "cnpj": "23.740.527/0001-58",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "HBTT": {
        "nome": "HABITAT I",
        "cnpj": "26.846.202/0001-42",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "HUSC": {
        "nome": "HOSPITAL UNIMED SUL CAPIXABA",
        "cnpj": "28.851.767/0001-43",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "FIIB": {
        "nome": "INDUSTRIAL DO BRASIL",
        "cnpj": "14.217.108/0001-45",
        "nome_adm": "COINVALORES CCVM LTDA",
        "cnpj_adm": "00.336.036/0001-40",
    },
    "FINF": {
        "nome": "INFRA REAL STATE",
        "cnpj": "18.369.510/0001-04",
        "nome_adm": "PLANNER CORRETORA DE VALORES SA",
        "cnpj_adm": "00.806.535/0001-54",
    },
    "FMOF": {
        "nome": "MEMORIAL OFFICE",
        "cnpj": "01.633.741/0001-72",
        "nome_adm": "COIN - DTVM LTDA.",
        "cnpj_adm": "61.384.004/0001-05",
    },
    "MBRF": {
        "nome": "MERCANTIL DO BRASIL",
        "cnpj": "13.500.306/0001-59",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "MGFF": {
        "nome": "MOGNO FUNDO DE FUNDOS",
        "cnpj": "29.216.463/0001-77",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "NPAR": {
        "nome": "NESTPAR",
        "cnpj": "24.814.916/0001-43",
        "nome_adm": "PLANNER CORRETORA DE VALORES SA",
        "cnpj_adm": "00.806.535/0001-54",
    },
    "PABY": {
        "nome": "PANAMBY",
        "cnpj": "00.613.094/0001-74",
        "nome_adm": "BRKB DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "33.923.111/0001-29",
    },
    "FPNG": {
        "nome": "PEDRA NEGRA RENDA IMOBILIÁRIA",
        "cnpj": "17.161.979/0001-82",
        "nome_adm": "BR-CAPITAL DTVM S.A.",
        "cnpj_adm": "44.077.014/0001-89",
    },
    "VPSI": {
        "nome": "POLO SHOPPING INDAIATUBA",
        "cnpj": "14.721.889/0001-00",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "FPAB": {
        "nome": "PROJETO ÁGUA BRANCA",
        "cnpj": "03.251.720/0001-18",
        "nome_adm": "COIN - DTVM LTDA.",
        "cnpj_adm": "61.384.004/0001-05",
    },
    "RBRY": {
        "nome": "FII RBR PCRI",
        "cnpj": "30.166.700/0001-11",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "RBRP": {
        "nome": "RBR PROPERTIES",
        "cnpj": "21.408.063/0001-51",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "RCRB": {
        "nome": "FII RIOB RC",
        "cnpj": "03.683.056/0001-86",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "RBED": {
        "nome": "FII RIOB ED",
        "cnpj": "13.873.457/0001-52",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "RBVA": {
        "nome": "FII RIOB VA",
        "cnpj": "15.576.907/0001-70",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "RNGO": {
        "nome": "RIO NEGRO",
        "cnpj": "15.006.286/0001-90",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "SFND": {
        "nome": "SÃO FERNANDO",
        "cnpj": "09.350.920/0001-04",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "FISC": {
        "nome": "FII SC 401",
        "cnpj": "12.804.013/0001-00",
        "nome_adm": "CORRETORA GERAL DE VALORES E CAMBIO LTDA",
        "cnpj_adm": "92.858.380/0001-18",
    },
    "SCPF": {
        "nome": "SCP",
        "cnpj": "01.657.856/0001-05",
        "nome_adm": "BR-CAPITAL DTVM S.A.",
        "cnpj_adm": "44.077.014/0001-89",
    },
    "SDIL": {
        "nome": "SDI LOGÍSTICA RIO",
        "cnpj": "16.671.412/0001-93",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "SHPH": {
        "nome": "SHOPPING PATIO HIGIENOPOLIS",
        "cnpj": "03.507.519/0001-59",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "TGAR": {
        "nome": "TG ATIVO REAL",
        "cnpj": "25.032.881/0001-53",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "ONEF": {
        "nome": "THE ONE",
        "cnpj": "12.948.291/0001-23",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "TOUR": {
        "nome": "FII TOUR II",
        "cnpj": "30.578.316/0001-26",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "FVBI": {
        "nome": "VBI FL 4440",
        "cnpj": "13.022.993/0001-44",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "VERE": {
        "nome": "VEREDA",
        "cnpj": "08.693.497/0001-82",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "FVPQ": {
        "nome": "VIA PARQUE SHOPPING",
        "cnpj": "00.332.266/0001-31",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "FIVN": {
        "nome": "VIDA NOVA",
        "cnpj": "17.854.016/0001-64",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "VTLT": {
        "nome": "VOTORANTIM LOGÍSTICA",
        "cnpj": "27.368.600/0001-63",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "VSHO": {
        "nome": "FII VOT SHOP",
        "cnpj": "23.740.595/0001-17",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "IBFF": {
        "nome": "FII FOF BREI",
        "cnpj": "33.721.517/0001-29",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "PLCR": {
        "nome": "FII PLURAL R",
        "cnpj": "32.527.683/0001-26",
        "nome_adm": "PLURAL S.A. BANCO MÚLTIPLO",
        "cnpj_adm": "45.246.410/0001-55",
    },
    "CVBI": {
        "nome": "FII VBI CRI",
        "cnpj": "28.729.197/0001-13",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "MCCI": {
        "nome": "FII MAUA",
        "cnpj": "23.648.935/0001-84",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "ARRI": {
        "nome": "FII ATRIO",
        "cnpj": "32.006.821/0001-21",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "HOSI": {
        "nome": "FII HOUSI",
        "cnpj": "34.081.631/0001-02",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "IRDM": {
        "nome": "IRIDIUM RECEBÍVEIS IMOBILIÁRIOS",
        "cnpj": "28.830.325/0001-10",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "KFOF": {
        "nome": "FII KINEAFOF",
        "cnpj": "30.091.444/0001-40",
        "nome_adm": "INTRAG DTVM LTDA.",
        "cnpj_adm": "62.418.140/0001-31",
    },
    "OUCY": {
        "nome": "OURINVEST CYRELA",
        "cnpj": "28.516.650/0001-03",
        "nome_adm": "BANCO OURINVEST S.A.",
        "cnpj_adm": "78.632.767/0001-20",
    },
    "GSFI": {
        "nome": "FII GENERAL",
        "cnpj": "11.769.604/0001-13",
        "nome_adm": "PLANNER CORRETORA DE VALORES SA",
        "cnpj_adm": "00.806.535/0001-54",
    },
    "GGRC": {
        "nome": "GGR COVEPI RENDA",
        "cnpj": "26.614.291/0001-00",
        "nome_adm": "CM CAPITAL MARKETS DTVM LTDA",
        "cnpj_adm": "02.671.743/0001-19",
    },
    "RCFA": {
        "nome": "FII GP RCFA",
        "cnpj": "27.771.586/0001-44",
        "nome_adm": "FRAM CAPITAL DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.",
        "cnpj_adm": "13.673.855/0001-25",
    },
    "HABT": {
        "nome": "FII HABIT II",
        "cnpj": "30.578.417/0001-05",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "ATCR": {
        "nome": "HAZ",
        "cnpj": "14.631.148/0001-39",
        "nome_adm": "RJI CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA",
        "cnpj_adm": "42.066.258/0001-30",
    },
    "HCTR": {
        "nome": "FII HECTARE",
        "cnpj": "30.248.180/0001-96",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "ATSA": {
        "nome": "HEDGE ATRIUM SHOPPING SANTO ANDRÉ",
        "cnpj": "12.809.972/0001-00",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "HGBS": {
        "nome": "CSHG BRASIL SHOPPING",
        "cnpj": "08.431.747/0001-06",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "HLOG": {
        "nome": "FII HEDGELOG",
        "cnpj": "27.486.542/0001-72",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "HRDF": {
        "nome": "FII HREALTY",
        "cnpj": "16.929.519/0001-99",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "HPDP": {
        "nome": "FII HEDGE RE",
        "cnpj": "35.586.415/0001-73",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "HMOC": {
        "nome": "FII HEDMOCA",
        "cnpj": "14.733.211/0001-48",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "HFOF": {
        "nome": "HEDGE TOP FOFII 3",
        "cnpj": "18.307.582/0001-19",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "TFOF": {
        "nome": "HEDGE TOP FOFII ",
        "cnpj": "20.834.884/0001-97",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "HSML": {
        "nome": "FII HSI MALL",
        "cnpj": "32.892.018/0001-31",
        "nome_adm": "SANTANDER SECURITIES SERVICES BRASIL DTVM S.A",
        "cnpj_adm": "62.318.407/0001-19",
    },
    "BICR": {
        "nome": "FII INTER",
        "cnpj": "34.007.109/0001-72",
        "nome_adm": "INTER DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS",
        "cnpj_adm": "18.945.670/0001-46",
    },
    "RBBV": {
        "nome": "JHSF RIO BRAVO FAZENDA BOA VISTA CAPITAL PROTEGIDO",
        "cnpj": "16.915.868/0001-51",
        "nome_adm": "CAIXA ECONOMICA FEDERAL",
        "cnpj_adm": "00.360.305/0001-04",
    },
    "JPPA": {
        "nome": "FII JPPMOGNO",
        "cnpj": "30.982.880/0001-00",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "JPPC": {
        "nome": "JPP CAPITAL",
        "cnpj": "17.216.625/0001-98",
        "nome_adm": "BANCO FINAXIS S.A.",
        "cnpj_adm": "11.758.741/0001-52",
    },
    "JSRE": {
        "nome": "JS REAL ESTATE MULTIGESTÃO",
        "cnpj": "13.371.132/0001-71",
        "nome_adm": "BANCO J. SAFRA S.A.",
        "cnpj_adm": "03.017.677/0001-20",
    },
    "JTPR": {
        "nome": "JT PREV FII DESENVOLVIMENTO HABITACIONAL",
        "cnpj": "23.876.086/0001-16",
        "nome_adm": "PLANNER CORRETORA DE VALORES SA",
        "cnpj_adm": "00.806.535/0001-54",
    },
    "KNHY": {
        "nome": "KINEA HIGH YIELD CRI",
        "cnpj": "30.130.708/0001-28",
        "nome_adm": "INTRAG DTVM LTDA.",
        "cnpj_adm": "62.418.140/0001-31",
    },
    "KNRE": {
        "nome": "KINEA II REAL ESTATE EQUITY",
        "cnpj": "14.423.780/0001-97",
        "nome_adm": "INTRAG DTVM LTDA.",
        "cnpj_adm": "62.418.140/0001-31",
    },
    "KNIP": {
        "nome": "KINEA ÍNDICE DE PREÇOS",
        "cnpj": "24.960.430/0001-13",
        "nome_adm": "INTRAG DTVM LTDA.",
        "cnpj_adm": "62.418.140/0001-31",
    },
    "KNRI": {
        "nome": "KINEA RENDA IMOBILIÁRIA",
        "cnpj": "12.005.956/0001-65",
        "nome_adm": "INTRAG DTVM LTDA.",
        "cnpj_adm": "62.418.140/0001-31",
    },
    "KNCR": {
        "nome": "KINEA RENDIMENTOS IMOBILIÁRIOS",
        "cnpj": "16.706.958/0001-32",
        "nome_adm": "INTRAG DTVM LTDA.",
        "cnpj_adm": "62.418.140/0001-31",
    },
    "LGCP": {
        "nome": "FII LGCP INT",
        "cnpj": "34.598.181/0001-11",
        "nome_adm": "INTER DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS",
        "cnpj_adm": "18.945.670/0001-46",
    },
    "LUGG": {
        "nome": "FII LUGGO",
        "cnpj": "34.835.191/0001-23",
        "nome_adm": "INTER DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS",
        "cnpj_adm": "18.945.670/0001-46",
    },
    "DMAC": {
        "nome": "FII MAC",
        "cnpj": "30.579.348/0001-46",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "MALL": {
        "nome": "MALLS BRASIL PLURAL",
        "cnpj": "26.499.833/0001-32",
        "nome_adm": "GENIAL INVESTIMENTOS CORRETORA DE VALORES MOBILIÁRIOS S.A.",
        "cnpj_adm": "27.652.684/0001-62",
    },
    "MXRF": {
        "nome": "MAXI RENDA",
        "cnpj": "97.521.225/0001-25",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "MFII": {
        "nome": "MÉRITO DESENVOLVIMENTO IMOBILIÁRIO",
        "cnpj": "16.915.968/0001-88",
        "nome_adm": "PLANNER CORRETORA DE VALORES SA",
        "cnpj_adm": "00.806.535/0001-54",
    },
    "PRTS": {
        "nome": "MULTI PROPERTIES FII",
        "cnpj": "22.957.521/0001-74",
        "nome_adm": "BANCO MODAL S.A.",
        "cnpj_adm": "30.723.886/0001-62",
    },
    "SHOP": {
        "nome": "MULTI SHOPPINGS",
        "cnpj": "22.459.737/0001-00",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "NEWL": {
        "nome": "FII NEWPORT",
        "cnpj": "32.527.626/0001-47",
        "nome_adm": "PLURAL S.A. BANCO MÚLTIPLO",
        "cnpj_adm": "45.246.410/0001-55",
    },
    "OUJP": {
        "nome": "OURINVEST JPP",
        "cnpj": "26.091.656/0001-50",
        "nome_adm": "FINAXIS CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.",
        "cnpj_adm": "03.317.692/0001-94",
    },
    "ORPD": {
        "nome": "OURO PRETO DESENVOLVIMENTO IMOBILIÁRIO I",
        "cnpj": "19.107.604/0001-60",
        "nome_adm": "PLANNER CORRETORA DE VALORES SA",
        "cnpj_adm": "00.806.535/0001-54",
    },
    "PATC": {
        "nome": "FII PATRIA",
        "cnpj": "30.048.651/0001-12",
        "nome_adm": "MODAL D.T.V.M. LTDA",
        "cnpj_adm": "05.389.174/0001-01",
    },
    "PLRI": {
        "nome": "POLO RECEBÍVEIS IMOBILIÁRIOS I",
        "cnpj": "14.080.689/0001-16",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "PORD": {
        "nome": "POLO RECEBÍVEIS IMOBILIÁRIOS II",
        "cnpj": "17.156.502/0001-09",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "PBLV": {
        "nome": "FII PROLOGIS",
        "cnpj": "31.962.875/0001-06",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "QAGR": {
        "nome": "FII QUASAR A",
        "cnpj": "32.754.734/0001-52",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "RSPD": {
        "nome": "FII RBRESID3",
        "cnpj": "19.249.989/0001-08",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "RBDS": {
        "nome": "RB CAPITAL DESENVOLVIMENTO RESIDENCIAL II",
        "cnpj": "11.945.604/0001-27",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "RBGS": {
        "nome": "RB CAPITAL GENERAL SHOPPING SULACAP",
        "cnpj": "13.652.006/0001-95",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "RBCO": {
        "nome": "FII R INCOME",
        "cnpj": "31.894.369/0001-19",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "RBRD": {
        "nome": "RB CAPITAL RENDA II",
        "cnpj": "09.006.914/0001-34",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "RBTS": {
        "nome": "FII RB TFO",
        "cnpj": "29.299.737/0001-39",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "RBRF": {
        "nome": "RBR ALPHA FUNDO DE FUNDOS - FII",
        "cnpj": "27.529.279/0001-51",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "DOMC": {
        "nome": "REAG RENDA IMOBILIÁRIA",
        "cnpj": "17.374.696/0001-19",
        "nome_adm": "MONETAR DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "12.063.256/0001-27",
    },
    "RBVO": {
        "nome": "RIO BRAVO CRÉDITO IMOBILIÁRIO II",
        "cnpj": "15.769.670/0001-44",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "RBFF": {
        "nome": "FII RIOB FF",
        "cnpj": "17.329.029/0001-14",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "SAAG": {
        "nome": "SANTANDER AGÊNCIAS",
        "cnpj": "16.915.840/0001-14",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "SADI": {
        "nome": "FII SANT PAP",
        "cnpj": "32.903.521/0001-45",
        "nome_adm": "SANTANDER SECURITIES SERVICES BRASIL DTVM S.A",
        "cnpj_adm": "62.318.407/0001-19",
    },
    "SARE": {
        "nome": "FII SANT REN",
        "cnpj": "32.903.702/0001-71",
        "nome_adm": "SANTANDER SECURITIES SERVICES BRASIL DTVM S.A",
        "cnpj_adm": "62.318.407/0001-19",
    },
    "FISD": {
        "nome": "SÃO DOMINGOS",
        "cnpj": "16.543.270/0001-89",
        "nome_adm": "RJI CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA",
        "cnpj_adm": "42.066.258/0001-30",
    },
    "WPLZ": {
        "nome": "SHOPPING WEST PLAZA",
        "cnpj": "09.326.861/0001-39",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
    "REIT": {
        "nome": "SOCOPA FUNDO DE INVESTIMENTO IMOBILIÁRIO",
        "cnpj": "16.841.067/0001-99",
        "nome_adm": "SOCOPA SOCIEDADE CORRETORA PAULISTA SA",
        "cnpj_adm": "62.285.390/0001-40",
    },
    "SPTW": {
        "nome": "SP DOWNTOWN",
        "cnpj": "15.538.445/0001-05",
        "nome_adm": "GENIAL INVESTIMENTOS CORRETORA DE VALORES MOBILIÁRIOS S.A.",
        "cnpj_adm": "27.652.684/0001-62",
    },
    "SPAF": {
        "nome": "SPA FUNDO DE INVESTIMENTO IMOBILIÁRIO - FII",
        "cnpj": "18.311.024/0001-27",
        "nome_adm": "PLURAL S.A. BANCO MÚLTIPLO",
        "cnpj_adm": "45.246.410/0001-55",
    },
    "STRX": {
        "nome": "FII STARX",
        "cnpj": "11.044.355/0001-07",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "TSNC": {
        "nome": "TRANSINC",
        "cnpj": "17.007.443/0001-07",
        "nome_adm": "BANCO FINAXIS S.A.",
        "cnpj_adm": "11.758.741/0001-52",
    },
    "TCPF": {
        "nome": "FII TREECORP",
        "cnpj": "26.990.011/0001-50",
        "nome_adm": "BR-CAPITAL DTVM S.A.",
        "cnpj_adm": "44.077.014/0001-89",
    },
    "XTED": {
        "nome": "TRX EDIFÍCIOS CORPORATIVOS",
        "cnpj": "15.006.267/0001-63",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "TRXF": {
        "nome": "FII TRX REAL",
        "cnpj": "28.548.288/0001-52",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "VGIR": {
        "nome": "VALORA RE III",
        "cnpj": "29.852.732/0001-91",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "VLJS": {
        "nome": "VECTOR QUELUZ LAJES CORPORATIVAS",
        "cnpj": "13.842.683/0001-76",
        "nome_adm": "PLANNER CORRETORA DE VALORES SA",
        "cnpj_adm": "00.806.535/0001-54",
    },
    "VILG": {
        "nome": "FII VINCILOG",
        "cnpj": "24.853.044/0001-22",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "VINO": {
        "nome": "FII VINC COR",
        "cnpj": "12.516.185/0001-70",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "VISC": {
        "nome": "VINCI SHOPPING CENTERS",
        "cnpj": "17.554.274/0001-25",
        "nome_adm": "BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "13.486.793/0001-42",
    },
    "VOTS": {
        "nome": "VOTORANTIM SECURITIES MASTER",
        "cnpj": "17.870.926/0001-30",
        "nome_adm": "VOTORANTIM ASSET MANAGEMENT DTVM LTDA.",
        "cnpj_adm": "03.384.738/0001-98",
    },
    "XPCM": {
        "nome": "XP CORPORATE MACAÉ",
        "cnpj": "16.802.320/0001-03",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "XPCI": {
        "nome": "FII XP CRED",
        "cnpj": "28.516.301/0001-91",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "XPHT": {
        "nome": "FII XP HOT",
        "cnpj": "18.308.516/0001-63",
        "nome_adm": "GENIAL INVESTIMENTOS CORRETORA DE VALORES MOBILIÁRIOS S.A.",
        "cnpj_adm": "27.652.684/0001-62",
    },
    "XPIN": {
        "nome": "XP INDUSTRIAL",
        "cnpj": "28.516.325/0001-40",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "XPLG": {
        "nome": "XP LOG",
        "cnpj": "26.502.794/0001-85",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "XPML": {
        "nome": "XP MALLS",
        "cnpj": "28.757.546/0001-00",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "XPPR": {
        "nome": "FII XP PROP",
        "cnpj": "30.654.849/0001-40",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "XPSF": {
        "nome": "FII XP SELEC",
        "cnpj": "30.983.020/0001-90",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "YCHY": {
        "nome": "FII YAGUARA",
        "cnpj": "28.267.696/0001-36",
        "nome_adm": "VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.",
        "cnpj_adm": "22.610.500/0001-88",
    },
    "ARFI": {
        "nome": "ÁQUILLA RENDA",
        "cnpj": "14.069.202/0001-02",
        "nome_adm": "FOCO DTVM LTDA.",
        "cnpj_adm": "00.329.598/0001-67",
    },
    "BBFI": {
        "nome": "BB PROGRESSIVO",
        "cnpj": "07.000.400/0001-46",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "CPTS": {
        "nome": "CAPITANIA SECURITIES II",
        "cnpj": "18.979.895/0001-13",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "DAMT": {
        "nome": "FII DIAMANTE",
        "cnpj": "26.642.727/0001-66",
        "nome_adm": "BANCO MODAL S.A.",
        "cnpj_adm": "30.723.886/0001-62",
    },
    "DOVL": {
        "nome": "FII DOVEL",
        "cnpj": "10.522.648/0001-81",
        "nome_adm": "BNY MELLON SERVICOS FINANCEIROS DTVM S.A.",
        "cnpj_adm": "02.201.501/0001-61",
    },
    "ANCR": {
        "nome": "ANCAR CI",
        "cnpj": "07.789.135/0001-27",
        "nome_adm": "GENIAL INVESTIMENTOS CORRETORA DE VALORES MOBILIÁRIOS S.A.",
        "cnpj_adm": "27.652.684/0001-62",
    },
    "BMLC": {
        "nome": "BM BRASCAN LAJES CORPORATIVAS",
        "cnpj": "14.376.247/0001-11",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "FAMB": {
        "nome": "EDIFÍCIO ALMIRANTE BARROSO",
        "cnpj": "05.562.312/0001-02",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "ELDO": {
        "nome": "ELDORADO",
        "cnpj": "13.022.994/0001-99",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "SHDP": {
        "nome": "SHOPPING PARQUE DOM PEDRO",
        "cnpj": "07.224.019/0001-60",
        "nome_adm": "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
        "cnpj_adm": "59.281.253/0001-23",
    },
    "SAIC": {
        "nome": "SIA CORPORATE",
        "cnpj": "17.311.079/0001-74",
        "nome_adm": "BRB DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.",
        "cnpj_adm": "33.850.686/0001-69",
    },
    "WTSP": {
        "nome": "OURINVEST RE I",
        "cnpj": "28.693.595/0001-27",
        "nome_adm": "BANCO OURINVEST S.A.",
        "cnpj_adm": "78.632.767/0001-20",
    },
    "BRHT": {
        "nome": "BR HOTÉIS",
        "cnpj": "15.461.076/0001-91",
        "nome_adm": "ELITE CCVM LTDA",
        "cnpj_adm": "28.048.783/0001-00",
    },
    "CXCE": {
        "nome": "CAIXA CEDAE",
        "cnpj": "10.991.914/0001-15",
        "nome_adm": "CAIXA ECONOMICA FEDERAL",
        "cnpj_adm": "00.360.305/0001-04",
    },
    "EDFO": {
        "nome": "EDIFÍCIO OUROINVEST",
        "cnpj": "06.175.262/0001-73",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "GESE": {
        "nome": "FII GEN SEV",
        "cnpj": "17.007.528/0001-95",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "OULG": {
        "nome": "FII OURILOG",
        "cnpj": "13.974.819/0001-00",
        "nome_adm": "BANCO OURINVEST S.A.",
        "cnpj_adm": "78.632.767/0001-20",
    },
    "LATR": {
        "nome": "LATERES",
        "cnpj": "17.209.378/0001-00",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "LOFT": {
        "nome": "FII LOFT I",
        "cnpj": "19.722.048/0001-31",
        "nome_adm": "MODAL D.T.V.M. LTDA",
        "cnpj_adm": "05.389.174/0001-01",
    },
    "DRIT": {
        "nome": "MULTIGESTÃO RENDA COMERCIAL",
        "cnpj": "10.456.810/0001-00",
        "nome_adm": (
            "RIO BRAVO INVESTIMENTOS - "
            "DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA"
        ),
        "cnpj_adm": "72.600.026/0001-81",
    },
    "NVIF": {
        "nome": "FII NOVA I",
        "cnpj": "22.003.469/0001-17",
        "nome_adm": "MODAL D.T.V.M. LTDA",
        "cnpj_adm": "05.389.174/0001-01",
    },
    "FTCE": {
        "nome": "OPORTUNITY",
        "cnpj": "01.235.622/0001-61",
        "nome_adm": "BNY MELLON SERVICOS FINANCEIROS DTVM S.A.",
        "cnpj_adm": "02.201.501/0001-61",
    },
    "PRSN": {
        "nome": "LATERES",
        "cnpj": "14.056.001/0001-62",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "FIIP": {
        "nome": "RB CAPITAL RENDA I",
        "cnpj": "08.696.175/0001-97",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "RCRI": {
        "nome": "FII RB CRI",
        "cnpj": "26.511.274/0001-39",
        "nome_adm": "OLIVEIRA TRUST DTVM S.A.",
        "cnpj_adm": "36.113.876/0001-91",
    },
    "FOFT": {
        "nome": "Hedge TOP FOFII 2",
        "cnpj": "16.875.388/0001-04",
        "nome_adm": (
            "HEDGE INVESTMENTS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA."
        ),
        "cnpj_adm": "07.253.654/0001-76",
    },
}


def get_investment_type(code: str) -> str:
    """Checks if code is ETF, FII, STOCKS or NOT_FOUND.

    Args:
        code (str): asset code.

    Returns:
        str: ETF, FII, STOCKS or NOT_FOUND.
    """
    if code in STOCKS:
        return "STOCKS"
    # ETF and FII code can end in 11 or 11B
    if len(code) == 6 and code.endswith("11"):
        code = code[:-2]
    elif len(code) == 7 and code.endswith("11B"):
        code = code[:-3]
    if code in FIIS:
        return "FII"
    if code in ETFS:
        return "ETF"
    return "NOT_FOUND"


def get_trading_rate() -> float:
    """Return fixes trading rate.

    Returns:
        float: constant float.
    """
    return LIQUIDACAO_RATE


def get_emoluments_rates(
    dates: List[datetime.datetime], auction_trades: List[int]
) -> List[float]:
    """Get the list of emuluments rates.

    Args:
        dates (List[datetime.datetime]): list of trade days.
        auction_trades (List[int]): list of indexes of trades in auction.

    Returns:
        List[float]: list of rates.
    """
    rates = []
    last_period = 0
    for date in dates:
        for idx_period, period in enumerate(
            EMOLUMENTOS_PERIODS[last_period:], start=last_period
        ):
            if period.start_date <= date <= period.end_date:
                last_period = idx_period
                rates.append(period.rate)
                break
        else:
            sys.exit(
                "Nenhum período de emolumentos encontrado para a data: {}".format(date)
            )
    for trade in auction_trades:
        rates[trade] = EMOLUMENTOS_AUCTION_RATE
    return rates
