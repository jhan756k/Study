package ch03;

public class PersonTest {
    public static void main(String[] args) {
        Person p = new Person("한준희", 0);
        p.printPerson();

        p.setName("배강민");
        p.setAge(25);
        p.printPerson();

    }
}
