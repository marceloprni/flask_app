from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

db = SQLAlchemy(app)

class Expedicao(db.Model):
    __tablename__= 'expedicao'
    
    #CABEÇARIO
    id = db.Column(db.Integer, primary_key=True)
    osexpedicao  = db.Column(db.String(150), nullable=False)
    opexdicao = db.Column(db.String(150))
    modeloexpedicao = db.Column(db.String(150))
    dataexpedicao = db.Column(db.String(150))
    serieexpedicao = db.Column(db.String(150))
    conversortorqueexpedicao = db.Column(db.String(3))

    #BODY DA PAGINA
    porcaconveror = db.Column(db.String(3))
    chapainercia = db.Column(db.String(3))
    sensorrotacaoentrada = db.Column(db.String(3))
    sensorrotacaosaida = db.Column(db.String(3))
    sensorrotacaotampa = db.Column(db.String(3))
    sensorpressao = db.Column(db.String(3))
    sensorpressaoquebrado = db.Column(db.String(3))
    reguladorfluxo = db.Column(db.String(3))
    reguladorquebrado = db.Column(db.String(3))
    trocadorcalor = db.Column(db.String(3))
    trocadorcaloramassado = db.Column(db.String(3))
    sensorvelocimetro = db.Column(db.String(3))
    sensorvelocimetroquebrado = db.Column(db.String(3))
    sensorvelocimetrotampa = db.Column(db.String(3))
    chaveseletora = db.Column(db.String(3))
    chaveseletoraquebrado = db.Column(db.String(3))
    sensorrotacaomotor = db.Column(db.String(3))
    sensorrotacaomotorquebrado = db.Column(db.String(3))
    tubovaretaoleo = db.Column(db.String(3))
    caixatransferencia = db.Column(db.String(3))
    mangueirastubos = db.Column(db.String(3))
    sensoresexternos = db.Column(db.String(3))
    alavancaseletora = db.Column(db.String(3))
    caixaconectores = db.Column(db.String(3))
    caixaconectoresquebrados = db.Column(db.String(3))
    suporteconectores = db.Column(db.String(3))
    respiro = db.Column(db.String(3))
    bujaonivel = db.Column(db.String(3))
    suportecaboseletor = db.Column(db.String(3))
    guiadacarcaca = db.Column(db.String(3))
    guiaquantidade = db.Column(db.String(3))
    prisioneirocarcaca = db.Column(db.String(3))
    suportecoximinferior = db.Column(db.String(3))
    suportelevantamento = db.Column(db.String(3))
    varetaoleo = db.Column(db.String(3))
    coxins = db.Column(db.String(3))
    chicoteexternos = db.Column(db.String(150))
    eixossaida = db.Column(db.String(150))
    # RODA PÉ
    observacaoexpedicao = db.Column(db.String(1000))
    expedicao_image = db.Column(db.LargeBinary)
    expedicao_name = db.Column(db.String(1000))
    expedicao_mimetype = db.Column(db.Text)

    def __init__(self, osexpedicao, opexdicao, modeloexpedicao, dataexpedicao, serieexpedicao, conversortorqueexpedicao, porcaconveror, chapainercia, sensorrotacaoentrada, sensorrotacaosaida, sensorrotacaotampa, sensorpressao, sensorpressaoquebrado, reguladorfluxo, reguladorquebrado, trocadorcalor, trocadorcaloramassado, sensorvelocimetro, sensorvelocimetroquebrado, sensorvelocimetrotampa, chaveseletora, chaveseletoraquebrado, sensorrotacaomotor, sensorrotacaomotorquebrado, tubovaretaoleo, caixatransferencia, mangueirastubos, sensoresexternos, alavancaseletora, caixaconectores, caixaconectoresquebrados, suporteconectores, respiro, bujaonivel, suportecaboseletor, guiadacarcaca, guiaquantidade, prisioneirocarcaca, suportecoximinferior, suportelevantamento, varetaoleo, coxins, chicoteexternos, eixossaida, observacaoexpedicao, expedicao_image,expedicao_name,expedicao_mimetype):
        self.osexpedicao = osexpedicao
        self.opexdicao = opexdicao
        self.modeloexpedicao = modeloexpedicao
        self.dataexpedicao = dataexpedicao
        self.serieexpedicao = serieexpedicao
        self.conversortorqueexpedicao = conversortorqueexpedicao
        self.porcaconveror = porcaconveror
        self.chapainercia = chapainercia
        self.sensorrotacaoentrada = sensorrotacaoentrada
        self.sensorrotacaosaida =  sensorrotacaosaida
        self.sensorrotacaotampa = sensorrotacaotampa
        self.sensorpressao = sensorpressao	
        self.sensorpressaoquebrado = sensorpressaoquebrado
        self.reguladorfluxo = reguladorfluxo
        self.reguladorquebrado = reguladorquebrado
        self.trocadorcalor = trocadorcalor
        self.trocadorcaloramassado = trocadorcaloramassado 
        self.sensorvelocimetro = sensorvelocimetro
        self.sensorvelocimetroquebrado = sensorvelocimetroquebrado
        self.sensorvelocimetrotampa = sensorvelocimetrotampa
        self.chaveseletora = chaveseletora	
        self.chaveseletoraquebrado = chaveseletoraquebrado
        self.sensorrotacaomotor = sensorrotacaomotor
        self.sensorrotacaomotorquebrado = sensorrotacaomotorquebrado
        self.tubovaretaoleo = tubovaretaoleo	
        self.caixatransferencia = caixatransferencia
        self.mangueirastubos = mangueirastubos
        self.sensoresexternos = sensoresexternos
        self.alavancaseletora = alavancaseletora
        self.caixaconectores = caixaconectores	
        self.caixaconectoresquebrados = caixaconectoresquebrados
        self.suporteconectores = suporteconectores
        self.respiro = respiro	
        self.bujaonivel = bujaonivel
        self.suportecaboseletor = suportecaboseletor
        self.guiadacarcaca = guiadacarcaca
        self.guiaquantidade = guiaquantidade	
        self.prisioneirocarcaca = prisioneirocarcaca
        self.suportecoximinferior = suportecoximinferior
        self.suportelevantamento = suportelevantamento
        self.varetaoleo = varetaoleo
        self.coxins = coxins	
        self.chicoteexternos = chicoteexternos	
        self.eixossaida = eixossaida
        #rodape
        self.observacaoexpedicao = observacaoexpedicao
        self.expedicao_image = expedicao_image
        self.expedicao_name = expedicao_name
        self.expedicao_mimetype = expedicao_mimetype
        
    def __repr__(self):
        return '<Expedicao %r>' % self.id


class Desmontagem(db.Model):
    __tablename__= 'desmontagem'

    #Cabeçario
    id_desmontagem = db.Column(db.Integer,primary_key=True)
    os_desmontagem = db.Column(db.String(50), nullable=False)
    op_desmontagem = db.Column(db.String(50))
    modelo_desmontagem = db.Column(db.String(50))
    data_desmontagem = db.Column(db.String(50))
    serie_desmontagem = db.Column(db.String(50))
    conver_torque_desmontagem = db.Column(db.String(50))

    #Corpo 
    vazamento_conversor_desmontagem = db.Column(db.String(3)) 
    vazamento_carter_desmontagem =  db.Column(db.String(3))
    vazamento_entre_carcacas_desmontagem = db.Column(db.String(3))
    vazamento_saida_desmontagem = db.Column(db.String(3))
    vazamento_obs_desmontagem = db.Column(db.String(200))
    oleo_limpo_desmontagem = db.Column(db.String(3))
    oleo_queimado_desmontagem = db.Column(db.String(3))
    oleo_contaminado_desmontagem = db.Column(db.String(3))
    oleo_obs_desmontagem = db.Column(db.String(200))
    ced_disco_aco_desmontagem = db.Column(db.String(3))
    ced_disco_revestido_desmontagem = db.Column(db.String(3))
    ced_gasto_desmontagem = db.Column(db.String(3))
    ced_obs_desmontagem = db.Column(db.String(200))
    pistoes_rasgado_desmontagem = db.Column(db.String(3))
    pistoes_gasto_desmontagem = db.Column(db.String(3))
    pistoes_obs_desmontagem = db.Column(db.String(200))
    bdo_engregaem_quebrada_desmontagem = db.Column(db.String(3))
    bdo_desgaste_desmontagem = db.Column(db.String(3))
    bdo_bucha_rol_desmontagem = db.Column(db.String(3))
    bdo_obs_desmontagem = db.Column(db.String(200))
    planetario_dentes_quebrado_desmontagem = db.Column(db.String(3)) 
    planetario_fundida_desmontagem = db.Column(db.String(3))
    planetario_obs_desmontagem = db.Column(db.String(200))
    rolamento_danificado_desmontagem = db.Column(db.String(3))
    rolamento_danificado_quebrado = db.Column(db.String(3))
    rolamento_obs_desmontagem = db.Column(db.String(200))
    carter_amassado_desmontagem = db.Column(db.String(3))
    carter_quebrado_desmontagem = db.Column(db.String(3))
    carter_obs_desmontagem = db.Column(db.String(200))
    carcaca_dan_capa_seca_desmontagem = db.Column(db.String(3))
    carcaca_dan_principal_desmontagem = db.Column(db.String(3))
    carcaca_dan_tampa_desmontagem = db.Column(db.String(3))
    carcarca_dan_obs_desmontagem = db.Column(db.String(200))
    cinta_freio_queimada_desmontagem = db.Column(db.String(3)) 
    cinta_freio_quebrada_desmontagem = db.Column(db.String(3))
    cinta_freio_gasta_desmontagem = db.Column(db.String(3))
    cinta_freio_obs_desmontagem = db.Column(db.String(200))
    tambores_queimada_desmontagem = db.Column(db.String(3)) 
    tambores_quebrados_desmontagem = db.Column(db.String(3))
    tambores_gasta_desmontagem = db.Column(db.String(3))
    tambores_obs_desmontagem = db.Column(db.String(200))
    eixos_estrias_danificada_desmontagem = db.Column(db.String(3)) 
    eixos_ponta_danificada_desmontagem = db.Column(db.String(3))
    eixos_estrias_gasta_desmontagem = db.Column(db.String(3))
    eixos_sup_vedacao_danif_desmontagem = db.Column(db.String(3))
    eixos_obs_desmontagem = db.Column(db.String(200))
    coroa_danificado_desmontagem = db.Column(db.String(3))
    coroa_obs_desmontagem = db.Column(db.String(200))
    filtro_quebrado_desmontagem = db.Column(db.String(3))
    filtro_amassado_desmontagem = db.Column(db.String(3))
    filtro_obs_desmontagem = db.Column(db.String(200))
    obser_obs_desmontagem = db.Column(db.String(3000))
    selecionar_image = db.Column(db.LargeBinary)
    selecionar_name_desmontagem = db.Column(db.String(1000))
    selecionar_foto_desmontagem = db.Column(db.Text)

    def __init__(self, os_desmontagem, op_desmontagem, modelo_desmontagem, data_desmontagem, serie_desmontagem, conver_torque_desmontagem, vazamento_conversor_desmontagem, vazamento_carter_desmontagem, vazamento_entre_carcacas_desmontagem, vazamento_saida_desmontagem, vazamento_obs_desmontagem, oleo_limpo_desmontagem, oleo_queimado_desmontagem, oleo_contaminado_desmontagem, oleo_obs_desmontagem, ced_disco_aco_desmontagem, ced_disco_revestido_desmontagem, ced_gasto_desmontagem, ced_obs_desmontagem, pistoes_rasgado_desmontagem, pistoes_gasto_desmontagem, pistoes_obs_desmontagem, bdo_engregaem_quebrada_desmontagem, bdo_desgaste_desmontagem, bdo_bucha_rol_desmontagem, bdo_obs_desmontagem, planetario_dentes_quebrado_desmontagem, planetario_fundida_desmontagem, planetario_obs_desmontagem, rolamento_danificado_desmontagem, rolamento_danificado_quebrado, rolamento_obs_desmontagem, carter_amassado_desmontagem, carter_quebrado_desmontagem, carter_obs_desmontagem, carcaca_dan_capa_seca_desmontagem, carcaca_dan_principal_desmontagem, carcaca_dan_tampa_desmontagem, carcarca_dan_obs_desmontagem, cinta_freio_queimada_desmontagem, cinta_freio_quebrada_desmontagem, cinta_freio_gasta_desmontagem, cinta_freio_obs_desmontagem, tambores_queimada_desmontagem, tambores_quebrados_desmontagem, tambores_gasta_desmontagem, tambores_obs_desmontagem, eixos_estrias_danificada_desmontagem, eixos_ponta_danificada_desmontagem, eixos_estrias_gasta_desmontagem, eixos_sup_vedacao_danif_desmontagem, eixos_obs_desmontagem, coroa_danificado_desmontagem, coroa_obs_desmontagem, filtro_quebrado_desmontagem, filtro_amassado_desmontagem, filtro_obs_desmontagem, obser_obs_desmontagem, selecionar_image, selecionar_name_desmontagem, selecionar_foto_desmontagem):
        self.os_desmontagem = os_desmontagem  
        self.op_desmontagem = op_desmontagem   
        self.modelo_desmontagem = modelo_desmontagem 
        self.data_desmontagem = data_desmontagem
        self.serie_desmontagem = serie_desmontagem 
        self.conver_torque_desmontagem = conver_torque_desmontagem
        self.vazamento_conversor_desmontagem = vazamento_conversor_desmontagem
        self.vazamento_carter_desmontagem = vazamento_carter_desmontagem 
        self.vazamento_entre_carcacas_desmontagem = vazamento_entre_carcacas_desmontagem 
        self.vazamento_saida_desmontagem = vazamento_saida_desmontagem
        self.vazamento_obs_desmontagem = vazamento_obs_desmontagem
        self.oleo_limpo_desmontagem = oleo_limpo_desmontagem
        self.oleo_queimado_desmontagem = oleo_queimado_desmontagem
        self.oleo_contaminado_desmontagem = oleo_contaminado_desmontagem
        self.oleo_obs_desmontagem = oleo_obs_desmontagem 
        self.ced_disco_aco_desmontagem = ced_disco_aco_desmontagem
        self.ced_disco_revestido_desmontagem = ced_disco_revestido_desmontagem
        self.ced_gasto_desmontagem = ced_gasto_desmontagem 
        self.ced_obs_desmontagem = ced_obs_desmontagem
        self.pistoes_rasgado_desmontagem = pistoes_rasgado_desmontagem
        self.pistoes_gasto_desmontagem = pistoes_gasto_desmontagem
        self.pistoes_obs_desmontagem = pistoes_obs_desmontagem
        self.bdo_engregaem_quebrada_desmontagem = bdo_engregaem_quebrada_desmontagem
        self.bdo_desgaste_desmontagem = bdo_desgaste_desmontagem
        self.bdo_bucha_rol_desmontagem = bdo_bucha_rol_desmontagem
        self.bdo_obs_desmontagem = bdo_obs_desmontagem
        self.planetario_dentes_quebrado_desmontagem = planetario_dentes_quebrado_desmontagem
        self.planetario_fundida_desmontagem = planetario_fundida_desmontagem
        self.planetario_obs_desmontagem = planetario_obs_desmontagem
        self.rolamento_danificado_desmontagem = rolamento_danificado_desmontagem 
        self.rolamento_danificado_quebrado = rolamento_danificado_quebrado
        self.rolamento_obs_desmontagem = rolamento_obs_desmontagem
        self.carter_amassado_desmontagem = carter_amassado_desmontagem
        self.carter_quebrado_desmontagem = carter_quebrado_desmontagem 
        self.carter_obs_desmontagem = carter_obs_desmontagem
        self.carcaca_dan_capa_seca_desmontagem = carcaca_dan_capa_seca_desmontagem
        self.carcaca_dan_principal_desmontagem = carcaca_dan_principal_desmontagem
        self.carcaca_dan_tampa_desmontagem = carcaca_dan_tampa_desmontagem
        self.carcarca_dan_obs_desmontagem = carcarca_dan_obs_desmontagem
        self.cinta_freio_queimada_desmontagem = cinta_freio_queimada_desmontagem
        self.cinta_freio_quebrada_desmontagem = cinta_freio_quebrada_desmontagem
        self.cinta_freio_gasta_desmontagem = cinta_freio_gasta_desmontagem 
        self.cinta_freio_obs_desmontagem = cinta_freio_obs_desmontagem
        self.tambores_queimada_desmontagem = tambores_queimada_desmontagem
        self.tambores_quebrados_desmontagem = tambores_quebrados_desmontagem
        self.tambores_gasta_desmontagem = tambores_gasta_desmontagem
        self.tambores_obs_desmontagem = tambores_obs_desmontagem
        self.eixos_estrias_danificada_desmontagem = eixos_estrias_danificada_desmontagem 
        self.eixos_ponta_danificada_desmontagem = eixos_ponta_danificada_desmontagem
        self.eixos_estrias_gasta_desmontagem = eixos_estrias_gasta_desmontagem
        self.eixos_sup_vedacao_danif_desmontagem = eixos_sup_vedacao_danif_desmontagem
        self.eixos_obs_desmontagem = eixos_obs_desmontagem 
        self.coroa_danificado_desmontagem = coroa_danificado_desmontagem
        self.coroa_obs_desmontagem = coroa_obs_desmontagem 
        self.filtro_quebrado_desmontagem = filtro_quebrado_desmontagem
        self.filtro_amassado_desmontagem = filtro_amassado_desmontagem
        self.filtro_obs_desmontagem = filtro_obs_desmontagem
        self.obser_obs_desmontagem = obser_obs_desmontagem
        self.selecionar_image = selecionar_image
        self.selecionar_name_desmontagem = selecionar_name_desmontagem
        self.selecionar_foto_desmontagem = selecionar_foto_desmontagem

    def __repr__(self):
        return '<Desmontagem %r>' % self.id_desmontagem


