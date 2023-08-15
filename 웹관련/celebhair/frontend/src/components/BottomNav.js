import "../styles/BottomNav.css"
import GitHubIcon from '@mui/icons-material/GitHub';
import FacebookIcon from '@mui/icons-material/Facebook';
import MailOutlineIcon from '@mui/icons-material/MailOutline';

const BottomNav = () => {

    return (  
        <div className="bottom-nav">
            <h1>인공지능 헤어스타일 체험 앱</h1>
            <p>Simulate your hairstyle with other people's photos</p>
            <p>Made by 한준희</p>
            <div className="links">
                <a href="https://github.com/jhan756k" target="_blank">
                    <GitHubIcon style={{ color: 'white' }}/>
                </a>

                <a href="https://www.facebook.com/profile.php?id=100077321226749" target="_blank" className="fb">
                    <FacebookIcon style={{ color: 'white' }}/>
                </a>

                <a href="mailto:jhan756k@gmail.com" target="_blank">
                    <MailOutlineIcon style={{ color: 'white' }}/>
                </a>
            </div>
        </div>
    );
}
 
export default BottomNav;