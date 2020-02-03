package com.zyuxuan.concurrent.thread;
import org.apache.commons.lang3.RandomUtils;

import java.util.logging.Logger;
/**自定义线程01：继承自Thread
 * Created by zhangyuxuan on 2020/2/3
 */
public class MyThread extends Thread {
//    private static final Logger LOGGER = Logger.getLogger(MyThread.class);
    private static final Logger LOGGER = Logger.getLogger("com.zyuxuan.concurrent.thread.MyThread");

    /**
     * <p>重写Thread类的构造器，用以给线程命名</br>
     * 此种方式无需定义name变量以指定线程名，因为父类Thread中已有。</p>
     **/
    public MyThread(String name) {
        super(name);
    }

    /**
     * <p>业务代码写在run()方法中，此方法无返回值</p>
     **/
    @Override
    public void run(){
        //run()方法无法抛出异常
//    public void run() throws Exception{
        Integer interval = RandomUtils.nextInt(1000,9000);
        LOGGER.info("线程[" + super.getName() + "]正在运行，预计运行" + interval + "...");
        try {
            Thread.sleep(interval);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }finally {
            LOGGER.info("...线程[" + super.getName() + "]运行结束");
        }
    }

    /**
     * <p>测试自定义线程</p>
     **/
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            //通过new创建一个线程
            Thread thread = new MyThread("MyThread-" + i);
            //通过start()启动线程
            thread.start();
        }
    }
}
