from flask import Flask, render_template, request, url_for, redirect
from models import app, db, Inspecao, Montagem, Teste_final, Expedicao, Desmontagem, Inspecao1, Inspecao2
from werkzeug.utils import secure_filename
from flask_cors import CORS

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/" )
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/expedicao", methods= ['POST', 'GET'])
def expedicao():
    
    if request.method == 'POST':

        #CABEÇALHO 
        osexpedicao = request.form.get('osExpedicao')
        opexdicao =  request.form.get('opExpedicao')
        modeloexpedicao = request.form.get('modeloExpedicao')
        dataexpedicao = request.form.get('dataExpedicao')
        serieexpedicao = request.form.get('serieExpedicao')

        conversortorqueexpedicao = request.form.get('conversorTorqueExpedicao')
        if not conversortorqueexpedicao:
            conversortorqueexpedicao = "Não"

        #BODY DA PAGINA
        porcaconveror = request.form.get('porcaConversor')
        if not porcaconveror:
            porcaconveror = "Não"

        chapainercia = request.form.get('chapaInercia')
        if not chapainercia:
            chapainercia = "Não"

        sensorrotacaoentrada = request.form.get('sensorRotacaoEntrada') 
        if not sensorrotacaoentrada:
            sensorrotacaoentrada = "Não"

        sensorrotacaosaida = request.form.get('sensorRotacaoSaida')
        if not sensorrotacaosaida:
            sensorrotacaosaida = "Não"

        sensorrotacaotampa = request.form.get('sensorRotacaoTampa')
        if not sensorrotacaotampa:
            sensorrotacaotampa = "Não"

        sensorpressao = request.form.get('sensorPressao')
        if not sensorpressao:
            sensorpressao = "Não"

        sensorpressaoquebrado = request.form.get('sensorPressoaQuebrado')
        if not sensorpressaoquebrado:
            sensorpressaoquebrado = "Não"

        reguladorfluxo = request.form.get('reguladorFluxo')
        if not reguladorfluxo:
            reguladorfluxo = "Não"

        reguladorquebrado = request.form.get('reguladorQuebrado')
        if not reguladorquebrado:
            reguladorquebrado = "Não"

        trocadorcalor = request.form.get('trocadorCalor')
        if not trocadorcalor:
            trocadorcalor = "Não"

        trocadorcaloramassado = request.form.get('trocadorCalorAmassado')
        if not trocadorcaloramassado:
            trocadorcaloramassado = "Não"

        sensorvelocimetro = request.form.get('sensorVelocimetro')
        if not sensorvelocimetro:
            sensorvelocimetro = "Não"

        sensorvelocimetroquebrado = request.form.get('sensorVelocimetroQuebrado')
        if not sensorvelocimetroquebrado:
            sensorvelocimetroquebrado = "Não"

        sensorvelocimetrotampa = request.form.get('sensorVelocimetroTampa')
        if not sensorvelocimetrotampa:
            sensorvelocimetrotampa = "Não"

        chaveseletora = request.form.get('chaveSeletora')
        if not chaveseletora:
            chaveseletora = "Não"

        chaveseletoraquebrado = request.form.get('chaveSeletoraQuebrado')
        if not chaveseletoraquebrado:
            chaveseletoraquebrado = "Não"

        sensorrotacaomotor = request.form.get('sensorRotacaoMotor')
        if not sensorrotacaomotor:
            sensorrotacaomotor = "Não"

        sensorrotacaomotorquebrado = request.form.get('sensorRotacaoMotorQuebrado')
        if not sensorrotacaomotorquebrado:
            sensorrotacaomotorquebrado = "Não"

        tubovaretaoleo = request.form.get('tuboVaretaOleo')
        if not tubovaretaoleo:
            tubovaretaoleo = "Não"

        caixatransferencia = request.form.get('caixaTransferencia')
        if not caixatransferencia:
            caixatransferencia = "Não"

        mangueirastubos = request.form.get('mangueirasTubos')
        if not mangueirastubos:
            mangueirastubos = "Não"

        sensoresexternos = request.form.get('sensoresExternos')
        if not sensoresexternos:
            sensoresexternos = "Não"

        alavancaseletora = request.form.get('alavancaSeletora')
        if not alavancaseletora:
            alavancaseletora = "Não"

        caixaconectores = request.form.get('caixaConectores')
        if not caixaconectores:
            caixaconectores = "Não"

        caixaconectoresquebrados = request.form.get('caixaConectoresQuebrados')
        if not caixaconectoresquebrados:
            caixaconectoresquebrados = "Não"

        suporteconectores = request.form.get('suporteConectores')
        if not suporteconectores:
            suporteconectores = "Não"

        respiro = request.form.get('respiro')
        if not respiro:
            respiro = "Não"

        bujaonivel = request.form.get('bujaoNivel')
        if not bujaonivel:
            bujaonivel = "Não"

        suportecaboseletor = request.form.get('suporteCaboSeletor')
        if not suportecaboseletor:
            suportecaboseletor = "Não"

        guiadacarcaca = request.form.get('guiaDaCarcaca')
        if not guiadacarcaca:
            guiadacarcaca = "Não"

        guiaquantidade = request.form.get('guiaQuantidade')

        prisioneirocarcaca = request.form.get('prisioneiroCarcaca')
        if not prisioneirocarcaca:
            prisioneirocarcaca = "Não"

        suportecoximinferior = request.form.get('suporteCoximInferior')
        if not suportecoximinferior:
            suportecoximinferior = "Não"

        suportelevantamento = request.form.get('suporteLevantamento')
        if not suportelevantamento:
            suportelevantamento = "Não"

        varetaoleo = request.form.get('varetaOleo')
        if not varetaoleo:
            varetaoleo = "Não"

        coxins = request.form.get('coxins')
        if not coxins:
            coxins = "Não"

        chicoteexternos = request.form.get('chicoteExternos')
        if not chicoteexternos:
            chicoteexternos = "Não"

        eixossaida = request.form.get('eixosSaida')
        if not eixossaida:
            eixossaida = "Não"
        # RODA PÉ
        observacaoexpedicao = request.form.get('observacaoExpedicao')
        imagem = request.files.get('inserirFoto1')
        expedicao_image = imagem.read()
        expedicao_name = imagem.filename
        expedicao_mimetype = imagem.mimetype

        salvar_expedicao = Expedicao(osexpedicao, opexdicao, modeloexpedicao, dataexpedicao, serieexpedicao, conversortorqueexpedicao, porcaconveror, chapainercia, sensorrotacaoentrada, sensorrotacaosaida, sensorrotacaotampa, sensorpressao, sensorpressaoquebrado, reguladorfluxo, reguladorquebrado, trocadorcalor, trocadorcaloramassado, sensorvelocimetro, sensorvelocimetroquebrado, sensorvelocimetrotampa, chaveseletora, chaveseletoraquebrado, sensorrotacaomotor, sensorrotacaomotorquebrado, tubovaretaoleo, caixatransferencia, mangueirastubos, sensoresexternos, alavancaseletora, caixaconectores, caixaconectoresquebrados, suporteconectores, respiro, bujaonivel, suportecaboseletor, guiadacarcaca, guiaquantidade, prisioneirocarcaca, suportecoximinferior, suportelevantamento, varetaoleo, coxins, chicoteexternos, eixossaida, observacaoexpedicao, expedicao_image,expedicao_name,expedicao_mimetype)
        db.session.add(salvar_expedicao)
        db.session.commit()
    return render_template('expedicao.html')

@app.route("/desmontagem", methods= ['POST', 'GET'])
def desmontagem():

    if request.method == 'POST':

        os_desmontagem = request.form.get('os_desmontagem')
        op_desmontagem = request.form.get('op_desmontagem')
        modelo_desmontagem = request.form.get('modelo_desmontagem')
        data_desmontagem = request.form.get('data_desmontagem')
        serie_desmontagem = request.form.get('serie_desmontagem')
        conver_torque_desmontagem = request.form.get('conver_torque_desmontagem')
        
        vazamento_conversor_desmontagem = request.form.get('vazamento_conversor_desmontagem')
        if not vazamento_conversor_desmontagem:
            vazamento_conversor_desmontagem = "Não"
        
        vazamento_carter_desmontagem = request.form.get('vazamento_carter_desmontagem')
        if not vazamento_carter_desmontagem:
            vazamento_carter_desmontagem = "Não"

        vazamento_entre_carcacas_desmontagem = request.form.get('vazamento_entre_carcacas_desmontagem')
        if not vazamento_entre_carcacas_desmontagem:
            vazamento_entre_carcacas_desmontagem = "Não"

        vazamento_saida_desmontagem = request.form.get('vazamento_saida_desmontagem')
        if not vazamento_saida_desmontagem:
            vazamento_saida_desmontagem = "Não"
            
        vazamento_obs_desmontagem = request.form.get('vazamento_obs_desmontagem')
       
        oleo_limpo_desmontagem = request.form.get('oleo_limpo_desmontagem')
        if not oleo_limpo_desmontagem:
            oleo_limpo_desmontagem = "Não"

        oleo_queimado_desmontagem = request.form.get('oleo_queimado_desmontagem')
        if not oleo_queimado_desmontagem:
            oleo_queimado_desmontagem = "Não"

        oleo_contaminado_desmontagem = request.form.get('oleo_contaminado_desmontagem')
        if not oleo_contaminado_desmontagem:
            oleo_contaminado_desmontagem = "Não"

        oleo_obs_desmontagem = request.form.get('oleo_obs_desmontagem')
        
        ced_disco_aco_desmontagem = request.form.get('ced_disco_aco_desmontagem')
        if not ced_disco_aco_desmontagem:
            ced_disco_aco_desmontagem = "Não"

        ced_disco_revestido_desmontagem = request.form.get('ced_disco_revestido_desmontagem')
        if not ced_disco_revestido_desmontagem:
            ced_disco_revestido_desmontagem = "Não"

        ced_gasto_desmontagem = request.form.get('ced_gasto_desmontagem')
        if not ced_gasto_desmontagem:
            ced_gasto_desmontagem = "Não"

        ced_obs_desmontagem = request.form.get('ced_obs_desmontagem')
        
        pistoes_rasgado_desmontagem = request.form.get('pistoes_rasgado_desmontagem')
        if not pistoes_rasgado_desmontagem:
            pistoes_rasgado_desmontagem = "Não"

        pistoes_gasto_desmontagem = request.form.get('pistoes_gasto_desmontagem')
        if not pistoes_gasto_desmontagem:
            pistoes_gasto_desmontagem = "Não"

        pistoes_obs_desmontagem = request.form.get('pistoes_obs_desmontagem')
       
        bdo_engregaem_quebrada_desmontagem = request.form.get('bdo_engregaem_quebrada_desmontagem')
        if not bdo_engregaem_quebrada_desmontagem:
            bdo_engregaem_quebrada_desmontagem = "Não"

        bdo_desgaste_desmontagem = request.form.get('bdo_desgaste_desmontagem')
        if not bdo_desgaste_desmontagem:
            bdo_desgaste_desmontagem = "Não"

        bdo_bucha_rol_desmontagem = request.form.get('bdo_desgaste_desmontagem')
        if not bdo_bucha_rol_desmontagem:
            bdo_bucha_rol_desmontagem = "Não"

        bdo_obs_desmontagem = request.form.get('bdo_obs_desmontagem')

        planetario_dentes_quebrado_desmontagem = request.form.get('planetario_dentes_quebrado_desmontagem')
        if not planetario_dentes_quebrado_desmontagem:
            planetario_dentes_quebrado_desmontagem  = "Não"

        planetario_fundida_desmontagem = request.form.get('planetario_fundida_desmontagem')
        if not planetario_fundida_desmontagem:
            planetario_fundida_desmontagem = "Não"

        planetario_obs_desmontagem = request.form.get('planetario_obs_desmontagem')
    
        rolamento_danificado_desmontagem = request.form.get('rolamento_danificado_desmontagem')
        if not rolamento_danificado_desmontagem:
            rolamento_danificado_desmontagem = "Não"

        rolamento_danificado_quebrado = request.form.get('rolamento_danificado_quebrado')
        if not rolamento_danificado_quebrado:
            rolamento_danificado_quebrado = "Não"

        rolamento_obs_desmontagem = request.form.get('rolamento_obs_desmontagem')
        
        carter_amassado_desmontagem = request.form.get('carter_amassado_desmontagem')
        if not carter_amassado_desmontagem:
            carter_amassado_desmontagem = "Não"

        carter_quebrado_desmontagem = request.form.get('carter_quebrado_desmontagem')
        if not carter_quebrado_desmontagem:
            carter_quebrado_desmontagem = "Não"

        carter_obs_desmontagem = request.form.get('carter_obs_desmontagem')
        
        carcaca_dan_capa_seca_desmontagem = request.form.get('carcaca_dan_capa_seca_desmontagem')
        if not carcaca_dan_capa_seca_desmontagem:
            carcaca_dan_capa_seca_desmontagem = "Não"

        carcaca_dan_principal_desmontagem = request.form.get('carcaca_dan_principal_desmontagem')
        if not carcaca_dan_principal_desmontagem:
            carcaca_dan_principal_desmontagem = "Não"

        carcaca_dan_tampa_desmontagem = request.form.get('carcaca_dan_tampa_desmontagem')
        if not carcaca_dan_tampa_desmontagem:
            carcaca_dan_tampa_desmontagem = "Não"

        carcarca_dan_obs_desmontagem = request.form.get('carcarca_dan_obs_desmontagem')

        cinta_freio_queimada_desmontagem = request.form.get('cinta_freio_queimada_desmontagem')
        if not cinta_freio_queimada_desmontagem:
            cinta_freio_queimada_desmontagem = "Não"

        cinta_freio_quebrada_desmontagem = request.form.get('cinta_freio_quebrada_desmontagem')
        if not cinta_freio_quebrada_desmontagem:
            cinta_freio_quebrada_desmontagem = "Não"

        cinta_freio_gasta_desmontagem = request.form.get('cinta_freio_gasta_desmontagem')
        if not cinta_freio_gasta_desmontagem:
            cinta_freio_gasta_desmontagem = "Não"

        cinta_freio_obs_desmontagem = request.form.get('cinta_freio_obs_desmontagem')
        
        tambores_queimada_desmontagem = request.form.get('tambores_queimada_desmontagem')
        if not tambores_queimada_desmontagem:
            tambores_queimada_desmontagem = "Não"

        tambores_quebrados_desmontagem = request.form.get('tambores_quebrados_desmontagem')
        if not tambores_quebrados_desmontagem:
            tambores_quebrados_desmontagem = "Não"

        tambores_gasta_desmontagem = request.form.get(' tambores_gasta_desmontagem')
        if not  tambores_gasta_desmontagem:
             tambores_gasta_desmontagem = "Não"

        tambores_obs_desmontagem = request.form.get('tambores_obs_desmontagem')

        eixos_estrias_danificada_desmontagem = request.form.get('eixos_estrias_danificada_desmontagem')
        if not eixos_estrias_danificada_desmontagem:
            eixos_estrias_danificada_desmontagem = "Não"

        eixos_ponta_danificada_desmontagem = request.form.get('eixos_ponta_danificada_desmontagem')
        if not eixos_ponta_danificada_desmontagem:
            eixos_ponta_danificada_desmontagem = "Não"

        eixos_estrias_gasta_desmontagem = request.form.get('eixos_estrias_gasta_desmontagem')
        if not eixos_estrias_gasta_desmontagem:
            eixos_estrias_gasta_desmontagem = "Não"

        eixos_sup_vedacao_danif_desmontagem = request.form.get('eixos_sup_vedacao_danif_desmontagem')
        if not eixos_sup_vedacao_danif_desmontagem:
            eixos_sup_vedacao_danif_desmontagem = "Não"

        eixos_obs_desmontagem = request.form.get('eixos_obs_desmontagem')
        

        coroa_danificado_desmontagem = request.form.get('coroa_danificado_desmontagem')
        if not coroa_danificado_desmontagem:
            coroa_danificado_desmontagem = "Não"

        coroa_obs_desmontagem = request.form.get('coroa_obs_desmontagem')
        
        filtro_quebrado_desmontagem = request.form.get('filtro_quebrado_desmontagem')
        if not filtro_quebrado_desmontagem:
            filtro_quebrado_desmontagem = "Não"

        filtro_amassado_desmontagem = request.form.get('filtro_amassado_desmontagem')
        if not filtro_amassado_desmontagem:
            filtro_amassado_desmontagem = "Não"
        
        filtro_obs_desmontagem = request.form.get('filtro_obs_desmontagem')

        obser_obs_desmontagem = request.form.get('obser_obs_desmontagem')
        imagem_desmontagem = request.files.get('selecionar_foto_desmontagem')
        selecionar_image = imagem_desmontagem.read()
        selecionar_name_desmontagem  = imagem_desmontagem.filename
        selecionar_foto_desmontagem = imagem_desmontagem.mimetype

        salvar_desmontagem = Desmontagem(os_desmontagem, op_desmontagem, modelo_desmontagem, data_desmontagem, serie_desmontagem, conver_torque_desmontagem, vazamento_conversor_desmontagem, vazamento_carter_desmontagem, vazamento_entre_carcacas_desmontagem, vazamento_saida_desmontagem, vazamento_obs_desmontagem, oleo_limpo_desmontagem, oleo_queimado_desmontagem, oleo_contaminado_desmontagem, oleo_obs_desmontagem, ced_disco_aco_desmontagem, ced_disco_revestido_desmontagem, ced_gasto_desmontagem, ced_obs_desmontagem, pistoes_rasgado_desmontagem, pistoes_gasto_desmontagem, pistoes_obs_desmontagem, bdo_engregaem_quebrada_desmontagem, bdo_desgaste_desmontagem, bdo_bucha_rol_desmontagem, bdo_obs_desmontagem, planetario_dentes_quebrado_desmontagem, planetario_fundida_desmontagem, planetario_obs_desmontagem, rolamento_danificado_desmontagem, rolamento_danificado_quebrado, rolamento_obs_desmontagem, carter_amassado_desmontagem, carter_quebrado_desmontagem, carter_obs_desmontagem, carcaca_dan_capa_seca_desmontagem, carcaca_dan_principal_desmontagem, carcaca_dan_tampa_desmontagem, carcarca_dan_obs_desmontagem, cinta_freio_queimada_desmontagem, cinta_freio_quebrada_desmontagem, cinta_freio_gasta_desmontagem, cinta_freio_obs_desmontagem, tambores_queimada_desmontagem, tambores_quebrados_desmontagem, tambores_gasta_desmontagem, tambores_obs_desmontagem, eixos_estrias_danificada_desmontagem, eixos_ponta_danificada_desmontagem, eixos_estrias_gasta_desmontagem, eixos_sup_vedacao_danif_desmontagem, eixos_obs_desmontagem, coroa_danificado_desmontagem, coroa_obs_desmontagem, filtro_quebrado_desmontagem, filtro_amassado_desmontagem, filtro_obs_desmontagem, obser_obs_desmontagem, selecionar_image, selecionar_name_desmontagem, selecionar_foto_desmontagem)
        db.session.add(salvar_desmontagem)
        db.session.commit()
    return render_template('desmontagem.html')

