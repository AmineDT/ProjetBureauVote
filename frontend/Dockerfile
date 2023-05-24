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

# Serve the app with a static server
CMD ["npx", "serve", "-s", "build", "-l", "3000"]

# Expose the port
EXPOSE 3000
