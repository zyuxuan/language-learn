package com.zyuxuan.concurrent.thread;

import org.apache.commons.lang3.RandomUtils;

import java.util.logging.Logger;


/**
 * 自定义线程02：实现Runnable接口
 * Created by zhangyuxuan on 2020/2/2
 */
public class MyRunnableImpl implements Runnable{
    //private static final Logger LOGGER = Logger.getLogger(MyRunnableImpl.class);
    private static final Logger LOGGER = Logger.getLogger("com.zyuxuan.concurrent.thread.MyRunnableImpl");

    /** 线程名(需要手动指定) */
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MyRunnableImpl(String name) {
        this.name = name;
    }

    /**
     * <p>义务代码在run()方法中，此方法无返回值</p>
     **/
    @Override
    public void run() {
        Integer interval = RandomUtils.nextInt(1000,5000);
        LOGGER.info("线程[" + this.getName() + "]正在运行，预计运行" + interval + "...");
        try {
            Thread.sleep(interval);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }finally {
            LOGGER.info("...线程[" + this.getName() + "]运行结束");
        }
    }

    /**
     * <p>自定义线程实现类测试</p>
     **/
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            //通过new创建一个线程
            Runnable runnable = new MyRunnableImpl("MyRunnableImpl-" + i);
            //通过new Thread.start()启动线程
            new Thread(runnable).start();
        }
    }
}