@app.route("/inspecao", methods= ['POST', 'GET'])
def inspecao():

    if request.method == 'POST':

        os_insp = request.form.get('os_insp')
        op_insp = request.form.get('op_insp')
        modelo_insp = request.form.get('modelo_insp')
        conversor_insp = request.form.get('conversor_insp')
        data_insp = request.form.get('data_insp')
        serie_insp = request.form.get('serie_insp')
        nome_insp = request.form.get('nome_insp')

        carc_p_trincas = request.form.get('carc_p_trincas')
        if not carc_p_trincas:
            carc_p_trincas = "Não"
        carc_p_rolamentos = request.form.get('carc_p_rolamentos')
        if not carc_p_rolamentos:
            carc_p_rolamentos = "Não"
        carc_p_alojamento = request.form.get('carc_p_alojamento ')
        if not carc_p_alojamento:
            carc_p_alojamento = "Não"
        carc_p_alojamento_ac = request.form.get('carc_p_alojamento_ac')
        if not carc_p_alojamento_ac:
            carc_p_alojamento_ac = "Não"
        carc_p_alojamento_rts = request.form.get('carc_p_alojamento_rts')
        if not carc_p_alojamento_rts:
            carc_p_alojamento_rts = "Não"
        carc_p_fhpcf2f3 = request.form.get('carc_p_fhpcf2f3')
        if not carc_p_fhpcf2f3:
            carc_p_fhpcf2f3 = "Não"
        carc_p_capa_rolam = request.form.get('carc_p_capa_rolam')
        if not carc_p_capa_rolam:
            carc_p_capa_rolam = "Não"
        carc_p_guias = request.form.get('carc_p_guias')
        if not carc_p_guias:
            carc_p_guias = "Não"
        carc_p_superficies_vedacao = request.form.get('carc_p_superficies_vedacao')
        if not carc_p_superficies_vedacao:
            carc_p_superficies_vedacao = "Não"

        bomb_sce = request.form.get('bomb_sce')
        if not bomb_sce:
            bomb_sce = "Não"
        bomb_guias = request.form.get('bomb_guias')
        if not bomb_guias:
            bomb_guias = "Não"
        bomb_riscos = request.form.get('bomb_riscos')
        if not bomb_riscos:
            bomb_riscos = "Não"
        bomb_desgaste_b = request.form.get('bomb_desgaste_b')

        bomb_dcb = request.form.get('bomb_dcb')
        if not bomb_dcb:
            bomb_dcb = "Não"
        bomb_demm = request.form.get('bomb_demm')
        if not bomb_demm:
            bomb_demm = "Não"
        bomb_elaem = request.form.get('bomb_elaem')
        if not bomb_elaem:
            bomb_elaem = "Não"
        bomb_desgaste = request.form.get('bomb_desgaste')
        if not bomb_desgaste:
            bomb_desgaste = "Não"
        bomb_desgaste_eixo = request.form.get('bomb_desgaste_eixo')

        tamb_descoloracao = request.form.get('tamb_descoloracao')
        if not tamb_descoloracao:
            tamb_descoloracao = "Não"
        tamb_scf = request.form.get('tamb_scf')
        if not tamb_scf:
            tamb_scf = "Não"
        tamb_scb = request.form.get('tamb_scb')
        if not tamb_scb:
            tamb_scb = "Não"
        tamb_cav = request.form.get('tamb_cav')
        if not tamb_cav:
            tamb_cav = "Não"
        tamb_estrias = request.form.get('tamb_estrias')
        if not tamb_estrias:
            tamb_estrias = "Não"
        tamb_desgaste = request.form.get('tamb_desgaste')

        tamb2_descoloracao = request.form.get('tamb2_descoloracao')
        if not tamb2_descoloracao:
            tamb2_descoloracao = "Não"
        tamb2_scf = request.form.get('tamb2_scf')
        if not tamb2_scf:
            tamb2_scf = "Não"
        tamb2_d_quebrados = request.form.get('tamb2_d_quebrados')
        if not tamb2_d_quebrados:
            tamb2_d_quebrados = "Não"
        tamb2_rad = request.form.get('tamb2_rad')
        if not tamb2_rad:
            tamb2_rad = "Não"
        tamb2_estrias = request.form.get('tamb2_estrias')
        if not tamb2_estrias:
            tamb2_estrias = "Não"

        dife_trincas = request.form.get('dife_trincas')
        if not dife_trincas:
            dife_trincas = "Não"
        dife_rolamento = request.form.get('dife_rolamento')
        if not dife_rolamento:
            dife_rolamento = "Não"
        dife_sca = request.form.get('dife_sca')
        if not dife_sca:
            dife_sca = "Não"
        dife_estrias = request.form.get('dife_estrias')
        if not dife_estrias:
            dife_estrias = "Não"
        dife_daep = request.form.get('dife_daep')
        if not dife_daep:
            dife_daep = "Não"
        dife_des = request.form.get('dife_des')
        if not dife_des:
            dife_des = "Não"
        dife_dcr = request.form.get('dife_dcr')
        if not  dife_dcr:
             dife_dcr = "Não"
        dife_ds = request.form.get('dife_ds')
        if not dife_ds:
             dife_ds = "Não"

        suportem_derretimento = request.form.get('suportem_derretimento')
        if not suportem_derretimento:
            suportem_derretimento = "Não"
        suportem_deformação = request.form.get('suportem_deformação')
        if not suportem_deformação:
            suportem_deformação = "Não"
        surpotem_empenamento = request.form.get('surpotem_empenamento')
        if not surpotem_empenamento:
            surpotem_empenamento = "Não"

        hast_dhp = request.form.get('hast_dhp')
        if not hast_dhp:
            hast_dhp = "Não"
        hast_tma = request.form.get('hast_tma')
        if not hast_tma:
            hast_tma = "Não"
        hast_oxidacao = request.form.get('hast_oxidacao')
        if not hast_oxidacao:
            hast_oxidacao = "Não"

        disc_queima = request.form.get('disc_queima')
        if not disc_queima:
            disc_queima = "Não"
        disc_desg = request.form.get('disc_desg')
        if not disc_desg:
            disc_desg = "Não"
        disc_empen = request.form.get('disc_empen')
        if not  disc_empen:
             disc_empen = "Não"
        disc_deform = request.form.get('disc_deform')
        if not disc_deform:
              disc_deform = "Não"

        pistao_tq = request.form.get('pistao_tq')
        if not pistao_tq:
            pistao_tq = "Não"
        pistao_desgaste = request.form.get('pistao_desgaste')
        if not pistao_desgaste:
            pistao_desgaste = "Não"
        pistao_cas = request.form.get('pistao_cas')
        if not pistao_cas:
            pistao_cas = "Não "
        pistao_em = request.form.get('pistao_em')
        if not pistao_em:
            pistao_em = "Não"

        caixa_c_quebras = request.form.get('caixa_c_quebras')
        if not caixa_c_quebras:
            caixa_c_quebras = "Não"
        caixa_c_trincas = request.form.get('caixa_c_trincas')
        if not caixa_c_trincas:
            caixa_c_trincas = "Não"
        caixa_c_ft = request.form.get('caixa_c_ft')
        if not caixa_c_ft:
            caixa_c_ft = "Não"

        sensor_derretimento = request.form.get('sensor_derretimento')
        if not sensor_derretimento:
            sensor_derretimento = "Não"
        sensor_estado_cabo = request.form.get('sensor_estado_cabo')
        if not sensor_estado_cabo:
            sensor_estado_cabo = "Não"
        sensor_e_conector = request.form.get('sensor_e_conector')
        if not sensor_e_conector:
            sensor_e_conector = "Não"

        sensor_p_trincas = request.form.get('sensor_p_trincas')
        if not sensor_p_trincas:
            sensor_p_trincas = "Não"
        sensor_p_presencao = request.form.get('sensor_p_presencao')
        if not sensor_p_presencao:
            sensor_p_presencao = "Não"
        sensor_p_estado = request.form.get('sensor_p_estado')
        if not sensor_p_estado:
            sensor_p_estado = "Não"
        sensor_p_estado_conector = request.form.get('sensor_p_estado_conector')
        if not sensor_p_estado_conector:
            sensor_p_estado_conector = "Não"

        chapa_empenamento = request.form.get('chapa_empenamento')
        if not chapa_empenamento:
            chapa_empenamento = "Não"
        chapa_amassados = request.form.get('chapa_amassados')
        if not chapa_amassados:
            chapa_amassados = "Não"
        chapa_oxidacao = request.form.get('chapa_oxidacao')
        if not chapa_oxidacao:
            chapa_oxidacao = "Não"

        capa_trincas = request.form.get('capa_trincas')
        if not capa_trincas:
            capa_trincas = "Não"
        capa_rosca = request.form.get('capa_rosca')
        if not capa_rosca:
            capa_rosca = "Não"
        capa_rolamentos = request.form.get('capa_rolamentos')
        if not capa_rolamentos:
            capa_rolamentos = "Não"
        capa_abo = request.form.get('capa_abo')
        if not capa_abo:
            capa_abo = "Não"
        capa_ars = request.form.get('capa_ars')
        if not capa_ars:
            capa_ars = "Não"
        capa_sv = request.form.get('capa_sv ')
        if not capa_sv:
            capa_sv = "Não"

        tampa_tq = request.form.get('tampa_tq')
        if not tampa_tq:
            tampa_tq = "Não"
        tampa_rosca = request.form.get('tampa_rosca')
        if not tampa_rosca:
            tampa_rosca = "Não"
        tampa_apf1 = request.form.get('tampa_apf1')
        if not tampa_apf1:
            tampa_apf1 = "Não"
        tampa_svj = request.form.get('tampa_svj')
        if not tampa_svj:
            tampa_svj = "Não"
        tampa_scb = request.form.get('tampa_scb')
        if not tampa_scb:
            tampa_scb = "Não"
        tampa_aneis = request.form.get('tampa_aneis')
        if not tampa_aneis:
            tampa_aneis = "Não"

        placa_trincas = request.form.get('placa_trincas')
        if not placa_trincas:
            placa_trincas = "Não"
        placa_roscas = request.form.get('placa_roscas')
        if not placa_roscas:
            placa_roscas = "Não"
        placa_riscos = request.form.get('placa_riscos')
        if not placa_riscos:
            placa_riscos = "Não"
        placa_desgaste = request.form.get('placa_desgaste')
        

        cubo_scbs = request.form.get('cubo_scbs')
        if not cubo_scbs:
            cubo_scbs = "Não"
        cubo_estrias = request.form.get('cubo_estrias')
        if not cubo_estrias:
            cubo_estrias = "Não"
        cubo_ram = request.form.get('cubo_ram')
        if not cubo_ram:
            cubo_ram = "Não"
        cubo_dba = request.form.get('cubo_dba')
        
    
        conjunto_descolo = request.form.get('conjunto_descolo')
        if not conjunto_descolo:
            conjunto_descolo = "Não"
        conjunto_dentes = request.form.get('conjunto_dentes')
        if not conjunto_dentes:
            conjunto_dentes = "Não"
        conjunto_roscas = request.form.get('conjunto_roscas')
        if not conjunto_roscas:
            conjunto_roscas = "Não"
        conjunto_sccr = request.form.get('conjunto_sccr')
        if not conjunto_sccr:
            conjunto_sccr = "Não"
        conjunto_dr = request.form.get('conjunto_dr')
        if not conjunto_dr:
            conjunto_dr = "Não"
        conjunto_oxidacao = request.form.get('conjunto_oxidacao')
        if not conjunto_oxidacao:
            conjunto_oxidacao = "Não"
        conjunto_desgaste = request.form.get('conjunto_desgaste')
        
    
        tambor_descoloracao = request.form.get('tambor_descoloracao')
        if not tambor_descoloracao:
            tambor_descoloracao = "Não"
        tambor_entalhe = request.form.get('tambor_entalhe')
        if not tambor_entalhe:
            tambor_entalhe = "Não"
        tambor_estrias = request.form.get('tambor_estrias')
        if not tambor_estrias:
            tambor_estrias = "Não"
        tambor_alojamento = request.form.get('tambor_alojamento')
        if not tambor_alojamento:
            tambor_alojamento = "Não"
        tambor_sat = request.form.get('tambor_sat')
        if not tambor_sat:
            tambor_sat = "Não"
    
        pinhao_rolamentos = request.form.get('pinhao_rolamentos')
        if not pinhao_rolamentos:
            pinhao_rolamentos = "Não"
        pinhao_gr = request.form.get('pinhao_gr')
        if not pinhao_gr:
            pinhao_gr = "Não"
        pinhao_ram = request.form.get('pinhao_ram')
        if not pinhao_ram:
            pinhao_ram = "Não"

        emgrenagem_descoloracao = request.form.get('emgrenagem_descoloracao')
        if not emgrenagem_descoloracao:
            emgrenagem_descoloracao = "Não"
        emgrenagem_estrias = request.form.get('emgrenagem_estrias')
        if not emgrenagem_estrias:
            emgrenagem_estrias = "Não"
        emgrenagem_dq = request.form.get('emgrenagem_dq')
        if not emgrenagem_dq:
            emgrenagem_dq = "Não"

        suporte_e_descoloracao = request.form.get('suporte_e_descoloracao')
        if not suporte_e_descoloracao:
            suporte_e_descoloracao = "Não"
        suporte_e_eede = request.form.get('suporte_e_eede')
        if not suporte_e_eede:
            suporte_e_eede = "Não"
        suporte_e_dq = request.form.get('suporte_e_dq')
        if not suporte_e_dq:
            suporte_e_dq = "Não"

        cinta_f_ef = request.form.get('cinta_f_ef')
        if not cinta_f_ef:
            cinta_f_ef = "Não"
        cinta_f_craf = request.form.get('cinta_f_craf')
        if not cinta_f_craf:
            cinta_f_craf = "Não"
        cinta_f_queima = request.form.get('cinta_f_queima')
        if not cinta_f_queima:
            cinta_f_queima = "Não"
        cinta_f_deformacao = request.form.get('cinta_f_deformacao')
        if not cinta_f_deformacao:
            cinta_f_deformacao = "Não"
        cinta_f_ancoragem = request.form.get('cinta_f_ancoragem')
        if not cinta_f_ancoragem:
            cinta_f_ancoragem = "Não"

        rolamento_dcp = request.form.get('rolamento_dcp')
        if not rolamento_dcp:
            rolamento_dcp = "Não"
        rolamento_qpr = request.form.get('rolamento_qpr')
        if not rolamento_qpr:
             rolamento_qpr = "Não"

        control_trincas = request.form.get('control_trincas')
        if not control_trincas:
            control_trincas = "Não"
        control_estados = request.form.get('control_estados')
        if not control_estados:
             control_estados = "Não"
        control_estado = request.form.get('control_estado')
        if not control_estados:
            control_estados = "Não"

        respiro_rasgos = request.form.get('respiro_rasgos')
        if not respiro_rasgos:
            respiro_rasgos = "Não"
        respiro_presenca = request.form.get('respiro_presenca')
        if not respiro_presenca:
            respiro_presenca = "Não"
        respiro_deformacao = request.form.get('respiro_deformacao')
        if not respiro_deformacao:
            respiro_deformacao = "Não"

        chave_sc_quebras = request.form.get('chave_sc_quebras')
        if not chave_sc_quebras:
            chave_sc_quebras = "Não"
        chave_sc_vdfd = request.form.get('chave_sc_vdfd')
        if not chave_sc_vdfd:
            chave_sc_vdfd = "Não"
        chave_sc_ec = request.form.get('chave_sc_ec')
        if not chave_sc_ec:
            chave_sc_ec = "Não"
        chave_sc_ect = request.form.get('chave_sc_ect')
        if not chave_sc_ect:
            chave_sc_ect = "Não"
        chave_sc_etpa = request.form.get('chave_sc_etpa')
        if not chave_sc_etpa:
            chave_sc_etpa = "Não"

        compon_ps2 = request.form.get('compon_ps2')
        compon_eixoin = request.form.get('compon_eixoin')
        compon_bomba5 = request.form.get('compon_bomba5')
        compon_bomb2 = request.form.get('compon_bomb2')
        compon_bomb23 = request.form.get('compon_bomb23')
    
        compon_n1 = request.form.get('compon_n1')
        compon_n2 = request.form.get('compon_n2')
        compon_f3n1 = request.form.get('compon_f3n1')
        compon_f3n2 = request.form.get('compon_f3n2')

        compon_e1 = request.form.get('compon_e1')
        compon_vist_montador1 = request.form.get('compon_vist_montador1')
        compon_e2 = request.form.get('compon_e2')
        compon_visit_montador2 = request.form.get('compon_visit_montador2')
        compon_eixo_axial = request.form.get('compon_eixo_axial')
        compon_visit_montador3 = request.form.get('compon_visit_montador3')
        
        salvar_inspe = Inspecao1(os_insp, op_insp, modelo_insp, conversor_insp, data_insp, serie_insp, nome_insp, carc_p_trincas, carc_p_rolamentos, carc_p_alojamento, carc_p_alojamento_ac, carc_p_alojamento_rts, carc_p_fhpcf2f3, carc_p_capa_rolam, carc_p_guias, carc_p_superficies_vedacao, bomb_sce, bomb_guias, bomb_riscos, bomb_desgaste_b, bomb_dcb, bomb_demm, bomb_elaem, bomb_desgaste, bomb_desgaste_eixo, tamb_descoloracao, tamb_scf, tamb_scb, tamb_cav, tamb_estrias, tamb_desgaste, tamb2_descoloracao, tamb2_scf, tamb2_d_quebrados, tamb2_rad, tamb2_estrias, dife_trincas, dife_rolamento, dife_sca, dife_estrias, dife_daep, dife_des, dife_dcr, dife_ds, suportem_derretimento, suportem_deformação, surpotem_empenamento, hast_dhp, hast_tma, hast_oxidacao, disc_queima, disc_desg, disc_empen, disc_deform, pistao_tq, pistao_desgaste, pistao_cas, pistao_em, caixa_c_quebras, caixa_c_trincas, caixa_c_ft, sensor_derretimento, sensor_estado_cabo, sensor_e_conector, sensor_p_trincas, sensor_p_presencao, sensor_p_estado, sensor_p_estado_conector, chapa_empenamento, chapa_amassados, chapa_oxidacao, capa_trincas, capa_rosca, capa_rolamentos, capa_abo, capa_ars, capa_sv, tampa_tq, tampa_rosca, tampa_apf1, tampa_svj, tampa_scb, tampa_aneis, placa_trincas, placa_roscas, placa_riscos, placa_desgaste, cubo_scbs, cubo_estrias, cubo_ram, cubo_dba, conjunto_descolo, conjunto_dentes, conjunto_roscas, conjunto_sccr, conjunto_dr, conjunto_oxidacao, conjunto_desgaste, tambor_descoloracao, tambor_entalhe, tambor_estrias, tambor_alojamento, tambor_sat, pinhao_rolamentos, pinhao_gr, pinhao_ram, emgrenagem_descoloracao, emgrenagem_estrias, emgrenagem_dq, suporte_e_descoloracao, suporte_e_eede, suporte_e_dq, cinta_f_ef, cinta_f_craf, cinta_f_queima, cinta_f_deformacao, cinta_f_ancoragem, rolamento_dcp, rolamento_qpr, control_trincas, control_estados, control_estado, respiro_rasgos, respiro_presenca, respiro_deformacao, chave_sc_quebras, chave_sc_vdfd, chave_sc_ec, chave_sc_ect, chave_sc_etpa, compon_ps2, compon_eixoin, compon_bomba5, compon_bomb2, compon_bomb23, compon_n1, compon_n2, compon_f3n1, compon_f3n2, compon_e1, compon_vist_montador1, compon_e2, compon_visit_montador2, compon_eixo_axial, compon_visit_montador3)
        db.session.add(salvar_inspe)
        db.session.commit()
    return render_template('inspecao.html')

