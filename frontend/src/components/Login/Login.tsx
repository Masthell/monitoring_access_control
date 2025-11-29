import { useState } from "react";
import "./Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Login:", { email, password });
  };

  return (
    <div className="login-container">
      <div className="sphere1"></div>
      <div className="sphere2"></div>

      <div className="login-content">
        <div className="logo-section">
          <img src="/vite.png" className="logo" alt="logo" />
          <h1>support dashboard</h1>
        </div>

        <form className="login-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="input"
              placeholder="E-mail"
            />
          </div>

          <div className="form-group">
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="input"
              placeholder="Password"
            />
          </div>

          <button type="submit" className="login-button">
            Войти
          </button>
        </form>

        <div className="signup-section">
          <p className="signup-text">
            Нет аккаунта?{" "}
            <a href="/register" className="signup-link">
              Зарегистрироваться
            </a>
          </p>
          <a href="#" className="forgot-link">
            Забыли пароль?
          </a>
        </div>
      </div>
    </div>
  );
}

export default Login;
