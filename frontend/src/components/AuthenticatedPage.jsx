import React from 'react';

const AuthenticatedPage = ({ username }) => {
  return (
    <div>
      <h1>Welcome, {username}!</h1>
      {/* Display other authenticated content */}
    </div>
  );
};

export default AuthenticatedPage;