@app.route("/inspecao_1", methods= ['POST','GET'])
def inspecao_1():
    
    if request.method == 'POST':

        Inspecao_ordem = request.form.get('inspecao_ordem')
        Inspecao_op = request.form.get('inspecao_op')
        Inspecao_modelo = request.form.get('inspecao_modelo')
        Inspecao_conversor_toque = request.form.get('inspecao_conversor_torque')
        Inspecao_data = request.form.get('inspecao_data')
        Inspecao_serie = request.form.get('inspecao_serie')
        Inspecao_nome = request.form.get('inspecao_nome')

        #Carcaça Principal
        Inspecao_carcaca_trinca_quebras = request.form.get('inspecao_carcaca_ctrinca_quebras')
        if not Inspecao_carcaca_trinca_quebras:
            Inspecao_carcaca_trinca_quebras = "Não"
        
        Inspecao_carcaca_rolamentos = request.form.get('inspecao_carcaca_rolamentos')
        if not Inspecao_carcaca_rolamentos:
            Inspecao_carcaca_rolamentos = "Não"

        Inspecao_carcaca_alojamento_pistao = request.form.get('inspecao_carcaca_alojamento_pistao')
        if not Inspecao_carcaca_alojamento_pistao:
            Inspecao_carcaca_alojamento_pistao = "Não"

        Inspecao_carcaca_alojamento_acumuladores = request.form.get('inspecao_carcaca_alojamento_acumuladores')
        if not Inspecao_carcaca_alojamento_acumuladores:
            Inspecao_carcaca_alojamento_acumuladores = "Não"

        Inspecao_carcaca_alojamento_retentores = request.form.get('inspecao_carcaca_alojamento_retentores')
        if not Inspecao_carcaca_alojamento_retentores:
            Inspecao_carcaca_alojamento_retentores = "Não"

        Inspecao_carcaca_furo_hastes_pistoes = request.form.get('inspecao_carcaca_furo_hastes_pistoes')
        if not Inspecao_carcaca_furo_hastes_pistoes:
            Inspecao_carcaca_furo_hastes_pistoes = "Não"

        Inspecao_carcaca_capa_rolamentos = request.form.get('inspecao_carcaca_capa_rolamentos')
        if not Inspecao_carcaca_capa_rolamentos:
            Inspecao_carcaca_capa_rolamentos = "Não"

        Inspecao_carcaca_guias_carcaca = request.form.get('inspecao_carcaca_guias_carcaca')
        if not Inspecao_carcaca_guias_carcaca:
            Inspecao_carcaca_guias_carcaca = "Não"
        
        Inspecao_carcaca_superficies_vedacao = request.form.get('inspecao_carcaca_superficies_vedacao')
        if not Inspecao_carcaca_superficies_vedacao:
            Inspecao_carcaca_superficies_vedacao = "Não"

        #Bomba de Óleo
        Inspecao_bomb_oleo_superficies_contato_engrenagens = request.form.get('inspecao_bomb_oleo_superficies_contato_engrenagens')
        if not Inspecao_bomb_oleo_superficies_contato_engrenagens:
            Inspecao_bomb_oleo_superficies_contato_engrenagens = "Não"
        
        Inspecao_bomb_oleo_guias = request.form.get('inspecao_bomb_oleo_guias')
        if not Inspecao_bomb_oleo_guias:
            Inspecao_bomb_oleo_guias = "Não"

        Inspecao_bomb_oleo_riscos = request.form.get('inspecao_bomb_oleo_riscos')
        if not Inspecao_bomb_oleo_riscos:
            Inspecao_bomb_oleo_riscos = "Não"
        
        Inspecao_bomb_oleo_diametro_bucha = request.form.get('inspecao_bomb_oleo_diametro_bucha')
        
        Inspecao_bomb_oleo_desgaste_chapa_bomba = request.form.get('inspecao_bomb_oleo_desgaste_chapa_bomba')
        if not Inspecao_bomb_oleo_desgaste_chapa_bomba:
            Inspecao_bomb_oleo_desgaste_chapa_bomba = "Não"

        Inspecao_bomb_oleo_desgaste_engrangem_motora = request.form.get('inspecao_bomb_oleo_desgaste_engrangem_motora')
        if not Inspecao_bomb_oleo_desgaste_engrangem_motora:
            Inspecao_bomb_oleo_desgaste_engrangem_motora = "Não"
        
        Inspecao_bomb_oleo_estado_lingueta = request.form.get('inspecao_bomb_oleo_estado_lingueta')
        if not Inspecao_bomb_oleo_estado_lingueta:
            Inspecao_bomb_oleo_estado_lingueta = "Não"

        #Eixo Entrada
        Inspecao_eixo_entrada_superficie_contato = request.form.get('inspecao_eixo_entrada_superficie_contato')
        if not Inspecao_eixo_entrada_superficie_contato:
            Inspecao_eixo_entrada_superficie_contato = "Não"
        
        Inspecao_eixo_entrada_estrias = request.form.get('inspecao_eixo_entrada_estrias')
        if not Inspecao_eixo_entrada_estrias:
            Inspecao_eixo_entrada_estrias = "Não"
        
        Inspecao_eixo_entrada_alojamento_pistao = request.form.get('inspecao_eixo_entrada_alojamento_pistao')
        if not Inspecao_eixo_entrada_alojamento_pistao:
            Inspecao_eixo_entrada_alojamento_pistao = "Não"
        
        Inspecao_eixo_entrada_contato_anel_vedacao = request.form.get('inspecao_eixo_entrada_contato_anel_vedacao')
        if not Inspecao_eixo_entrada_contato_anel_vedacao:
            Inspecao_eixo_entrada_contato_anel_vedacao = "Não"

        Inspecao_eixo_entrada_diametro_bucha = request.form.get('inspecao_eixo_entrada_diametro_bucha')

        #Tambor C1
        Inspecao_tambor_c1_descoloracao = request.form.get('inspecao_tambor_c1_descoloracao')
        if not Inspecao_tambor_c1_descoloracao:
            Inspecao_tambor_c1_descoloracao = "Não"

        Inspecao_tambor_c1_entalhe_encaixe = request.form.get('inspecao_tambor_c1_entalhe_encaixe')
        if not Inspecao_tambor_c1_entalhe_encaixe:
            Inspecao_tambor_c1_entalhe_encaixe = "Não"
        
        Inspecao_tambor_c1_estrias = request.form.get('inspecao_tambor_c1_estrias')
        if not Inspecao_tambor_c1_estrias:
            Inspecao_tambor_c1_estrias = "Não"
        
        Inspecao_tambor_c1_alojamento_pistao = request.form.get('inspecao_tambor_c1_alojamento_pistao')
        if not Inspecao_tambor_c1_alojamento_pistao:
            Inspecao_tambor_c1_alojamento_pistao = "Não"
        
        Inspecao_tambor_c1_sup_apoio_trava = request.form.get('inspecao_tambor_c1_sup_apoio_trava')
        if not Inspecao_tambor_c1_sup_apoio_trava:
            Inspecao_tambor_c1_sup_apoio_trava = "Não"

        #Tambor B1
        Inspecao_tambor_b1_descoloracao = request.form.get('inspecao_tambor_b1_descoloracao')
        if not Inspecao_tambor_b1_descoloracao:
            Inspecao_tambor_b1_descoloracao = "Não"
        
        Inspecao_tambor_b1_entalhe_encaixe = request.form.get('inspecao_tambor_b1_entalhe_encaixe')
        if not Inspecao_tambor_b1_entalhe_encaixe:
            Inspecao_tambor_b1_entalhe_encaixe = "Não"
        
        Inspecao_tambor_b1_estrias = request.form.get('inspecao_tambor_b1_estrias')
        if not Inspecao_tambor_b1_estrias:
            Inspecao_tambor_b1_estrias = "Não"
        
        Inspecao_tambor_b1_alojamento_pistao = request.form.get('inspecao_tambor_b1_alojamento_pistao')
        if not Inspecao_tambor_b1_alojamento_pistao:
            Inspecao_tambor_b1_alojamento_pistao = "Não"

        Inspecao_tambor_b1_sup_apoio_trava = request.form.get('inspecao_tambor_b1_sup_apoio_trava')
        if not Inspecao_tambor_b1_sup_apoio_trava:
            Inspecao_tambor_b1_sup_apoio_trava = "Não"

        #Conjunto C2
        Inspecao_conjunto_c2_descoloracao = request.form.get('inspecao_conjunto_c2_descoloracao')
        if not Inspecao_conjunto_c2_descoloracao:
            Inspecao_conjunto_c2_descoloracao = "Não"
        
        Inspecao_conjunto_c2_entalhe_encaixe = request.form.get('inspecao_conjunto_c2_entalhe_encaixe')
        if not Inspecao_conjunto_c2_entalhe_encaixe:
            Inspecao_conjunto_c2_entalhe_encaixe = "Não"
        
        Inspecao_conjunto_c2_estrias = request.form.get('inspecao_conjunto_c2_estrias')
        if not Inspecao_conjunto_c2_estrias:
            Inspecao_conjunto_c2_estrias = "Não"
        
        Inspecao_conjunto_c2_alojamento_pistao = request.form.get('inspecao_conjunto_c2_alojamento_pistao')
        if not Inspecao_conjunto_c2_alojamento_pistao:
            Inspecao_conjunto_c2_alojamento_pistao = "Não"
        
        Inspecao_conjunto_c2_sup_apoio_trava = request.form.get('inspecao_conjunto_c2_sup_apoio_trava')
        if not Inspecao_conjunto_c2_sup_apoio_trava:
            Inspecao_conjunto_c2_sup_apoio_trava = "Não"

        #Diferencial 
        Inspecao_diferencial_trincas_quebras = request.form.get('inspecao_diferencial_trincas_quebras')
        if not Inspecao_diferencial_trincas_quebras:
            Inspecao_diferencial_trincas_quebras = "Não"

        Inspecao_diferencial_rolamento = request.form.get('inspecao_diferencial_rolamento')
        if not Inspecao_diferencial_rolamento:
            Inspecao_diferencial_rolamento = "Não"
        
        Inspecao_diferencial_superficies_arruelas = request.form.get('inspecao_diferencial_superficies_arruelas')
        if not Inspecao_diferencial_superficies_arruelas:
            Inspecao_diferencial_superficies_arruelas = "Não"
        
        Inspecao_diferencial_estrias = request.form.get('inspecao_diferencial_estrias')
        if not Inspecao_diferencial_estrias:
            Inspecao_diferencial_estrias = "Não"
        
        Inspecao_diferencial_desgaste_arruela = request.form.get('inspecao_diferencial_desgaste_arruela')
        if not Inspecao_diferencial_desgaste_arruela:
            Inspecao_diferencial_desgaste_arruela = "Não"
        
        Inspecao_diferencial_desgaste_eixo = request.form.get('inspecao_diferencial_desgaste_eixo')
        if not Inspecao_diferencial_desgaste_eixo:
            Inspecao_diferencial_desgaste_eixo = "Não"

        Inspecao_diferencial_desgaste_capa = request.form.get('inspecao_diferencial_desgaste_capa')
        if not Inspecao_diferencial_desgaste_capa:
            Inspecao_diferencial_desgaste_capa = "Não"
        
        Inspecao_diferencial_desgaste_satelite = request.form.get('inspecao_diferencial_desgaste_satelite')
        if not Inspecao_diferencial_desgaste_satelite:
            Inspecao_diferencial_desgaste_satelite = "Não"

        #Mola de Retorno
        Inspecao_mola_retorno_oxidacao = request.form.get('inspecao_mola_retorno_oxidacao')
        if not Inspecao_mola_retorno_oxidacao:
            Inspecao_mola_retorno_oxidacao = "Não"
        
        Inspecao_mola_retorno_deformacao = request.form.get('inspecao_mola_retorno_deformacao')
        if not Inspecao_mola_retorno_deformacao:
            Inspecao_mola_retorno_deformacao = "Não"
        
        Inspecao_mola_retorno_empenamento = request.form.get('inspecao_mola_retorno_empenamento')
        if not Inspecao_mola_retorno_empenamento:
            Inspecao_mola_retorno_empenamento = "Não"

        #Hastes dos Pistões
        Inspecao_haste_pistao_desgaste_haste = request.form.get('inspecao_haste_pistao_desgaste_haste')
        if not Inspecao_haste_pistao_desgaste_haste:
            Inspecao_haste_pistao_desgaste_haste = "Não"
        
        Inspecao_haste_pistao_componentes = request.form.get('inspecao_haste_pistao_componentes')
        if not Inspecao_haste_pistao_componentes:
            Inspecao_haste_pistao_componentes = "Não"
        
        Inspecao_haste_pistao_oxidacao = request.form.get('inspecao_haste_pistao_oxidacao')
        if not Inspecao_haste_pistao_oxidacao:
            Inspecao_haste_pistao_oxidacao = "Não"

        #Discos de Embreagem
        Inspecao_disco_embreagem_queima = request.form.get('inspecao_disco_embreagem_queima')
        if not Inspecao_disco_embreagem_queima:
            Inspecao_disco_embreagem_queima = "Não"
        
        Inspecao_disco_embreagem_desgaste = request.form.get('inspecao_disco_embreagem_desgaste')
        if not Inspecao_disco_embreagem_desgaste:
            Inspecao_disco_embreagem_desgaste = "Não"

        Inspecao_disco_embreagem_empenamento = request.form.get('inspecao_disco_embreagem_empenamento')
        if not Inspecao_disco_embreagem_empenamento:
            Inspecao_disco_embreagem_empenamento = "Não"
        
        Inspecao_disco_embreagem_deformacao = request.form.get('inspecao_disco_embreagem_deformacao')
        if not Inspecao_disco_embreagem_deformacao:
            Inspecao_disco_embreagem_deformacao = "Não"

        #Pistão de Acionamento B1
        Inspecao_pistao_trinca_quebra = request.form.get('inspecao_pistao_trinca_quebra')
        if not Inspecao_pistao_trinca_quebra:
            Inspecao_pistao_trinca_quebra = "Não"
        
        Inspecao_pistao_desgaste = request.form.get('inspecao_pistao_desgaste')
        if not Inspecao_pistao_desgaste:
            Inspecao_pistao_desgaste = "Não"
        
        Inspecao_pistao_canais_aneis = request.form.get('inspecao_pistao_canais_aneis')
        if not Inspecao_pistao_canais_aneis:
            Inspecao_pistao_canais_aneis = "Não"

        Inspecao_pistao_estado_mola = request.form.get('inspecao_pistao_estado_mola')
        if not Inspecao_pistao_estado_mola:
            Inspecao_pistao_estado_mola = "Não"

        #Conectores
        Inspecao_conectores_quebra = request.form.get('inspecao_conectores_quebra')
        if not Inspecao_conectores_quebra:
            Inspecao_conectores_quebra = "Não"
        
        Inspecao_conectores_trincas = request.form.get('inspecao_conectores_trincas')
        if not Inspecao_conectores_trincas:
            Inspecao_conectores_trincas = "Não"

        Inspecao_conectores_oxidacao = request.form.get('insepcao_conectores_oxidacao')
        if not Inspecao_conectores_oxidacao:
            Inspecao_conectores_oxidacao = "Não"

        #Sensor de Rotação de Entrada
        Inspecao_sensor_rotacao_derretimento = request.form.get('inspecao_sensor_rotacao_derretimento')
        if not Inspecao_sensor_rotacao_derretimento:
            Inspecao_sensor_rotacao_derretimento = "Não"
        
        Inspecao_sensor_rotacao_estado_cabo = request.form.get('inspecao_sensor_rotacao_estado_cabo')
        if not Inspecao_sensor_rotacao_estado_cabo:
            Inspecao_sensor_rotacao_estado_cabo = "Não"
        
        Inspecao_sensor_rotacao_estado_conector = request.form.get('insepcao_sensor_rotacao_estado_conector')
        if not Inspecao_sensor_rotacao_estado_conector:
            Inspecao_sensor_rotacao_estado_conector = "Não"

        #Sensor de Pressão
        Inspecao_sensor_pressao1_trinca_quebra = request.form.get('inspecao_sensor_pressao1_trinca_quebra')
        if not Inspecao_sensor_pressao1_trinca_quebra:
            Inspecao_sensor_pressao1_trinca_quebra = "Não"

        Inspecao_sensor_pressao1_presenca_esfera = request.form.get('inspecao_sensor_pressao1_presenca_esfera')
        if not Inspecao_sensor_pressao1_presenca_esfera:
            Inspecao_sensor_pressao1_presenca_esfera = "Não"
        
        Inspecao_sensor_pressao1_estado_cabo = request.form.get('inspecao_sensor_pressao1_estado_cabo')
        if not Inspecao_sensor_pressao1_estado_cabo:
            Inspecao_sensor_pressao1_estado_cabo = "Não"
        
        Inspecao_sensor_pressao1_estado_conector = request.form.get('inspecao_sensor_pressao1_estado_conector')
        if not Inspecao_sensor_pressao1_estado_conector:
            Inspecao_sensor_pressao1_estado_conector = "Não"

        #Capa Seca
        Inspecao_capa_seca_trinca_quebra = request.form.get('inspecao_capa_seca_trinca_quebra')
        if not Inspecao_capa_seca_trinca_quebra:
            Inspecao_capa_seca_trinca_quebra = "Não"

        Inspecao_capa_seca_rocas = request.form.get('inspecao_capa_seca_rocas')
        if not Inspecao_capa_seca_rocas:
            Inspecao_capa_seca_rocas = "Não"
        
        Inspecao_capa_seca_capa_rolamento = request.form.get('inspecao_capa_seca_capa_rolamento')
        if not Inspecao_capa_seca_capa_rolamento:
            Inspecao_capa_seca_capa_rolamento = "Não"
        
        Inspecao_capa_seca_alojamento_bomb_oleo = request.form.get('inspecao_capa_seca_alojamento_bomb_oleo')
        if not Inspecao_capa_seca_alojamento_bomb_oleo:
            Inspecao_capa_seca_alojamento_bomb_oleo = "Não"
        
        Inspecao_capa_seca_alojamento_retentores = request.form.get('inspecao_capa_seca_alojamento_retentores')
        if not Inspecao_capa_seca_alojamento_retentores:
            Inspecao_capa_seca_alojamento_retentores = "Não"
        
        Inspecao_capa_seca_superficie_vedacao = request.form.get('inspecao_capa_seca_superficie_vedacao')
        if not Inspecao_capa_seca_superficie_vedacao:
            Inspecao_capa_seca_superficie_vedacao = "Não"

        #Tampa Traseira
        Inspecao_tampa_traseira_trinca_quebra = request.form.get('inspecao_tampa_traseira_trinca_quebra')
        if not Inspecao_tampa_traseira_trinca_quebra:
            Inspecao_tampa_traseira_trinca_quebra = "Não"
        
        Inspecao_tampa_traseira_roscas = request.form.get('inspecao_tampa_traseira_roscas')
        if not Inspecao_tampa_traseira_roscas:
            Inspecao_tampa_traseira_roscas = "Não"
        
        Inspecao_tampa_traseira_alojamentos = request.form.get('inspecao_tampa_traseira_alojamentos')
        if not Inspecao_tampa_traseira_alojamentos:
            Inspecao_tampa_traseira_alojamentos = "Não"
        
        Inspecao_tampa_traseira_superficie_vedacao = request.form.get('inspecao_tampa_traseira_superficie_vedacao')
        if not Inspecao_tampa_traseira_superficie_vedacao:
            Inspecao_tampa_traseira_superficie_vedacao = "Não"
        
        Inspecao_tampa_traseira_superficie_contato = request.form.get('inspecao_tampa_traseira_superficie_contato')
        if not Inspecao_tampa_traseira_superficie_contato:
            Inspecao_tampa_traseira_superficie_contato = "Não"
        
        Inspecao_tampa_traseira_aneis = request.form.get('inspecao_tampa_traseira_aneis')
        if not Inspecao_tampa_traseira_aneis:
            Inspecao_tampa_traseira_aneis = "Não"

        #Placa da Bomba
        Inspecao_placa_bomba_trinca_quebra = request.form.get('inspecao_placa_bomba_trinca_quebra')
        if not Inspecao_placa_bomba_trinca_quebra:
            Inspecao_placa_bomba_trinca_quebra = "Não"
        
        Inspecao_placa_bomba_roscas = request.form.get('inspecao_placa_bomba_roscas')
        if not Inspecao_placa_bomba_roscas:
            Inspecao_placa_bomba_roscas = "Não"
        
        Inspecao_placa_bomba_riscos = request.form.get('inspecao_placa_bomba_riscos')
        if not Inspecao_placa_bomba_riscos:
            Inspecao_placa_bomba_riscos = "Não"

        Inspecao_placa_bomba_diametro_bucha = request.form.get('inspecao_placa_bomba_diametro_bucha')

        #Cubo da Carcaça
        Inspecao_cubo_rolamento = request.form.get('inspecao_cubo_rolamento')
        if not Inspecao_cubo_rolamento:
            Inspecao_cubo_rolamento = "Não"

        Inspecao_cubo_apoio_anel = request.form.get('inspecao_cubo_apoio_anel')
        if not Inspecao_cubo_apoio_anel:
            Inspecao_cubo_apoio_anel = "Não"
        
        Inspecao_cubo_rolamento_axial = request.form.get('inspecao_cubo_rolamento_axial')
        if not Inspecao_cubo_rolamento_axial:
            Inspecao_cubo_rolamento_axial = "Não"
        
        Inspecao_cubo_diametro_bucha = request.form.get('inspecao_cubo_diametro_bucha')

        #Conjunto de Planetárias
        Inspecao_planetaria_descoloracao = request.form.get('inspecao_planetaria_descoloracao')
        if not Inspecao_planetaria_descoloracao:
            Inspecao_planetaria_descoloracao = "Não"

        Inspecao_planetaria_dente = request.form.get('inspecao_planetaria_dente')
        if not Inspecao_planetaria_dente:
            Inspecao_planetaria_dente = "Não"

        Inspecao_planetaria_roscas = request.form.get('inspecao_planetaria_roscas')
        if not Inspecao_planetaria_roscas:
            Inspecao_planetaria_roscas = "Não"
        
        Inspecao_planetaria_superficie_contato = request.form.get('inspecao_planetaria_superficie_contato')
        if not Inspecao_planetaria_superficie_contato:
            Inspecao_planetaria_superficie_contato = "Não"
        
        Inspecao_planetaria_desgaste_rolamento = request.form.get('inspecao_planetaria_desgaste_rolamento')
        if not Inspecao_planetaria_desgaste_rolamento:
            Inspecao_planetaria_desgaste_rolamento = "Não"
        
        Inspecao_planetaria_oxidacao = request.form.get('inspecao_planetaria_oxidacao')
        if not Inspecao_planetaria_oxidacao:
            Inspecao_planetaria_oxidacao = "Não"
        
        Inspecao_planetaria_diamentro_bucha = request.form.get('inspecao_planetaria_diamentro_bucha')

        #Tambor C3
        Inspecao_tambor_c3_descoloracao = request.form.get('inspecao_tambor_c3_descoloracao')
        if not Inspecao_tambor_c3_descoloracao:
            Inspecao_tambor_c3_descoloracao = "Não"
        
        Inspecao_tambor_c3_entalhe_encaixe = request.form.get('inspecao_tambor_c3_entalhe_encaixe')
        if not Inspecao_tambor_c3_entalhe_encaixe:
            Inspecao_tambor_c3_entalhe_encaixe = "Não"
        
        Inspecao_tambor_c3_estrias = request.form.get('inspecao_tambor_c3_estrias')
        if not Inspecao_tambor_c3_estrias:
            Inspecao_tambor_c3_estrias = "Não"
        
        Inspecao_tambor_c3_alojamento_pistao = request.form.get('inspecao_tambor_c3_alojamento_pistao')
        if not Inspecao_tambor_c3_alojamento_pistao:
            Inspecao_tambor_c3_alojamento_pistao = "Não"
        
        Inspecao_tambor_c3_sup_apoio_trava = request.form.get('inspecao_tambor_c3_sup_apoio_trava')
        if not Inspecao_tambor_c3_sup_apoio_trava:
            Inspecao_tambor_c3_sup_apoio_trava = "Não"

        #Conjunto B2
        Inspecao_conjunto_b2_descoloracao = request.form.get('inspecao_conjunto_b2_descoloracao')
        if not Inspecao_conjunto_b2_descoloracao:
            Inspecao_conjunto_b2_descoloracao = "Não"
        
        Inspecao_conjunto_b2_entalhe_encaixe = request.form.get('inspecao_conjunto_b2_entalhe_encaixe')
        if not Inspecao_conjunto_b2_entalhe_encaixe:
            Inspecao_conjunto_b2_entalhe_encaixe = "Não"
        
        Inspecao_conjunto_b2_estrias = request.form.get('inspecao_conjunto_b2_estrias')
        if not Inspecao_conjunto_b2_estrias:
            Inspecao_conjunto_b2_estrias = "Não"
        
        Inspecao_conjunto_b2_alojamento_pistao = request.form.get('inspecao_conjunto_b2_alojamento_pistao')
        if not Inspecao_conjunto_b2_alojamento_pistao:
            Inspecao_conjunto_b2_alojamento_pistao = "Não"
        
        Inspecao_conjunto_b2_sup_apoio_trava = request.form.get('inspecao_conjunto_b2_sup_apoio_trava')    
        if not Inspecao_conjunto_b2_sup_apoio_trava:
            Inspecao_conjunto_b2_sup_apoio_trava = "Não"

        #Pinhão
        Inspecao_pinhao_rolamento = request.form.get('inspecao_pinhao_rolamento')
        if not Inspecao_pinhao_rolamento:
            Inspecao_pinhao_rolamento = "Não"
        
        Inspecao_pinhao_gaiola = request.form.get('inspecao_pinhao_gaiola')
        if not Inspecao_pinhao_gaiola:
            Inspecao_pinhao_gaiola = "Não"
        
        Inspecao_pinhao_rolamento_axial = request.form.get('inspecao_pinhao_rolamento_axial')
        if not Inspecao_pinhao_rolamento_axial:
            Inspecao_pinhao_rolamento_axial = "Não"

        #Engranagem Solar
        Inspecao_engrenagem_rolamento = request.form.get('inspecao_engrenagem_rolamento')
        if not Inspecao_engrenagem_rolamento:
            Inspecao_engrenagem_rolamento = "Não"
        
        Inspecao_engrenagem_gaiola = request.form.get('inspecao_engrenagem_gaiola')
        if not Inspecao_engrenagem_gaiola:
            Inspecao_engrenagem_gaiola = "Não"
        
        Inspecao_engrenagem_rolamento_axial = request.form.get('inspecao_engrenagem_rolamento_axial')
        if not Inspecao_engrenagem_rolamento_axial:
            Inspecao_engrenagem_rolamento_axial = "Não"

        #Suporte de Engrenagem Solar
        Inspecao_sup_engrenagem_descoloracao = request.form.get('inspecao_sup_engrenagem_descoloracao')
        if not Inspecao_sup_engrenagem_descoloracao:
            Inspecao_sup_engrenagem_descoloracao = "Não"
        
        Inspecao_sup_engrenagem_entalhe_encaixe = request.form.get('inspecao_sup_engrenagem_entalhe_encaixe')
        if not Inspecao_sup_engrenagem_entalhe_encaixe:
            Inspecao_sup_engrenagem_entalhe_encaixe = "Não"
        
        Inspecao_sup_engrenagem_dente = request.form.get('inspecao_sup_engrenagem_dente')
        if not Inspecao_sup_engrenagem_dente:
            Inspecao_sup_engrenagem_dente = "Não"

        #Rolamentos axiais e Calços
        Inspecao_rolamentos_axiais_derretimentos = request.form.get('inspecao_rolamentos_axiais_derretimentos')
        if not Inspecao_rolamentos_axiais_derretimentos:
            Inspecao_rolamentos_axiais_derretimentos = "Não"
        
        Inspecao_rolamentos_axiais_quebra_pista = request.form.get('inspecao_rolamentos_axiais_quebra_pista')
        if not Inspecao_rolamentos_axiais_quebra_pista:
            Inspecao_rolamentos_axiais_quebra_pista = "Não"

        #Trocador de Calor
        Inspecao_trocador_trinca_quebra = request.form.get('inspecao_trocador_trinca_quebra')
        if not Inspecao_trocador_trinca_quebra:
            Inspecao_trocador_trinca_quebra = "Não"
        
        Inspecao_trocador_furo_interno = request.form.get('inspecao_trocador_furo_interno')
        if not Inspecao_trocador_furo_interno:
            Inspecao_trocador_furo_interno = "Não"

        #Respiro
        Inspecao_respiro_rasgos = request.form.get('inspecao_respiro_rasgos')
        if not Inspecao_respiro_rasgos:
            Inspecao_respiro_rasgos = "Não"
        
        Inspecao_respiro_presenca_tampa = request.form.get('inspecao_respiro_presenca_tampa')
        if not Inspecao_respiro_presenca_tampa:
            Inspecao_respiro_presenca_tampa = "Não"
        
        Inspecao_respiro_deformacao = request.form.get('inspecao_respiro_deformacao')
        if not Inspecao_respiro_deformacao:
            Inspecao_respiro_deformacao = "Não"

        #Chave Seletora
        Inspecao_chave_quebra = request.form.get('inspecao_chave_quebra')
        if not Inspecao_chave_quebra:
            Inspecao_chave_quebra = "Não"
        
        Inspecao_chave_estado_conector = request.form.get('inspecao_chave_estado_conector')
        if not Inspecao_chave_estado_conector:
            Inspecao_chave_estado_conector = "Não"
        
        Inspecao_chave_estado_terminal = request.form.get('inspecao_chave_estado_terminal')
        if not Inspecao_chave_estado_terminal:
            Inspecao_chave_estado_terminal = "Não"

        #Sensor de Pressão
        Inspecao_sensor_pressao2_trinca_quebra = request.form.get('inspecao_sensor_pressao2_trinca_quebra')
        if not Inspecao_sensor_pressao2_trinca_quebra:
            Inspecao_sensor_pressao2_trinca_quebra = "Não"
        
        Inspecao_sensor_pressao2_presenca_esfera = request.form.get('inspecao_sensor_pressao2_presenca_esfera')
        if not Inspecao_sensor_pressao2_presenca_esfera:
            Inspecao_sensor_pressao2_presenca_esfera = "Não"
        
        Inspecao_sensor_pressao2_estado_cabo = request.form.get('inspecao_sensor_pressao2_estado_cabo')
        if not Inspecao_sensor_pressao2_estado_cabo:
            Inspecao_sensor_pressao2_estado_cabo = "Não"
        
        Inspecao_sensor_pressao2_estado_conector = request.form.get('inspecao_snesor_pressao2_estado_conector')
        if not Inspecao_sensor_pressao2_estado_conector:
            Inspecao_sensor_pressao2_estado_conector = "Não"

        #Chapa Defletora de Óleo do Diferencial
        Inspecao_chapa_empenamento = request.form.get('inspecao_chapa_empenamento')
        if not Inspecao_chapa_empenamento:
            Inspecao_chapa_empenamento = "Não"
        
        Inspecao_chapa_amassado = request.form.get('inspecao_chapa_amassado')
        if not Inspecao_chapa_amassado:
            Inspecao_chapa_amassado = "Não"
        
        Inspecao_chapa_oxidacao = request.form.get('inspecao_chapa_oxidacao')
        if not Inspecao_chapa_oxidacao:
            Inspecao_chapa_oxidacao = "Não"

        #Informações Adicionais
        Inspecao_c1_observacao = request.form.get('inspecao_c1_observacao')
        Inspecao_c2_observacao = request.form.get('inspecao_c2_observacao')
        Inspecao_c3_observacao = request.form.get('inspecao_c3_observacao')
        Inspecao_b1_observacao = request.form.get('inspecao_b1_observacao')
        Inspecao_b2_observacao = request.form.get('inspecao_b2_observacao')
        Inspecao_suporte_observacao = request.form.get('inspecao_suporte_observacao')
        Inspecao_relacao_observacao = request.form.get('inspecao_relacao_observacao')
        Inspecao_bomba_observacao = request.form.get('inspecao_bomba_observacao')
        Inspecao_rolamentos_observacao = request.form.get('inspecao_rolamentos_observacao')

        #Ajuste
        Inspecao_c1_ajuste = request.form.get('inspecao_c1_ajuste')
        Inspecao_c1_visto = request.form.get('inspecao_c1_visto')
        Inspecao_c2_ajuste = request.form.get('inspecao_c2_ajuste')
        Inspecao_c2_visto = request.form.get('inspecao_c2_visto')
        Inspecao_c3_ajuste = request.form.get('inspecao_c3_ajuste')
        Inspecao_c3_visto = request.form.get('inspecao_c3_visto')
        Inspecao_b1_ajuste = request.form.get('inspecao_b1_ajuste')
        Inspecao_b1_visto = request.form.get('inspecao_b1_visto')
        Inspecao_b2_ajuste = request.form.get('inspecao_b2_ajuste')
        Inspecao_b2_visto = request.form.get('inspecao_b2_visto')    
        print(Inspecao_c1_ajuste)
        salva_inspecao = Inspecao(Inspecao_ordem,Inspecao_op,Inspecao_modelo,Inspecao_conversor_toque,Inspecao_data,Inspecao_serie,Inspecao_nome,Inspecao_carcaca_trinca_quebras,Inspecao_carcaca_rolamentos,Inspecao_carcaca_alojamento_pistao,Inspecao_carcaca_alojamento_acumuladores,Inspecao_carcaca_alojamento_retentores,Inspecao_carcaca_furo_hastes_pistoes,Inspecao_carcaca_capa_rolamentos,Inspecao_carcaca_guias_carcaca,Inspecao_carcaca_superficies_vedacao,Inspecao_bomb_oleo_superficies_contato_engrenagens,Inspecao_bomb_oleo_guias,Inspecao_bomb_oleo_riscos,Inspecao_bomb_oleo_diametro_bucha,Inspecao_bomb_oleo_desgaste_chapa_bomba,Inspecao_bomb_oleo_desgaste_engrangem_motora,Inspecao_bomb_oleo_estado_lingueta,Inspecao_eixo_entrada_superficie_contato,Inspecao_eixo_entrada_estrias,Inspecao_eixo_entrada_alojamento_pistao,Inspecao_eixo_entrada_contato_anel_vedacao,Inspecao_eixo_entrada_diametro_bucha,Inspecao_tambor_c1_descoloracao,Inspecao_tambor_c1_entalhe_encaixe,Inspecao_tambor_c1_estrias, Inspecao_tambor_c1_alojamento_pistao,Inspecao_tambor_c1_sup_apoio_trava,Inspecao_tambor_b1_descoloracao,Inspecao_tambor_b1_entalhe_encaixe,Inspecao_tambor_b1_estrias,Inspecao_tambor_b1_alojamento_pistao,Inspecao_tambor_b1_sup_apoio_trava,Inspecao_conjunto_c2_descoloracao,Inspecao_conjunto_c2_entalhe_encaixe,Inspecao_conjunto_c2_estrias,Inspecao_conjunto_c2_alojamento_pistao,Inspecao_conjunto_c2_sup_apoio_trava,Inspecao_diferencial_trincas_quebras,Inspecao_diferencial_rolamento,Inspecao_diferencial_superficies_arruelas,Inspecao_diferencial_estrias,Inspecao_diferencial_desgaste_arruela,Inspecao_diferencial_desgaste_eixo,Inspecao_diferencial_desgaste_capa,Inspecao_diferencial_desgaste_satelite,Inspecao_mola_retorno_oxidacao,Inspecao_mola_retorno_deformacao,Inspecao_mola_retorno_empenamento,Inspecao_haste_pistao_desgaste_haste,Inspecao_haste_pistao_componentes,Inspecao_haste_pistao_oxidacao,Inspecao_disco_embreagem_queima,Inspecao_disco_embreagem_desgaste,Inspecao_disco_embreagem_empenamento,Inspecao_disco_embreagem_deformacao,Inspecao_pistao_trinca_quebra,Inspecao_pistao_desgaste,Inspecao_pistao_canais_aneis,Inspecao_pistao_estado_mola,Inspecao_conectores_quebra,Inspecao_conectores_trincas,Inspecao_conectores_oxidacao,Inspecao_sensor_rotacao_derretimento,Inspecao_sensor_rotacao_estado_cabo,Inspecao_sensor_rotacao_estado_conector,Inspecao_sensor_pressao1_trinca_quebra,Inspecao_sensor_pressao1_presenca_esfera,Inspecao_sensor_pressao1_estado_cabo,Inspecao_sensor_pressao1_estado_conector,Inspecao_capa_seca_trinca_quebra,Inspecao_capa_seca_rocas,Inspecao_capa_seca_capa_rolamento,Inspecao_capa_seca_alojamento_bomb_oleo,Inspecao_capa_seca_alojamento_retentores,Inspecao_capa_seca_superficie_vedacao,Inspecao_tampa_traseira_trinca_quebra,Inspecao_tampa_traseira_roscas,Inspecao_tampa_traseira_alojamentos,Inspecao_tampa_traseira_superficie_vedacao,Inspecao_tampa_traseira_superficie_contato,Inspecao_tampa_traseira_aneis,Inspecao_placa_bomba_trinca_quebra,Inspecao_placa_bomba_roscas,Inspecao_placa_bomba_riscos,Inspecao_placa_bomba_diametro_bucha,Inspecao_cubo_rolamento,Inspecao_cubo_apoio_anel,Inspecao_cubo_rolamento_axial,Inspecao_cubo_diametro_bucha,Inspecao_planetaria_descoloracao,Inspecao_planetaria_dente,Inspecao_planetaria_roscas,Inspecao_planetaria_superficie_contato,Inspecao_planetaria_desgaste_rolamento,Inspecao_planetaria_oxidacao,Inspecao_planetaria_diamentro_bucha,Inspecao_tambor_c3_descoloracao,Inspecao_tambor_c3_entalhe_encaixe,Inspecao_tambor_c3_estrias,Inspecao_tambor_c3_alojamento_pistao,Inspecao_tambor_c3_sup_apoio_trava,Inspecao_conjunto_b2_descoloracao,Inspecao_conjunto_b2_entalhe_encaixe,Inspecao_conjunto_b2_estrias,Inspecao_conjunto_b2_alojamento_pistao,Inspecao_conjunto_b2_sup_apoio_trava,Inspecao_pinhao_rolamento,Inspecao_pinhao_gaiola,Inspecao_pinhao_rolamento_axial,Inspecao_engrenagem_rolamento,Inspecao_engrenagem_gaiola,Inspecao_engrenagem_rolamento_axial,Inspecao_sup_engrenagem_descoloracao,Inspecao_sup_engrenagem_entalhe_encaixe,Inspecao_sup_engrenagem_dente,Inspecao_rolamentos_axiais_derretimentos,Inspecao_rolamentos_axiais_quebra_pista,Inspecao_trocador_trinca_quebra,Inspecao_trocador_furo_interno,Inspecao_respiro_rasgos,Inspecao_respiro_presenca_tampa,Inspecao_respiro_deformacao,Inspecao_chave_quebra,Inspecao_chave_estado_conector,Inspecao_chave_estado_terminal,Inspecao_sensor_pressao2_trinca_quebra,Inspecao_sensor_pressao2_presenca_esfera,Inspecao_sensor_pressao2_estado_cabo,Inspecao_sensor_pressao2_estado_conector,Inspecao_chapa_empenamento,Inspecao_chapa_amassado,Inspecao_chapa_oxidacao,Inspecao_c1_observacao,Inspecao_c2_observacao,Inspecao_c3_observacao,Inspecao_b1_observacao,Inspecao_b2_observacao,Inspecao_suporte_observacao,Inspecao_relacao_observacao,Inspecao_bomba_observacao,Inspecao_rolamentos_observacao,Inspecao_c1_ajuste,Inspecao_c1_visto,Inspecao_c2_ajuste,Inspecao_c2_visto,Inspecao_c3_ajuste,Inspecao_c3_visto,Inspecao_b1_ajuste,Inspecao_b1_visto,Inspecao_b2_ajuste,Inspecao_b2_visto)
        db.session.add(salva_inspecao)
        db.session.commit()
    return render_template('inspecao_1.html')

