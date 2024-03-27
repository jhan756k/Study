import org.hyunjun.school.*;
import java.util.List;

class GetFood {
  public static void main(String[] args) throws SchoolException {
    School api = new School(School.Type.HIGH, School.Region.KANGWON, "K100000414");
  
    List<SchoolMenu> menu = api.getMonthlyMenu(2023, 4);
    
    // 2016년 4월 22일 저녁 급식 식단표
    System.out.println(menu.get(21).dinner);
  }
}

