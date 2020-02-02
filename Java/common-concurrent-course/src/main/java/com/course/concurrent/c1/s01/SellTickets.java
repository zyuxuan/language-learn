package com.course.concurrent.c1.s01;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created by zhangyuxuan on 2020/2/1
 */
public class SellTickets {
    public static void main(String[] args) {
//        sellNotThreadSafe();
        sellThreadSafe();
    }

    private static int totalTickets = 10000;

    /*
    *  线程不安全的原因：
    *    totalTickets--不是原子操作，它实际是包含了两个步骤：先读取变量做减法，再赋值。
    *    在减完但还没赋值的时候可能另一个线程就来读取该变量
    * */
    private static void sellNotThreadSafe(){
        ExecutorService executorService = Executors.newFixedThreadPool(2);
        Runnable runnableA = new Runnable() {
            int threadTickets = 0;
            @Override
            public void run() {
                while(totalTickets > 0){
                    totalTickets--;
                    threadTickets++;
                }
                System.out.println("Thread A buys " + threadTickets + " tickets");
            }
        };

        Runnable runnableB = new Runnable() {
            int threadTickets = 0;
            @Override
            public void run() {
                while(totalTickets > 0){
                    totalTickets--;
                    threadTickets++;
                }
                System.out.println("Thread B buys " + threadTickets + " tickets");
            }
        };

        executorService.execute(runnableA);
        executorService.execute(runnableB);
    }

    private static AtomicInteger atomicTotalTickets = new AtomicInteger(10000);

    private static void sellThreadSafe(){
        ExecutorService executorService = Executors.newFixedThreadPool(2);
        Runnable runnableA = new Runnable() {
            int threadTickets = 0;
            @Override
            public void run() {
                while(atomicTotalTickets.get() > 0){
                    atomicTotalTickets.decrementAndGet();
                    threadTickets++;
                }
                System.out.println("Thread A buys " + threadTickets + " tickets");
            }
        };

        Runnable runnableB = new Runnable() {
            int threadTickets = 0;
            @Override
            public void run() {
                while(atomicTotalTickets.get() > 0){
                    atomicTotalTickets.decrementAndGet();
                    threadTickets++;
                }
                System.out.println("Thread B buys " + threadTickets + " tickets");
            }
        };

        executorService.execute(runnableA);
        executorService.execute(runnableB);
    }
}