@app.route("/inspecao_2", methods= ['POST', 'GET'])
def inspecao_2():

    if request.method == 'POST':
        os_insp2 = request.form.get('os_insp2')
        op_insp2 = request.form.get('op_insp2')
        modelo_insp2 = request.form.get('modelo_insp2')
        conversor_insp2 = request.form.get('conversor_insp2')
        data_inps2 = request.form.get('data_inps2')
        serie_insp2 = request.form.get('serie_insp2')
        nome_insp2 = request.form.get('nome_insp2')

        carc_trinca_insp2 = request.form.get('carc_trinca_insp2')
        if not carc_trinca_insp2:
            carc_trinca_insp2 = "Não"
        carc_rolam_insp2 = request.form.get('carc_rolam_insp2')
        if not carc_rolam_insp2:
            carc_rolam_insp2 = "Não"
        carc_aloj_insp2 = request.form.get('carc_aloj_insp2')
        if not carc_aloj_insp2:
            carc_aloj_insp2 = "Não"
        carc_acumu_insp2 = request.form.get('carc_acumu_insp2')
        if not carc_acumu_insp2:
            carc_acumu_insp2 = "Não"
        carc_reten_insp2 = request.form.get('carc_reten_insp2')
        if not carc_reten_insp2:
            carc_reten_insp2 = "Não"
        carc_pist_insp2 = request.form.get('carc_pist_insp2')
        if not carc_pist_insp2:
            carc_pist_insp2 = "Não"
        carc_capa_insp2 = request.form.get('carc_capa_insp2')
        if not carc_capa_insp2:
            carc_capa_insp2 = "Não"
        carc_guia_insp2 = request.form.get('carc_guia_insp2')
        if not carc_guia_insp2:
            carc_guia_insp2 = "Não"
        carc_veda_insp2 = request.form.get('carc_veda_insp2')
        if not carc_veda_insp2:
            carc_veda_insp2 = "Não"

        bomb_super_insp2 = request.form.get('bomb_super_insp2')
        if not bomb_super_insp2:
            bomb_super_insp2 = "Não"
        bomb_guia_insp2 = request.form.get('bomb_guia_insp2')
        if not bomb_guia_insp2:
            bomb_guia_insp2 = "Não"
        bomb_risco_inps2 = request.form.get('bomb_risco_inps2')
        if not bomb_risco_inps2:
            bomb_risco_inps2 = "Não"
        bomb_dia_insp2 = request.form.get('bomb_dia_insp2')
        
        bomb_desg_insp2 = request.form.get('bomb_desg_insp2')
        if not bomb_desg_insp2:
            bomb_desg_insp2 = "Não"
        bomb_eng_insp2 = request.form.get('bomb_eng_insp2')
        if not bomb_eng_insp2:
            bomb_eng_insp2 = "Não"
        bomb_estados_insp2 = request.form.get('bomb_estados_insp2')

        eixo_supr_insp2 = request.form.get('eixo_supr_insp2')
        if not eixo_supr_insp2:
            eixo_supr_insp2 = "Não"
        eixo_estrias_insp2 = request.form.get('eixo_estrias_insp2')
        if not eixo_estrias_insp2:
            eixo_estrias_insp2 = "Não"
        eixo_pist_insp2 = request.form.get('eixo_pist_insp2')
        if not eixo_pist_insp2:
            eixo_pist_insp2 = "Não"
        eixo_cont_insp2 = request.form.get('eixo_cont_insp2')
        if not eixo_cont_insp2:
             eixo_cont_insp2 = "Não"
        eixo_dia_insp2 = request.form.get('eixo_dia_insp2')

        tambor_desc_insp2 = request.form.get('tambor_desc_insp2')
        if not tambor_desc_insp2:
            tambor_desc_insp2 = "Não"
        tambor_ent_insp2 = request.form.get('tambor_ent_insp2')
        if not tambor_ent_insp2:
            tambor_ent_insp2 = "Não"
        tambor_estrias_insp2 = request.form.get('tambor_estrias_insp2')
        if not tambor_estrias_insp2:
            tambor_estrias_insp2 = "Não"
        tambor_pist_insp2 = request.form.get('tambor_pist_insp2')
        if not tambor_pist_insp2:
            tambor_pist_insp2 = "Não"
        tambor_sup_insp2 = request.form.get('tambor_sup_insp2')
        if not tambor_sup_insp2:
            tambor_sup_insp2 = "Não"

        tambor2_des_insp2 = request.form.get('tambor2_des_insp2')
        if not tambor2_des_insp2:
            tambor2_des_insp2 = "Não"
        tambor2_ent_insp2 = request.form.get('tambor2_ent_insp2')
        if not tambor2_ent_insp2:
            tambor2_ent_insp2 = "Não"
        tambor2_estrias_insp2 = request.form.get('tambor2_estrias_insp2') 
        if not tambor2_estrias_insp2:
            tambor2_estrias_insp2 = "Não"
        tambor2_pist_insp2 = request.form.get('tambor2_pist_insp2')
        if not tambor2_pist_insp2:
            tambor2_pist_insp2 = "Não"
        tambor2_trava_insp2 = request.form.get('tambor2_trava_insp2')
        if not tambor2_trava_insp2:
            tambor2_trava_insp2 = "Não" 

        tamb3_desc_insp2 = request.form.get('tamb3_desc_insp2')
        if not tamb3_desc_insp2:
            tamb3_desc_insp2 = "Não"
        tamb3_enc_insp2 = request.form.get('tamb3_enc_insp2')
        if not tamb3_enc_insp2:
            tamb3_enc_insp2 = "Não"
        tamb3_estrias_insp2 = request.form.get('tamb3_estrias_insp2')
        if not tamb3_estrias_insp2:
            tamb3_estrias_insp2 = "Não"
        tamb3_pist_insp2 = request.form.get('tamb3_pist_insp2')
        if not tamb3_pist_insp2:
            tamb3_pist_insp2 = "Não"
        tamb3_trava_insp2 = request.form.get('tamb3_trava_insp2')
        if not tamb3_trava_insp2:
            tamb3_trava_insp2 = "Não"

        dife_trinca_insp2 = request.form.get('dife_trinca_insp2')
        if not dife_trinca_insp2:
            dife_trinca_insp2 = "Não"
        dife_rolam_insp2 = request.form.get('dife_rolam_insp2')
        if not dife_rolam_insp2:
            dife_rolam_insp2 = "Não" 
        dife_super_insp2 = request.form.get('dife_super_insp2')
        if not dife_super_insp2:
            dife_super_insp2 = "Não"
        dife_estrias_insp2 = request.form.get('dife_estrias_insp2')
        if not dife_estrias_insp2:
            dife_estrias_insp2 = "Não"
        dife_desg_insp2 = request.form.get('dife_desg_insp2')
        if not dife_desg_insp2:
            dife_desg_insp2 = "Não"
        dife_eixo_insp2 = request.form.get('dife_eixo_insp2')
        if not dife_eixo_insp2:
            dife_eixo_insp2 = "Não"
        dife_capa_insp2 = request.form.get('dife_capa_insp2')
        if not dife_capa_insp2:
            dife_capa_insp2 = "Não"
        dife_sate_insp2 = request.form.get('dife_sate_insp2')
        if not dife_sate_insp2:
            dife_sate_insp2 = "Não"

        mola_oxi_insp2 = request.form.get('mola_oxi_insp2')
        if not mola_oxi_insp2:
            mola_oxi_insp2 = "Não"
        mola_def_insp2 = request.form.get('mola_def_insp2')
        if not mola_def_insp2:
            mola_def_insp2 = "Não"
        mola_emp_insp2 = request.form.get('mola_emp_insp2')
        if not mola_emp_insp2:
            mola_emp_insp2 = "Não"

        hast_pos_insp2 = request.form.get('hast_pos_insp2')
        if not hast_pos_insp2:
            hast_pos_insp2 = "Não"
        hast_mol_insp2 = request.form.get('hast_mol_insp2')
        if not hast_mol_insp2:
            hast_mol_insp2 = "Não"
        hast_oxid_insp2 = request.form.get('hast_oxid_insp2')
        if not hast_oxid_insp2:
            hast_oxid_insp2 = "Não"

        conect_quebra_insp2 = request.form.get('conect_quebra_insp2')
        if not conect_quebra_insp2:
            conect_quebra_insp2 = "Não"
        conect_trincas_insp2 = request.form.get('conect_trincas_insp2')
        if not conect_trincas_insp2:
            conect_trincas_insp2 = "Não"
        conect_oxid_insp2 = request.form.get('conect_oxid_insp2')
        if not conect_oxid_insp2:
            conect_oxid_insp2 = "Não"

        sensor_der_insp2 = request.form.get('sensor_der_insp2')
        if not sensor_der_insp2:
            sensor_der_insp2 = "Não"
        sensor_cab_insp2 = request.form.get('sensor_cab_insp2 ')
        if not sensor_cab_insp2:
            sensor_cab_insp2 = "Não"
        sensor_conec_insp2 = request.form.get('sensor_conec_insp2')
        if not sensor_conec_insp2:
            sensor_conec_insp2 = "Não"

        snpres_trinca_insp2 = request.form.get('snpres_trinca_insp2')
        if not snpres_trinca_insp2:
            snpres_trinca_insp2 = "Não"
        snpres_esfera_insp2 = request.form.get('snpres_esfera_insp2')
        if not snpres_esfera_insp2:
            snpres_esfera_insp2 = "Não"  
        snpres_cabo_insp2 = request.form.get('snpres_cabo_insp2')
        if not snpres_cabo_insp2:
            snpres_cabo_insp2 = "Não"
        snpres_conec_insp2 = request.form.get('snpres_conec_insp2')
        if not snpres_conec_insp2:
            snpres_conec_insp2 = "Não"

        chapa_quebra_insp2 = request.form.get('chapa_quebra_insp2')
        if not chapa_quebra_insp2:
            chapa_quebra_insp2 = "Não"  
        chapa_amassada_insp2 = request.form.get('chapa_amassada_insp2')
        if not chapa_amassada_insp2:
            chapa_amassada_insp2 = "Não"
        chapa_oxida_insp2 = request.form.get('chapa_oxida_insp2')
        if not chapa_oxida_insp2:
            chapa_oxida_insp2 = "Não"

        cpa_trinca_insp2 = request.form.get('cpa_trinca_insp2')
        if not cpa_trinca_insp2:
            cpa_trinca_insp2 = "Não"
        cpa_rosca_insp2 = request.form.get('cpa_rosca_insp2')
        if not cpa_rosca_insp2:
            cpa_rosca_insp2 = "Não"
        cpa_rolam_insp2 = request.form.get('cpa_rolam_insp2')
        if not cpa_rolam_insp2:
            cpa_rolam_insp2 = "Não"
        cpa_aloj_insp2 = request.form.get('cpa_aloj_insp2')
        if not cpa_aloj_insp2:
            cpa_aloj_insp2 = "Não"
        cpa_retent_insp2 = request.form.get('cpa_retent_insp2 ')
        if not cpa_retent_insp2:
            cpa_retent_insp2 = "Não"
        cpa_super_insp2 = request.form.get('cpa_super_insp2')
        if not cpa_super_insp2:
            cpa_super_insp2 = "Não"

        tampa_trinca_insp2 = request.form.get('tampa_trinca_insp2')
        if not tampa_trinca_insp2:
            tampa_trinca_insp2 = "Não"
        tampa_rosca_insp2 = request.form.get('tampa_rosca_insp2')
        if not tampa_rosca_insp2:
            tampa_rosca_insp2 = "Não" 
        tampa_aloj_insp2 = request.form.get('tampa_aloj_insp2')
        if not tampa_aloj_insp2:
            tampa_aloj_insp2 = "Não" 
        tampa_ved_insp2 = request.form.get('tampa_ved_insp2')
        if not tampa_ved_insp2:
            tampa_ved_insp2 = "Não" 
        tampa_cont_insp2 = request.form.get('tampa_cont_insp2')
        if not tampa_cont_insp2:
            tampa_cont_insp2 = "Não"
        tampa_aneis_ins2 = request.form.get('tampa_aneis_ins2')
        if not tampa_aneis_ins2:
            tampa_aneis_ins2 = "Não"

        placa_trinca_insp2 = request.form.get('placa_trinca_insp2')
        if not placa_trinca_insp2:
            placa_trinca_insp2 = "Não"
        placa_rosca_insp2 = request.form.get('placa_rosca_insp2')
        if not placa_rosca_insp2:
            placa_rosca_insp2 = "Não"
        placa_risco_insp2 = request.form.get('placa_risco_insp2')
        if not placa_risco_insp2:
            placa_risco_insp2 = "Não"
        placa_dia_insp2 = request.form.get('placa_dia_insp2')
        
        cuba_rola_insp2 = request.form.get('cuba_rola_insp2')
        if not cuba_rola_insp2:
            cuba_rola_insp2 = "Não"
        cuba_aneis_insp2 = request.form.get('cuba_aneis_insp2')
        if not cuba_aneis_insp2:
            cuba_aneis_insp2 = "Não"
        cuba_axial_insp2 = request.form.get('cuba_axial_insp2')
        if not cuba_axial_insp2:
            cuba_axial_insp2 = "Não"
        cuba_dia_insp2 = request.form.get('cuba_dia_insp2')

        planet_desc_insp2 = request.form.get('planet_desc_insp2')
        if not planet_desc_insp2:
            planet_desc_insp2 = "Não"
        planet_dent_insp2 = request.form.get('planet_dent_insp2')
        if not planet_dent_insp2:
            planet_dent_insp2 = "Não"
        planet_dani_insp2 = request.form.get('planet_dani_insp2')
        if not planet_dani_insp2:
            planet_dani_insp2 = "Não"
        planet_super_insp2 = request.form.get('planet_super_insp2')
        if not planet_super_insp2:
            planet_super_insp2 = "Não"
        planet_dest_insp2 = request.form.get('planet_dest_insp2')
        if not planet_dest_insp2:
            planet_dest_insp2 = "Não"
        planet_oxida_insp2 = request.form.get('planet_oxida_insp2')
        if not planet_oxida_insp2:
            planet_oxida_insp2 = "Não"
        planet_dia_insp2 = request.form.get('planet_dia_insp2')
        
        tamb4_desc_insp2 = request.form.get('tamb4_desc_insp2')
        if not tamb4_desc_insp2:
            tamb4_desc_insp2 = "Não"
        tamb4_encaix_insp2 = request.form.get('tamb4_encaix_insp2')
        if not tamb4_encaix_insp2:
            tamb4_encaix_insp2 = "Não"
        tamb4_estrias_insp2 = request.form.get('tamb4_estrias_insp2')
        if not tamb4_estrias_insp2:
            tamb4_estrias_insp2 = "Não"
        tamb4_pist_insp2 = request.form.get('tamb4_pist_insp2')
        if not tamb4_pist_insp2:
            tamb4_pist_insp2 = "Não"
        tamb4_trava_insp2 = request.form.get('tamb4_trava_insp2')
        if not tamb4_trava_insp2:
            tamb4_trava_insp2 = "Não"

        tamb5_desc_insp2 = request.form.get('tamb5_desc_insp2')
        if not tamb5_desc_insp2:
            tamb5_desc_insp2 = "Não"
        tamb5_disc_insp2 = request.form.get('tamb5_disc_insp2')
        if not tamb5_disc_insp2:
            tamb5_disc_insp2 = "Não"
        tamb5_estrias_insp2 = request.form.get('tamb5_estrias_insp2')
        if not tamb5_estrias_insp2:
            tamb5_estrias_insp2 = "Não"
        tamb5_pist_insp2 = request.form.get('tamb5_pist_insp2')
        if not tamb5_pist_insp2:
            tamb5_pist_insp2 = "Não"
        tamb5_trava_insp2 = request.form.get('tamb5_trava_insp2')
        if not tamb5_trava_insp2:
            tamb5_trava_insp2 = "Não"

        embre_queima_insp2 = request.form.get('embre_queima_insp2')
        if not embre_queima_insp2:
            embre_queima_insp2 = "Não"
        embre_desg_insp2 = request.form.get('embre_desg_insp2')
        if not embre_desg_insp2:
            embre_desg_insp2 = "Não"
        embre_empena_insp2 = request.form.get('embre_empena_insp2')
        if not embre_empena_insp2:
            embre_empena_insp2 = "Não"
        embre_def_insp2 = request.form.get('embre_def_insp2')
        if not embre_def_insp2:
            embre_def_insp2 = "Não"
        embre_obs_insp2 = request.form.get('embre_obs_insp2')

        acion_trinca_insp2 = request.form.get('acion_trinca_insp2')
        if not acion_trinca_insp2:
            acion_trinca_insp2 = "Não"
        acion_desgt_insp2 = request.form.get('acion_desgt_insp2')
        if not acion_desgt_insp2:
            acion_desgt_insp2 = "Não"
        acion_aneis_insp2 = request.form.get('acion_aneis_insp2')
        if not acion_aneis_insp2:
            acion_aneis_insp2 = "Não"
        acion_mola_insp2 = request.form.get('acion_mola_insp2')
        if not acion_mola_insp2:
            acion_mola_insp2 = "Não"

        troca_quebras_insp2 = request.form.get('troca_quebras_insp2')
        if not troca_quebras_insp2:
            troca_quebras_insp2 = "Não"
        troca_furo_insp2 = request.form.get('troca_furo_insp2')
        if not troca_furo_insp2:
            troca_furo_insp2 = "Não"

        respiro_rasgo_insp2 = request.form.get('respiro_rasgo_insp2')
        if not respiro_rasgo_insp2:
            respiro_rasgo_insp2 = "Não"
        respiro_tamp_insp2 = request.form.get('respiro_tamp_insp2')
        if not respiro_tamp_insp2:
            respiro_tamp_insp2 = "Não"
        respiro_defor_insp2 = request.form.get('respiro_defor_insp2')
        if not respiro_defor_insp2:
            respiro_defor_insp2 = "Não"
 
        chsele_quebras_inspe2 = request.form.get('chsele_quebras_inspe2')
        if not chsele_quebras_inspe2:
            chsele_quebras_inspe2 = "Não"
        chsele_conect_insp2 = request.form.get('chsele_conect_insp2')
        if not chsele_conect_insp2:
            chsele_conect_insp2 = "Não" 
        chsele_termi_insp2 = request.form.get('chsele_termi_insp2')
        if not chsele_termi_insp2:
            chsele_termi_insp2 = "Não"

        inf_ps2_insp2 = request.form.get('inf_ps2_insp2')
        inf_eix_insp2 = request.form.get('inf_eix_insp2')
        inf_bomb_insp2 = request.form.get('inf_bomb_insp2')
        inf_bomba_insp2 = request.form.get('inf_bomba_insp2')
        inf_bombb_ins2 = request.form.get('inf_bombb_ins2')
        inf_n1_insp2 = request.form.get('inf_n1_insp2')
        inf_n2_insp2 = request.form.get('inf_n2_insp2') 
        inf_f3n1_insp2 = request.form.get('inf_f3n1_insp2')
        inf_f3n2_insp2 = request.form.get('inf_f3n2_insp2')
        inf_conj1_insp2 = request.form.get('inf_conj1_insp2') 
        inf_mont1_insp2 = request.form.get('inf_mont1_insp2')
        inf_conj2_insp2 = request.form.get('inf_conj2_insp2')
        inf_mont2_insp2 = request.form.get('inf_mont2_insp2')
        inf_conj3_insp2 = request.form.get('inf_conj3_insp2')
        inf_mont3_insp2 = request.form.get('inf_mont3_insp2')
        inf_conj4_insp2 = request.form.get('inf_conj4_insp2')
        inf_mont4_insp2 = request.form.get('inf_mont4_insp2')
        inf_conj5_insp2 = request.form.get('inf_conj5_insp2')
        inf_mont5_insp2 = request.form.get('inf_mont5_insp2')

        salvar_inspecao2 = Inspecao2(os_insp2, op_insp2, modelo_insp2, conversor_insp2, data_inps2, serie_insp2, nome_insp2, carc_trinca_insp2, carc_rolam_insp2, carc_aloj_insp2, carc_acumu_insp2, carc_reten_insp2, carc_pist_insp2, carc_capa_insp2, carc_guia_insp2, carc_veda_insp2, bomb_super_insp2, bomb_guia_insp2, bomb_risco_inps2, bomb_dia_insp2, bomb_desg_insp2, bomb_eng_insp2, bomb_estados_insp2, eixo_supr_insp2, eixo_estrias_insp2, eixo_pist_insp2, eixo_cont_insp2, eixo_dia_insp2, tambor_desc_insp2, tambor_ent_insp2, tambor_estrias_insp2, tambor_pist_insp2, tambor_sup_insp2, tambor2_des_insp2, tambor2_ent_insp2, tambor2_estrias_insp2, tambor2_pist_insp2, tambor2_trava_insp2, tamb3_desc_insp2, tamb3_enc_insp2, tamb3_estrias_insp2, tamb3_pist_insp2, tamb3_trava_insp2, dife_trinca_insp2, dife_rolam_insp2, dife_super_insp2, dife_estrias_insp2, dife_desg_insp2, dife_eixo_insp2, dife_capa_insp2, dife_sate_insp2, mola_oxi_insp2, mola_def_insp2, mola_emp_insp2, hast_pos_insp2, hast_mol_insp2, hast_oxid_insp2, conect_quebra_insp2, conect_trincas_insp2, conect_oxid_insp2, sensor_der_insp2, sensor_cab_insp2, sensor_conec_insp2, snpres_trinca_insp2, snpres_esfera_insp2, snpres_cabo_insp2, snpres_conec_insp2, chapa_quebra_insp2, chapa_amassada_insp2, chapa_oxida_insp2, cpa_trinca_insp2, cpa_rosca_insp2, cpa_rolam_insp2, cpa_aloj_insp2, cpa_retent_insp2, cpa_super_insp2, tampa_trinca_insp2, tampa_rosca_insp2, tampa_aloj_insp2, tampa_ved_insp2, tampa_cont_insp2, tampa_aneis_ins2, placa_trinca_insp2, placa_rosca_insp2, placa_risco_insp2, placa_dia_insp2, cuba_rola_insp2, cuba_aneis_insp2, cuba_axial_insp2, cuba_dia_insp2, planet_desc_insp2, planet_dent_insp2, planet_dani_insp2, planet_super_insp2, planet_dest_insp2, planet_oxida_insp2, planet_dia_insp2, tamb4_desc_insp2, tamb4_encaix_insp2, tamb4_estrias_insp2, tamb4_pist_insp2, tamb4_trava_insp2, tamb5_desc_insp2, tamb5_disc_insp2, tamb5_estrias_insp2, tamb5_pist_insp2, tamb5_trava_insp2, embre_queima_insp2, embre_desg_insp2, embre_empena_insp2, embre_def_insp2, embre_obs_insp2, acion_trinca_insp2, acion_desgt_insp2, acion_aneis_insp2, acion_mola_insp2, troca_quebras_insp2, troca_furo_insp2, respiro_rasgo_insp2, respiro_tamp_insp2, respiro_defor_insp2, chsele_quebras_inspe2, chsele_conect_insp2, chsele_termi_insp2, inf_ps2_insp2, inf_eix_insp2, inf_bomb_insp2, inf_bomba_insp2, inf_bombb_ins2, inf_n1_insp2, inf_n2_insp2, inf_f3n1_insp2, inf_f3n2_insp2, inf_conj1_insp2, inf_mont1_insp2, inf_conj2_insp2, inf_mont2_insp2, inf_conj3_insp2, inf_mont3_insp2, inf_conj4_insp2, inf_mont4_insp2, inf_conj5_insp2, inf_mont5_insp2)
        db.session.add(salvar_inspecao2)
        db.session.commit()
    return render_template('inspecao_2.html')

