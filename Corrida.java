import java.math.BigDecimal;
import java.sql.Date;

public class Corrida {
	
	private int id;
	private	int sucata;
	private String turma;
	private Date data;
	private	BigDecimal producao;
	private	BigDecimal tap_to_tap;
	private	BigDecimal power_on;
	private BigDecimal power_off;
	private	BigDecimal temperatura;	
	private	EnergiaEletrica eletrica;
	private	EnergiaQuimica quimica;

	
	public BigDecimal producaoAcumulada() {
		
	}
	
	public BigDecimal calcularRendimento() {
		
	}
	
	public BigDecimal calcularPotencia() {
		
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getSucata() {
		return sucata;
	}

	public void setSucata(int sucata) {
		this.sucata = sucata;
	}

	public String getTurma() {
		return turma;
	}

	public void setTurma(String turma) {
		this.turma = turma;
	}

	public Date getData() {
		return data;
	}

	public void setData(Date data) {
		this.data = data;
	}

	public BigDecimal getProducao() {
		return producao;
	}

	public void setProducao(BigDecimal producao) {
		this.producao = producao;
	}

	public BigDecimal getTap_to_tap() {
		return tap_to_tap;
	}

	public void setTap_to_tap(BigDecimal tap_to_tap) {
		this.tap_to_tap = tap_to_tap;
	}

	public BigDecimal getPower_on() {
		return power_on;
	}

	public void setPower_on(BigDecimal power_on) {
		this.power_on = power_on;
	}

	public BigDecimal getPower_off() {
		return power_off;
	}

	public void setPower_off(BigDecimal power_off) {
		this.power_off = power_off;
	}

	public BigDecimal getTemperatura() {
		return temperatura;
	}

	public void setTemperatura(BigDecimal temperatura) {
		this.temperatura = temperatura;
	}

	public EnergiaEletrica getEletrica() {
		return eletrica;
	}

	public void setEletrica(EnergiaEletrica eletrica) {
		this.eletrica = eletrica;
	}

	public EnergiaQuimica getQuimica() {
		return quimica;
	}

	public void setQuimica(EnergiaQuimica quimica) {
		this.quimica = quimica;
	}
	
	
}
