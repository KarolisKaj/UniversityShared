package Dependencies;

/**
 * Created by Kay on 5/20/2017.
 */
public class Transaction implements  ITransaction {
    @Override
    public void ExecuteTransaction(String name, String accountNo, int amount) {
        System.out.println("Transaction executed");
    }
}
