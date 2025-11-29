import { useState } from "react";
import "./Register.css";

function Register() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Register:", formData);
  };

  return (
    <div className="register-container">
      <div className="sphere1"></div>
      <div className="sphere2"></div>

      <div className="register-content">
        <div className="logo-section">
          <img src="/vite.png" className="logo" alt="logo" />
          <h1>support dashboard</h1>
          <p className="subtitle">Создайте свой аккаунт</p>
        </div>

        <form className="register-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              name="name"
              type="text"
              value={formData.name}
              onChange={handleChange}
              required
              className="input"
              placeholder="Полное имя"
            />
          </div>

          <div className="form-group">
            <input
              name="email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="input"
              placeholder="E-mail"
            />
          </div>

          <div className="form-group">
            <input
              name="password"
              type="password"
              value={formData.password}
              onChange={handleChange}
              required
              className="input"
              placeholder="Пароль"
            />
          </div>

          <div className="form-group">
            <input
              name="confirmPassword"
              type="password"
              value={formData.confirmPassword}
              onChange={handleChange}
              required
              className="input"
              placeholder="Подтвердите пароль"
            />
          </div>

          <button type="submit" className="login-button">
            Зарегистрироваться
          </button>
        </form>

        <div className="signup-section">
          <p className="signup-text">
            Уже есть аккаунт?{" "}
            <a href="/login" className="signup-link">
              Войти
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default Register;