class Inspecao1(db.Model):
    
    __tablename__ = 'inspecao1'

    id_insp = db.Column(db.Integer, primary_key=True)
    os_insp = db.Column(db.String(50), nullable=False)
    op_insp = db.Column(db.String(50))
    modelo_insp = db.Column(db.String(50))
    conversor_insp = db.Column(db.String(50))
    data_insp = db.Column(db.String(50))
    serie_insp = db.Column(db.String(50))
    nome_insp = db.Column(db.String(100))

    carc_p_trincas = db.Column(db.String(3))
    carc_p_rolamentos = db.Column(db.String(3))
    carc_p_alojamento = db.Column(db.String(3))
    carc_p_alojamento_ac = db.Column(db.String(3))
    carc_p_alojamento_rts = db.Column(db.String(3))
    carc_p_fhpcf2f3 = db.Column(db.String(3))
    carc_p_capa_rolam = db.Column(db.String(3))
    carc_p_guias = db.Column(db.String(3))
    carc_p_superficies_vedacao = db.Column(db.String(3))

    bomb_sce = db.Column(db.String(3))
    bomb_guias = db.Column(db.String(3))
    bomb_riscos = db.Column(db.String(3))
    bomb_desgaste_b = db.Column(db.String(1000))
    bomb_dcb = db.Column(db.String(3))
    bomb_demm = db.Column(db.String(3))
    bomb_elaem = db.Column(db.String(3))
    bomb_desgaste = db.Column(db.String(1000))
    bomb_desgaste_eixo = db.Column(db.String(1000))

    tamb_descoloracao = db.Column(db.String(3))
    tamb_scf = db.Column(db.String(3))
    tamb_scb = db.Column(db.String(3))
    tamb_cav = db.Column(db.String(3))
    tamb_estrias = db.Column(db.String(3))
    tamb_desgaste = db.Column(db.String(1000))

    tamb2_descoloracao = db.Column(db.String(3)) 
    tamb2_scf = db.Column(db.String(3))
    tamb2_d_quebrados = db.Column(db.String(3))
    tamb2_rad = db.Column(db.String(3))
    tamb2_estrias = db.Column(db.String(3)) 

    dife_trincas = db.Column(db.String(3))
    dife_rolamento = db.Column(db.String(3))
    dife_sca = db.Column(db.String(3)) 
    dife_estrias = db.Column(db.String(3))
    dife_daep = db.Column(db.String(3))
    dife_des = db.Column(db.String(3))
    dife_dcr = db.Column(db.String(3))
    dife_ds = db.Column(db.String(3))

    suportem_derretimento = db.Column(db.String(3))
    suportem_deformação = db.Column(db.String(3))
    surpotem_empenamento = db.Column(db.String(3))

    hast_dhp = db.Column(db.String(3)) 
    hast_tma = db.Column(db.String(3))
    hast_oxidacao = db.Column(db.String(3))

    disc_queima = db.Column(db.String(3))
    disc_desg = db.Column(db.String(3))
    disc_empen = db.Column(db.String(3))
    disc_deform = db.Column(db.String(3))

    pistao_tq = db.Column(db.String(3))
    pistao_desgaste = db.Column(db.String(3))
    pistao_cas = db.Column(db.String(3))
    pistao_em = db.Column(db.String(3))

    caixa_c_quebras = db.Column(db.String(3))
    caixa_c_trincas = db.Column(db.String(3))
    caixa_c_ft = db.Column(db.String(3))

    sensor_derretimento = db.Column(db.String(3))
    sensor_estado_cabo = db.Column(db.String(3))
    sensor_e_conector = db.Column(db.String(3))

    sensor_p_trincas = db.Column(db.String(3))
    sensor_p_presencao = db.Column(db.String(3))
    sensor_p_estado = db.Column(db.String(3))
    sensor_p_estado_conector = db.Column(db.String(3))

    chapa_empenamento = db.Column(db.String(3)) 
    chapa_amassados = db.Column(db.String(3))
    chapa_oxidacao = db.Column(db.String(3))

    capa_trincas = db.Column(db.String(3)) 
    capa_rosca = db.Column(db.String(3)) 
    capa_rolamentos = db.Column(db.String(3)) 
    capa_abo = db.Column(db.String(3)) 
    capa_ars = db.Column(db.String(3)) 
    capa_sv = db.Column(db.String(3)) 

    tampa_tq = db.Column(db.String(3))
    tampa_rosca = db.Column(db.String(3))
    tampa_apf1 = db.Column(db.String(3))
    tampa_svj = db.Column(db.String(3))
    tampa_scb = db.Column(db.String(3))
    tampa_aneis = db.Column(db.String(3))

    placa_trincas = db.Column(db.String(3))
    placa_roscas = db.Column(db.String(3))
    placa_riscos = db.Column(db.String(3))
    placa_desgaste = db.Column(db.String(1000))

    cubo_scbs = db.Column(db.String(3))
    cubo_estrias = db.Column(db.String(3))
    cubo_ram = db.Column(db.String(3))
    cubo_dba = db.Column(db.String(1000))

    conjunto_descolo = db.Column(db.String(3))
    conjunto_dentes = db.Column(db.String(3))
    conjunto_roscas = db.Column(db.String(3))
    conjunto_sccr = db.Column(db.String(3))
    conjunto_dr = db.Column(db.String(3))
    conjunto_oxidacao = db.Column(db.String(3))
    conjunto_desgaste = db.Column(db.String(1000))

    tambor_descoloracao = db.Column(db.String(3))
    tambor_entalhe = db.Column(db.String(3))
    tambor_estrias = db.Column(db.String(3))
    tambor_alojamento = db.Column(db.String(3))
    tambor_sat = db.Column(db.String(3))

    pinhao_rolamentos = db.Column(db.String(3))
    pinhao_gr = db.Column(db.String(3))
    pinhao_ram = db.Column(db.String(3))

    emgrenagem_descoloracao = db.Column(db.String(3)) 
    emgrenagem_estrias = db.Column(db.String(3)) 
    emgrenagem_dq = db.Column(db.String(3)) 

    suporte_e_descoloracao = db.Column(db.String(3))
    suporte_e_eede = db.Column(db.String(3))
    suporte_e_dq = db.Column(db.String(3))

    cinta_f_ef = db.Column(db.String(3))
    cinta_f_craf = db.Column(db.String(3))
    cinta_f_queima = db.Column(db.String(3))
    cinta_f_deformacao = db.Column(db.String(3))
    cinta_f_ancoragem = db.Column(db.String(3))

    rolamento_dcp = db.Column(db.String(3))
    rolamento_qpr = db.Column(db.String(3))

    control_trincas = db.Column(db.String(3))
    control_estados = db.Column(db.String(3))
    control_estado = db.Column(db.String(3))

    respiro_rasgos = db.Column(db.String(3))
    respiro_presenca = db.Column(db.String(3))
    respiro_deformacao = db.Column(db.String(3))

    chave_sc_quebras = db.Column(db.String(3))
    chave_sc_vdfd = db.Column(db.String(3))
    chave_sc_ec = db.Column(db.String(3))
    chave_sc_ect = db.Column(db.String(3))
    chave_sc_etpa = db.Column(db.String(3))

    compon_ps2 = db.Column(db.String(3000))
    compon_eixoin = db.Column(db.String(3000))
    compon_bomba5 = db.Column(db.String(3000))
    compon_bomb2 = db.Column(db.String(3000))
    compon_bomb23 = db.Column(db.String(3000))

    compon_n1 = db.Column(db.String(3000))
    compon_n2 = db.Column(db.String(3000))
    compon_f3n1 = db.Column(db.String(3000))
    compon_f3n2 = db.Column(db.String(3000))

    compon_e1 = db.Column(db.String(3000))
    compon_vist_montador1 = db.Column(db.String(3000))
    compon_e2 = db.Column(db.String(3000))
    compon_visit_montador2 = db.Column(db.String(3000))
    compon_eixo_axial = db.Column(db.String(3000))
    compon_visit_montador3 = db.Column(db.String(3000))

    def __init__(self, os_insp, op_insp, modelo_insp, conversor_insp, data_insp, serie_insp, nome_insp, carc_p_trincas, carc_p_rolamentos, carc_p_alojamento, carc_p_alojamento_ac, carc_p_alojamento_rts, carc_p_fhpcf2f3, carc_p_capa_rolam, carc_p_guias, carc_p_superficies_vedacao, bomb_sce, bomb_guias, bomb_riscos, bomb_desgaste_b, bomb_dcb, bomb_demm, bomb_elaem, bomb_desgaste, bomb_desgaste_eixo, tamb_descoloracao, tamb_scf, tamb_scb, tamb_cav, tamb_estrias, tamb_desgaste, tamb2_descoloracao, tamb2_scf, tamb2_d_quebrados, tamb2_rad, tamb2_estrias, dife_trincas, dife_rolamento, dife_sca, dife_estrias, dife_daep, dife_des, dife_dcr, dife_ds, suportem_derretimento, suportem_deformação, surpotem_empenamento, hast_dhp, hast_tma, hast_oxidacao, disc_queima, disc_desg, disc_empen, disc_deform, pistao_tq, pistao_desgaste, pistao_cas, pistao_em, caixa_c_quebras, caixa_c_trincas, caixa_c_ft, sensor_derretimento, sensor_estado_cabo, sensor_e_conector, sensor_p_trincas, sensor_p_presencao, sensor_p_estado, sensor_p_estado_conector, chapa_empenamento, chapa_amassados, chapa_oxidacao, capa_trincas, capa_rosca, capa_rolamentos, capa_abo, capa_ars, capa_sv, tampa_tq, tampa_rosca, tampa_apf1, tampa_svj, tampa_scb, tampa_aneis, placa_trincas, placa_roscas, placa_riscos, placa_desgaste, cubo_scbs, cubo_estrias, cubo_ram, cubo_dba, conjunto_descolo, conjunto_dentes, conjunto_roscas, conjunto_sccr, conjunto_dr, conjunto_oxidacao, conjunto_desgaste, tambor_descoloracao, tambor_entalhe, tambor_estrias, tambor_alojamento, tambor_sat, pinhao_rolamentos, pinhao_gr, pinhao_ram, emgrenagem_descoloracao, emgrenagem_estrias, emgrenagem_dq, suporte_e_descoloracao, suporte_e_eede, suporte_e_dq, cinta_f_ef, cinta_f_craf, cinta_f_queima, cinta_f_deformacao, cinta_f_ancoragem, rolamento_dcp, rolamento_qpr, control_trincas, control_estados, control_estado, respiro_rasgos, respiro_presenca, respiro_deformacao, chave_sc_quebras, chave_sc_vdfd, chave_sc_ec, chave_sc_ect, chave_sc_etpa, compon_ps2, compon_eixoin, compon_bomba5, compon_bomb2, compon_bomb23, compon_n1, compon_n2, compon_f3n1, compon_f3n2, compon_e1, compon_vist_montador1, compon_e2, compon_visit_montador2, compon_eixo_axial, compon_visit_montador3):

        self.os_insp = os_insp
        self.op_insp = op_insp
        self.modelo_insp = modelo_insp
        self.conversor_insp = conversor_insp
        self.data_insp = data_insp
        self.serie_insp = serie_insp
        self.nome_insp = nome_insp

        self.carc_p_trincas = carc_p_trincas
        self.carc_p_rolamentos = carc_p_rolamentos
        self.carc_p_alojamento = carc_p_alojamento
        self.carc_p_alojamento_ac = carc_p_alojamento_ac
        self.carc_p_alojamento_rts = carc_p_alojamento_rts
        self.carc_p_fhpcf2f3 = carc_p_fhpcf2f3
        self.carc_p_capa_rolam = carc_p_capa_rolam
        self.carc_p_guias = carc_p_guias
        self.carc_p_superficies_vedacao = carc_p_superficies_vedacao

        self.bomb_sce = bomb_sce
        self.bomb_guias = bomb_guias
        self.bomb_riscos = bomb_riscos
        self.bomb_desgaste_b = bomb_desgaste_b
        self.bomb_dcb = bomb_dcb
        self.bomb_demm = bomb_demm
        self.bomb_elaem = bomb_elaem
        self.bomb_desgaste = bomb_desgaste
        self.bomb_desgaste_eixo = bomb_desgaste_eixo

        self.tamb_descoloracao = tamb_descoloracao
        self.tamb_scf = tamb_scf
        self.tamb_scb = tamb_scb
        self.tamb_cav = tamb_cav
        self.tamb_estrias = tamb_estrias
        self.tamb_desgaste = tamb_desgaste

        self.tamb2_descoloracao = tamb2_descoloracao
        self.tamb2_scf = tamb2_scf
        self.tamb2_d_quebrados = tamb2_d_quebrados
        self.tamb2_rad = tamb2_rad
        self.tamb2_estrias = tamb2_estrias

        self.dife_trincas = dife_trincas
        self.dife_rolamento = dife_rolamento
        self.dife_sca = dife_sca
        self.dife_estrias = dife_estrias
        self.dife_daep = dife_daep
        self.dife_des = dife_des
        self.dife_dcr = dife_dcr
        self.dife_ds = dife_ds

        self.suportem_derretimento = suportem_derretimento 
        self.suportem_deformação = suportem_deformação
        self.surpotem_empenamento = surpotem_empenamento

        self.hast_dhp = hast_dhp
        self.hast_tma = hast_tma
        self.hast_oxidacao = hast_oxidacao

        self.disc_queima = disc_queima
        self.disc_desg = disc_desg
        self.disc_empen = disc_empen
        self.disc_deform = disc_deform

        self.pistao_tq = pistao_tq
        self.pistao_desgaste = pistao_desgaste
        self.pistao_cas = pistao_cas 
        self.pistao_em = pistao_em 

        self.caixa_c_quebras = caixa_c_quebras
        self.caixa_c_trincas = caixa_c_trincas 
        self.caixa_c_ft = caixa_c_ft

        self.sensor_derretimento = sensor_derretimento
        self.sensor_estado_cabo = sensor_estado_cabo
        self.sensor_e_conector = sensor_e_conector

        self.sensor_p_trincas = sensor_p_trincas
        self.sensor_p_presencao = sensor_p_presencao
        self.sensor_p_estado = sensor_p_estado
        self.sensor_p_estado_conector = sensor_p_estado_conector

        self.chapa_empenamento = chapa_empenamento
        self.chapa_amassados = chapa_amassados
        self.chapa_oxidacao = chapa_oxidacao 

        self.capa_trincas = capa_trincas
        self.capa_rosca = capa_rosca
        self.capa_rolamentos = capa_rolamentos
        self.capa_abo = capa_abo
        self.capa_ars = capa_ars
        self.capa_sv = capa_sv

        self.tampa_tq = tampa_tq
        self.tampa_rosca = tampa_rosca
        self.tampa_apf1 = tampa_apf1
        self.tampa_svj = tampa_svj
        self.tampa_scb = tampa_scb
        self.tampa_aneis = tampa_aneis

        self.placa_trincas = placa_trincas
        self.placa_roscas = placa_roscas
        self.placa_riscos = placa_riscos
        self.placa_desgaste = placa_desgaste

        self.cubo_scbs = cubo_scbs
        self.cubo_estrias = cubo_estrias
        self.cubo_ram = cubo_ram
        self.cubo_dba = cubo_dba

        self.conjunto_descolo = conjunto_descolo 
        self.conjunto_dentes = conjunto_dentes
        self.conjunto_roscas = conjunto_roscas 
        self.conjunto_sccr = conjunto_sccr
        self.conjunto_dr = conjunto_dr
        self.conjunto_oxidacao = conjunto_oxidacao
        self.conjunto_desgaste = conjunto_desgaste

        self.tambor_descoloracao = tambor_descoloracao
        self.tambor_entalhe = tambor_entalhe
        self.tambor_estrias = tambor_estrias
        self.tambor_alojamento = tambor_alojamento
        self.tambor_sat = tambor_sat

        self.pinhao_rolamentos = pinhao_rolamentos
        self.pinhao_gr = pinhao_gr 
        self.pinhao_ram = pinhao_ram

        self.emgrenagem_descoloracao = emgrenagem_descoloracao
        self.emgrenagem_estrias = emgrenagem_estrias 
        self.emgrenagem_dq = emgrenagem_dq

        self.suporte_e_descoloracao = suporte_e_descoloracao
        self.suporte_e_eede = suporte_e_eede
        self.suporte_e_dq = suporte_e_dq

        self.cinta_f_ef = cinta_f_ef
        self.cinta_f_craf = cinta_f_craf
        self.cinta_f_queima = cinta_f_queima
        self.cinta_f_deformacao = cinta_f_deformacao
        self.cinta_f_ancoragem = cinta_f_ancoragem

        self.rolamento_dcp = rolamento_dcp
        self.rolamento_qpr = rolamento_qpr

        self.control_trincas = control_trincas
        self.control_estados = control_estados
        self.control_estado = control_estado

        self.respiro_rasgos = respiro_rasgos
        self.respiro_presenca = respiro_presenca
        self.respiro_deformacao = respiro_deformacao

        self.chave_sc_quebras = chave_sc_quebras
        self.chave_sc_vdfd = chave_sc_vdfd
        self.chave_sc_ec = chave_sc_ec 
        self.chave_sc_ect = chave_sc_ect
        self.chave_sc_etpa = chave_sc_etpa

        self.compon_ps2 = compon_ps2
        self.compon_eixoin = compon_eixoin
        self.compon_bomba5 = compon_bomba5
        self.compon_bomb2 = compon_bomb2
        self.compon_bomb23 = compon_bomb23

        self.compon_n1 = compon_n1
        self.compon_n2 = compon_n2
        self.compon_f3n1 = compon_f3n1
        self.compon_f3n2 = compon_f3n2

        self.compon_e1 = compon_e1
        self.compon_vist_montador1 = compon_vist_montador1
        self.compon_e2 = compon_e2
        self.compon_visit_montador2 = compon_visit_montador2
        self.compon_eixo_axial = compon_eixo_axial 
        self.compon_visit_montador3 = compon_visit_montador3 

    def __repr__(self):
        return '<Inspecao1 %r>' % self.id_insp


