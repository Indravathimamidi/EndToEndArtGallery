import java.util.*;
import java.io.*;

public class PrimeFactor{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter num1:");
        long num1 = sc.nextLong();
        System.out.print("Enter num2");
        long num2 = sc.nextLong();
        ArrayList<Long> list = new ArrayList<>();

        long limit =(num1<num2)?num1:num2;
        for(long i=2; i<limit; i++)
        {
            if(num1%i ==0 && num2%i==0)
            {
                if(checkPrime(i))
                {
                    list.add(i);
                }
            }
        }
        if(list.size()==0)
        {
            System.out.print("No common factors");
        }
        else if(list.size()==1){
            System.out.print("Common factors is:"+list);
        }
        else{
            System.out.print("Common factors are:"+list);

        }
    }
    public static boolean checkPrime(long i)
    {
        for(long k=2; k<Math.sqrt(i); k++)
        {
            if(i%k==0)
            {
                return false;
            }
        }
        return true;
    }
}
