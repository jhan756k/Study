import LoginForm from "../components/LoginForm";
import BottomNav from "../components/BottomNav";
import TopNav from "../components/TopNav";
import "../styles/LoginPage.css";

const LoginPage = () => {
    return (  
        <div className="App">
            <TopNav />
            <LoginForm />
            <BottomNav />
        </div>
    );
}
 
export default LoginPage;