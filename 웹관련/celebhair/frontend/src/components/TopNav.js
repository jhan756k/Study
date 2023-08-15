import "../styles/TopNav.css"
import { useNavigate } from "react-router-dom";

const TopNav = () => {
    const navigate = useNavigate();

    return (  
        <div className="divtitle">
            <button className="title" onClick={()=>{navigate("/")}}>헤어스타일 체험</button>
            <button className="login" onClick={()=>{navigate("/login")}}>로그인</button>
        </div>
    );
}
 
export default TopNav;