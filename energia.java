import java.math.BigDecimal;

public class energia {
    private int potenciaMW;
    private int potenciakWh;
    private int kWhT;
    private int kWhMin;
    private int lan02;
    private int carvao;
    private BigDecimal cjO2;
    private BigDecimal cjGn;
    private int pwOff;
    private int pwOn;
    private int ttt;
    private int temp;

    public energia(int potenciaMW, int potenciakWh, int kWhT, int kWhmin, int lan02, int carvao, BigDecimal cjO2,
            BigDecimal cjgn, int pwOff, int pwOn, int ttt, int temp) {
        this.setPotenciaMW(potenciaMW);
        this.setPotenciakWh(potenciakWh);
        this.setkWhT(kWhT);
        this.kWhmin = kWhmin;
        this.setLan02(lan02);
        this.setCarvao(carvao);
        this.setCjO2(cjO2);
        this.cjgn = cjgn;
        this.setPwOff(pwOff);
        this.setPwOn(pwOn);
        this.setTtt(ttt);
        this.setTemp(temp);
    }

    //criar metodos 
    //calcular acumulado(kwh/t)
    //calcular acumulado(kwh/min)

    public int getPotenciaMW() {
        return potenciaMW;
    }

    public void setPotenciaMW(int potenciaMW) {
        this.potenciaMW = potenciaMW;
    }

    public int getPotenciakWh() {
        return potenciakWh;
    }

    public void setPotenciakWh(int potenciakWh) {
        this.potenciakWh = potenciakWh;
    }

    public int getkWhT() {
        return kWhT;
    }

    public void setkWhT(int kWhT) {
        this.kWhT = kWhT;
    }

    public int getkWhMin() {
        return kWhMin;
    }

    public void setkWhMin(int kWhMin) {
        this.kWhMin = kWhMin;
    }

    public int getLan02() {
        return lan02;
    }

    public void setLan02(int lan02) {
        this.lan02 = lan02;
    }

    public int getCarvao() {
        return carvao;
    }

    public void setCarvao(int carvao) {
        this.carvao = carvao;
    }

    public BigDecimal getCjO2() {
        return cjO2;
    }

    public void setCjO2(BigDecimal cjO2) {
        this.cjO2 = cjO2;
    }

    public BigDecimal getCjGn() {
        return cjGn;
    }

    public void setCjGn(BigDecimal cjGn) {
        this.cjGn = cjGn;
    }

    public int getPwOff() {
        return pwOff;
    }

    public void setPwOff(int pwOff) {
        this.pwOff = pwOff;
    }

    public int getPwOn() {
        return pwOn;
    }

    public void setPwOn(int pwOn) {
        this.pwOn = pwOn;
    }

    public int getTtt() {
        return ttt;
    }

    public void setTtt(int ttt) {
        this.ttt = ttt;
    }

    public int getTemp() {
        return temp;
    }

    public void setTemp(int temp) {
        this.temp = temp;
    }
    
}