class Inspecao(db.Model):
	
    __tablename__ = 'inspecao'
    
    inspecao_id = db.Column(db.Integer,primary_key=True)
    inspecao_ordem = db.Column(db.String(50),nullable=False)
    inspecao_op = db.Column(db.String(50))
    inspecao_modelo = db.Column(db.String(50))
    inspecao_conversor_torque = db.Column(db.String(50))
    inspecao_data = db.Column(db.String(50))
    inspecao_serie = db.Column(db.String(50))
    inspecao_nome = db.Column(db.String(50))
    
    #Carcaça Principal
    inspecao_carcaca_trinca_quebras = db.Column(db.String(3))
    inspecao_carcaca_rolamentos = db.Column(db.String(3))
    inspecao_carcaca_alojamento_pistao = db.Column(db.String(3))
    inspecao_carcaca_alojamento_acumuladores = db.Column(db.String(3))
    inspecao_carcaca_alojamento_retentores = db.Column(db.String(3))
    inspecao_carcaca_furo_hastes_pistoes = db.Column(db.String(3))
    inspecao_carcaca_capa_rolamentos = db.Column(db.String(3))
    inspecao_carcaca_guias_carcaca = db.Column(db.String(3))
    inspecao_carcaca_superficies_vedacao = db.Column(db.String(3))

    #Bomba de Óleo
    inspecao_bomb_oleo_superficies_contato_engrenagens = db.Column(db.String(3))
    inspecao_bomb_oleo_guias = db.Column(db.String(3))
    inspecao_bomb_oleo_riscos = db.Column(db.String(3))
    inspecao_bomb_oleo_diametro_bucha = db.Column(db.String(50))
    inspecao_bomb_oleo_desgaste_chapa_bomba = db.Column(db.String(3))
    inspecao_bomb_oleo_desgaste_engrangem_motora = db.Column(db.String(3))
    inspecao_bomb_oleo_estado_lingueta = db.Column(db.String(3))

    #Eixo Entrada
    inspecao_eixo_entrada_superficie_contato = db.Column(db.String(3))
    inspecao_eixo_entrada_estrias = db.Column(db.String(3))
    inspecao_eixo_entrada_alojamento_pistao = db.Column(db.String(3))
    inspecao_eixo_entrada_contato_anel_vedacao = db.Column(db.String(3))
    inspecao_eixo_entrada_diametro_bucha = db.Column(db.String(50))

    #Tambor C1
    inspecao_tambor_c1_descoloracao = db.Column(db.String(3))
    inspecao_tambor_c1_entalhe_encaixe = db.Column(db.String(3))
    insepcao_tambor_c1_estrias = db.Column(db.String(3))
    inspecao_tambor_c1_alojamento_pistao = db.Column(db.String(3))
    inspecao_tambor_c1_sup_apoio_trava = db.Column(db.String(3))

    #Tambor B1
    inspecao_tambor_b1_descoloracao = db.Column(db.String(3))
    inspecao_tambor_b1_entalhe_encaixe = db.Column(db.String(3))
    inspecao_tambor_b1_estrias = db.Column(db.String(3))
    inspecao_tambor_b1_alojamento_pistao = db.Column(db.String(3))
    inspecao_tambor_b1_sup_apoio_trava = db.Column(db.String(3))

    #Conjunto C2
    inspecao_conjunto_c2_descoloracao = db.Column(db.String(3))
    inspecao_conjunto_c2_entalhe_encaixe = db.Column(db.String(3))
    inspecao_conjunto_c2_estrias = db.Column(db.String(3))
    inspecao_conjunto_c2_alojamento_pistao = db.Column(db.String(3))
    inspecao_conjunto_c2_sup_apoio_trava = db.Column(db.String(3))

    #Diferencial 
    inspecao_diferencial_trincas_quebras = db.Column(db.String(3))
    inspecao_diferencial_rolamento = db.Column(db.String(3))
    inspecao_diferencial_superficies_arruelas = db.Column(db.String(3))
    inspecao_diferencial_estrias = db.Column(db.String(3))
    inspecao_diferencial_desgaste_arruela = db.Column(db.String(3))
    inspecao_diferencial_desgaste_eixo = db.Column(db.String(3))
    inspecao_diferencial_desgaste_capa = db.Column(db.String(3))
    inspecao_diferencial_desgaste_satelite = db.Column(db.String(3))

    #Mola de Retorno
    inspecao_mola_retorno_oxidacao = db.Column(db.String(3))
    inspecao_mola_retorno_deformacao = db.Column(db.String(3))
    inspecao_mola_retorno_empenamento = db.Column(db.String(3))

    #Hastes dos Pistões
    inspecao_haste_pistao_desgaste_haste = db.Column(db.String(3))
    inspecao_haste_pistao_componentes = db.Column(db.String(3))
    inspecao_haste_pistao_oxidacao = db.Column(db.String(3))

    #Discos de Embreagem
    inspecao_disco_embreagem_queima = db.Column(db.String(3))
    inspecao_disco_embreagem_desgaste = db.Column(db.String(3))
    inspecao_disco_embreagem_empenamento = db.Column(db.String(3))
    inspecao_disco_embreagem_deformacao = db.Column(db.String(3))

    #Pistão de Acionamento B1
    inspecao_pistao_trinca_quebra = db.Column(db.String(3))
    inspecao_pistao_desgaste = db.Column(db.String(3))
    inspecao_pistao_canais_aneis = db.Column(db.String(3))
    inspecao_pistao_estado_mola = db.Column(db.String(3))

    #Conectores
    inspecao_conectores_quebra = db.Column(db.String(3))
    inspecao_conectores_trincas = db.Column(db.String(3))
    inspecao_conectores_oxidacao = db.Column(db.String(3))

    #Sensor de Rotação de Entrada
    inspecao_sensor_rotacao_derretimento = db.Column(db.String(3))
    inspecao_sensor_rotacao_estado_cabo = db.Column(db.String(3))
    inspecao_sensor_rotacao_estado_conector = db.Column(db.String(3))

    #Sensor de Pressão
    inspecao_sensor_pressao1_trinca_quebra = db.Column(db.String(3))
    inspecao_sensor_pressao1_presenca_esfera = db.Column(db.String(3))
    inspecao_sensor_pressao1_estado_cabo = db.Column(db.String(3))
    inspecao_sensor_pressao1_estado_conector = db.Column(db.String(3))

    #Capa Seca
    inspecao_capa_seca_trinca_quebra = db.Column(db.String(3))
    inspecao_capa_seca_rocas = db.Column(db.String(3))
    inspecao_capa_seca_capa_rolamento = db.Column(db.String(3))
    inspecao_capa_seca_alojamento_bomb_oleo = db.Column(db.String(3))
    inspecao_capa_seca_alojamento_retentores = db.Column(db.String(3))
    inspecao_capa_seca_superficie_vedacao = db.Column(db.String(3))

    #Tampa Traseira
    inspecao_tampa_traseira_trinca_quebra = db.Column(db.String(3))
    inspecao_tampa_traseira_roscas = db.Column(db.String(3))
    inspecao_tampa_traseira_alojamentos = db.Column(db.String(3))
    inspecao_tampa_traseira_superficie_vedacao = db.Column(db.String(3))
    inspecao_tampa_traseira_superficie_contato = db.Column(db.String(3))
    inspecao_tampa_traseira_aneis = db.Column(db.String(3))

    #Placa da Bomba
    inspecao_placa_bomba_trinca_quebra = db.Column(db.String(3))
    inspecao_placa_bomba_roscas = db.Column(db.String(3))
    inspecao_placa_bomba_riscos = db.Column(db.String(3))
    inspecao_placa_bomba_diametro_bucha = db.Column(db.String(3))

    #Cubo da Carcaça
    inspecao_cubo_rolamento = db.Column(db.String(3))
    inspecao_cubo_apoio_anel = db.Column(db.String(3))
    inspecao_cubo_rolamento_axial = db.Column(db.String(3))
    inspecao_cubo_diametro_bucha = db.Column(db.String(3))

    #Conjunto de Planetárias
    inspecao_planetaria_descoloracao = db.Column(db.String(3))
    inspecao_planetaria_dente = db.Column(db.String(3))
    inspecao_planetaria_roscas = db.Column(db.String(3))
    inspecao_planetaria_superficie_contato = db.Column(db.String(3))
    inspecao_planetaria_desgaste_rolamento = db.Column(db.String(3))
    inspecao_planetaria_oxidacao = db.Column(db.String(3))
    inspecao_planetaria_diamentro_bucha = db.Column(db.String(3))

    #Tambor C3
    inspecao_tambor_c3_descoloracao = db.Column(db.String(3))
    inspecao_tambor_c3_entalhe_encaixe = db.Column(db.String(3))
    inspecao_tambor_c3_estrias = db.Column(db.String(3))
    inspecao_tambor_c3_alojamento_pistao = db.Column(db.String(3))
    inspecao_tambor_c3_sup_apoio_trava = db.Column(db.String(3))
    
    #Conjunto B2
    inspecao_conjunto_b2_descoloracao = db.Column(db.String(3))
    inspecao_conjunto_b2_entalhe_encaixe = db.Column(db.String(3))
    inspecao_conjunto_b2_estrias = db.Column(db.String(3))
    inspecao_conjunto_b2_alojamento_pistao = db.Column(db.String(3))
    inspecao_conjunto_b2_sup_apoio_trava = db.Column(db.String(3))

    #Pinhão
    inspecao_pinhao_rolamento = db.Column(db.String(3))
    inspecao_pinhao_gaiola = db.Column(db.String(3))
    inspecao_pinhao_rolamento_axial = db.Column(db.String(3))

    #Engranagem Solar
    inspecao_engrenagem_rolamento = db.Column(db.String(3))
    inspecao_engrenagem_gaiola = db.Column(db.String(3))
    inspecao_engrenagem_rolamento_axial = db.Column(db.String(3))

    #Suporte de Engrenagem Solar
    inspecao_sup_engrenagem_descoloracao = db.Column(db.String(3))
    inspecao_sup_engrenagem_entalhe_encaixe = db.Column(db.String(3))
    inspecao_sup_engrenagem_dente = db.Column(db.String(3))

    #Rolamentos axiais e Calços
    inspecao_rolamentos_axiais_derretimentos = db.Column(db.String(3))
    inspecao_rolamentos_axiais_quebra_pista = db.Column(db.String(3))

    #Trocador de Calor
    inspecao_trocador_trinca_quebra = db.Column(db.String(3))
    inspecao_trocador_furo_interno = db.Column(db.String(3))

    #Respiro
    inspecao_respiro_rasgos = db.Column(db.String(3))
    inspecao_respiro_presenca_tampa = db.Column(db.String(3))
    inspecao_respiro_deformacao = db.Column(db.String(3))

    #Chave Seletora
    inspecao_chave_quebra = db.Column(db.String(3))
    inspecao_chave_estado_conector = db.Column(db.String(3))
    inspecao_chave_estado_terminal = db.Column(db.String(3))

    #Sensor de Pressão
    inspecao_sensor_pressao2_trinca_quebra = db.Column(db.String(3))
    inspecao_sensor_pressao2_presenca_esfera = db.Column(db.String(3))
    inspecao_sensor_pressao2_estado_cabo = db.Column(db.String(3))
    inspecao_sensor_pressao2_estado_conector = db.Column(db.String(3))

    #Chapa Defletora de Óleo do Diferencial
    inspecao_chapa_empenamento = db.Column(db.String(3))
    inspecao_chapa_amassado = db.Column(db.String(3))
    inspecao_chapa_oxidacao = db.Column(db.String(3))

    #Informações Adicionais
    inspecao_c1_observacao = db.Column(db.String(50))
    inspecao_c2_observacao = db.Column(db.String(50))
    inspecao_c3_observacao = db.Column(db.String(50))
    inspecao_b1_observacao = db.Column(db.String(50))
    inspecao_b2_observacao = db.Column(db.String(50))
    inspecao_suporte_observacao = db.Column(db.String(50))
    inspecao_relacao_observacao = db.Column(db.String(50))
    inspecao_bomba_observacao = db.Column(db.String(50))
    inspecao_rolamentos_observacao = db.Column(db.String(50))

    #Ajuste
    inspecao_c1_ajuste = db.Column(db.String(50))
    inspecao_c1_visto = db.Column(db.String(50))
    inspecao_c2_ajuste = db.Column(db.String(50))
    inspecao_c2_visto = db.Column(db.String(50))
    inspecao_c3_ajuste = db.Column(db.String(50))
    inspecao_c3_visto = db.Column(db.String(50))
    inspecao_b1_ajuste = db.Column(db.String(50))
    inspecao_b1_visto = db.Column(db.String(50))
    inspecao_b2_ajuste = db.Column(db.String(50))
    inspecao_b2_visto = db.Column(db.String(50))


    def __init__(self, inspecao_ordem,inspecao_op,inspecao_modelo,inspecao_conversor_toque,inspecao_data,inspecao_serie,inspecao_nome,inspecao_carcaca_trinca_quebras,inspecao_carcaca_rolamentos,inspecao_carcaca_alojamento_pistao,inspecao_carcaca_alojamento_acumuladores,inspecao_carcaca_alojamento_retentores,inspecao_carcaca_furo_hastes_pistoes,inspecao_carcaca_capa_rolamentos,inspecao_carcaca_guias_carcaca,inspecao_carcaca_superficies_vedacao,inspecao_bomb_oleo_superficies_contato_engrenagens,inspecao_bomb_oleo_guias,inspecao_bomb_oleo_riscos,inspecao_bomb_oleo_diametro_bucha,inspecao_bomb_oleo_desgaste_chapa_bomba,inspecao_bomb_oleo_desgaste_engrangem_motora,inspecao_bomb_oleo_estado_lingueta,inspecao_eixo_entrada_superficie_contato,inspecao_eixo_entrada_estrias,inspecao_eixo_entrada_alojamento_pistao,inspecao_eixo_entrada_contato_anel_vedacao,inspecao_eixo_entrada_diametro_bucha,inspecao_tambor_c1_descoloracao,inspecao_tambor_c1_entalhe_encaixe,inspecao_tambor_c1_estrias, inspecao_tambor_c1_alojamento_pistao,inspecao_tambor_c1_sup_apoio_trava,inspecao_tambor_b1_descoloracao,inspecao_tambor_b1_entalhe_encaixe,inspecao_tambor_b1_estrias,inspecao_tambor_b1_alojamento_pistao,inspecao_tambor_b1_sup_apoio_trava,inspecao_conjunto_c2_descoloracao,inspecao_conjunto_c2_entalhe_encaixe,inspecao_conjunto_c2_estrias,inspecao_conjunto_c2_alojamento_pistao,inspecao_conjunto_c2_sup_apoio_trava,inspecao_diferencial_trincas_quebras,inspecao_diferencial_rolamento,inspecao_diferencial_superficies_arruelas,inspecao_diferencial_estrias,inspecao_diferencial_desgaste_arruela,inspecao_diferencial_desgaste_eixo,inspecao_diferencial_desgaste_capa,inspecao_diferencial_desgaste_satelite,inspecao_mola_retorno_oxidacao,inspecao_mola_retorno_deformacao,inspecao_mola_retorno_empenamento,inspecao_haste_pistao_desgaste_haste,inspecao_haste_pistao_componentes,inspecao_haste_pistao_oxidacao,inspecao_disco_embreagem_queima,inspecao_disco_embreagem_desgaste,inspecao_disco_embreagem_empenamento,inspecao_disco_embreagem_deformacao,inspecao_pistao_trinca_quebra,inspecao_pistao_desgaste,inspecao_pistao_canais_aneis,inspecao_pistao_estado_mola,inspecao_conectores_quebra,inspecao_conectores_trincas,insepcao_conectores_oxidacao,inspecao_sensor_rotacao_derretimento,inspecao_sensor_rotacao_estado_cabo,inspecao_sensor_rotacao_estado_conector,inspecao_sensor_pressao1_trinca_quebra,inspecao_sensor_pressao1_presenca_esfera,inspecao_sensor_pressao1_estado_cabo,inspecao_sensor_pressao1_estado_conector,inspecao_capa_seca_trinca_quebra,inspecao_capa_seca_rocas,inspecao_capa_seca_capa_rolamento,inspecao_capa_seca_alojamento_bomb_oleo,inspecao_capa_seca_alojamento_retentores,inspecao_capa_seca_superficie_vedacao,inspecao_tampa_traseira_trinca_quebra,inspecao_tampa_traseira_roscas,inspecao_tampa_traseira_alojamentos,inspecao_tampa_traseira_superficie_vedacao,inspecao_tampa_traseira_superficie_contato,inspecao_tampa_traseira_aneis,inspecao_placa_bomba_trinca_quebra,inspecao_placa_bomba_roscas,inspecao_placa_bomba_riscos,inspecao_placa_bomba_diametro_bucha,inspecao_cubo_rolamento,inspecao_cubo_apoio_anel,inspecao_cubo_rolamento_axial,inspecao_cubo_diametro_bucha,inspecao_planetaria_descoloracao,inspecao_planetaria_dente,inspecao_planetaria_roscas,inspecao_planetaria_superficie_contato,inspecao_planetaria_desgaste_rolamento,inspecao_planetaria_oxidacao,inspecao_planetaria_diamentro_bucha,inspecao_tambor_c3_descoloracao,inspecao_tambor_c3_entalhe_encaixe,inspecao_tambor_c3_estrias,inspecao_tambor_c3_alojamento_pistao,inspecao_tambor_c3_sup_apoio_trava,inspecao_conjunto_b2_descoloracao,inspecao_conjunto_b2_entalhe_encaixe,inspecao_conjunto_b2_estrias,inspecao_conjunto_b2_alojamento_pistao,inspecao_conjunto_b2_sup_apoio_trava,inspecao_pinhao_rolamento,inspecao_pinhao_gaiola,inspecao_pinhao_rolamento_axial,inspecao_engrenagem_rolamento,inspecao_engrenagem_gaiola,inspecao_engrenagem_rolamento_axial,inspecao_sup_engrenagem_descoloracao,inspecao_sup_engrenagem_entalhe_encaixe,inspecao_sup_engrenagem_dente,inspecao_rolamentos_axiais_derretimentos,inspecao_rolamentos_axiais_quebra_pista,inspecao_trocador_trinca_quebra,inspecao_trocador_furo_interno,inspecao_respiro_rasgos,inspecao_respiro_presenca_tampa,inspecao_respiro_deformacao,inspecao_chave_quebra,inspecao_chave_estado_conector,inspecao_chave_estado_terminal,inspecao_sensor_pressao2_trinca_quebra,inspecao_sensor_pressao2_presenca_esfera,inspecao_sensor_pressao2_estado_cabo,inspecao_sensor_pressao2_estado_conector,inspecao_chapa_empenamento,inspecao_chapa_amassado,inspecao_chapa_oxidacao,inspecao_c1_observacao,inspecao_c2_observacao,inspecao_c3_observacao,inspecao_b1_observacao,inspecao_b2_observacao,inspecao_suporte_observacao,inspecao_relacao_observacao,inspecao_bomba_observacao,inspecao_rolamentos_observacao,inspecao_c1_ajuste,inspecao_c1_visto,inspecao_c2_ajuste,inspecao_c2_visto,inspecao_c3_ajuste,inspecao_c3_visto,inspecao_b1_ajuste,inspecao_b1_visto,inspecao_b2_ajuste,inspecao_b2_visto):
        self.inspecao_ordem = inspecao_ordem
        self.inspecao_op = inspecao_op
        self.inspecao_modelo = inspecao_modelo
        self.inspecao_conversor_torque = inspecao_conversor_toque
        self.inspecao_data = inspecao_data
        self.inspecao_serie = inspecao_serie
        self.inspecao_nome = inspecao_nome
        
        #Carcaça Principal
        self.inspecao_carcaca_trinca_quebras = inspecao_carcaca_trinca_quebras
        self.inspecao_carcaca_rolamentos = inspecao_carcaca_rolamentos
        self.inspecao_carcaca_alojamento_pistao = inspecao_carcaca_alojamento_pistao
        self.inspecao_carcaca_alojamento_acumuladores = inspecao_carcaca_alojamento_acumuladores
        self.inspecao_carcaca_alojamento_retentores = inspecao_carcaca_alojamento_retentores
        self.inspecao_carcaca_furo_hastes_pistoes = inspecao_carcaca_furo_hastes_pistoes
        self.inspecao_carcaca_capa_rolamentos = inspecao_carcaca_capa_rolamentos
        self.inspecao_carcaca_guias_carcaca = inspecao_carcaca_guias_carcaca
        self.inspecao_carcaca_superficies_vedacao = inspecao_carcaca_superficies_vedacao

        #Bomba de Óleo
        self.inspecao_bomb_oleo_superficies_contato_engrenagens = inspecao_bomb_oleo_superficies_contato_engrenagens
        self.inspecao_bomb_oleo_guias = inspecao_bomb_oleo_guias
        self.inspecao_bomb_oleo_riscos = inspecao_bomb_oleo_riscos
        self.inspecao_bomb_oleo_diametro_bucha = inspecao_bomb_oleo_diametro_bucha
        self.inspecao_bomb_oleo_desgaste_chapa_bomba = inspecao_bomb_oleo_desgaste_chapa_bomba
        self.inspecao_bomb_oleo_desgaste_engrangem_motora = inspecao_bomb_oleo_desgaste_engrangem_motora
        self.inspecao_bomb_oleo_estado_lingueta = inspecao_bomb_oleo_estado_lingueta

        #Eixo Entrada
        self.inspecao_eixo_entrada_superficie_contato = inspecao_eixo_entrada_superficie_contato
        self.inspecao_eixo_entrada_estrias = inspecao_eixo_entrada_estrias
        self.inspecao_eixo_entrada_alojamento_pistao = inspecao_eixo_entrada_alojamento_pistao
        self.inspecao_eixo_entrada_contato_anel_vedacao = inspecao_eixo_entrada_contato_anel_vedacao
        self.inspecao_eixo_entrada_diametro_bucha = inspecao_eixo_entrada_diametro_bucha

        #Tambor C1
        self.inspecao_tambor_c1_descoloracao = inspecao_tambor_c1_descoloracao
        self.inspecao_tambor_c1_entalhe_encaixe = inspecao_tambor_c1_entalhe_encaixe
        self.inspecao_tambor_c1_estrias = inspecao_tambor_c1_estrias
        self.inspecao_tambor_c1_alojamento_pistao = inspecao_tambor_c1_alojamento_pistao
        self.inspecao_tambor_c1_sup_apoio_trava = inspecao_tambor_c1_sup_apoio_trava

        #Tambor B1
        self.inspecao_tambor_b1_descoloracao = inspecao_tambor_b1_descoloracao
        self.inspecao_tambor_b1_entalhe_encaixe = inspecao_tambor_b1_entalhe_encaixe
        self.inspecao_tambor_b1_estrias = inspecao_tambor_b1_estrias
        self.inspecao_tambor_b1_alojamento_pistao = inspecao_tambor_b1_alojamento_pistao
        self.inspecao_tambor_b1_sup_apoio_trava = inspecao_tambor_b1_sup_apoio_trava

        #Conjunto C2
        self.inspecao_conjunto_c2_descoloracao = inspecao_conjunto_c2_descoloracao
        self.inspecao_conjunto_c2_entalhe_encaixe = inspecao_conjunto_c2_entalhe_encaixe
        self.inspecao_conjunto_c2_estrias = inspecao_conjunto_c2_estrias
        self.inspecao_conjunto_c2_alojamento_pistao = inspecao_conjunto_c2_alojamento_pistao
        self.inspecao_conjunto_c2_sup_apoio_trava = inspecao_conjunto_c2_sup_apoio_trava

        #Diferencial 
        self.inspecao_diferencial_trincas_quebras = inspecao_diferencial_trincas_quebras
        self.inspecao_diferencial_rolamento = inspecao_diferencial_rolamento
        self.inspecao_diferencial_superficies_arruelas = inspecao_diferencial_superficies_arruelas
        self.inspecao_diferencial_estrias = inspecao_diferencial_estrias
        self.inspecao_diferencial_desgaste_arruela = inspecao_diferencial_desgaste_arruela
        self.inspecao_diferencial_desgaste_eixo = inspecao_diferencial_desgaste_eixo
        self.inspecao_diferencial_desgaste_capa = inspecao_diferencial_desgaste_capa
        self.inspecao_diferencial_desgaste_satelite = inspecao_diferencial_desgaste_satelite

        #Mola de Retorno
        self.inspecao_mola_retorno_oxidacao = inspecao_mola_retorno_oxidacao
        self.inspecao_mola_retorno_deformacao = inspecao_mola_retorno_deformacao
        self.inspecao_mola_retorno_empenamento = inspecao_mola_retorno_empenamento

        #Hastes dos Pistões
        self.inspecao_haste_pistao_desgaste_haste = inspecao_haste_pistao_desgaste_haste
        self.inspecao_haste_pistao_componentes = inspecao_haste_pistao_componentes
        self.inspecao_haste_pistao_oxidacao = inspecao_haste_pistao_oxidacao

        #Discos de Embreagem
        self.inspecao_disco_embreagem_queima = inspecao_disco_embreagem_queima
        self.inspecao_disco_embreagem_desgaste = inspecao_disco_embreagem_desgaste
        self.inspecao_disco_embreagem_empenamento = inspecao_disco_embreagem_empenamento
        self.inspecao_disco_embreagem_deformacao = inspecao_disco_embreagem_deformacao

        #Pistão de Acionamento B1
        self.inspecao_pistao_trinca_quebra = inspecao_pistao_trinca_quebra
        self.inspecao_pistao_desgaste = inspecao_pistao_desgaste
        self.inspecao_pistao_canais_aneis = inspecao_pistao_canais_aneis
        self.inspecao_pistao_estado_mola = inspecao_pistao_estado_mola

        #Conectores
        self.inspecao_conectores_quebra = inspecao_conectores_quebra
        self.inspecao_conectores_trincas = inspecao_conectores_trincas
        self.insepcao_conectores_oxidacao = insepcao_conectores_oxidacao

        #Sensor de Rotação de Entrada
        self.inspecao_sensor_rotacao_derretimento = inspecao_sensor_rotacao_derretimento
        self.inspecao_sensor_rotacao_estado_cabo = inspecao_sensor_rotacao_estado_cabo
        self.insepcao_sensor_rotacao_estado_conector = inspecao_sensor_rotacao_estado_conector

        #Sensor de Pressão
        self.inspecao_sensor_pressao1_trinca_quebra = inspecao_sensor_pressao1_trinca_quebra
        self.inspecao_sensor_pressao1_presenca_esfera = inspecao_sensor_pressao1_presenca_esfera
        self.inspecao_sensor_pressao1_estado_cabo = inspecao_sensor_pressao1_estado_cabo
        self.inspecao_sensor_pressao1_estado_conector = inspecao_sensor_pressao1_estado_conector

        #Capa Seca
        self.inspecao_capa_seca_trinca_quebra = inspecao_capa_seca_trinca_quebra
        self.inspecao_capa_seca_rocas = inspecao_capa_seca_rocas
        self.inspecao_capa_seca_capa_rolamento = inspecao_capa_seca_capa_rolamento
        self.inspecao_capa_seca_alojamento_bomb_oleo = inspecao_capa_seca_alojamento_bomb_oleo
        self.inspecao_capa_seca_alojamento_retentores = inspecao_capa_seca_alojamento_retentores
        self.inspecao_capa_seca_superficie_vedacao = inspecao_capa_seca_superficie_vedacao

        #Tampa Traseira
        self.inspecao_tampa_traseira_trinca_quebra = inspecao_tampa_traseira_trinca_quebra
        self.inspecao_tampa_traseira_roscas = inspecao_tampa_traseira_roscas
        self.inspecao_tampa_traseira_alojamentos = inspecao_tampa_traseira_alojamentos
        self.inspecao_tampa_traseira_superficie_vedacao = inspecao_tampa_traseira_superficie_vedacao
        self.inspecao_tampa_traseira_superficie_contato = inspecao_tampa_traseira_superficie_contato
        self.inspecao_tampa_traseira_aneis = inspecao_tampa_traseira_aneis

        #Placa da Bomba
        self.inspecao_placa_bomba_trinca_quebra = inspecao_placa_bomba_trinca_quebra
        self.inspecao_placa_bomba_roscas = inspecao_placa_bomba_roscas
        self.inspecao_placa_bomba_riscos = inspecao_placa_bomba_riscos
        self.inspecao_placa_bomba_diametro_bucha = inspecao_placa_bomba_diametro_bucha

        #Cubo da Carcaça
        self.inspecao_cubo_rolamento = inspecao_cubo_rolamento
        self.inspecao_cubo_apoio_anel = inspecao_cubo_apoio_anel
        self.inspecao_cubo_rolamento_axial = inspecao_cubo_rolamento_axial
        self.inspecao_cubo_diametro_bucha = inspecao_cubo_diametro_bucha

        #Conjunto de Planetárias
        self.inspecao_planetaria_descoloracao = inspecao_planetaria_descoloracao
        self.inspecao_planetaria_dente = inspecao_planetaria_dente
        self.inspecao_planetaria_roscas = inspecao_planetaria_roscas
        self.inspecao_planetaria_superficie_contato = inspecao_planetaria_superficie_contato
        self.inspecao_planetaria_desgaste_rolamento = inspecao_planetaria_desgaste_rolamento
        self.inspecao_planetaria_oxidacao = inspecao_planetaria_oxidacao
        self.inspecao_planetaria_diamentro_bucha = inspecao_planetaria_diamentro_bucha

        #Tambor C3
        self.inspecao_tambor_c3_descoloracao = inspecao_tambor_c3_descoloracao
        self.inspecao_tambor_c3_entalhe_encaixe = inspecao_tambor_c3_entalhe_encaixe
        self.inspecao_tambor_c3_estrias = inspecao_tambor_c3_estrias
        self.inspecao_tambor_c3_alojamento_pistao = inspecao_tambor_c3_alojamento_pistao
        self.inspecao_tambor_c3_sup_apoio_trava = inspecao_tambor_c3_sup_apoio_trava
        
        #Conjunto B2
        self.inspecao_conjunto_b2_descoloracao = inspecao_conjunto_b2_descoloracao
        self.inspecao_conjunto_b2_entalhe_encaixe = inspecao_conjunto_b2_entalhe_encaixe
        self.inspecao_conjunto_b2_estrias = inspecao_conjunto_b2_estrias
        self.inspecao_conjunto_b2_alojamento_pistao = inspecao_conjunto_b2_alojamento_pistao
        self.inspecao_conjunto_b2_sup_apoio_trava = inspecao_conjunto_b2_sup_apoio_trava

        #Pinhão
        self.inspecao_pinhao_rolamento = inspecao_pinhao_rolamento
        self.inspecao_pinhao_gaiola = inspecao_pinhao_gaiola
        self.inspecao_pinhao_rolamento_axial = inspecao_pinhao_rolamento_axial

        #Engranagem Solar
        self.inspecao_engrenagem_rolamento = inspecao_engrenagem_rolamento
        self.inspecao_engrenagem_gaiola = inspecao_engrenagem_gaiola
        self.inspecao_engrenagem_rolamento_axial = inspecao_engrenagem_rolamento_axial

        #Suporte de Engrenagem Solar
        self.inspecao_sup_engrenagem_descoloracao = inspecao_sup_engrenagem_descoloracao
        self.inspecao_sup_engrenagem_entalhe_encaixe = inspecao_sup_engrenagem_entalhe_encaixe
        self.inspecao_sup_engrenagem_dente = inspecao_sup_engrenagem_dente

        #Rolamentos axiais e Calços
        self.inspecao_rolamentos_axiais_derretimentos = inspecao_rolamentos_axiais_derretimentos
        self.inspecao_rolamentos_axiais_quebra_pista = inspecao_rolamentos_axiais_quebra_pista

        #Trocador de Calor
        self.inspecao_trocador_trinca_quebra = inspecao_trocador_trinca_quebra
        self.inspecao_trocador_furo_interno = inspecao_trocador_furo_interno

        #Respiro
        self.inspecao_respiro_rasgos = inspecao_respiro_rasgos
        self.inspecao_respiro_presenca_tampa = inspecao_respiro_presenca_tampa
        self.inspecao_respiro_deformacao = inspecao_respiro_deformacao

        #Chave Seletora
        self.inspecao_chave_quebra = inspecao_chave_quebra
        self.inspecao_chave_estado_conector = inspecao_chave_estado_conector
        self.inspecao_chave_estado_terminal = inspecao_chave_estado_terminal

        #Sensor de Pressão
        self.inspecao_sensor_pressao2_trinca_quebra = inspecao_sensor_pressao2_trinca_quebra
        self.inspecao_sensor_pressao2_presenca_esfera = inspecao_sensor_pressao2_presenca_esfera
        self.inspecao_sensor_pressao2_estado_cabo = inspecao_sensor_pressao2_estado_cabo
        self.inspecao_sensor_pressao2_estado_conector = inspecao_sensor_pressao2_estado_conector

        #Chapa Defletora de Óleo do Diferencial
        self.inspecao_chapa_empenamento = inspecao_chapa_empenamento
        self.inspecao_chapa_amassado = inspecao_chapa_amassado
        self.inspecao_chapa_oxidacao = inspecao_chapa_oxidacao

        #Informações Adicionais
        self.inspecao_c1_observacao = inspecao_c1_observacao
        self.inspecao_c2_observacao = inspecao_c2_observacao
        self.inspecao_c3_observacao = inspecao_c3_observacao
        self.inspecao_b1_observacao = inspecao_b1_observacao
        self.inspecao_b2_observacao = inspecao_b2_observacao
        self.inspecao_suporte_observacao = inspecao_suporte_observacao
        self.inspecao_relacao_observacao = inspecao_relacao_observacao
        self.inspecao_bomba_observacao = inspecao_bomba_observacao
        self.inspecao_rolamentos_observacao = inspecao_rolamentos_observacao

        #Ajuste
        self.inspecao_c1_ajuste = inspecao_c1_ajuste
        self.inspecao_c1_visto = inspecao_c1_visto
        self.inspecao_c2_ajuste = inspecao_c2_ajuste
        self.inspecao_c2_visto = inspecao_c2_visto
        self.inspecao_c3_ajuste = inspecao_c3_ajuste
        self.inspecao_c3_visto = inspecao_c3_visto
        self.inspecao_b1_ajuste = inspecao_b1_ajuste
        self.inspecao_b1_visto = inspecao_b1_visto
        self.inspecao_b2_ajuste = inspecao_b2_ajuste
        self.inspecao_b2_visto = inspecao_b2_visto


    def __repr__(self):
        return '<Pessoa %r>' % self.inspecao_id

