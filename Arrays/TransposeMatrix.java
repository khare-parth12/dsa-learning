public class TransposeMatrix {
    public static void transposeSquare(int[][] matrix){
        if (matrix == null || matrix.length == 0) return;
        int n = matrix.length;

        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if (i==j) continue;

                int temp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
    }

    public static int[][] transposeRectangle(int[][] matrix){
        if (matrix == null || matrix.length == 0) return new int[0][0];

        int n = matrix.length;
        int m = matrix[0].length;

        int[][] result = new int[m][n];
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                result[j][i] = matrix[i][j];
            }
        }
        return result;

    }
    public static void main(String args[]){

    }    
}
