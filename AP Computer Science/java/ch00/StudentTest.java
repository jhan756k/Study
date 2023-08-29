public class StudentTest {
    public static void main(String[] args) {
        Student s1 = new Student(17, "오지훈", 180);

        for (int i = 0; i < 5; i++) {
            float randnum = (float)(Math.random() * 50 + 50);
            s1.addGrade(randnum);
        }

        s1.getAverage();
        System.out.println(s1.toString());
    }
}
