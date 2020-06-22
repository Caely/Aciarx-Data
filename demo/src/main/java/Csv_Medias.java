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