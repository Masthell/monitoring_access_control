import { useState } from "react";
import "./App.css";

function App() {
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
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="input"
              placeholder="E-mail"
            />
          </div>

          <div className="form-group">
            <div className="password-header"></div>
            <input
              id="password"
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
            Don't have an account?{" "}
            <a href="#" className="signup-link">
              Sign up
            </a>
            <a href="#" className="forgot-link">
              Forgot password?
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
