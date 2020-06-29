import java.io.IOException;
import java.util.List;

public class Csv_Medias {

    private List<List<String>> table;

    public void set_table(String path) throws IOException {
        Csv_reader csv = new Csv_reader();
        csv.set_path(path);
        this.table = csv.get_csv();
    }

    public List<List<String>> get_table() {
        return this.table;
    }


    /*get valor methods */
    public Float get_acumulado_dia(int dia) {
        int index = 1;
        return get_valor_in_row(dia,index);
    }

    public Float get_numero_corridas_dia(int dia) {
        int index = 2;
        return get_valor_in_row(dia,index);
    }

    public Float get_pon_dia(int dia) {
        int index = 3;
        return get_valor_in_row(dia,index);
    }

    public Float get_poff_dia(int dia) {
        int index = 4;
        return get_valor_in_row(dia,index);
    }

    public Float get_pon_extra_dia(int dia) {
        int index = 5;
        return get_valor_in_row(dia,index);
    }

    public Float get_poff_extra_dia(int dia) {
        int index = 6;
        return get_valor_in_row(dia,index);
    }

    public Float get_sucata(int dia) {
        int index = 7;
        return get_valor_in_row(dia,index);
    }

    public Float get_potencia_mw(int dia) {
        int index = 8;
        return get_valor_in_row(dia,index);
    }

    public Float get_potencia_kwh(int dia) {
        int index = 9;
        return get_valor_in_row(dia,index);
    }

    public Float get_kwh_t(int dia) {
        int index = 10;
        return get_valor_in_row(dia,index);
    }

    public Float get_kwh_min(int dia) {
        int index = 11;
        return get_valor_in_row(dia,index);
    }

    public Float get_lan_o2(int dia) {
        int index = 12;
        return get_valor_in_row(dia,index);
    }

    public Float get_carvao(int dia) {
        int index = 13;
        return get_valor_in_row(dia,index);
    }

    public Float get_cj_o2(int dia) {
        int index = 14;
        return get_valor_in_row(dia,index);
    }

    public Float get_cj_gn(int dia) {
        int index = 15;
        return get_valor_in_row(dia,index);
    }


    /* mean methods */
    public Float get_media_producao(int dia) {
        Float media = get_acumulado_dia(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_sucata(int dia) {
        Float media = get_sucata(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_rendimento_diario(int dia) {
        Float media = (get_sucata(dia) - get_acumulado_dia(dia));
        if(media <= 0) {
            media = Float.parseFloat("100");
        }
        else {
            media = 100 - media;
        }
        return media;
    }

    public Float get_media_potencia_mw(int dia) {
        Float media = get_potencia_mw(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_potencia_kwh(int dia) {
        Float media = get_potencia_kwh(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_kwh_t(int dia) {
        Float media = get_media_kwh_t(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_kwh_min(int dia) {
        Float media = get_kwh_min(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_lan_o2(int dia) {
        Float media = get_lan_o2(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_carvao(int dia) {
        Float media = get_carvao(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_cj_o2(int dia) {
        Float media = get_cj_o2(dia) / get_numero_corridas_dia(dia);
        return media;
    }

    public Float get_media_cj_gn(int dia) {
        Float media = get_cj_gn(dia) / get_numero_corridas_dia(dia);
        return media;
    }


    /* base methods */    
    public Float get_valor_in_row(int dia,int index) {
        Float error = Float.parseFloat("-1.0");
        Float aux;
        for(int i = 1;i < table.size();i++) {
            aux = Float.parseFloat(table.get(i).get(0));
            if(aux == dia) {
                return get_valor(i,index);
            }
        }
        return error;
    }


    public Float get_valor(int linha,int coluna) {
        return Float.parseFloat(table.get(linha).get(coluna));
    }
}