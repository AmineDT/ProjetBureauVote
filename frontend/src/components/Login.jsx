import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AuthenticatedPage from './AuthenticatedPage';

const Login = () => {
  const [authenticated, setAuthenticated] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  useEffect(() => {
    // Fetch the CSRF token and set it in axios defaults
    axios.get('http://localhost:5001/api/auth/csrf/')
      .then(response => {
        axios.defaults.headers.post['X-CSRFToken'] = response.data.csrfToken;
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleLogin = () => {
    // Perform login request to the backend
    axios.post('http://localhost:5001/api/auth/login/', { username, password }, { withCredentials: true })
      .then(response => {
        // Update the authentication status and set the username
        setAuthenticated(true);
        setUsername(username);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      {authenticated ? (
        <AuthenticatedPage username={username} />
      ) : (
        <div>
          <h1>Login</h1>
          {/* Your login form */}
          <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
          <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </div>
  );
};

export default Login;
