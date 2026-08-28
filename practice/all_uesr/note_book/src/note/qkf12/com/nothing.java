package note.qkf12.com;

public class nothing {
    private String date;
    private String type;
    private double money;

    public nothing(){}

    public nothing(String date, String type, double money){
        this.date = date;
        this.type = type;
        this.money = money;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public double getMoney() {
        return money;
    }

    public void setMoney(double money) {
        this.money = money;
    }

    @Override
    public String toString() {
        return "nothing{" +
                "date='" + date + '\'' +
                ", type='" + type + '\'' +
                ", money=" + money +
                '}';
    }
}
