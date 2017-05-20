import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.Signature;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

import javax.naming.InvalidNameException;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

/**
 * Created by Kay on 5/20/2017.
 */
@Aspect
public class MemoizationProxy {
    private static ConcurrentHashMap<String, ConcurrentHashMap<Object, Object>> _memoizedValues = new ConcurrentHashMap<String, ConcurrentHashMap<Object, Object>>();

    @Pointcut("execution(* void (..))")
    private void AnyVoidMethod() {
    }

    @Pointcut("within(Dependencies.*)")
    private void InDependencies() {
    }

    @Pointcut("execution(public * *(*))")
    private void OneArgument() {
    }




    @Around("!AnyVoidMethod() && InDependencies() && OneArgument()")
    public Object GenericMemoizationMethod(ProceedingJoinPoint pjp) throws Throwable {
        Object value = pjp.getArgs()[0];
        String signature = pjp.getSignature().toString();
        if (_memoizedValues.containsKey(signature)) {
            ConcurrentHashMap _innerMap = _memoizedValues.get(signature);
            if (_innerMap.containsKey(value))
                return _innerMap.get(value);
            else {
                Object output = pjp.proceed();
                _innerMap.put(value, output);
                return output;
            }
        } else {
            Object output = pjp.proceed();
            _memoizedValues.put(signature, new ConcurrentHashMap<Object, Object>());
            _memoizedValues.get(signature).put(value, output);
            return output;
        }
    }
}
