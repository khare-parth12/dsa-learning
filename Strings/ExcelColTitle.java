// Leetcode 168

public class ExcelColTitle{
    public String convertToTitle(int columnNumber) {
        String res = "";
        int n = 'A';

        while (columnNumber>0){
            columnNumber--;
            char currCol = (char)((columnNumber%26) + n);
            res = currCol + res;
            columnNumber = Math.floorDiv(columnNumber, 26);
        }
        return res;
    }
     public static void main(String[] args) {

    }
}