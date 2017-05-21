package LocalConfigs;

import Dependencies.IExample;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by Kay on 5/21/2017.
 */
public class Bootstrapper {

    ApplicationContext ctx;

    public void Start() {
        ctx = new ClassPathXmlApplicationContext("/LocalConfigs/IoCConfig.xml");

        String[] exportNames = ctx.getBeanDefinitionNames();
        System.out.println("//------CONTAINER CONTENT-------------");
        for (int i = 0; i < exportNames.length; i++){
            System.out.println(exportNames[i]);
        }
        System.out.println("//------CONTAINER CONTENT END---------");

        
        // First assignment in 5th Lab.
        IExample example = ((IExample) ctx.getBean("example"));
        System.out.println(((ICountable)example).getCount());
        example.FirstMethod();
        example.SecondMethod(4);
        example.ThirdMethod();
        example.FourthMethod("Karolis", 1);
        System.out.println(((ICountable)example).getCount());



    }
}
