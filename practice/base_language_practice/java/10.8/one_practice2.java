public class one_practice2 {
    static void main() {
        String n = "ac";
        String m = "bdf";

        int number1 = n.length();
        char[] chars1 = n.toCharArray();

        int number2 = m.length();
        char[] chars2 = m.toCharArray();

        if (number1 < number2) {
            for (int i = 0; i < number1; i++) {
                System.out.println( "第 " +(i+1) +" 个字符" + chars1[i]);
            }
        }

        for (int i = 0; i < number1; i++) {
            System.out.println( "第 " +(i+1) +" 个字符" + chars1[i]);
        }

    }
}
