package com.zyuxuan.concurrent.thread;
import org.apache.commons.lang3.RandomUtils;

import java.util.concurrent.*;
import java.util.logging.Logger;
/**自定义线程03：实现Callable接口
 * Created by zhangyuxuan on 2020/2/3
 */
//注意，Callable是一个泛型接口
public class MyCallableImpl implements Callable<Integer> {
//    private static final Logger LOGGER = Logger.getLogger(MyCallableImpl.class);
    private static final Logger LOGGER = Logger.getLogger("com.zyuxuan.concurrent.thread.MyCallableImpl");

    /**
     * <p>实现Callable需要重写call方法，此方法有返回值</p>
     **/
    @Override
    public Integer call() throws Exception {
        Integer interval = RandomUtils.nextInt(1000, 5000);
        Thread.sleep(interval);
        return interval;
    }

    /**
     * <p>实现Callable示例</p>
     **/
    public static void main(String[] args) throws ExecutionException, InterruptedException, TimeoutException {
        //Future、Callable一般与Executor结合使用
        //Executor负责创建线程池服务
        //实现Callable接口形成的线程类，负责处理业务逻辑，并将处理结果返回
        //Future接口负责接收Callable接口返回的值
        ExecutorService executor = Executors.newFixedThreadPool(5);
        try {
            //定义一组返回值
            Future<Integer>[] futures = new Future[5];
            //向线程池提交任务
            for (int i = 0; i < 5; i++) {
                //注意Future的参数化类型要与Callable的参数化类型一致
                futures[i] = executor.submit(new MyCallableImpl());
            }
            //输出执行结果
            for (int i = 0; i < 5; i++) {
                LOGGER.info(futures[i].get()+"");
            }
        }finally {//将关闭线程池放在finally中，最大限度保证线程安全
            //记得关闭这个线程池
            executor.shutdown();
        }
    }
}
