package LocalConfigs;

import org.aspectj.lang.annotation.Aspect;

/**
 * Created by Kay on 5/21/2017.
 */
@Aspect
public class Countable implements ICountable {
    private int counter = 0;

    @Override
    public void inc() {
        counter++;
    }

    @Override
    public void dec() {
        counter--;
    }

    @Override
    public int getCount() {
        return counter;
    }
}
