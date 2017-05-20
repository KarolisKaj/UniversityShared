package Dependencies;

/**
 * Created by Kay on 5/20/2017.
 */
public class DeepLearning implements IDeepLearning {
    @Override
    public int LearnStuff(int startingIndex) throws InterruptedException {
        Thread.sleep(2500);
        return ++startingIndex;
    }
}
