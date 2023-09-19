public class UnderGrad extends Student{
    public UnderGrad(){
        super();
    }

    public UnderGrad(String studName, int[] studTests, String studGrade){
        super(studName, studTests, studGrade);
    }

    public void computeGrade(){
        if (getTestAverage() >= 70)
            setGrade("Pass for undergrad");
        else
            setGrade("Fail for undergrad");
    }
}
