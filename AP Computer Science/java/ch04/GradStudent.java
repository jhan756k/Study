package java.ch04;

public class GradStudent extends Student{
    private int gradID;

    public GradStudent(){
        super();
        gradID = 0;
    }

    public GradStudent(String studName, int[] studTests, String studGrade, int gradStudID){
        super(studName, studTests, studGrade);
        gradID = gradStudID;
    }

    public int getID(){
        return gradID;
    }

    public void computeGrade(){
        super.computeGrade();
        if (getTestAverage() >= 90)
            setGrade("Pass with distinction");
    }
}