import "../styles/HomePage.css"
import TopNav from "../components/TopNav";
import BottomNav from "../components/BottomNav";
import FaceImage from "../components/FaceImage";

const HomePage = () => {

    return (  
        <div className="App">
            <TopNav />
            <FaceImage />
            <BottomNav />
        </div>
    );
}
 
export default HomePage;
