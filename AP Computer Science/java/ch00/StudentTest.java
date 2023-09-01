import chn.util.*;

public class StudentTest {
    public static void main(String[] args) {

        FileInput io = new FileInput("student.txt");
        int numStudents = io.readInt();
        Student apcs[] = new Student[numStudents];
        float totalAvg = 0.0f;
        float variance = 0.0f;

        // Read Data
        for (int i = 0; i < numStudents; i++) {
            apcs[i] = new Student();
            apcs[i].setName(io.readLine());
            apcs[i].setAge(io.readInt());
            apcs[i].setHeight((float) io.readDouble());

            for (int j = 0; j < 3; j++) {
                apcs[i].addGrade((float) io.readDouble());
            }

            if (i != numStudents - 1) {
                io.readLine();
            }
        }

        // Sort Students by Grade
        for (int i = 0; i < numStudents - 1; i++) {
            for (int j = i + 1; j < numStudents; j++) {
                if (apcs[i].getFinalGrade() < apcs[j].getFinalGrade()) {
                    Student temp = apcs[i];
                    apcs[i] = apcs[j];
                    apcs[j] = temp;
                }
            }
        }

        // Print Data
        for (int i = 0; i < numStudents; i++) {
            totalAvg += apcs[i].getFinalGrade();
            System.out.println(apcs[i].toString());
            System.out.println("--------------------------");
        }

        // Print Stats
        totalAvg /= numStudents;
        System.out.println();
        System.out.println("Number of Students: " + numStudents);
        System.out.println("Average of the Class: " + totalAvg);

        for (int i = 0; i < numStudents; i++) {
            variance += Math.pow(apcs[i].getFinalGrade() - totalAvg, 2);
        }
        variance /= numStudents;
        System.out.println("Variance of the Class: " + variance);
        System.out.println("Standard Deviation of the Class: " + Math.sqrt(variance));
    }
}
