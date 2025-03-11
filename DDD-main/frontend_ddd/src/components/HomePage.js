import React from 'react';
import styles from './HomePage.module.css';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
      <div className={styles['hero-section']}>
        <nav className={styles['navbar']}>
          <div className={styles['logo']}>SportSync</div>

          {/* Button for Documentation */}
          <a
            href="https://docs.google.com/document/d/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button className={styles['button']}>
              <p className={styles['button-text']}>Documentation</p>
            </button>
          </a>

          {/* Button for PPT */}
          <a
            href="https://docs.google.com/presentation/d/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button className={styles['buttonp']}>
              <p className={styles['buttonp-text']}>PPT</p>
            </button>
          </a>

          {/* Login Button */}
          <Link to="/loginform">
            <button className={styles["cssbuttons-io-button"]}>
              Login
              <div className={styles.icon}>
                <svg
                  height="24"
                  width="24"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path d="M0 0h24v24H0z" fill="none"></path>
                  <path
                    d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
                    fill="currentColor"
                  ></path>
                </svg>
              </div>
            </button>
          </Link>
        </nav>

        <div className={styles['hero-section-content']}>
          <h2>Welcome to the Driver Monitoring System</h2>
          <h6>
            Our cutting-edge system ensures the safety of drivers by detecting
            signs of drowsiness and fatigue. With real-time alerts and
            monitoring, we aim to keep drivers alert and prevent accidents
            caused by tiredness. Start your journey to safer roads today!
          </h6>
        </div>
      </div>

      <div className={styles['white']}>
        <h2>
          Driver drowsiness detection is a system that uses a combination of
          computer vision and machine learning to monitor a driver’s behavior
          and identify signs of fatigue or sleepiness.
        </h2>

        <Link to="/features">
          <button className={styles.learnMoreCustom}>
            <span className={styles.circle} aria-hidden="true">
              <span className={styles.icon + ' ' + styles.arrow}></span>
            </span>
            <span className={styles.buttonText}>Learn More</span>
          </button>
        </Link>
      </div>
    </div>
  );
};

export default HomePage;
