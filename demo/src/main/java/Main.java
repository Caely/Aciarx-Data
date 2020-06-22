import java.io.IOException;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
/*
        Csv_Medias media_15 = new Csv_Medias();
        media_15.set_table("/Users/renan/Documents/git/Aciarx-Data/reader CSV/RELATORIO_MEDIA_3_2020.csv");
        List<List<String>> table = media_15.get_table();
        System.out.println(table);
        System.out.println(media_15.get_acumulado_dia(15));
        System.out.println(media_15.get_numero_corridas_dia(15));
        System.out.println(media_15.get_pon_dia(15));
        System.out.println(media_15.get_poff_dia(15));
        System.out.println(media_15.get_pon_extra_dia(15));
        System.out.println(media_15.get_poff_extra_dia(15)); 
*/
        Csv_Turnos turno = new Csv_Turnos();
        turno.set_table("/Users/renan/Documents/git/Aciarx-Data/reader CSV/RELATORIO_PRODUCAO_15_3_2020_21_.csv");
        List<List<String>> table = turno.get_table();
        System.out.println(table);
        System.out.println(turno.get_numero_corrida(1));
        System.out.println(turno.get_turma(1));
        System.out.println(turno.get_producao(1));
        System.out.println(turno.get_producao_acumulada(1));
        System.out.println(turno.get_sucata(1));
        System.out.println(turno.get_rendimento(1));

    }

}