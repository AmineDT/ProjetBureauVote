# Dockerfile

# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the remaining app files to the container
COPY . .

# Build the React app
RUN npm run build

# Expose the desired port
EXPOSE 3000

# Define the command to run the app
CMD ["npm", "start"]