@app.route("/montagem", methods = ['POST','GET'])
def montagem():

    if request.method == 'POST':
        
        montagem_ordem = request.form.get('montagem_ordem')
        montagem_op = request.form.get('montagem_op')
        montagem_modelo = request.form.get('montagem_modelo')
        montagem_conversor_torque = request.form.get('montagem_conversor_torque')
        montagem_data = request.form.get('montagem_data')
        montagem_serie = request.form.get('montagem_serie')
        montagem_nome = request.form.get('montagem_nome')

        #Tampa Traseira
        montagem_tampa_traseira = request.form.get('montagem_tampa_traseira')
        
        #Carcaça principal
        montagem_carcaca_principal = request.form.get('montagem_carcaca_principal')
        
        #Tampa do Bloco Hidráulico
        montagem_tampa_bloco_hidra = request.form.get('montagem_tampa_bloco_hidra')
        
        #Bloco Hidráulico na transmissão
        montagem_bloco_pre_torque = request.form.get('montagem_bloco_pre_torque')
        montagem_bloco_torque = request.form.get('montagem_bloco_torque')

        #Porca de rolamento central
        montagem_porca_pre_torque = request.form.get('montagem_porca_pre_torque')
        montagem_porca_torque = request.form.get('montagem_porca_torque')

        #Parafusos do rolamento central
        montagem_parafuso_rolamento = request.form.get('montagem_parafuso_rolamento')

        #Parafuso de ancoragem das cintas
        montagem_parafuso_ancoragem = request.form.get('montagem_parafuso_ancoragem')

        #Parfusos do sensor de pressão
        montagem_parafuso_sensor_pressao = request.form.get('montagem_parafuso_sensor_pressao')

        #Parfusos do sensor de rot. De saída
        montagem_parafuso_sensor_rotacao = request.form.get('montagem_parafuso_sensor_rotacao')

        #Carcaça da bomba de óleo
        montagem_carcaca_bomb_oleo_pre_torque = request.form.get('montagem_carcaca_bomb_oleo_pre_torque')
        montagem_carcaca_bomb_oleo_torque = request.form.get('montagem_carcaca_bomb_oleo_torque')

        #Conjunto da bomba na transmissão
        montagem_conjunto_bomba_pre_torque = request.form.get('montagem_conjunto_bomba_pre_torque')
        montagem_conjunto_bomba_torque = request.form.get('montagem_conjunto_bomba_torque')

        #Parafuso do eixo seletor
        montagem_parafuso_eixo = request.form.get('montagem_parafuso_eixo')

        #Parafuso do trocador de calor
        montagem_parafuso_trocador = request.form.get('montagem_parafuso_trocador')

        #Parafusos da coroa (dif. de Ferro Fundido)
        montagem_parafuso_coroa_ferro = request.form.get('montagem_parafuso_coroa_ferro')

        #Parafusos da coroa (dif. de Alumínio)
        montagem_parafuso_coroa_aluminio = request.form.get('montagem_parafuso_coroa_aluminio')

        #Parfusos da chave seletora (CMF)
        montagem_parafuso_chave_seletora = request.form.get('montagem_parafuso_chave_seletora')

        #Parfusos do sensor do velocímetro
        montagem_parafuso_velocimetro = request.form.get('montagem_parafuso_velocimetro')

        #Parfusos do controle de débito do permutador
        montagem_parafuso_controle = request.form.get('montagem_parafuso_controle')

        salva_montagem = Montagem(montagem_ordem,montagem_op,montagem_modelo,montagem_conversor_torque,montagem_data,montagem_serie,montagem_nome,montagem_tampa_traseira,montagem_carcaca_principal,montagem_tampa_bloco_hidra,montagem_bloco_pre_torque,montagem_bloco_torque,montagem_porca_pre_torque,montagem_porca_torque,montagem_parafuso_rolamento,montagem_parafuso_ancoragem,montagem_parafuso_sensor_pressao,montagem_parafuso_sensor_rotacao,montagem_carcaca_bomb_oleo_pre_torque,montagem_carcaca_bomb_oleo_torque,montagem_conjunto_bomba_pre_torque,montagem_conjunto_bomba_torque,montagem_parafuso_eixo,montagem_parafuso_trocador,montagem_parafuso_coroa_ferro,montagem_parafuso_coroa_aluminio,montagem_parafuso_chave_seletora,montagem_parafuso_velocimetro,montagem_parafuso_controle)

        db.session.add(salva_montagem)
        db.session.commit()

    return render_template('montagem.html')

