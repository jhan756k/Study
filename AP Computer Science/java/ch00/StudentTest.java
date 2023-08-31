import chn.util.*;

public class StudentTest {
    public static void main(String[] args) {

        FileInput io = new FileInput("student.txt");
        Student apcs [] = new Student[8];

        for (int i = 0; i < apcs.length; i++) {
            apcs[i] = new Student();
            apcs[i].setName(io.readLine());
            apcs[i].setAge(io.readInt());
            apcs[i].setHeight((float)io.readDouble());
            for (int j = 0; j < 5; j++) {
                apcs[i].addGrade((float)io.readDouble());
            }
            if (i != apcs.length - 1) {
                io.readLine();
            }
            System.out.println(apcs[i].toString());
            System.out.println();
        }
    }
}
