import requests
import re


###### Login Pagina Inicial
payload = {
    'login': 'administrador',
    'senha': 's@udi_v307'
    }

req = requests.Session()
login = req.post('https://voxis.unimedlestefluminense.coop.br/saudi/login', data=payload, verify=False)

# print(login.text)

####### Acesso pagina 1

headers = {}
payload = {}
busca0 = req.post('https://voxis.unimedlestefluminense.coop.br/saudi/relatorioNotasUpload.do?task=buscarTransacoes', data=payload, verify=False)

# print(busca0.text)

pattern = re.compile("SAUDI_CONTROLE_SESSION_ID\" value=(.*)")
busca_sessao = re.search(pattern, busca0.text)
sessao = busca_sessao.group(0).split("\"")[2]
cookie_session = str(req.cookies.values()[0])
print("sessao: {}\nCookie_Session: {}\n\n".format(sessao, cookie_session))
# print(busca0.text)


###### Acesso pagina 2
JSESSIONID = "JSESSIONID=" + cookie_session
REFERER = "https://voxis.unimedlestefluminense.coop.br/saudi/relatorioNotasUpload.do?com.acol.mapasite.ITEM_MENU=9242&com.acol.mapasite.APLICACAO=4071&flgAcessoMenu=true&SAUDI_CONTROLE_SESSION_ID=" + sessao

headers = {
    "Host": "voxis.unimedlestefluminense.coop.br",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": REFERER,
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "314",
    "Cookie": JSESSIONID,
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive",
}


payload = {
    "anoCompetencia":"",
    "cboModalidade":"",
    "cboPrestador":"",
    "cboSaida":"HTML",
    "com.acol.mapasite.ITEM_MENU":"9242",
    "dataUploadAte.ano":"2018",
    "dataUploadAte.dia":"27",
    "dataUploadAte.mes":"09",
    "dataUploadDe.ano":"2018",
    "dataUploadDe.dia":"01",
    "dataUploadDe.mes":"09",
    "forward":"",
    "mesCompetencia":"",
    "rdRelatorioPorDia":"NAO",
    "SAUDI_CONTROLE_SESSION_ID":sessao,
    "task":"",
            }


busca1 = req.post('https://voxis.unimedlestefluminense.coop.br/saudi/relatorioNotasUpload.do?task=buscarTransacoes', data=payload, headers=headers, cookies={"JSESSIONID":cookie_session }, verify=False)

print(busca1.text)
# print(busca1.headers)
#print(busca1.cookies.)
print("Status Code: {}".format(busca1.status_code))
