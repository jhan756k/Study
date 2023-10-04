package ch03;

public class Person {
    private String name;
    private int age;

    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    public String toString(){
        return name + ": " + age + "살";
    }

    public void printPerson() {
        System.out.println(this); // 객체 자신을 출력
    }
}
