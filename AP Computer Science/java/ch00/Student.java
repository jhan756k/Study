public class Student {
    private int myAge;
    private String myName;
    private float[] myGrades;
    private float myHeight;

    public Student() {
        myAge = 0;
        myName = "";
        myHeight = 0.0f;
    }

    public Student(int age, String name, float height) {
        myAge = age;
        myName = name;
        myHeight = height;
    }

    {
        myGrades = new float[]{0.0f, 0.0f, 0.0f, 0.0f, 0.0f};
    }

    public void setAge(int age) {
        myAge = age;
    }

    public void setName(String name) {
        myName = name;
    }

    public void setHeight(float height) {
        myHeight = height;
    }

    public String getGrade() {
        String gString = "";
        for (int i = 0; i < 5; i++) {
            gString += myGrades[i] + " ";
        }
        return gString;
    }

    public float getHeight() {
        return myHeight;
    }

    public int getAge() {
        return myAge;
    }

    public String getName() {
        return myName;
    }

    public void addGrade(float grade) {
        boolean isAdded = false;
        for (int i = 0; i < 5; i++) {
            if (myGrades[i] == 0.0f) {
                myGrades[i] = grade;
                isAdded = true;
                break;
            }
        }

        if (!isAdded) {
            System.out.println("You already added 5 grades.");
        }
    }

    public float getAverage() {
        float sum = 0.0f;
        int pnum = 0;
        float avg = 0.0f;
        for (int i = 0; i < myGrades.length; i++) {
            if (myGrades[i] != 0.0f) {
                pnum++;
                sum += myGrades[i];
            }
        }
        avg = sum / pnum;
        return avg;
    }

    public String toString() {
        return "Name: " + getName() + "\nAge: " + getAge() + "\nHeight: " + getHeight() + "\nGrades: " + getGrade() + "\nAVG: " + getAverage();
    }
}
