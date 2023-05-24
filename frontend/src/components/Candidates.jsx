import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Candidates = () => {
    const [candidates, setCandidates] = useState([]);
  
    useEffect(() => {
      // Fetch candidates data from the API
      axios.get('http://localhost:5001/api/candidates/')
        .then(response => setCandidates(response.data))
        .catch(error => console.error(error));
    }, []);
  
    return (
      <div>
        <h1>Candidates</h1>
        <ul>
          {candidates.map(candidate => (
            <li key={candidate.id}>{candidate.name}</li>
          ))}
        </ul>
      </div>
    );
  };
  
  export default Candidates;
  