class   Inspecao2(db.Model):
    __tablename__ = 'inspecao2'

    id_insp2 = db.Column(db.Integer, primary_key=True)
    os_insp2 = db.Column(db.String(50), nullable=False)
    op_insp2 = db.Column(db.String(50))
    modelo_insp2 = db.Column(db.String(50))
    conversor_insp2 = db.Column(db.String(50))
    data_inps2 = db.Column(db.String(50))
    serie_insp2 = db.Column(db.String(50))
    nome_insp2 = db.Column(db.String(50))

    carc_trinca_insp2 = db.Column(db.String(3))
    carc_rolam_insp2 = db.Column(db.String(3))
    carc_aloj_insp2 = db.Column(db.String(3))
    carc_acumu_insp2 = db.Column(db.String(3))
    carc_reten_insp2 = db.Column(db.String(3))
    carc_pist_insp2 = db.Column(db.String(3))
    carc_capa_insp2 = db.Column(db.String(3))
    carc_guia_insp2 = db.Column(db.String(3))
    carc_veda_insp2 = db.Column(db.String(3))

    bomb_super_insp2 = db.Column(db.String(3))
    bomb_guia_insp2 = db.Column(db.String(3))
    bomb_risco_inps2 = db.Column(db.String(3))
    bomb_dia_insp2 = db.Column(db.String(500))
    bomb_desg_insp2 = db.Column(db.String(3))
    bomb_eng_insp2 = db.Column(db.String(3))
    bomb_estados_insp2 = db.Column(db.String(3))

    eixo_supr_insp2 = db.Column(db.String(3))
    eixo_estrias_insp2 = db.Column(db.String(3))
    eixo_pist_insp2 = db.Column(db.String(3))
    eixo_cont_insp2 = db.Column(db.String(3))
    eixo_dia_insp2 = db.Column(db.String(3))

    tambor_desc_insp2 = db.Column(db.String(3))
    tambor_ent_insp2 = db.Column(db.String(3))
    tambor_estrias_insp2 = db.Column(db.String(3))
    tambor_pist_insp2 = db.Column(db.String(3))
    tambor_sup_insp2 = db.Column(db.String(3))

    tambor2_des_insp2 = db.Column(db.String(3))
    tambor2_ent_insp2 = db.Column(db.String(3))
    tambor2_estrias_insp2 = db.Column(db.String(3))
    tambor2_pist_insp2 = db.Column(db.String(3))
    tambor2_trava_insp2 = db.Column(db.String(3))

    tamb3_desc_insp2 = db.Column(db.String(3))
    tamb3_enc_insp2 = db.Column(db.String(3))
    tamb3_estrias_insp2 = db.Column(db.String(3))
    tamb3_pist_insp2 = db.Column(db.String(3))
    tamb3_trava_insp2 = db.Column(db.String(3))

    dife_trinca_insp2 = db.Column(db.String(3))
    dife_rolam_insp2 = db.Column(db.String(3))
    dife_super_insp2 = db.Column(db.String(3))
    dife_estrias_insp2 = db.Column(db.String(3))
    dife_desg_insp2 = db.Column(db.String(3))
    dife_eixo_insp2 = db.Column(db.String(3))
    dife_capa_insp2 = db.Column(db.String(3))
    dife_sate_insp2 = db.Column(db.String(3))

    mola_oxi_insp2 = db.Column(db.String(3))
    mola_def_insp2 = db.Column(db.String(3))
    mola_emp_insp2 = db.Column(db.String(3))

    hast_pos_insp2 = db.Column(db.String(3))
    hast_mol_insp2 = db.Column(db.String(3))
    hast_oxid_insp2 = db.Column(db.String(3))

    conect_quebra_insp2 = db.Column(db.String(3))
    conect_trincas_insp2 = db.Column(db.String(3))
    conect_oxid_insp2 = db.Column(db.String(3))

    sensor_der_insp2 = db.Column(db.String(3))
    sensor_cab_insp2 = db.Column(db.String(3))
    sensor_conec_insp2 = db.Column(db.String(3))

    snpres_trinca_insp2 = db.Column(db.String(3))
    snpres_esfera_insp2 = db.Column(db.String(3))
    snpres_cabo_insp2 = db.Column(db.String(3))
    snpres_conec_insp2 = db.Column(db.String(3))

    chapa_quebra_insp2 = db.Column(db.String(3))
    chapa_amassada_insp2 = db.Column(db.String(3))
    chapa_oxida_insp2 = db.Column(db.String(3))

    cpa_trinca_insp2 = db.Column(db.String(3))
    cpa_rosca_insp2 = db.Column(db.String(3))
    cpa_rolam_insp2 = db.Column(db.String(3))
    cpa_aloj_insp2 = db.Column(db.String(3))
    cpa_retent_insp2 = db.Column(db.String(3))
    cpa_super_insp2 = db.Column(db.String(3))

    tampa_trinca_insp2 = db.Column(db.String(3))
    tampa_rosca_insp2 = db.Column(db.String(3))
    tampa_aloj_insp2 = db.Column(db.String(3))
    tampa_ved_insp2 = db.Column(db.String(3))
    tampa_cont_insp2 = db.Column(db.String(3))
    tampa_aneis_ins2 = db.Column(db.String(3))

    placa_trinca_insp2 = db.Column(db.String(3))
    placa_rosca_insp2 = db.Column(db.String(3))
    placa_risco_insp2 = db.Column(db.String(3))
    placa_dia_insp2 = db.Column(db.String(500))

    cuba_rola_insp2 = db.Column(db.String(3))
    cuba_aneis_insp2 = db.Column(db.String(3))
    cuba_axial_insp2 = db.Column(db.String(3))
    cuba_dia_insp2 = db.Column(db.String(500))

    planet_desc_insp2 = db.Column(db.String(3))
    planet_dent_insp2 = db.Column(db.String(3))
    planet_dani_insp2 = db.Column(db.String(3))
    planet_super_insp2 = db.Column(db.String(3))
    planet_dest_insp2 = db.Column(db.String(3))
    planet_oxida_insp2 = db.Column(db.String(3))
    planet_dia_insp2 = db.Column(db.String(500))

    tamb4_desc_insp2 = db.Column(db.String(3))
    tamb4_encaix_insp2 = db.Column(db.String(3))
    tamb4_estrias_insp2 = db.Column(db.String(3))
    tamb4_pist_insp2 = db.Column(db.String(3))
    tamb4_trava_insp2 = db.Column(db.String(3))

    tamb5_desc_insp2 = db.Column(db.String(3))
    tamb5_disc_insp2 = db.Column(db.String(3))
    tamb5_estrias_insp2 = db.Column(db.String(3))
    tamb5_pist_insp2 = db.Column(db.String(3))
    tamb5_trava_insp2 = db.Column(db.String(3))

    embre_queima_insp2 = db.Column(db.String(3))
    embre_desg_insp2 = db.Column(db.String(3))
    embre_empena_insp2 = db.Column(db.String(3))
    embre_def_insp2 = db.Column(db.String(3))
    embre_obs_insp2 = db.Column(db.String(1000))

    acion_trinca_insp2 = db.Column(db.String(3))
    acion_desgt_insp2 = db.Column(db.String(3))
    acion_aneis_insp2 = db.Column(db.String(3))
    acion_mola_insp2 = db.Column(db.String(3))

    troca_quebras_insp2 = db.Column(db.String(3))
    troca_furo_insp2 = db.Column(db.String(3))

    respiro_rasgo_insp2 = db.Column(db.String(3))
    respiro_tamp_insp2 = db.Column(db.String(3))
    respiro_defor_insp2 = db.Column(db.String(3))
 
    chsele_quebras_inspe2 = db.Column(db.String(3))
    chsele_conect_insp2 = db.Column(db.String(3))
    chsele_termi_insp2 = db.Column(db.String(3))

    inf_ps2_insp2 = db.Column(db.String(3000))
    inf_eix_insp2 = db.Column(db.String(3000))
    inf_bomb_insp2 = db.Column(db.String(3000))
    inf_bomba_insp2 = db.Column(db.String(3000))
    inf_bombb_ins2 = db.Column(db.String(3000))
    inf_n1_insp2 = db.Column(db.String(3000))
    inf_n2_insp2 = db.Column(db.String(3000))
    inf_f3n1_insp2 = db.Column(db.String(3000))
    inf_f3n2_insp2 = db.Column(db.String(3000))
    inf_conj1_insp2 = db.Column(db.String(3000))
    inf_mont1_insp2 = db.Column(db.String(3000))
    inf_conj2_insp2 = db.Column(db.String(3000))
    inf_mont2_insp2 = db.Column(db.String(3000))
    inf_conj3_insp2 = db.Column(db.String(3000))
    inf_mont3_insp2 = db.Column(db.String(3000))
    inf_conj4_insp2 = db.Column(db.String(3000))
    inf_mont4_insp2 = db.Column(db.String(300))
    inf_conj5_insp2 = db.Column(db.String(3000))
    inf_mont5_insp2 = db.Column(db.String(3000))

    def __init__(self, os_insp2, op_insp2, modelo_insp2, conversor_insp2, data_inps2, serie_insp2, nome_insp2, carc_trinca_insp2, carc_rolam_insp2, carc_aloj_insp2, carc_acumu_insp2, carc_reten_insp2, carc_pist_insp2, carc_capa_insp2, carc_guia_insp2, carc_veda_insp2, bomb_super_insp2, bomb_guia_insp2, bomb_risco_inps2, bomb_dia_insp2, bomb_desg_insp2, bomb_eng_insp2, bomb_estados_insp2, eixo_supr_insp2, eixo_estrias_insp2, eixo_pist_insp2, eixo_cont_insp2, eixo_dia_insp2, tambor_desc_insp2, tambor_ent_insp2, tambor_estrias_insp2, tambor_pist_insp2, tambor_sup_insp2, tambor2_des_insp2, tambor2_ent_insp2, tambor2_estrias_insp2, tambor2_pist_insp2, tambor2_trava_insp2, tamb3_desc_insp2, tamb3_enc_insp2, tamb3_estrias_insp2, tamb3_pist_insp2, tamb3_trava_insp2, dife_trinca_insp2, dife_rolam_insp2, dife_super_insp2, dife_estrias_insp2, dife_desg_insp2, dife_eixo_insp2, dife_capa_insp2, dife_sate_insp2, mola_oxi_insp2, mola_def_insp2, mola_emp_insp2, hast_pos_insp2, hast_mol_insp2, hast_oxid_insp2, conect_quebra_insp2, conect_trincas_insp2, conect_oxid_insp2, sensor_der_insp2, sensor_cab_insp2, sensor_conec_insp2, snpres_trinca_insp2, snpres_esfera_insp2, snpres_cabo_insp2, snpres_conec_insp2, chapa_quebra_insp2, chapa_amassada_insp2, chapa_oxida_insp2, cpa_trinca_insp2, cpa_rosca_insp2, cpa_rolam_insp2, cpa_aloj_insp2, cpa_retent_insp2, cpa_super_insp2, tampa_trinca_insp2, tampa_rosca_insp2, tampa_aloj_insp2, tampa_ved_insp2, tampa_cont_insp2, tampa_aneis_ins2, placa_trinca_insp2, placa_rosca_insp2, placa_risco_insp2, placa_dia_insp2, cuba_rola_insp2, cuba_aneis_insp2, cuba_axial_insp2, cuba_dia_insp2, planet_desc_insp2, planet_dent_insp2, planet_dani_insp2, planet_super_insp2, planet_dest_insp2, planet_oxida_insp2, planet_dia_insp2, tamb4_desc_insp2, tamb4_encaix_insp2, tamb4_estrias_insp2, tamb4_pist_insp2, tamb4_trava_insp2, tamb5_desc_insp2, tamb5_disc_insp2, tamb5_estrias_insp2, tamb5_pist_insp2, tamb5_trava_insp2, embre_queima_insp2, embre_desg_insp2, embre_empena_insp2, embre_def_insp2, embre_obs_insp2, acion_trinca_insp2, acion_desgt_insp2, acion_aneis_insp2, acion_mola_insp2, troca_quebras_insp2, troca_furo_insp2, respiro_rasgo_insp2, respiro_tamp_insp2, respiro_defor_insp2, chsele_quebras_inspe2, chsele_conect_insp2, chsele_termi_insp2, inf_ps2_insp2, inf_eix_insp2, inf_bomb_insp2, inf_bomba_insp2, inf_bombb_ins2, inf_n1_insp2, inf_n2_insp2, inf_f3n1_insp2, inf_f3n2_insp2, inf_conj1_insp2, inf_mont1_insp2, inf_conj2_insp2, inf_mont2_insp2, inf_conj3_insp2, inf_mont3_insp2, inf_conj4_insp2, inf_mont4_insp2, inf_conj5_insp2, inf_mont5_insp2):
        self.os_insp2 = os_insp2
        self.op_insp2 = op_insp2
        self.modelo_insp2 = modelo_insp2
        self.conversor_insp2 = conversor_insp2
        self.data_inps2 = data_inps2
        self.serie_insp2 = serie_insp2
        self.nome_insp2 = nome_insp2

        self.carc_trinca_insp2 = carc_trinca_insp2
        self.carc_rolam_insp2 = carc_rolam_insp2
        self.carc_aloj_insp2 = carc_aloj_insp2
        self.carc_acumu_insp2 = carc_acumu_insp2
        self.carc_reten_insp2 = carc_reten_insp2
        self.carc_pist_insp2 = carc_pist_insp2
        self.carc_capa_insp2 = carc_capa_insp2
        self.carc_guia_insp2 = carc_guia_insp2
        self.carc_veda_insp2 = carc_veda_insp2

        self.bomb_super_insp2 = bomb_super_insp2
        self.bomb_guia_insp2 = bomb_guia_insp2
        self.bomb_risco_inps2 = bomb_risco_inps2
        self.bomb_dia_insp2 = bomb_dia_insp2

        self.bomb_super_insp2 = bomb_super_insp2
        self.bomb_guia_insp2 = bomb_guia_insp2
        self.bomb_risco_inps2 = bomb_risco_inps2
        self.bomb_dia_insp2 = bomb_dia_insp2
        self.bomb_desg_insp2 = bomb_desg_insp2
        self.bomb_eng_insp2 = bomb_eng_insp2
        self.bomb_estados_insp2 = bomb_estados_insp2

        self.eixo_supr_insp2 = eixo_supr_insp2
        self.eixo_estrias_insp2 = eixo_estrias_insp2
        self.eixo_pist_insp2 = eixo_pist_insp2
        self.eixo_cont_insp2 = eixo_cont_insp2
        self.eixo_dia_insp2 = eixo_dia_insp2

        self.tambor_desc_insp2 = tambor_desc_insp2
        self.tambor_ent_insp2 = tambor_ent_insp2
        self.tambor_estrias_insp2 = tambor_estrias_insp2
        self.tambor_pist_insp2 = tambor_pist_insp2
        self.tambor_sup_insp2 = tambor_sup_insp2

        self.tambor2_des_insp2 = tambor2_des_insp2
        self.tambor2_ent_insp2 = tambor2_ent_insp2
        self.tambor2_estrias_insp2 = tambor2_estrias_insp2
        self.tambor2_pist_insp2 = tambor2_pist_insp2
        self.tambor2_trava_insp2 = tambor2_trava_insp2

        self.tamb3_desc_insp2 = tamb3_desc_insp2
        self.tamb3_enc_insp2 = tamb3_enc_insp2
        self.tamb3_estrias_insp2 = tamb3_estrias_insp2
        self.tamb3_pist_insp2 = tamb3_pist_insp2
        self.tamb3_trava_insp2 = tamb3_trava_insp2

        self.dife_trinca_insp2 = dife_trinca_insp2
        self.dife_rolam_insp2 = dife_rolam_insp2
        self.dife_super_insp2 = dife_super_insp2
        self.dife_estrias_insp2 = dife_estrias_insp2
        self.dife_desg_insp2 = dife_desg_insp2
        self.dife_eixo_insp2 = dife_eixo_insp2
        self.dife_capa_insp2 = dife_capa_insp2
        self.dife_sate_insp2 = dife_sate_insp2

        self.mola_oxi_insp2 = mola_oxi_insp2
        self.mola_def_insp2 = mola_def_insp2
        self.mola_emp_insp2 = mola_emp_insp2

        self.hast_pos_insp2 = hast_pos_insp2
        self.hast_mol_insp2 = hast_mol_insp2 
        self.hast_oxid_insp2 = hast_oxid_insp2
        
        self.conect_quebra_insp2 = conect_quebra_insp2
        self.conect_trincas_insp2 = conect_trincas_insp2
        self.conect_oxid_insp2 = conect_oxid_insp2

        self.sensor_der_insp2 = sensor_der_insp2
        self.sensor_cab_insp2 = sensor_cab_insp2
        self.sensor_conec_insp2 = sensor_conec_insp2

        self.snpres_trinca_insp2 = snpres_trinca_insp2
        self.snpres_esfera_insp2 = snpres_esfera_insp2
        self.snpres_cabo_insp2 = snpres_cabo_insp2
        self.snpres_conec_insp2 = snpres_conec_insp2

        self.chapa_quebra_insp2 = chapa_quebra_insp2
        self.chapa_amassada_insp2 = chapa_amassada_insp2
        self.chapa_oxida_insp2 = chapa_oxida_insp2

        self.cpa_trinca_insp2 = cpa_trinca_insp2
        self.cpa_rosca_insp2 = cpa_rosca_insp2
        self.cpa_rolam_insp2 = cpa_rolam_insp2
        self.cpa_aloj_insp2 = cpa_aloj_insp2
        self.cpa_retent_insp2 = cpa_retent_insp2
        self.cpa_super_insp2 = cpa_super_insp2 

        self.tampa_trinca_insp2 = tampa_trinca_insp2
        self.tampa_rosca_insp2 = tampa_rosca_insp2
        self.tampa_aloj_insp2 = tampa_aloj_insp2
        self.tampa_ved_insp2 = tampa_ved_insp2
        self.tampa_cont_insp2 = tampa_cont_insp2
        self.tampa_aneis_ins2 = tampa_aneis_ins2

        self.placa_trinca_insp2 = placa_trinca_insp2
        self.placa_rosca_insp2 = placa_rosca_insp2
        self.placa_risco_insp2 = placa_risco_insp2
        self.placa_dia_insp2 = placa_dia_insp2 

        self.cuba_rola_insp2 = cuba_rola_insp2
        self.cuba_aneis_insp2 = cuba_aneis_insp2 
        self.cuba_axial_insp2 = cuba_axial_insp2
        self.cuba_dia_insp2 = cuba_dia_insp2

        self.planet_desc_insp2 = planet_desc_insp2
        self.planet_dent_insp2 = planet_dent_insp2 
        self.planet_dani_insp2 = planet_dani_insp2
        self.planet_super_insp2 = planet_super_insp2
        self.planet_dest_insp2 = planet_dest_insp2
        self.planet_oxida_insp2 = planet_oxida_insp2
        self.planet_dia_insp2 = planet_dia_insp2

        self.tamb4_desc_insp2 = tamb4_desc_insp2
        self.tamb4_encaix_insp2 = tamb4_encaix_insp2
        self.tamb4_estrias_insp2 = tamb4_estrias_insp2
        self.tamb4_pist_insp2 = tamb4_pist_insp2
        self.tamb4_trava_insp2 = tamb4_trava_insp2

        self.tamb5_desc_insp2 = tamb5_desc_insp2 
        self.tamb5_disc_insp2 = tamb5_disc_insp2
        self.tamb5_estrias_insp2 = tamb5_estrias_insp2
        self.tamb5_pist_insp2 = tamb5_pist_insp2
        self.tamb5_trava_insp2 = tamb5_trava_insp2

        self.embre_queima_insp2 = embre_queima_insp2
        self.embre_desg_insp2 = embre_desg_insp2
        self.embre_empena_insp2 = embre_empena_insp2
        self.embre_def_insp2 = embre_def_insp2
        self.embre_obs_insp2 = embre_obs_insp2

        self.acion_trinca_insp2 = acion_trinca_insp2
        self.acion_desgt_insp2 = acion_desgt_insp2
        self.acion_aneis_insp2 = acion_aneis_insp2
        self.acion_mola_insp2 = acion_mola_insp2

        self.troca_quebras_insp2 = troca_quebras_insp2
        self.troca_furo_insp2 = troca_furo_insp2

        self.respiro_rasgo_insp2 = respiro_rasgo_insp2
        self.respiro_tamp_insp2 = respiro_tamp_insp2 
        self.respiro_defor_insp2 = respiro_defor_insp2

        self.chsele_quebras_inspe2 = chsele_quebras_inspe2
        self.chsele_conect_insp2 = chsele_conect_insp2
        self.chsele_termi_insp2 = chsele_termi_insp2

        self.inf_ps2_insp2 = inf_ps2_insp2
        self.inf_eix_insp2 = inf_eix_insp2
        self.inf_bomb_insp2 = inf_bomb_insp2 
        self.inf_bomba_insp2 = inf_bomba_insp2
        self.inf_bombb_ins2 = inf_bombb_ins2
        self.inf_n1_insp2 = inf_n1_insp2
        self.inf_n2_insp2 = inf_n2_insp2 
        self.inf_f3n1_insp2 = inf_f3n1_insp2
        self.inf_f3n2_insp2 = inf_f3n2_insp2
        self.inf_conj1_insp2 = inf_conj1_insp2
        self.inf_mont1_insp2 = inf_mont1_insp2
        self.inf_conj2_insp2 = inf_conj2_insp2 
        self.inf_mont2_insp2 = inf_mont2_insp2
        self.inf_conj3_insp2 = inf_conj3_insp2
        self.inf_mont3_insp2 = inf_mont3_insp2
        self.inf_conj4_insp2 = inf_conj4_insp2
        self.inf_mont4_insp2 = inf_mont4_insp2 
        self.inf_conj5_insp2 = inf_conj5_insp2 
        self.inf_mont5_insp2 = inf_mont5_insp2 

    def __repr__(self):
        return '<Inspecao2 %r>' % self.id_insp2

