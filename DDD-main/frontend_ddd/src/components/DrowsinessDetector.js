import React, { useState } from 'react';
import './DrowsinessDetector.css'; // Optional: For styles

const DrowsinessDetector = () => {
  const [logs, setLogs] = useState([]); // State to store logs

  // Add a log for start, stop, or SOS events
  const logEvent = (type) => {
    <div className='fullDDD'></div>
    const timestamp = new Date().toLocaleString(); // Get the current timestamp
    const logMessage =
      type === 'start'
        ? `Started detection at ${timestamp}`
        : type === 'stop'
        ? `Stopped detection at ${timestamp}`
        : `SOS triggered at ${timestamp}`;
    setLogs((prevLogs) => [...prevLogs, logMessage]); // Add the log locally
    console.log(logMessage); // Optional: Log in the browser console
  };

  // Trigger Python backend for Start Detection
  const startCamera = async () => {
    logEvent('start');
    try {
      await fetch('http://localhost:5000/start-detection');
    } catch (error) {
      console.error('Error starting detection:', error);
    }
  };

  // Trigger Python backend for Stop Detection
  const stopCamera = async () => {
    logEvent('stop');
    try {
      await fetch('http://localhost:5000/stop-detection');
    } catch (error) {
      console.error('Error stopping detection:', error);
    }
  };

  // Download logs as a text file
  const downloadLogs = () => {
    const element = document.createElement('a'); // Create a new anchor element
    const file = new Blob([logs.join('\n')], { type: 'text/plain' }); // Create a text file with logs
    element.href = URL.createObjectURL(file); // Create a download URL for the file
    element.download = 'logs.txt'; // Set the file name
    document.body.appendChild(element); // Append the element to the body temporarily
    element.click(); // Programmatically click the anchor to trigger download
    document.body.removeChild(element); // Remove the element after download
  };

  return (

    <div className='fullDDD'>
    <div className="drowsiness-detector">
      <h1>Drowsiness Detector</h1>

      <div className="controls">
        <button onClick={startCamera} className='sosbutton'>Start Camera</button>
        <button onClick={stopCamera} className='sosbutton'>Stop Camera</button>
        <button onClick={() => logEvent('sos')} className='yesosbutton'>SOS</button>
      </div>

      {/* Log Box to display logs */}
      <div className="log-box">
        <h3>Detection Logs</h3>
        <ul style={{ listStyleType: 'none' }}>
          {logs.map((log, index) => (
            <li key={index}>{log}</li>
          ))}
        </ul>

        {/* Download Logs Button */}
        
      </div>
      <button onClick={downloadLogs} className='buttonDownload'>Download Logs</button>
    </div>
    </div>
  );
};

export default DrowsinessDetector;
