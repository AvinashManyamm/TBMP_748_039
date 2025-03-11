import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import DrowsinessDetector from './components/DrowsinessDetector';
import HomePage from './components/HomePage';
import LoginForm from './components/LoginPage';
import Features from './components/Features';

function App() {
  return (
    <Router>
      <div className="App">
        <main>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/detection" element={<DrowsinessDetector />} />
            <Route path="/loginform" element={<LoginForm />} />
            <Route path="/features" element={<Features />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
