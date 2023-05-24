import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Users = () => {
    const [users, setUsers] = useState([]);
  
    useEffect(() => {
      // Fetch users data from the API
      axios.get('http://localhost:5001/api/users/')
        .then(response => setUsers(response.data))
        .catch(error => console.error(error));
    }, []);
  
    return (
      <div>
        <h1>Users</h1>
        <ul>
          {users.map(user => (
            <li key={user.id}>{user.username}</li>
          ))}
        </ul>
      </div>
    );
  };
  
  export default Users;
  