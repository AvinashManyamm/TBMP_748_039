import React, { useState } from 'react';
import styles from './LoginPage.module.css';
import { Link } from 'react-router-dom';

const LoginPage = () => {
  const [passwordVisible, setPasswordVisible] = useState(false);

  const togglePasswordVisibility = () => {
    setPasswordVisible(prevState => !prevState);
  };

  return (
    <div className={styles['back']}>
    <form className={styles['modern-form']}>
      <div className={styles['form-title']}>Login</div>

      <div className={styles['form-body']}>
        <div className={styles['input-group']}>
          <div className={styles['input-wrapper']}>
            <svg fill="none" viewBox="0 0 24 24" className={styles['input-icon']}>
              <circle strokeWidth="1.5" stroke="currentColor" r="4" cy="8" cx="12"></circle>
              <path strokeLinecap="round" strokeWidth="1.5" stroke="currentColor" d="M5 20C5 17.2386 8.13401 15 12 15C15.866 15 19 17.2386 19 20"></path>
            </svg>
            <input required placeholder="Username" className={styles['form-input']} type="text" />
          </div>
        </div>

        

        <div className={styles['input-group']}>
          <div className={styles['input-wrapper']}>
            <svg fill="none" viewBox="0 0 24 24" className={styles['input-icon']}>
              <path strokeWidth="1.5" stroke="currentColor" d="M12 10V14M8 6H16C17.1046 6 18 6.89543 18 8V16C18 17.1046 17.1046 18 16 18H8C6.89543 18 6 17.1046 6 16V8C6 6.89543 6.89543 6 8 6Z"></path>
            </svg>
            <input required placeholder="Password" className={styles['form-input']} type={passwordVisible ? 'text' : 'password'} />
            <button type="button" className={styles['password-toggle']} onClick={togglePasswordVisibility}>
              <svg fill="none" viewBox="0 0 24 24" className={styles['eye-icon']}>
                <path strokeWidth="1.5" stroke="currentColor" d="M2 12C2 12 5 5 12 5C19 5 22 12 22 12C22 12 19 19 12 19C5 19 2 12 2 12Z"></path>
                <circle strokeWidth="1.5" stroke="currentColor" r="3" cy="12" cx="12"></circle>
              </svg>
            </button>
          </div>
        </div>
      </div>

    <Link to="/detection">
      <button className={styles['submit-button']} type="submit">
        <span className={styles['button-text']}>Submit</span>
        <div className={styles['button-glow']}></div>
      </button>
      </Link>

      <div className={styles['form-footer']}>
        <a href="#" className={styles['login-link']}>
          Forgot password? <span>click here</span>
        </a>
      </div>
    </form>
    </div>
  );
};

export default LoginPage;
