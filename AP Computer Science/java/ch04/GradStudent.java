public class GradStudent extends Student{

    public GradStudent(){
        super();
    }

    public GradStudent(String studName, int[] studTests, String studGrade){
        super(studName, studTests, studGrade);
    }

    public void computeGrade(){
        if (getTestAverage() >= 90)
            setGrade("Pass with distinction for grad");
        else if (getTestAverage() >= 80)
            setGrade("Pass with merit for grad");
        else if (getTestAverage() >= 70)
            setGrade("Pass for grad");
        else
            setGrade("Fail for grad");
    }
}