package Dependencies;

import org.aspectj.lang.annotation.Pointcut;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

/**
 * Created by Kay on 5/20/2017.
 */
//@Component("circus")
public class Circus implements ICircus {

    @Override
    public void SpawnClowns() {
        CreateClown();
    }

    public void CreateClown() {
        try {
            Thread.sleep(1000);
        } catch (Exception ex) {

        }
    }
}
