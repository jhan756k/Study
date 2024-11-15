package ch03;

public class Person {
    private String name;
    private int age;

    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setAge(int age){
        this.age = age;
    }

    public String getName(){
        return this.name;
    }

    public int getAge(){
        return age;
    }

    public String toString(){
        return name + ": " + age + "살";
    }

    public void printPerson() {
        System.out.println(this); // 객체 자신을 출력
    }
}
