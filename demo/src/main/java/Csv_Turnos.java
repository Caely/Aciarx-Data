import java.io.IOException;
import java.util.List;

public class Csv_Turnos {

    private List<List<String>> table;

    public void set_table(String path) throws IOException {
        Csv_reader csv = new Csv_reader();
        csv.set_path(path);
        this.table = csv.get_csv();
    }

    public List<List<String>> get_table() {
        return this.table;
    }


    public Float get_numero_corrida(int numero) {
        int index = 0;
        return get_valor(numero,index);
    }


    public String get_turma(int numero) {
        int index = 1;
        return table.get(numero).get(index);
    }

    public Float get_producao(int numero) {
        int index = 2;
        return get_valor(numero,index);
    }

    public Float get_producao_acumulada(int numero) {
        int index = 3;
        return get_valor(numero,index);
    }

    public Float get_sucata(int numero) {
        int index = 4;
        return get_valor(numero,index);
    }

    public Float get_rendimento(int numero) {
        int index = 5;
        return get_valor(numero,index);
    }

    public Float get_valor(int linha,int coluna) {
        Float error = Float.parseFloat("-1.0");
        if(table.size() >= linha && table.get(linha).size() >= coluna) {
            return Float.parseFloat(table.get(linha).get(coluna));
        }
        else {
            return error;
        }
    }
}