@app.route("/testefinal", methods = ['POST', 'GET'])
def testefinal():

    if request.method == 'POST':
        
        teste_final_ordem = request.form.get('teste_final_ordem')
        teste_final_op = request.form.get('teste_final_op')
        teste_final_modelo = request.form.get('teste_final_modelo')
        teste_final_conversor_torque = request.form.get('teste_final_conversor_torque')
        teste_final_data = request.form.get('teste_final_data')
        teste_final_serie = request.form.get('teste_final_serie')
        teste_final_nome = request.form.get('teste_final_nome') 

        #VERIFICAR SE NÃO HÁ CÓDIGOS DE AVARIA
        teste_final_verificar_avaria = request.form.get('teste_final_verificar_avaria')
        if not teste_final_verificar_avaria:
            teste_final_verificar_avaria = "Não"

        #VERIFICAR SE NÃO HÁ RUÍDOS(DIFERENCIAL)
        teste_final_verificar_ruido = request.form.get('teste_final_verificar_ruido')
        if not teste_final_verificar_ruido:
            teste_final_verificar_ruido = "Não"

        #TESTE PRESSURIZADO DE VAZAMENTO DE ÓLEO
        teste_final_pressurizado_oleo = request.form.get('teste_final_pressurizado_oleo')
        if not teste_final_pressurizado_oleo:
            teste_final_pressurizado_oleo = "Não"

        #INSTALAR TRAVA NO CONVERSOR DE TORQUE / TRAVA PARA TRANSPORTE
        teste_final_instalar_trava = request.form.get('teste_final_instalar_trava')
        if not teste_final_instalar_trava:
            teste_final_instalar_trava = "Não"

        #AVISOS E OBSERVAÇÕES / ANEXAR FOLHAS DE AVISOS - CONCESSIONÁRIO
        teste_final_avisos_observacoes = request.form.get('teste_final_avisos_observacoes')
        if not teste_final_avisos_observacoes:
            teste_final_avisos_observacoes = "Não"

        #PRESSÃO DE LINHA
        teste_final_pressao_linha = request.form.get('teste_final_pressao_linha')
        if not teste_final_pressao_linha:
            teste_final_pressao_linha = "Não"

        teste_final_pressao_linha_valor = request.form.get('teste_final_pressao_linha_valor')

        #AFERIÇÃO DO NÍVEL DE ÓLEO
        teste_final_afericao_oleo_valor = request.form.get('teste_final_afericao_oleo_valor')

        #TESTE DO SISTEMA PARKIN
        teste_final_sistema_parkin = request.form.get('teste_final_sistema_parkin')
        if not teste_final_sistema_parkin:
            teste_final_sistema_parkin = "Não"

        #VALIDAÇÃO DO TESTE
        teste_final_validacao = request.form.get('teste_final_validacao')
        if not teste_final_validacao:
            teste_final_validacao = "Não"

        #Observação
        teste_final_observacao = request.form.get('teste_final_observacao')
        
        salva_teste_final = Teste_final(teste_final_ordem,teste_final_op,teste_final_modelo,teste_final_conversor_torque,teste_final_data,teste_final_serie,teste_final_nome,teste_final_verificar_avaria,teste_final_verificar_ruido,teste_final_pressurizado_oleo,teste_final_instalar_trava,teste_final_avisos_observacoes,teste_final_pressao_linha,teste_final_pressao_linha_valor,teste_final_afericao_oleo_valor,teste_final_sistema_parkin,teste_final_validacao,teste_final_observacao)
        db.session.add(salva_teste_final)
        db.session.commit()

    return render_template('testefinal.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port = 5000, host = '127.0.0.1'); 