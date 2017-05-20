import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

import javax.naming.InvalidNameException;

/**
 * Created by Kay on 5/20/2017.
 */
@Aspect
public class TransactionValidation {
    @Pointcut("execution(public * *(..))")
    private void AnyPublicMethod() {}

    @Pointcut("within(Dependencies.*)")
    private void InDependencies() {}

    @Pointcut("AnyPublicMethod() && InDependencies() && args(name, accountNo, amount)")
    private void TradingOperation(String name, String accountNo, int amount) {}

    @Before("TradingOperation(name, accountNo, amount)")
    public void ValidateTrade(String name, String accountNo, int amount) throws Throwable {
        if(!"Karolis".equals(name))
            throw new InvalidNameException();
    }
}
