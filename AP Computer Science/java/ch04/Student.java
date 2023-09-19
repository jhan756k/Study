package java.ch04;

public class Student{
    public final static int NUM_TESTS = 3;
    private String name;
    private int[] tests;
    private String grade;

    public Student(){
        name = "";
        tests = new int[NUM_TESTS];
        grade = "";
    }

    public Student(String studName, int[] studTests, String studGrade){
        name = studName;
        tests = studTests;
        grade = studGrade;
    }

    public String getName(){
        return name;
    }

    public String getGrade(){
        return grade;
    }

    public void setGrade(String newGrade){
        grade = newGrade;
    }

    public void computeGrade(){
        if (name.equals("")) 
            grade = "No grade";
        else if (getTestAverage() >= 65)
            grade = "Pass";
        else
            grade = "Fail";
    }

    public double getTestAverage(){
        int total = 0;
        for (int score : tests)
            total += score;
        return (double)total / NUM_TESTS;
    }
}