class Montagem(db.Model):
    __tablename__ = 'montagem'

    montagem_id = db.Column(db.Integer,primary_key=True)
    montagem_ordem = db.Column(db.String(50),nullable=False)
    montagem_op = db.Column(db.String(50))
    montagem_modelo = db.Column(db.String(50))
    montagem_conversor_torque = db.Column(db.String(50))
    montagem_data = db.Column(db.String(50))
    montagem_serie = db.Column(db.String(50))
    montagem_nome = db.Column(db.String(50))

    #Tampa Traseira
    montagem_tampa_traseira = db.Column(db.String(50))
    
    #Carcaça principal
    montagem_carcaca_principal = db.Column(db.String(50))
    
    #Tampa do Bloco Hidráulico
    montagem_tampa_bloco_hidra = db.Column(db.String(50))
    
    #Bloco Hidráulico na transmissão
    montagem_bloco_pre_torque = db.Column(db.String(50))
    montagem_bloco_torque = db.Column(db.String(50))

    #Porca de rolamento central
    montagem_porca_pre_torque = db.Column(db.String(50))
    montagem_porca_torque = db.Column(db.String(50))

    #Parafusos do rolamento central
    montagem_parafuso_rolamento = db.Column(db.String(50))

    #Parafuso de ancoragem das cintas
    montagem_parafuso_ancoragem = db.Column(db.String(50))

    #Parfusos do sensor de pressão
    montagem_parafuso_sensor_pressao = db.Column(db.String(50))

    #Parfusos do sensor de rot. De saída
    montagem_parafuso_sensor_rotacao = db.Column(db.String(50))

    #Carcaça da bomba de óleo
    montagem_carcaca_bomb_oleo_pre_torque = db.Column(db.String(50))
    montagem_carcaca_bomb_oleo_torque = db.Column(db.String(50))

    #Conjunto da bomba na transmissão
    montagem_conjunto_bomba_pre_torque = db.Column(db.String(50))
    montagem_conjunto_bomba_torque = db.Column(db.String(50))

    #Parafuso do eixo seletor
    montagem_parafuso_eixo = db.Column(db.String(50))

    #Parafuso do trocador de calor
    montagem_parafuso_trocador = db.Column(db.String(50))

    #Parafusos da coroa (dif. de Ferro Fundido)
    montagem_parafuso_coroa_ferro = db.Column(db.String(50))

    #Parafusos da coroa (dif. de Alumínio)
    montagem_parafuso_coroa_aluminio = db.Column(db.String(50))

    #Parfusos da chave seletora (CMF)
    montagem_parafuso_chave_seletora = db.Column(db.String(50))

    #Parfusos do sensor do velocímetro
    montagem_parafuso_velocimetro = db.Column(db.String(50))

    #Parfusos do controle de débito do permutador
    montagem_parafuso_controle = db.Column(db.String(50))

    def __init__(self,montagem_ordem,montagem_op,montagem_modelo,montagem_conversor_torque,montagem_data,montagem_serie,montagem_nome,montagem_tampa_traseira,montagem_carcaca_principal,montagem_tampa_bloco_hidra,montagem_bloco_pre_torque,montagem_bloco_torque,montagem_porca_pre_torque,montagem_porca_torque,montagem_parafuso_rolamento,montagem_parafuso_ancoragem,montagem_parafuso_sensor_pressao,montagem_parafuso_sensor_rotacao,montagem_carcaca_bomb_oleo_pre_torque,montagem_carcaca_bomb_oleo_torque,montagem_conjunto_bomba_pre_torque,montagem_conjunto_bomba_torque,montagem_parafuso_eixo,montagem_parafuso_trocador,montagem_parafuso_coroa_ferro,montagem_parafuso_coroa_aluminio,montagem_parafuso_chave_seletora,montagem_parafuso_velocimetro,montagem_parafuso_controle):  
        self.montagem_ordem = montagem_ordem
        self.montagem_op = montagem_op
        self.montagem_modelo = montagem_modelo
        self.montagem_conversor_torque = montagem_conversor_torque
        self.montagem_data = montagem_data
        self.montagem_serie = montagem_serie
        self.montagem_nome = montagem_nome

        #Tampa Traseira
        self.montagem_tampa_traseira = montagem_tampa_traseira
        
        #Carcaça principal
        self.montagem_carcaca_principal = montagem_carcaca_principal
        
        #Tampa do Bloco Hidráulico
        self.montagem_tampa_bloco_hidra = montagem_tampa_bloco_hidra
        
        #Bloco Hidráulico na transmissão
        self.montagem_bloco_pre_torque = montagem_bloco_pre_torque
        self.montagem_bloco_torque = montagem_bloco_torque

        #Porca de rolamento central
        self.montagem_porca_pre_torque = montagem_porca_pre_torque
        self.montagem_porca_torque = montagem_porca_torque

        #Parafusos do rolamento central
        self.montagem_parafuso_rolamento = montagem_parafuso_rolamento

        #Parafuso de ancoragem das cintas
        self.montagem_parafuso_ancoragem = montagem_parafuso_ancoragem

        #Parfusos do sensor de pressão
        self.montagem_parafuso_sensor_pressao = montagem_parafuso_sensor_pressao

        #Parfusos do sensor de rot. De saída
        self.montagem_parafuso_sensor_rotacao = montagem_parafuso_sensor_rotacao

        #Carcaça da bomba de óleo
        self.montagem_carcaca_bomb_oleo_pre_torque = montagem_carcaca_bomb_oleo_pre_torque
        self.montagem_carcaca_bomb_oleo_torque = montagem_carcaca_bomb_oleo_torque

        #Conjunto da bomba na transmissão
        self.montagem_conjunto_bomba_pre_torque = montagem_conjunto_bomba_pre_torque
        self.montagem_conjunto_bomba_torque = montagem_conjunto_bomba_torque

        #Parafuso do eixo seletor
        self.montagem_parafuso_eixo = montagem_parafuso_eixo

        #Parafuso do trocador de calor
        self.montagem_parafuso_trocador = montagem_parafuso_trocador

        #Parafusos da coroa (dif. de Ferro Fundido)
        self.montagem_parafuso_coroa_ferro = montagem_parafuso_coroa_ferro

        #Parafusos da coroa (dif. de Alumínio)
        self.montagem_parafuso_coroa_aluminio = montagem_parafuso_coroa_aluminio

        #Parfusos da chave seletora (CMF)
        self.montagem_parafuso_chave_seletora = montagem_parafuso_chave_seletora

        #Parfusos do sensor do velocímetro
        self.montagem_parafuso_velocimetro = montagem_parafuso_velocimetro

        #Parfusos do controle de débito do permutador
        self.montagem_parafuso_controle = montagem_parafuso_controle

    def __repr__(self):
        return '<Pessoa %r>' % self.montagem_id


