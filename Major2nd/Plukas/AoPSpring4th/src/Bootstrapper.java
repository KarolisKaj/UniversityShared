import Dependencies.ICircus;
import Dependencies.IDeepLearning;
import Dependencies.ITransaction;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.logging.FileHandler;
import java.util.logging.Handler;

/**
 * Created by Kay on 5/20/2017.
 */
public class Bootstrapper {

    ApplicationContext ctx;

    public void Start() {
        //      ctx = new AnnotationConfigApplicationContext(IoCConfig.class);
        ctx = new ClassPathXmlApplicationContext("Beans.xml");

        // Demostration purposes

        // Check logging.
        ((ICircus) ctx.getBean("circus")).SpawnClowns();

        //Check Execution cancelation depending on params
        ITransaction transaction = ((ITransaction) ctx.getBean("transaction"));
        // Exception will be thrown
        try {
            transaction.ExecuteTransaction("Juozas", "123654", 1000000);
        } catch (Exception ex) {
        }
        // Exception wont be thrown
        transaction.ExecuteTransaction("Karolis", "123654", 1000000);

        // Memoization
        IDeepLearning deepLearning = ((IDeepLearning) ctx.getBean("deepLearning"));

        // Execution will be more than 2.5 seconds
        try {
            deepLearning.LearnStuff(54);
        } catch (Exception ex) {
        }
        // Memoized value will be retrieved faster than 2.5s
        try {
            deepLearning.LearnStuff(54);
        } catch (Exception ex) {
        }
    }
}
