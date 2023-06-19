import paho.mqtt.client as mqtt


broker_address = "192.168.0.101"
broker_port = 1883
username = "TCC-Gabriel"
senha = "tccgabriel"
client = mqtt.Client()

def on_message(client, userdata, msg):
    #print("Nova mensagem recebida no tópico '{msg.topic}': {msg.payload}")
    global ultima_mensagem
    ultima_mensagem = msg.payload.decode()

def dadosMQTT(topico):
    global ultima_mensagem
    ultima_mensagem = None 
    client.on_message = on_message
    client.username_pw_set(username, senha)
    client.connect(broker_address, broker_port, 60)
    client.subscribe(topico, qos=0) 
    
    client.loop_start()

    while ultima_mensagem is None:
        pass  # Aguarda até que a última mensagem seja recebida

    client.loop_stop()
    client.disconnect()

    return ultima_mensagem