class Teste_final(db.Model):

    __tablename__ = 'teste_final'
    
    teste_final_id = db.Column(db.Integer,primary_key=True)
    teste_final_ordem = db.Column(db.String(50),nullable=False)
    teste_final_op = db.Column(db.String(50))
    teste_final_modelo = db.Column(db.String(50))
    teste_final_conversor_torque = db.Column(db.String(50))
    teste_final_data = db.Column(db.String(50))
    teste_final_serie = db.Column(db.String(50))
    teste_final_nome = db.Column(db.String(50))    

    #VERIFICAR SE NÃO HÁ CÓDIGOS DE AVARIA
    teste_final_verificar_avaria = db.Column(db.String(3))

    #VERIFICAR SE NÃO HÁ RUÍDOS(DIFERENCIAL)
    teste_final_verificar_ruido = db.Column(db.String(3))

    #TESTE PRESSURIZADO DE VAZAMENTO DE ÓLEO
    teste_final_pressurizado_oleo = db.Column(db.String(3))

    #INSTALAR TRAVA NO CONVERSOR DE TORQUE / TRAVA PARA TRANSPORTE
    teste_final_instalar_trava = db.Column(db.String(3))

    #AVISOS E OBSERVAÇÕES / ANEXAR FOLHAS DE AVISOS - CONCESSIONÁRIO
    teste_final_avisos_observacoes = db.Column(db.String(3))

    #PRESSÃO DE LINHA
    teste_final_pressao_linha = db.Column(db.String(3))
    teste_final_pressao_linha_valor = db.Column(db.String(50))

    #AFERIÇÃO DO NÍVEL DE ÓLEO
    teste_final_afericao_oleo_valor = db.Column(db.String(50))

    #TESTE DO SISTEMA PARKIN
    teste_final_sistema_parkin = db.Column(db.String(3))

    #VALIDAÇÃO DO TESTE
    teste_final_validacao = db.Column(db.String(3))

    #Observação
    teste_final_observacao = db.Column(db.String(50))

    def __init__(self,teste_final_ordem,teste_final_op,teste_final_modelo,teste_final_conversor_torque,teste_final_data,teste_final_serie,teste_final_nome,teste_final_verificar_avaria,teste_final_verificar_ruido,teste_final_pressurizado_oleo,teste_final_instalar_trava,teste_final_avisos_observacoes,teste_final_pressao_linha,teste_final_pressao_linha_valor,teste_final_afericao_oleo_valor,teste_final_sistema_parkin,teste_final_validacao,teste_final_observacao):
        
        self.teste_final_ordem = teste_final_ordem
        self.teste_final_op = teste_final_op
        self.teste_final_modelo = teste_final_modelo
        self.teste_final_conversor_torque = teste_final_conversor_torque
        self.teste_final_data = teste_final_data
        self.teste_final_serie = teste_final_serie
        self.teste_final_nome = teste_final_nome

        #VERIFICAR SE NÃO HÁ CÓDIGOS DE AVARIA
        self.teste_final_verificar_avaria = teste_final_verificar_avaria

        #VERIFICAR SE NÃO HÁ RUÍDOS(DIFERENCIAL)
        self.teste_final_verificar_ruido = teste_final_verificar_ruido

        #TESTE PRESSURIZADO DE VAZAMENTO DE ÓLEO
        self.teste_final_pressurizado_oleo = teste_final_pressurizado_oleo

        #INSTALAR TRAVA NO CONVERSOR DE TORQUE / TRAVA PARA TRANSPORTE
        self.teste_final_instalar_trava = teste_final_instalar_trava

        #AVISOS E OBSERVAÇÕES / ANEXAR FOLHAS DE AVISOS - CONCESSIONÁRIO
        self.teste_final_avisos_observacoes = teste_final_avisos_observacoes

        #PRESSÃO DE LINHA
        self.teste_final_pressao_linha = teste_final_pressao_linha
        self.teste_final_pressao_linha_valor = teste_final_pressao_linha_valor

        #AFERIÇÃO DO NÍVEL DE ÓLEO
        self.teste_final_afericao_oleo_valor = teste_final_afericao_oleo_valor

        #TESTE DO SISTEMA PARKIN
        self.teste_final_sistema_parkin = teste_final_sistema_parkin

        #VALIDAÇÃO DO TESTE
        self.teste_final_validacao = teste_final_validacao

        #Observação
        self.teste_final_observacao = teste_final_observacao

    def __repr__(self):
        return '<Pessoa %r>' % self.teste_final_id