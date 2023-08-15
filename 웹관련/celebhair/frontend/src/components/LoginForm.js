const LoginForm = () => {
    return (  
        <div className="login-form">
            <h1>로그인</h1>
            <form>
                <input type="text" placeholder='아이디' />
                <input type="password" placeholder='비밀번호' />
            </form>
            <div className="enter">
                <a href="/sign-up" className="create-account">계정 만들기</a>
                <button className="login-button" onClick={() => (alert("아직 안만듬 히히"))}>로그인</button>
            </div>
        </div>    
    );
}
 
export default LoginForm;