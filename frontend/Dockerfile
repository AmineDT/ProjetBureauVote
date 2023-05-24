# Base image
FROM node:14-alpine

# Set working directory
WORKDIR /app/frontend

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the entire project
COPY . .

# Build the React app
RUN npm run build

# Start the React development server
CMD ["npm", "start"]

# Expose the port
EXPOSE 3000
