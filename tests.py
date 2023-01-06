import configparser
conf_writer = configparser.ConfigParser()
conf_writer['ppe'] ={
    'jacket': True,
    'helmate': True,
    'shou': True,
    'belt': True,
    'mask': False
}
conf_writer['tresh']={}
conf_writer['tresh']['gb']='dvgdsv'

with open('config.ini','w') as confile:
    conf_writer.write(confile)
