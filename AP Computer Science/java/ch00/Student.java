public class Student {
    private int myAge;
    private String myName;
    private float[] myGrades;
    private float myHeight;

    public Student() {
        myAge = 0;
        myName = "";
        myGrades = new float[5];
        myHeight = 0.0f;
    }

    public Student(int age, String name, float[] grades, float height) {
        myAge = age;
        myName = name;
        myGrades = grades;
        myHeight = height;
    }
}
