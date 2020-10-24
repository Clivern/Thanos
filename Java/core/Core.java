/**
 * Core
 */
public class Core {
    public class InternalCore {
        public String Something = "Something";
    }

    public static void main(String[] args) {
        System.out.println("Hello");

        // /////////////////////////
        // BASICS https://beginnersbook.com/2017/08/variables-in-java/
        // /////////////////////////
        int a;
        char b;
        String c;
        int[] d;
        int[] e;
        String[] f;

        short g = 200;
        long h = 200000L;
        double i = 22.4;
        float j = 22.4f;

        a = 2;
        b = 'A';
        c = "Hello";

        d = new int[3];
        d[0] = 32;

        e = new int[3];
        e[0] = 26;

        f = new String[3];
        f[0] = "DE";

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d[0]);
        System.out.println(e[0]);
        System.out.println(f[0]);

        System.out.println(g);
        System.out.println(h);
        System.out.println(i);
        System.out.println(j);

        (new Core()).testInternalCore();

        int num1 = 100;
        int num2 = 20;

        System.out.println("num1 + num2: " + (num1 + num2));
        System.out.println("num1 - num2: " + (num1 - num2));
        System.out.println("num1 * num2: " + (num1 * num2));
        System.out.println("num1 / num2: " + (num1 / num2));
        System.out.println("num1 % num2: " + (num1 % num2));

        boolean b1 = true;
        boolean b2 = false;

        System.out.println("b1 && b2: " + (b1 && b2));
        System.out.println("b1 || b2: " + (b1 || b2));
        System.out.println("!(b1 && b2): " + !(b1 && b2));

        int num3, num4;
        num3 = 25;

        num4 = (num3 == 10) ? 100 : 200;
        System.out.println("num4: " + num4);


        num4 = (num3 == 25) ? 100 : 200;
        System.out.println("num4: " + num4);


        int num = 1234;

        if (num < 100 && num >= 1) {
            System.out.println("Its a two digit number");
        } else if (num < 1000 && num >= 100) {
            System.out.println("Its a three digit number");
        } else {
            System.out.println("number is not between 1 & 99999");
        }


        int num13 = 1;

        switch (num13) {

            case 1:
                System.out.println("Case1: Value is: " + num13);

            case 2:
                System.out.println("Case2: Value is: " + num13);

            default:
                System.out.println("Case3: Value is: " + num13);
        }

        switch (num13) {
            case 1:
                System.out.println("Case1: Value is: " + num13);
                break;

            case 2:
                System.out.println("Case2: Value is: " + num13);
                break;

            default:
                System.out.println("Case3: Value is: " + num13);
        }

        char ch = 'b';

        switch (ch) {

            case 'd':
                System.out.println("Case1 ");
                break;

            case 'b':
                System.out.println("Case2 ");
                break;

            case 'x':
                System.out.println("Case3 ");
                break;

            case 'y':
                System.out.println("Case4 ");
                break;

            default:
                System.out.println("Default ");
        }

        for (int k = 0; k < 5; k++) {
            System.out.println("k = " + k);
        }

        int[] i_arr = {
            1,
            2,
            3,
            4,
            5,
            6,
            7
        };

        for (int k = 0; k < i_arr.length; k++) {
            System.out.println("k = " + k);
        }

        for (int elem: i_arr) {
            System.out.println("elem = " + elem);
        }

        String[] st_arr = {
            "hi",
            "hello",
            "bye"
        };

        for (String elem: st_arr) {
            System.out.println(elem);
        }

        int num20 = 1;

        while(num20 < 5) {
            System.out.println(num20);
            num20++;
        }

        do {
            System.out.println(num20);
            num20++;
        } while(num20 < 10);


        for(int p = 0; p < 10; p++) {
            if (p == 5){
                continue;
            }

            if (p == 8){
                break;
            }

            System.out.println(p);
        }

        // /////////////////////////
        // OOP https://beginnersbook.com/2013/04/oops-concepts/
        // /////////////////////////
    }

    public void testInternalCore() {
        InternalCore ic = new InternalCore();
        System.out.println(ic.Something);
    }
}