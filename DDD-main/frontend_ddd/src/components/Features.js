import React from 'react';
import styles from './Features.module.css';

const Features = () => {
  return (
    <div className={styles.featuresContainer}>
      <div className={styles.introSection}>
        <h2 className={styles.heading}>Our Key Features</h2>
        <p className={styles.introText}>
          Discover how our solution improves safety, enhances driver focus, and helps manage fleets more efficiently.
        </p>
      </div>

      <section className={styles.features}>
        <div className={styles.featureCard}>
          <img
            src="https://media.post.rvohealth.io/wp-content/uploads/2023/09/view-from-drivers-seat-truck-on-highway-driving-steering-wheel-1200x628-facebook-1200x628.jpg"
            alt="Improves Driver Safety"
            className={styles.featureImg}
          />
          <div className={styles.featureContent}>
            <h3>Improves Driver Safety</h3>
            <p>
              Detects early signs of drowsiness, distraction, or fatigue in drivers, providing timely alerts to prevent accidents.
            </p>
          </div>
        </div>

        <div className={styles.featureCard}>
          <img
            src="https://www.safewise.com/app/uploads/danger-texting-driving.jpg"
            alt="Enhances Focus"
            className={styles.featureImg}
          />
          <div className={styles.featureContent}>
            <h3>Enhances Focus</h3>
            <p>
              Constantly monitors driver activity, encouraging consistent attention and reducing the chances of accidents due to distractions.
            </p>
          </div>
        </div>
        

        
        <div className={styles.featureCard}>
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCfNbJ8xcwpn6o1vstFSzGpMTMjb1EQmGz-Q&s"
            alt="Provides Real-Time Alerts"
            className={styles.featureImg}
          />
          <div className={styles.featureContent}>
            <h3>Provides Real-Time Alerts</h3>
            <p>
              Real-time notifications help keep drivers safe by ensuring they respond to potential risks before they escalate.
            </p>
          </div>
        </div>

        <div className={styles.featureCard}>
          <img
            src="https://www.dat.com/resources/wp-content/uploads/2023/07/dat-longform-marketing-pages-guide-to-truck-fleet-management-min.jpg"
            alt="Helps Fleet Management"
            className={styles.featureImg}
          />
          <div className={styles.featureContent}>
            <h3>Helps Fleet Management</h3>
            <p>
              Reduces costly accidents and enhances the overall safety of a company's transportation operations.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Features;
