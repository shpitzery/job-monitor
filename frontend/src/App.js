import React, { useState, useEffect } from 'react';
import axios from 'axios';
import JobList from './components/JobList';

function App() {
    const [jobs, setJobs] = useState([]);

    useEffect(() => {
      axios.get("http://localhost:5001/jobs")
          .then(response => {
              console.log("Fetched jobs:", response.data); // Debugging
              setJobs(response.data);
          })
          .catch(error => console.error("Error fetching jobs:", error));
  }, []);

    return (
        <div>
            <JobList jobs={jobs} />
        </div>
    );
}

export default App;