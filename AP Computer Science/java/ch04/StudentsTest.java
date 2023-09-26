import chn.util.*;

public class StudentsTest {
    public static void main(String[] args) {

        FileInput io = new FileInput("java\\ch00\\student.txt");
        int numStudents = io.readInt();
        Student[] students = new Student[numStudents];
        int age = 0;
        String name = "";
        int[] grades = new int[3];

        // Read Data
        for (int i = 0; i < numStudents; i++) {
            name = io.readLine();
            age = io.readInt();

            // Remove Height
            io.readDouble();

            // Read Grades
            for (int j = 0; j < 3; j++) {
                grades[j] = (int) io.readDouble();
            }
            if (i != numStudents - 1)
                io.readLine();

            // Create Student
            if (age < 20) {
                students[i] = new UnderGrad(name, new int[] { grades[0], grades[1], grades[2] }, "Pass");
            } else {
                students[i] = new GradStudent(name, new int[] { grades[0], grades[1], grades[2] }, "Pass");
            }
        }

        for (Student s : students) {
            s.computeGrade();
            System.out.println(s.getGrade());   
        }
    }
}
