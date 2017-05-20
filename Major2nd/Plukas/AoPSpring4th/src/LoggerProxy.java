import com.google.common.base.Stopwatch;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.scheduling.quartz.LocalDataSourceJobStore;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.logging.FileHandler;
import java.util.logging.Handler;
import java.util.logging.Logger;


import static java.util.Date.*;

/**
 * Created by Kay on 5/20/2017.
 */
@Aspect
public class LoggerProxy {

    Logger _logger;

    public LoggerProxy(Logger logger) {
        _logger = logger;
    }


    // Pritaikymas bet kokiam metodui
    @Pointcut("within(Dependencies.*)execution(public * *(..))")
    public void AllMethodsInDependencies() {
    }

    @Around("AllMethodsInDependencies()")
    public Object doBasicProfiling(ProceedingJoinPoint pjp) throws Throwable {
        _logger.info(LocalDateTime.now() + " Method - " + pjp.getSignature().getName());
        Stopwatch stopwatch = new Stopwatch();
        stopwatch.start();
        Object retVal = pjp.proceed();
        stopwatch.stop();
        _logger.info(LocalDateTime.now() + " Elapsed: " + stopwatch.elapsedMillis()+ " " + pjp.getTarget().toString());

        return retVal;
    }
}
