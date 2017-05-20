package Dependencies;

import org.springframework.stereotype.Component;

/**
 * Created by Kay on 5/20/2017.
 */
//@Component
public class CircusFactory implements ICircusFactory {

    @Override
    public ICircus CreateCircus() {
        return new Circus();
    }
}
