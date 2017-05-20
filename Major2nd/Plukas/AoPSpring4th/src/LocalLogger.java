import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Handler;
import java.util.logging.Logger;

/**
 * Created by Kay on 5/20/2017.
 */
public class LocalLogger extends Logger {

    private LocalLogger(String name, String resourceBundleName) {
        super(name, resourceBundleName);
    }

    public static Logger createLogger() throws IOException {
        Handler handler = new FileHandler("C:\\Users\\Kay\\test.log");
        Logger.getLogger("Logger").addHandler(handler);;
        return Logger.getLogger("Logger");
    }

    private static Logger GetLogger() throws IOException {
        Handler handler = new FileHandler("C:\\Users\\Kay\\test.log", 1, 1);
        Logger.getLogger("Logger").addHandler(handler);;
        return Logger.getLogger("Logger");
    }
}
