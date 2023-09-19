package java.ch04;
import chn.util.*;

public class DriveTest {
    public static void main(String[] args) {

        FileInput io = new FileInput("java\\ch00\\student.txt");
        GradStudent gs = new GradStudent("배강민", new int[]{67, 99, 100}, "Pass", 1234);
        UnderGrad ug = new UnderGrad("박선우", new int[]{90, 98, 99}, "Pass");

        Student [] students = new Student[10];
        for (int i = 0; i < students.length; i++) {
            if (i % 2 == 0)
                students[i] = new GradStudent();
            else
                students[i] = new UnderGrad();
        }

        for (Student s : students) {
            s.computeGrade();
            
        }
    }
}
