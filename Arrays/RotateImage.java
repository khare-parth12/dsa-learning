// Leetcode 48

public class RotateImage {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int k = n - 1;

        for (int i = 0; i < n >> 1; i++) {
            for (int j = i; j < k - i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = temp;
            }
        }
    }
    
    public static void main(String[] args) {
        
    }
}
