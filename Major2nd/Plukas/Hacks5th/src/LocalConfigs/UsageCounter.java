package LocalConfigs;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.DeclareParents;
import org.aspectj.lang.annotation.Pointcut;

/**
 * Created by Kay on 5/21/2017.
 */
@Aspect
public class UsageCounter {
    @Pointcut("within(Dependencies.*)")
    private void InDependencies() {
    }

   @DeclareParents(value="Dependencies.*", defaultImpl=Countable.class)
    public static ICountable injection;

    @Before("InDependencies() && this(countable)")
    public void recordUsage(ICountable countable) {
        countable.inc();
    }

}

