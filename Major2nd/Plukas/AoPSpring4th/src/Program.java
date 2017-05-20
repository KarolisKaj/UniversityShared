import Dependencies.CircusFactory;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Created by Kay on 5/20/2017.
 */
public class Program {
    public static void main(String[] args) {
        Bootstrapper boot = new Bootstrapper();
        boot.Start();
        System.out.println("Bye");
    }
}
