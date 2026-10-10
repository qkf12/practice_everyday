public class One_tool {
    public static String add(String s1, String s2) {
        StringBuilder s = new StringBuilder();
        int n = 0 ;
       while (n < s1.length() || n < s2.length()) {
               if (n < s1.length()) {
                   s.append(s1.charAt(n));
               }
               if (n < s2.length()) {
                   s.append(s2.charAt(n));
               }
           n ++;
       }

        return s.toString();
    }
}
