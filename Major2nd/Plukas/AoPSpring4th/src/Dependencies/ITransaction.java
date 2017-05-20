package Dependencies;

/**
 * Created by Kay on 5/20/2017.
 */
public interface ITransaction {
    void ExecuteTransaction(String name, String accountNo, int amount);
}
