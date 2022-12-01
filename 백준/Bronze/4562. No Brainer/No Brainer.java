import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        for (int i = 0; i < a; i++) {
            int b = sc.nextInt();
            int c = sc.nextInt();
            if (b<c) System.out.println("NO BRAINS");
            else System.out.println("MMM BRAINS");
        }
    }
}